from langgraph.graph import StateGraph,START,END
from state import ResearchState

from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.synthesizer import synthesizer_agent

builder=StateGraph(ResearchState)

builder.add_node("planner",planner_agent)
builder.add_node("researcher",researcher_agent)
builder.add_node("analyst",analyst_agent)
builder.add_node("synthesizer",synthesizer_agent)

builder.add_edge(START,"planner")
builder.add_edge("planner","researcher")
builder.add_edge("researcher",'analyst')
builder.add_edge("analyst","synthesizer")
builder.add_edge("synthesizer",END)
