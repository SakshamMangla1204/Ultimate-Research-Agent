from state import ResearchState
from tools.web_search import web_search


def researcher_agent(state: ResearchState) -> dict:
    """Execute the current task by collecting evidence from the web."""
    current_task = state.get("current_task", {})

    if not current_task:
        return {
            "errors": ["Researcher received no current task from the state, please try again."]
        }

    if isinstance(current_task, dict):
        task_description = current_task.get("description", "") or current_task.get("task", "")
        task_id = current_task.get("id")
    else:
        task_description = str(current_task)
        task_id = None

    if not task_description:
        return {
            "errors": ["There is no task description found in the current task."]
        }

    search_results = web_search(task_description)

    if not search_results:
        return {
            "errors": ["No search results were found, please try again."]
        }

    # Clean search results: keep only entries with url + content.
    cleaned_sources = []
    for result in search_results:
        title = result.get("title", "")
        url = result.get("url", "")
        content = result.get("content", "")

        if not url or not content:
            continue

        cleaned_sources.append(
            {
                "title": title,
                "url": url,
                "content": content,
            }
        )

    if not cleaned_sources:
        return {
            "errors": [f"The sources could not be cleaned for the task: {task_description}"]
        }

    tool_call = {
        "tool": "tavily_search",
        "query": task_description,
    }

    tool_result = {
        "task": task_description,
        "results": search_results,
    }

    completed_tasks = list(state.get("completed_tasks", []))
    if task_id and task_id not in completed_tasks:
        completed_tasks = completed_tasks + [task_id]

    return {
        "sources": cleaned_sources,
        "source_metadata": state.get("source_metadata", []),
        "tool_calls": state.get("tool_calls", []) + [tool_call],
        "tool_results": state.get("tool_results", []) + [tool_result],
        "completed_tasks": completed_tasks,
        "current_task": {},
    }

