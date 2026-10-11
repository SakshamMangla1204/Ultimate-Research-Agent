from state import ResearchState

from llm import llm

from prompts import synthesizer_prompt


def synthesizer_agent(state: ResearchState) -> dict:

    """The Synthesizer is responsible for taking the research and analysis
    and converting them into a clear, concise report that the user can
    easily read and understand."""

    query = state["query"]

    goal = state.get("goal")

    sources = state.get("sources")

    analysis = state.get("analysis")

    constraints = state.get("constraints")

    output_requirements = state.get("output_requirements")

    if not sources:
        return{
            "errors":["there is no research available"]
        }

    prompt=synthesizer_prompt.format(
        query=query,
        goal=goal,
        sources=sources,
        analysis=analysis,
        constraints=constraints,
        output_requirements=output_requirements,
    )

    response=llm.invoke(prompt)
    final_report=response.content
    


    

    

    

    