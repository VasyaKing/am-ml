import os
import re
import faiss
import json
import time
import argparse
import numpy as np
from pathlib import Path
from typing import List, Tuple, Dict
from sentence_transformers import SentenceTransformer
from markdown_it import MarkdownIt

# ---------- Config ----------
MODEL_DEFAULT = "BAAI/bge-m3"
MODEL_LINK    = "https://huggingface.co/BAAI/bge-m3"
WORD_CHUNK_SIZE    = 250       # ~100–300 слов
WORD_CHUNK_OVERLAP = 40
SEPARATORS = ["\n## ", "\n### ", "\n\n", "\n", " ", ""]
# ----------------------------

md = MarkdownIt()

def extract_front_matter(text: str) -> Tuple[Dict[str, str], str]:
    """Parse YAML-like front-matter at top of file."""
    meta, body = {}, text
    if text.startswith('---'):
        parts = text.split('---', 2)
        fm, body = parts[1], parts[2].lstrip('\n')
        for line in fm.strip().splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body

def md_to_plain(markdown_text: str) -> str:
    """Convert Markdown to plain-ish text for stable splitting."""
    tokens = md.parse(markdown_text)
    return "\n".join(t.content for t in tokens if t.type == "inline" and t.content)

def word_count(s: str) -> int:
    return len(re.findall(r"\w+", s, flags=re.UNICODE))

# Try to use LangChain splitter; fallback to a simple splitter by words
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    def build_chunks(text: str) -> List[str]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=WORD_CHUNK_SIZE,
            chunk_overlap=WORD_CHUNK_OVERLAP,
            separators=SEPARATORS,
            length_function=word_count,
        )
        return splitter.split_text(text)
except Exception:
    # Minimal fallback: split by paragraphs, then pack to ~target words with overlap
    def build_chunks(text: str) -> List[str]:
        paras = re.split(r'\n\s*\n', text.strip())
        chunks, cur, cur_w = [], [], 0
        for p in paras:
            w = word_count(p)
            if cur_w + w <= WORD_CHUNK_SIZE:
                cur.append(p); cur_w += w
            else:
                if cur:
                    chunks.append("\n\n".join(cur))
                # start new
                cur = [p]; cur_w = w
                # introduce overlap by borrowing tail from previous chunk if exists
                if chunks:
                    tail = chunks[-1].split()
                    tail_overlap = " ".join(tail[max(0, len(tail)-WORD_CHUNK_OVERLAP):])
                    cur.insert(0, tail_overlap)
                    cur_w += word_count(tail_overlap)
            # finalize near target window
            if cur_w >= WORD_CHUNK_SIZE:
                chunks.append("\n\n".join(cur))
                # prepare next cur with overlap tail
                tail = " ".join(cur).split()
                overlap_text = " ".join(tail[max(0, len(tail)-WORD_CHUNK_OVERLAP):])
                cur, cur_w = ([overlap_text] if overlap_text else []), word_count(overlap_text)
        if cur:
            chunks.append("\n\n".join(cur))
        # clean empty
        return [c for c in chunks if word_count(c) > 0]

def split_with_positions(full_text: str) -> List[Tuple[str, int, int, int, int]]:
    """
    Return list of (chunk_text, start_word, end_word, start_char, end_char)
    Positions are relative to the *plain text*.
    """
    chunks = build_chunks(full_text)

    res = []
    current_word_pos = 0
    search_from_char = 0  # to find next occurrence safely

    for ch in chunks:
        ch_words = word_count(ch)

        # character positions (best effort, sliding window)
        start_char = full_text.find(ch, search_from_char)
        if start_char == -1:
            start_char = search_from_char
        end_char = start_char + len(ch)
        search_from_char = end_char

        res.append((ch, current_word_pos, current_word_pos + ch_words, start_char, end_char))
        current_word_pos += ch_words

    return res

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb_dir", required=True, help="Path to KB root containing *.md")
    ap.add_argument("--out_dir", required=True, help="Output directory for index files")
    ap.add_argument("--model", default=MODEL_DEFAULT, help="Embedding model (default: BAAI/bge-m3)")
    ap.add_argument("--batch", type=int, default=64, help="Embedding batch size")
    ap.add_argument("--pattern", default=None, help="Optional glob pattern, e.g. '**/*.md'. If omitted, rglob('*.md').")
    args = ap.parse_args()

    kb = Path(args.kb_dir)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    # Collect files
    files = sorted(kb.glob(args.pattern)) if args.pattern else sorted(kb.rglob("*.md"))
    if not files:
        raise SystemExit(f"No Markdown files found in: {kb} (pattern={args.pattern or '*.md recursive'})")

    # Load model
    model = SentenceTransformer(args.model)
    emb_dim = model.get_sentence_embedding_dimension()

    metas, texts = [], []

    for p in files:
        raw = p.read_text(encoding="utf-8")
        fm, body_md = extract_front_matter(raw)
        title = fm.get("title", p.stem)
        doc_id = fm.get("id", p.stem)

        # normalize source text
        body = md_to_plain(body_md)

        pieces = split_with_positions(body)  # (text, start_w, end_w, start_c, end_c)
        for i, (chunk_text, sw, ew, sc, ec) in enumerate(pieces):
            metas.append({
                "doc_path": str(p),
                "doc_id": doc_id,
                "title": title,
                "chunk_id": f"{doc_id}::chunk-{i:04d}",
                "start_word": sw,
                "end_word": ew,
                "start_char": sc,
                "end_char": ec
            })
            texts.append(chunk_text)

    # Encode
    t0 = time.time()
    emb = model.encode(
        texts,
        batch_size=args.batch,
        convert_to_numpy=True,
        show_progress_bar=True,
        normalize_embeddings=True  # IP on L2-norm = cosine
    ).astype("float32")
    build_secs = time.time() - t0

    # Index
    index = faiss.IndexFlatIP(emb_dim)
    index.add(emb)

    # Save
    faiss.write_index(index, str(out / "faiss.index"))
    np.save(out / "embeddings.npy", emb)
    with open(out / "metadata.jsonl", "w", encoding="utf-8") as f:
        for m in metas:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")

    info = {
        "model_name": args.model,
        "model_link": MODEL_LINK,
        "embedding_dim": int(emb_dim),
        "chunks_total": int(emb.shape[0]),
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "chunking": {
            "unit": "words",
            "chunk_size": WORD_CHUNK_SIZE,
            "overlap": WORD_CHUNK_OVERLAP,
            "separators": SEPARATORS
        }
    }
    with open(out / "INDEX_INFO.json", "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    print(json.dumps(info, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
