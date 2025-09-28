import argparse
import json
import os
import re
import sys
from typing import Any, Dict, List, Tuple, Optional

import faiss
import numpy as np
import yaml
from FlagEmbedding import BGEM3FlagModel

try:
    from openai import OpenAI
except Exception:
    OpenAI = None

try:
    import requests
except Exception:
    requests = None


TEXT_KEYS   = ["text", "page_content", "content", "chunk", "body", "excerpt"]
SOURCE_KEYS = ["source", "path", "file", "filepath", "doc_path"]
_SENT_SPLIT = re.compile(r"(?<=[.!?…])\s+|\n+")


def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_index(index_dir: str) -> Tuple[faiss.Index, List[Dict[str, Any]], Optional[str]]:
    idx_path  = os.path.join(index_dir, "faiss.index")
    meta_path = os.path.join(index_dir, "metadata.jsonl")
    if not os.path.exists(idx_path):
        raise FileNotFoundError(f"FAISS index not found: {idx_path}")
    if not os.path.exists(meta_path):
        raise FileNotFoundError(f"metadata.jsonl not found: {meta_path}")

    index = faiss.read_index(idx_path)
    metadata: List[Dict[str, Any]] = []
    with open(meta_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                metadata.append(json.loads(line))

    info_path = os.path.join(index_dir, "INDEX_INFO.json")
    old_base = None
    if os.path.exists(info_path):
        try:
            with open(info_path, "r", encoding="utf-8") as f:
                info = json.load(f)
            old_base = info.get("kb_dir") or info.get("source_root")
        except Exception:
            pass

    return index, metadata, old_base


def build_encoder(model_name: str) -> BGEM3FlagModel:
    return BGEM3FlagModel(model_name, use_fp16=True, normalize_embeddings=True)


def embed_query(encoder: BGEM3FlagModel, query: str) -> np.ndarray:
    out = encoder.encode_queries([query])  # {'dense_vecs': [[...]], ...}
    return np.array(out["dense_vecs"], dtype=np.float32)


def _first_nonempty(d: Dict[str, Any], keys: List[str]) -> Optional[str]:
    for k in keys:
        v = d.get(k)
        if isinstance(v, str) and v.strip():
            return v
    return None


def resolve_source(meta: Dict[str, Any], kb_dir: str, old_base: Optional[str]) -> Optional[str]:
    raw = _first_nonempty(meta, SOURCE_KEYS)
    if not raw:
        return None
    p = os.path.normpath(raw)

    if os.path.isabs(p) and os.path.exists(p):
        return p

    p2 = os.path.normpath(os.path.join(kb_dir, p))
    if os.path.exists(p2):
        return p2

    if old_base:
        ob = os.path.normpath(old_base)
        if p.startswith(ob):
            p3 = os.path.normpath(p.replace(ob, kb_dir, 1))
            if os.path.exists(p3):
                return p3

    p4 = os.path.join(kb_dir, os.path.basename(p))
    if os.path.exists(p4):
        return p4

    return None


def read_chunk_text(meta: Dict[str, Any], kb_dir: str, old_base: Optional[str]) -> str:
    t = _first_nonempty(meta, TEXT_KEYS)
    if isinstance(t, str) and t.strip():
        return t

    src = resolve_source(meta, kb_dir, old_base)
    if not src:
        return ""
    try:
        with open(src, "r", encoding="utf-8") as f:
            full = f.read()
        s, e = meta.get("start"), meta.get("end")
        if isinstance(s, int) and isinstance(e, int) and 0 <= s < e <= len(full):
            return full[s:e]
        return full
    except Exception:
        return ""


def search(index: faiss.Index, metadata: List[Dict[str, Any]], qvec: np.ndarray, top_k: int):
    D, I = index.search(qvec, top_k * 4)  # overfetch
    hits = []
    for dist, idx in zip(D[0], I[0]):
        if idx == -1:
            continue
        meta = metadata[idx] if 0 <= idx < len(metadata) else {}
        hits.append({"idx": int(idx), "dist": float(dist), "meta": meta})
    hits.sort(key=lambda x: x["dist"])
    return hits[:top_k]


def build_context(hits, kb_dir: str, old_base: Optional[str], max_chars: int) -> Tuple[str, List[str], List[str]]:
    parts, sources, raw_chunks = [], [], []
    total = 0
    for h in hits:
        meta = h["meta"]
        src = resolve_source(meta, kb_dir, old_base) or _first_nonempty(meta, SOURCE_KEYS) or f"id:{h['idx']}"
        chunk = read_chunk_text(meta, kb_dir, old_base).strip()
        if not chunk:
            continue
        chunk = chunk.replace("\u0000", " ").replace("\r", "")
        block = f"[SOURCE]: {src}\n[EXCERPT]:\n{chunk}\n"
        if total + len(block) > max_chars and parts:
            break
        parts.append(block)
        raw_chunks.append(chunk)
        total += len(block)
        if src not in sources:
            sources.append(str(src))
    return "\n\n".join(parts), sources, raw_chunks


def build_messages(system_prompt: str, examples: List[Dict[str, str]], question: str, context: str) -> List[Dict[str, str]]:
    """
    Few-shot messages: system + (user/assistant) pairs + final user with instruction + CONTEXT.
    """
    msgs: List[Dict[str, str]] = [{"role": "system", "content": system_prompt}]

    for ex in (examples or []):
        q = ex.get("q", "").strip()
        a = ex.get("a", "").strip()
        if q:
            msgs.append({"role": "user", "content": q})
        if a:
            msgs.append({"role": "assistant", "content": a})

    user_content = (
        f"QUESTION:\n{question}\n\n"
        f"CONTEXT (источники и выдержки):\n{context}\n\n"
        "Выводи только секции «Ответ:», «Ключевые доводы:», «Источники:».\n"
        "Не придумывай факты вне CONTEXT."
    )
    msgs.append({"role": "user", "content": user_content})
    return msgs


def ensure_ollama_model(base_url: str, model: str):
    if requests is None:
        return
    try:
        r = requests.get(base_url.replace("/v1", "") + "/api/tags", timeout=3)
        r.raise_for_status()
        models = {m.get("model") for m in r.json().get("models", [])}
        if model not in models:
            print(f"[fix] Ollama model '{model}' not found. Pull it:\n    ollama pull {model}")
            raise SystemExit(2)
    except Exception:
        print(f"[fix] Cannot reach Ollama at {base_url}. Start the service or run:  ollama serve")
        raise SystemExit(2)


def call_llm(base_url: str, api_key: str, model: str, messages: List[Dict[str, str]],
             temperature: float, max_tokens: int, num_samples: int = 1) -> str:
    if OpenAI is None:
        raise RuntimeError("openai package not installed. Run: py -m pip install openai")

    client = OpenAI(base_url=base_url, api_key=api_key)

    samples: List[str] = []
    for _ in range(max(1, int(num_samples))):
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        txt = resp.choices[0].message.content.strip()
        samples.append(txt)

    if len(samples) == 1:
        return samples[0]

    def first_line(s: str) -> str:
        return s.splitlines()[0].strip().lower()

    counts: Dict[str, int] = {}
    for s in samples:
        k = first_line(s)
        counts[k] = counts.get(k, 0) + 1

    best_first = max(counts.items(), key=lambda kv: kv[1])[0]
    for s in samples:
        if first_line(s) == best_first:
            return s
    return samples[0]


def extractive_fallback(question: str, chunks: List[str]) -> str:
    def tok(t: str):
        t = t.lower()
        t = re.sub(r"[^\wа-яё'-]+", " ", t)
        return [w for w in t.split() if len(w) > 2]

    q = set(tok(question))
    best, score = "", 0.0
    for ch in chunks:
        for sent in _SENT_SPLIT.split(ch.strip()):
            s = set(tok(sent))
            if not s:
                continue
            ov = len(q & s) / (len(q) + 1e-6)
            if ov > score:
                best, score = sent.strip(), ov

    ans = best or "В CONTEXT нет однозначного факта для краткого ответа."
    return f"Ответ: {ans}\nКлючевые доводы:\n- Ответ извлечён напрямую из ближайшего фрагмента.\nИсточники:\n- см. ниже."


def main():
    ap = argparse.ArgumentParser(description="RAG over FAISS + Ollama with few-shot prompting.")
    ap.add_argument("-q", "--question", required=True, help="User question")
    args = ap.parse_args()

    CONFIG_PATH = "C:/practicum/am-ml/Task4/rag_config.yaml"

    cfg = load_config(CONFIG_PATH)
    kb_dir    = cfg["kb_dir"]
    index_dir = cfg["index_dir"]

    index, metadata, old_base = load_index(index_dir)
    encoder = build_encoder(cfg["embedding_model"])
    qvec = embed_query(encoder, args.question)
    hits = search(index, metadata, qvec, top_k=cfg.get("top_k", 5))

    context, sources, raw_chunks = build_context(hits, kb_dir, old_base, max_chars=cfg.get("max_context_chars", 6000))

    print(f"[debug] hits={len(hits)}, sources={len(sources)}, chunks={len(raw_chunks)}")

    if not raw_chunks:
        print("Ответ: В CONTEXT нет подходящих фрагментов.\n\nОбоснование: не удалось прочитать текст фрагментов.")
        return

    llm_cfg = cfg.get("llm", {})
    use_llm = bool(llm_cfg.get("enabled", True))

    if use_llm:
        model = llm_cfg.get("model", "gemma3:4b")
        base_url = llm_cfg.get("base_url", "http://localhost:11434/v1")
        api_key = llm_cfg.get("api_key", "ollama")
        temperature = float(llm_cfg.get("temperature", 0.1))
        max_tokens = int(llm_cfg.get("max_tokens", 512))
        num_samples = int(llm_cfg.get("num_samples", 1))

        ensure_ollama_model(base_url, model)

        messages = build_messages(cfg["system_prompt"], cfg.get("examples", []), args.question, context)

        print("\n--- DEBUG: CONTEXT being sent to LLM ---\n")
        print(context[:5000])
        print("\n--- DEBUG: RAW CHUNKS ---")
        for i, ch in enumerate(raw_chunks):
            print(f"--- chunk {i} (len={len(ch)}):")
            print(ch[:800])
            print()
        print("\n--- DEBUG: END ---")

        try:
            answer = call_llm(base_url, api_key, model, messages, temperature, max_tokens, num_samples)
        except Exception as e:
            if args.debug:
                print(f"[debug] LLM call failed: {e!r}. Falling back to extractive.")
            answer = extractive_fallback(args.question, raw_chunks)
    else:
        answer = extractive_fallback(args.question, raw_chunks)

    print(answer)
    print("\nИсточники:")
    for s in sources:
        print(f" - {s}")

    print("\n---\nОбоснование (выдержки):")
    print(context)


if __name__ == "__main__":
    main()
