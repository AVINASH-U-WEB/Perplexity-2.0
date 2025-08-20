import httpx
from bs4 import BeautifulSoup
from langchain.tools import tool
from app.cache import cache, make_key
from app.providers import get_llm

USER_AGENT = "AI-Agent-Fetcher/1.0"

def _extract_text(html: str, max_chars: int):
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        t.decompose()
    
    title = (soup.title.string.strip() if soup.title and soup.title.string else "")
    text = "\n\n".join(p.get_text(separator=" ").strip() for p in soup.find_all("p") if p)
    
    return f"Title: {title}\n\nContent:\n{text[:max_chars]}"

@tool
def web_get(url: str, max_chars: int = 4000) -> str:
    """
    Fetches and extracts the main textual content from a given URL.
    Use this tool when the user provides a specific URL to read or summarize.
    """
    key = make_key("web_get", url, max_chars)
    cached = cache.get(key)
    if cached:
        return cached

    try:
        headers = {"User-Agent": USER_AGENT}
        with httpx.Client(timeout=10.0, follow_redirects=True) as client:
            r = client.get(url, headers=headers)
            r.raise_for_status()
    except Exception as e:
        return f"Error fetching {url}: {e}"

    extracted_content = _extract_text(r.text, max_chars=max_chars)
    
    prompt = f"Please summarize the following content from the URL {url}:\n\n{extracted_content}"
    llm = get_llm()
    
    try:
        response = llm.invoke(prompt)
        summary = response.content if hasattr(response, 'content') else str(response)
        output = f"Summary from {url}:\n\n{summary}"
        cache.set(key, output, ttl=3600)
        return output
    except Exception as e:
        return f"Error generating summary: {e}"