from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.providers import get_llm
import json

# Note: These functions are not currently used by search_tools.py but are
# available here for future enhancement of the search tool.

def heuristic_rerank(query: str, results: List[Dict], top_k: int = 5) -> List[Dict]:
    """Reranks results based on TF-IDF cosine similarity."""
    if not results:
        return []
    texts = [(r.get("title","") + " " + r.get("snippet","")).strip() for r in results]
    vectorizer = TfidfVectorizer().fit([query] + texts)
    qv = vectorizer.transform([query])
    dv = vectorizer.transform(texts)
    scores = cosine_similarity(qv, dv).flatten()
    for i, r in enumerate(results):
        r["_score"] = float(scores[i])
    return sorted(results, key=lambda x: x["_score"], reverse=True)[:top_k]

def llm_rerank(query: str, results: List[Dict], top_k: int = 5) -> List[Dict]:
    """Reranks results using an LLM to assign relevance scores."""
    if not results:
        return []

    items = [f"{i}) Title: {r.get('title', '')}\nSnippet: {r.get('snippet', '')}" for i, r in enumerate(results[:10])]
    prompt = (
        "You are a search-ranking assistant. Given the user query and the following search results, "
        "assign a relevance score from 0-100 to each result. Return a JSON array of objects with 'index' and 'score' keys.\n\n"
        f"User query: {query}\n\nResults:\n" + "\n\n".join(items) + "\n\nReturn only the JSON array."
    )

    llm = get_llm()
    try:
        resp = llm.invoke(prompt)
        raw_json = resp.content if hasattr(resp, "content") else str(resp)
        parsed = json.loads(raw_json)
        score_map = {p["index"]: p["score"] for p in parsed}
        for i, r in enumerate(results):
            r["_score"] = float(score_map.get(i, 0))
        return sorted(results, key=lambda x: x["_score"], reverse=True)[:top_k]
    except Exception:
        return heuristic_rerank(query, results, top_k=top_k) # Fallback