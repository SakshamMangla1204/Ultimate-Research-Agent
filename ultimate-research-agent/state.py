from typing import Any, TypedDict


class ResearchState(TypedDict, total=False):
    # User request (set by request_handler)
    query: str
    goal: str
    research_type: str
    constraints: dict[str, Any]
    output_requirements: dict[str, Any]

    # Planning (set by planner)
    plan: Any
    tasks: list[Any]
    current_task: dict[str, Any]
    completed_tasks: list[Any]

    # Sources (set by researcher)
    sources: list[dict[str, Any]]
    source_metadata: list[dict[str, Any]]

    # Analysis / final output
    analysis: str
    final_report: str

    # Tool tracking
    tool_calls: list[dict[str, Any]]
    tool_results: list[dict[str, Any]]

    # Errors
    errors: list[str]
