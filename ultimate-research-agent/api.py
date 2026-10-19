"""HTTP adapter for the flux.ai frontend.

Run with ``uvicorn api:app --reload`` from this project directory. The graph
itself remains the same synchronous LangGraph workflow used by main.py.
"""
from __future__ import annotations

from datetime import datetime, timezone
from time import perf_counter
from typing import Any
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="flux.ai Research API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class ResearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=10_000)


@app.get("/health")
def health() -> dict[str, str]:
    """Report API availability without initializing provider clients."""
    return {"status": "ok", "service": "flux.ai"}


@app.post("/research")
def run_research(request: ResearchRequest) -> dict[str, Any]:
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=422, detail="Query must not be empty.")

    # Import here so /health works even if provider keys have not been set.
    try:
        from graph.research_graph import graph
    except Exception as error:
        # Keep credentials and tracebacks out of the HTTP response.
        message = str(error)
        if "API KEY" in message.upper() or "API_KEY" in message.upper():
            detail = "The selected research model is not configured. Check the provider keys in the backend .env file."
        else:
            detail = "The research graph could not be initialized. Check backend configuration and logs."
        raise HTTPException(status_code=503, detail=detail) from error

    run_id = str(uuid4())
    started_at = datetime.now(timezone.utc)
    start = perf_counter()
    initial_state = {
        "query": query,
        "errors": [],
        "sources": [],
        "source_metadata": [],
        "tool_calls": [],
        "tool_results": [],
        "completed_tasks": [],
    }

    try:
        result = graph.invoke(initial_state, config={"recursion_limit": 30})
    except Exception as error:
        # Log server-side for diagnosis, but do not expose exception details
        # that may contain provider or search configuration.
        print(f"Research run {run_id} failed: {type(error).__name__}")
        message = str(error).lower()
        if any(marker in message for marker in ("resourceexhausted", "quota exceeded", "rate limit", "429")):
            detail = "The configured model provider is rate limited or out of quota. Check its usage and billing, or configure a different provider in config.py."
        elif any(marker in message for marker in ("api key", "api_key", "unauthorized", "401", "403")):
            detail = "The configured model or search provider rejected its credentials. Check the backend .env keys."
        else:
            detail = "Research execution failed. Check backend logs for details."
        raise HTTPException(status_code=502, detail=detail) from error

    completed_at = datetime.now(timezone.utc)
    sources = result.get("sources") or []
    safe_sources = [
        {
            "title": str(source.get("title") or "Untitled source"),
            "url": str(source.get("url") or ""),
            "content": str(source.get("content") or ""),
        }
        for source in sources
        if isinstance(source, dict) and source.get("url")
    ]
    report = result.get("final_report")
    errors = [str(item) for item in (result.get("errors") or [])]
    if not report:
        raise HTTPException(
            status_code=502,
            detail="The research graph completed without producing a report. " + (errors[0] if errors else ""),
        )

    return {
        "id": run_id,
        "query": query,
        "status": "completed",
        "report": str(report),
        "sources": safe_sources,
        "errors": errors,
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration": round(perf_counter() - start, 2),
    }
