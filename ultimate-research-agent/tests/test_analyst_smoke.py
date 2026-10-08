import json, sys, types, pathlib

# Stub llm so we don't need real API keys / network for this smoke test.
llm_mod = types.ModuleType("llm")

class FakeResp:
    content = json.dumps({
        "analysis": "Evidence covers the query adequately.",
        "research_sufficient": True,
        "missing_information": [],
    })

class FakeLLM:
    def invoke(self, prompt):
        assert "Query:" in prompt and "Sources:" in prompt, "prompt missing expected sections"
        return FakeResp()

llm_mod.llm = FakeLLM()
sys.modules["llm"] = llm_mod

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from agents.analyst import analyst_agent

# Case 1: happy path
state = {
    "query": "What causes auroras?",
    "goal": "Explain auroras",
    "research_type": "general",
    "constraints": {},
    "output_requirements": {},
    "current_task": {"id": "task_1", "description": "research auroras"},
    "sources": [{"title": "Aurora 101", "url": "https://x", "content": "solar wind"}],
    "tool_results": [{"task": "research auroras", "results": []}],
}
out = analyst_agent(state)
print("case1:", out)
assert out["analysis"].startswith("Evidence"), out
assert out["research_sufficient"] is True
assert out["missing_information"] == []

# Case 2: no sources at all -> error path, no LLM call
out2 = analyst_agent({"query": "q", "sources": [], "tool_results": []})
print("case2:", out2)
assert out2 == {"errors": ["there were no relevant sources"]}, out2

print("SMOKE_OK")
