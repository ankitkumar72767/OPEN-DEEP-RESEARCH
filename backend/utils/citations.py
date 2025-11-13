
from typing import List, Dict

def flatten_references(qa_blocks: List[dict]) -> List[dict]:
    """
    Returns a flat list of unique {title,url,published_time} ordered by first appearance.
    """
    seen = set()
    refs = []
    for b in qa_blocks:
        for r in b.get("results", []):
            url = r.get("url") or ""
            if url and url not in seen:
                seen.add(url)
                refs.append({
                    "title": r.get("title") or url,
                    "url": url,
                    "published_time": r.get("published_time", ""),
                })
    return refs
