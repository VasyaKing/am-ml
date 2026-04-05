import argparse, json
from pathlib import Path
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

def load_metadata(path: Path):
    meta = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            meta.append(json.loads(line))
    return meta

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index_dir", required=True, help="Папка с faiss.index, embeddings.npy, metadata.jsonl")
    ap.add_argument("--model", default="BAAI/bge-m3")
    ap.add_argument("--query", required=True, help="Строка запроса")
    ap.add_argument("--top_k", type=int, default=5)
    args = ap.parse_args()

    idx_dir = Path(args.index_dir)
    model = SentenceTransformer(args.model)

    # эмбеддинг запроса
    q_vec = model.encode([args.query], normalize_embeddings=True, convert_to_numpy=True)[0].astype("float32")

    # загрузка индекса
    index = faiss.read_index(str(idx_dir / "faiss.index"))
    meta = load_metadata(idx_dir / "metadata.jsonl")

    # поиск
    D, I = index.search(q_vec.reshape(1, -1), args.top_k)
    results = []
    for rank, (i, score) in enumerate(zip(I[0].tolist(), D[0].tolist()), 1):
        m = meta[i]
        results.append({
            "rank": rank,
            "score": round(float(score), 4),
            "chunk_id": m["chunk_id"],
            "title": m["title"],
            "path": m["doc_path"]
        })

    print(json.dumps({"query": args.query, "results": results}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
