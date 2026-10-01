"""Web search tool using the Tavily API."""

import os
from typing import Any

from dotenv import load_dotenv
from tavily import TavilyClient

from config import Config

load_dotenv()

_config = Config()
_api_key = os.getenv("TAVILY_API_KEY")
if not _api_key:
    raise ValueError("TAVILY_API_KEY is not set")

_client = TavilyClient(api_key=_api_key)


def web_search(query: str, max_results: int | None = None) -> list[dict[str, Any]]:
    """Search the web and return a normalized list of results.

    Each result is a dict with keys: title, url, content.
    Returns an empty list when nothing useful is found.
    """
    if not query or not query.strip():
        return []

    limit = max_results or _config.max_search_results

    response = _client.search(
        query=query,
        max_results=limit,
        include_answer=False,
        include_raw_content=False,
    )

    raw_results = response.get("results", []) if isinstance(response, dict) else []

    normalized: list[dict[str, Any]] = []
    for item in raw_results:
        if not isinstance(item, dict):
            continue
        normalized.append(
            {
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "content": item.get("content", ""),
            }
        )

    return normalized

