"""Web fetch tool: safely retrieve and extract readable text from a URL.

The ``validate_url`` helper performs basic SSRF protection by only
allowing ``http``/``https`` URLs whose hostname resolves to globally
routable IP addresses (blocking localhost / private / link-local
targets).
"""

from __future__ import annotations

import ipaddress
import socket
from html.parser import HTMLParser
from typing import Any
from urllib.parse import urlparse

import requests

# Tags whose textual content should be ignored entirely.
_SKIP_TAGS = {"script", "style", "noscript", "template", "head"}

# Tags that represent a hard break between blocks of text.
_BLOCK_TAGS = {
    "p", "div", "section", "article", "header", "footer", "aside",
    "ul", "ol", "li", "table", "tr", "td", "th",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "blockquote", "pre", "br", "hr", "figure", "figcaption",
}


class _TextExtractor(HTMLParser):
    """Extract human-readable text from HTML while dropping boilerplate."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in _SKIP_TAGS:
            self._skip_depth += 1
        elif tag in _BLOCK_TAGS:
            self._chunks.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in _SKIP_TAGS and self._skip_depth > 0:
            self._skip_depth -= 1
        elif tag in _BLOCK_TAGS:
            self._chunks.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth == 0 and data.strip():
            self._chunks.append(data)

    def text(self) -> str:
        raw = " ".join(self._chunks)
        lines = [line.strip() for line in raw.splitlines()]
        return "\n".join(line for line in lines if line)


def _extract_text(html: str) -> str:
    """Return the readable text content of an HTML document."""
    parser = _TextExtractor()
    parser.feed(html)
    return parser.text()


def validate_url(url: str) -> bool:
    """Check whether the URL uses HTTP/HTTPS and resolves only to
    globally reachable IPs.

    Returns ``True`` when the URL is safe to fetch, otherwise ``False``.
    """
    if not isinstance(url, str):
        return False

    try:
        parsed = urlparse(url.strip())
    except ValueError:
        return False

    # Only allow http/https.
    if parsed.scheme not in ("http", "https"):
        return False

    hostname = parsed.hostname
    if not hostname:
        return False

    # Reject URLs that embed credentials (user:pass@host).
    if parsed.username or parsed.password:
        return False

    try:
        # Resolve the hostname and inspect every returned IP address.
        addrinfo = socket.getaddrinfo(hostname, None)
    except (ValueError, OSError, socket.gaierror):
        return False

    addresses = {info[4][0] for info in addrinfo}
    if not addresses:
        return False

    for address in addresses:
        try:
            ip = ipaddress.ip_address(address)
        except ValueError:
            return False
        if not ip.is_global:
            return False

    return True


def web_fetch(url: str, timeout: int = 20) -> dict[str, Any]:
    """Fetch a URL and return a normalized result.

    Returns a dict with keys: ``url``, ``status``, ``title``, ``content``.
    On failure it returns the same shape with an ``error`` key instead of
    ``content``.
    """
    result: dict[str, Any] = {
        "url": url,
        "status": None,
        "title": "",
        "content": "",
    }

    if not isinstance(url, str) or not url.strip():
        result["error"] = "Invalid URL provided."
        return result

    if not validate_url(url):
        result["error"] = "URL failed safety validation (scheme or host not allowed)."
        return result

    try:
        response = requests.get(
            url.strip(),
            timeout=timeout,
            headers={"User-Agent": "UltimateResearchAgent/1.0"},
        )
    except requests.RequestException as exc:
        result["error"] = f"Request failed: {exc}"
        return result

    result["status"] = response.status_code

    if response.status_code != 200:
        result["error"] = f"Unexpected HTTP status {response.status_code}."
        return result

    # Prefer HTML parsing; fall back to raw text for non-HTML responses.
    content_type = response.headers.get("Content-Type", "")
    if "html" in content_type.lower():
        html = response.text
        title = ""
        start = html.lower().find("<title")
        if start != -1:
            start = html.find(">", start)
            end = html.lower().find("</title>", start)
            if start != -1 and end != -1:
                title = html[start + 1 : end].strip()
        result["title"] = title
        result["content"] = _extract_text(html)
    else:
        result["content"] = response.text.strip()

    return result