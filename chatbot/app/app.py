from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from utils import load_index

TOP_K = 5
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

app = FastAPI(title="Local FAISS Chatbot")

class AskRequest(BaseModel):
    question: str
    top_k: Optional[int] = None

class AskResponse(BaseModel):
    matches: List[str]

_index = None
_chunks = None
_embedder = None

def get_embedder():
    global _embedder
    if _embedder is None:
        _embedder = SentenceTransformer(MODEL_NAME)
    return _embedder

def get_index():
    global _index, _chunks
    if _index is None or _chunks is None:
        _index, _chunks = load_index()
    return _index, _chunks

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    try:
        k = req.top_k or TOP_K
        index, chunks = get_index()
        embedder = get_embedder()
        qvec = embedder.encode([req.question], normalize_embeddings=True, convert_to_numpy=True)
        D, I = index.search(qvec, k)
        results = []
        for idx in I[0]:
            if idx == -1:
                continue
            results.append(chunks[idx])
        return AskResponse(matches=results)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
