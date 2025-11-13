from typing import List, Dict
from tavily import TavilyClient

class SearcherAgent:
    def __init__(self, tavily_key: str):
        # Tavily client initialize
        self.client = TavilyClient(api_key=tavily_key)

    def search(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Returns a list of dicts: {title, url, content, published_time (if any)}
        """
        res = self.client.search(
            query=query,
            max_results=max_results,
            include_images=False
        )

        items = []
        for r in res.get("results", []):
            items.append({
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "content": r.get("content", ""),
                "published_time": r.get("published_time", ""),
            })
        return items
