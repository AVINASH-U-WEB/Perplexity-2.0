import os
from typing import List, Dict
from langchain.tools import tool
from app.cache import cache, make_key
from dotenv import load_dotenv

load_dotenv()

def _search_tavily(query: str, max_results: int = 5) -> List[Dict]:
    try:
        from tavily import TavilyClient
        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        data = client.search(query=query, max_results=max_results, search_depth="basic")
        return [{"title": r.get("title"), "url": r.get("url"), "snippet": r.get("content")} for r in data.get("results", [])]
    except Exception as e:
        print(f"Tavily search failed: {e}")
        return []

def _search_serpapi(query: str, max_results: int = 5) -> List[Dict]:
    try:
        from serpapi import GoogleSearch
        params = {"engine": "google", "q": query, "num": max_results, "api_key": os.getenv("SERPAPI_API_KEY")}
        search = GoogleSearch(params)
        res = search.get_dict()
        return [{"title": r.get("title"), "url": r.get("link"), "snippet": r.get("snippet")} for r in res.get("organic_results", [])]
    except Exception as e:
        print(f"SerpApi search failed: {e}")
        return []

def _search_ddg(query: str, max_results: int = 5) -> List[Dict]:
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=max_results)
            return [{"title": r.get("title"), "url": r.get("href"), "snippet": r.get("body")} for r in results]
    except Exception as e:
        print(f"DuckDuckGo search failed: {e}")
        return []

def _compact(results: List[Dict]) -> str:
    lines = []
    for i, r in enumerate(results, 1):
        lines.append(f"{i}. Title: {r.get('title')}\n   Snippet: {r.get('snippet')}\n   Source: {r.get('url')}")
    return "\n\n".join(lines) if lines else "No results found."

@tool
def web_search(query: str, max_results: int = 5) -> str:
    """
    Performs a web search using multiple providers and returns compacted results.
    Useful for finding up-to-date information, news, or general facts.
    """
    key = make_key("web_search", query, max_results)
    cached = cache.get(key)
    if cached:
        return cached

    providers = []
    if os.getenv("TAVILY_API_KEY"): providers.append(_search_tavily)
    if os.getenv("SERPAPI_API_KEY"): providers.append(_search_serpapi)
    providers.append(_search_ddg)

    results = []
    for search_func in providers:
        try:
            results = search_func(query, max_results)
            if results:
                print(f"Got results from {search_func.__name__}")
                break
        except Exception:
            continue
    
    compacted_results = _compact(results)
    cache.set(key, compacted_results, ttl=3600)
    return compacted_results