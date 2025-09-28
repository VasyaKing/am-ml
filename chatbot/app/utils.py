import os
import faiss
import numpy as np
from typing import List, Tuple

INDEX_DIR = "/app/faiss_index"
INDEX_FILE = os.path.join(INDEX_DIR, "index.faiss")
META_FILE  = os.path.join(INDEX_DIR, "meta.npy")  # stores text chunks

def ensure_dirs():
    os.makedirs(INDEX_DIR, exist_ok=True)

def save_index(index: faiss.IndexFlatIP, chunks: List[str]):
    ensure_dirs()
    faiss.write_index(index, INDEX_FILE)
    np.save(META_FILE, np.array(chunks, dtype=object), allow_pickle=True)

def load_index() -> Tuple[faiss.IndexFlatIP, List[str]]:
    ensure_dirs()
    if not (os.path.exists(INDEX_FILE) and os.path.exists(META_FILE)):
        raise FileNotFoundError("FAISS index not found. Please run ingest first.")
    index = faiss.read_index(INDEX_FILE)
    chunks = np.load(META_FILE, allow_pickle=True).tolist()
    return index, chunks
