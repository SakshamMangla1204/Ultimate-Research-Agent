from langgraph.graph import StateGraph,START,END
from state import ResearchState

from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.synthesizer import synthesizer_agent

def route_after_analyst(state: ResearchState) -> str:
    if state.get("research_sufficient", False):
        return "synthesizer"

    return "researcher"

builder=StateGraph(ResearchState)

builder.add_node("planner",planner_agent)
builder.add_node("researcher",researcher_agent)
builder.add_node("analyst",analyst_agent)
builder.add_node("synthesizer",synthesizer_agent)

builder.add_edge(START,"planner")
builder.add_edge("planner","researcher")
builder.add_edge("researcher",'analyst')
builder.add_conditional_edges(
    "analyst",
    route_after_analyst,
    {
        "researcher": "researcher",
        "synthesizer": "synthesizer",
    },
)
builder.add_edge("synthesizer",END)

graph=builder.compile()
