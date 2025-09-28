import os
import glob
from sentence_transformers import SentenceTransformer
import faiss
from utils import save_index

DATA_DIR = "/data"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 120
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def chunk_text(text: str, chunk_size: int, overlap: int):
    if len(text) <= chunk_size:
        return [text]
    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(text), step):
        chunks.append(text[i:i+chunk_size])
        if i + chunk_size >= len(text):
            break
    return chunks

def main():
    files = glob.glob(os.path.join(DATA_DIR, "*.txt"))
    if not files:
        print("No .txt files found in /data.")
        return

    all_chunks = []
    for f in files:
        with open(f, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read().strip()
            chunks = chunk_text(content, CHUNK_SIZE, CHUNK_OVERLAP)
            for c in chunks:
                all_chunks.append(f"[{os.path.basename(f)}] {c}")

    print(f"Total chunks: {len(all_chunks)}")

    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(all_chunks, normalize_embeddings=True, convert_to_numpy=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    save_index(index, all_chunks)
    print("FAISS index built and saved.")

if __name__ == "__main__":
    main()
