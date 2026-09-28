from typing import Any,TypedDict

class ResearchState(TypedDict):
    ##USER QUERY
    query:str
    constraints:list[dict[str,Any]]
    research_type:str
    output_requirments:str

    #PLANNNING AND PLOTTING

    plan:str
    task:str
    current_task:str
    completed_task:str 

    # sources
    sources:list[dict[str]]
    sources_metadata:list[dict[str]]

    #Analysis 
    analysis:str

    #Final Output 
    final_output:str

    #tool calls
    tools_used: list[dict[str,Any]]
    tools_output: list[dict[str,Any]]

    #errors
    errors: list[dict[str,Any]]
    





   