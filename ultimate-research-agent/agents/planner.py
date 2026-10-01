import json

from llm import llm
from state import ResearchState
from prompts.planner import PLANNER_PROMPT


def planner_agent(state: ResearchState) -> dict:
    """Planner agent is only responsible to plan how the actions will take place and structures the user request into an actionable research plan."""
    query = state["query"]
    goal = state.get("goal", "")
    research_type = state.get("research_type", "general")
    constraints = state.get("constraints", {})
    output_requirements = state.get("output_requirements", {})

    prompt = PLANNER_PROMPT.format(
        query=query,
        goal=goal,
        research_type=research_type,
        constraints=constraints,
        output_requirements=output_requirements,
    )

    response = llm.invoke(prompt)
    response_text = response.content

    try:
        result = json.loads(response_text)

    except json.JSONDecodeError:
        return {
            "errors": [
                "planner returned an invalid JSON response."
            ]
        }

    tasks = result.get("tasks", [])

    current_task = tasks[0] if tasks else {}

    return {
        "goal": result.get("goal", ""),
        "research_type": result.get("research_type", ""),
        "constraints": result.get("constraints", ""),
        "output_requirements": result.get("output_requirements", ""),
        "plan": result.get("plan", ""),
        "tasks": tasks,
        "current_task": current_task,
    }

