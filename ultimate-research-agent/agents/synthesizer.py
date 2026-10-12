from state import ResearchState

from llm import llm

from prompts.synthesizer import SYNTHESIZER_PROMPT


def synthesizer_agent(state: ResearchState) -> dict:
    """The synthesizer agent is responsible for formatting and preparing the final answer that will be delivered to the user."""
    query = state["query"]
    goal = state.get("goal", "")
    sources = state.get("sources", [])
    analysis = state.get("analysis", "")
    constraints = state.get("constraints", "")
    output_requirements = state.get("output_requirements", "")

    if not sources:
        return {
            "errors": ["Synthesizer: there is no research available to synthesize."]
        }

    prompt = SYNTHESIZER_PROMPT.format(
        query=query,
        goal=goal,
        sources=sources,
        constraints=constraints,
        analysis=analysis,
        output_requirements=output_requirements,
    )

    response = llm.invoke(prompt)
    final_report = response.content

    if not isinstance(final_report, str) or not final_report.strip():
        return {
            "errors": ["Synthesizer: the LLM returned an empty or invalid report."]
        }

    return {
        "final_report": final_report.strip()
    }
