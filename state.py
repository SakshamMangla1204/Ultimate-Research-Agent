
from typing import Any, TypedDict


class ResearchState(TypedDict):

    # User Request
    query: str
    goal: str
    research_type: str
    constraints: dict[str, Any]
    output_requirements: dict[str, Any]

    # Planning
    plan: list[dict[str, Any]]
    tasks: list[dict[str, Any]]
    completed_tasks: list[str]
    current_task: dict[str, Any]

    # Sources
    sources: list[dict[str, Any]]
    source_metadata: list[dict[str, Any]]

    # Tools
    tool_calls: list[dict[str, Any]]
    tool_results: list[dict[str, Any]]
