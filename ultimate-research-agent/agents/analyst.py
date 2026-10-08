import json
from state import ResearchState
from llm import llm

from prompts.analyst import ANALYST_PROMPT

def analyst_agent(state:ResearchState)->dict:
    """Evaluate whether the gathered evidence is sufficient to answer the query."""
    query=state['query']
    goal=state.get('goal',"")
    research_type=state.get('research_type',"general")
    constraints=state.get("constraints","")
    output_requirements=state.get("output_requirements","")
    current_task=state.get("current_task","")
    sources=state.get("sources","")
    tool_result=state.get("tool_results","")

    if not sources and not tool_result:
        return{
            "errors":["there were no relevant sources"]

        }

    prompt=ANALYST_PROMPT.format(
        query=query,
        goal=goal,
        research_type=research_type,
        constraints=constraints,
        output_requirements=output_requirements,
        current_task=current_task,
        sources=sources,
        tool_result=tool_result,

    )

    response=llm.invoke(prompt)

    response_text=response.content

    try:
        result=json.loads(response_text)

    except json.JSONDecodeError:
        return{
            "errors":["Analyst return an invalid json responnse."]

        }

    analysis=result.get("analysis","")

    research_sufficient=result.get(
        "research_sufficient",
        False
    )

    missing_information=result.get("missing_information",[])

    return{
        "analysis":analysis,
        "research_sufficient":research_sufficient,
        "missing_information":missing_information,
    }









