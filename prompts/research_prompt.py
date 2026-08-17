import json 
from state import ResearchState
from llm import llm 

def planner_agent(state:ResearchState) -> ResearchState:
    query=state["query"]
    constraints=state.get["constraints",()]
    


