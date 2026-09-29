from state import ResearchState


def request_handler(query: str) -> ResearchState:
    return {
        "query": query,

        "goal": "",
        "research_type": "general",

        "constraints": {},
        "output_requirements": {},

        "plan": [],
        "tasks": [],
        "completed_tasks": [],
        "current_task": {},

        "sources": [],
        "source_metadata": [],

        "analysis": "",
        "final_report": "",

        "tool_calls": [],
        "tool_results": [],

        "errors": [],
    }
