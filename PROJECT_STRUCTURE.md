# The Ultimate Research Agent — Project Structure & Content Reference

> **Purpose of this document:** a complete, readable map of the repository. Every file is
> listed with the exact content it currently holds (verbatim, in code blocks), so this
> document alone describes the whole project without needing to open each file.
>
> **Verified against commit:** `0189cb2` — *"Initial commit: General Research Agent with
> LangGraph pipeline"* (branch `main`).
>
> **Honest status of the repo:** **44 files tracked at commit `0189cb2`** (45 on disk, counting
> the gitignored `.env`), but **only 11 contain any content**. The other **34 are 0-byte
> placeholders**. There are **two parallel copies** of the project (a flat root layout and a
> nested `ultimate-research-agent/` package). Neither copy is runnable as-is — details in
> [Section 8](#8-honest-status-gaps-and-inconsistencies).
>
> **Note on `.env`:** this file exists on disk but is **ignored by git** (it is listed in
> `.gitignore`), so `git ls-tree` does not count it. It is documented here in Section 3.1
> because it is part of your working environment — and it holds live-looking API keys.


---

## 1. Top-Level Directory Tree

```text
General Research agent/                  <- repo root
│
├── .env                                 (341 B)  secrets — API keys (see warning in §3.1)
│                                                  *** .gitignored: on disk, NOT in git ***
├── .gitignore                           ( 64 B)
├── requirements.txt                     (727 B)  root dependency list
├── config.py                            (544 B)  app + LLM + Tavily constants
├── logger.py                            (210 B)  logging config (module-level only)
├── state.py                             (536 B)  ResearchState TypedDict
├── main.py                              (  0 B)  EMPTY entrypoint
│
├── agents/
│   ├── __init__.py                      (  0 B)  EMPTY
│   └── research_agent.py                (  0 B)  EMPTY
│
├── graph/
│   ├── __init__.py                      (  0 B)  EMPTY
│   ├── builder.py                       (  0 B)  EMPTY
│   ├── edges.py                         (  0 B)  EMPTY
│   └── nodes.py                         (  0 B)  EMPTY
│
├── prompts/
│   ├── __init__.py                      (  0 B)  EMPTY
│   └── research_prompt.py               (200 B)  planner_agent stub (incomplete, broken)
│
├── tools/
│   ├── __init__.py                      (  0 B)  EMPTY
│   └── tavily_search.py                 (  0 B)  EMPTY
│
├── tests/
│   └── __init__.py                      (  0 B)  EMPTY   (no tests exist)
│
├── utils/
│   ├── formatter.py                     (  0 B)  EMPTY
│   └── validator.py                     (  0 B)  EMPTY
│       (note: there is NO utils/__init__.py)
│
└── ultimate-research-agent/             <- second, partially-written copy
    ├── main.py                          (268 B)  working LLM smoke test
    ├── config.py                        (735 B)  MODEL_NAME/TEMPERATURE + Config class
    ├── llm.py                           (326 B)  ChatGoogleGenerativeAI singleton
    ├── logger.py                        (  0 B)  EMPTY
    ├── state.py                         (  0 B)  EMPTY
    ├── requirements.txt                 (  0 B)  EMPTY
    │
    ├── agents/
    │   ├── __init__.py                  (  0 B)  EMPTY
    │   ├── planner.py                   (  0 B)  EMPTY
    │   ├── researcher.py                (  0 B)  EMPTY
    │   ├── analyst.py                   (  0 B)  EMPTY
    │   ├── synthesizer.py               (  0 B)  EMPTY
    │   └── request_handler.py           (  0 B)  EMPTY
    │
    ├── graph/
    │   ├── __init__.py                  (  0 B)  EMPTY
    │   └── research_graph.py            (673 B)  LangGraph wiring (complete, no compile())
    │
    ├── prompts/
    │   ├── __init__.py                  (  0 B)  EMPTY
    │   ├── planner.py                   (  0 B)  EMPTY
    │   ├── researcher.py                (  0 B)  EMPTY
    │   ├── analyst.py                   (  0 B)  EMPTY
    │   ├── synthesizer.py               (  0 B)  EMPTY
    │   └── request_handler.py           (  0 B)  EMPTY
    │
    ├── tools/
    │   ├── __init__.py                  (  0 B)  EMPTY
    │   ├── web_search.py                (  0 B)  EMPTY
    │   └── web_fetch.py                 (  0 B)  EMPTY
    │
    └── utils/
        ├── __init__.py                  (  0 B)  EMPTY
        └── helpers.py                   (  0 B)  EMPTY
```

### File count summary

Verified with `git ls-tree -r HEAD --name-only` plus per-file byte counts (`.git/`, `.venv/`,
`__pycache__/` excluded):

| Set | Count |
|---|---|
| Files **tracked in git** at `0189cb2` | **44** |
| Files **on disk** (the 44 tracked + the untracked, gitignored `.env`) | **45** |
| Files that are **empty (0 bytes)** | **34** |
| Files that **contain content** | **11** |

`.env` is `.gitignore`d, so it is *not* one of the 44 tracked files, yet it *is* on disk — the
reason the two totals differ by one.

Per-directory breakdown (authoritative, generated from git):

| Directory | Tracked files | Empty | With content |
|---|---|---|---|
| `.` (repo root, non-recursive) | 44 | 34 | 10 |
| `agents/` | 2 | 2 | 0 |
| `graph/` | 4 | 4 | 0 |
| `prompts/` | 2 | 1 | 1 |
| `tools/` | 2 | 2 | 0 |
| `tests/` | 1 | 1 | 0 |
| `utils/` | 2 | 2 | 0 |
| `ultimate-research-agent/` (recursive) | 25 | 21 | 4 |

The root row is the recursive total; the rows under it are nested subsets, so the correct
non-double-counted split is:

| Group | Files | With content | Empty |
|---|---|---|---|
| Root-level files (`config.py`, `logger.py`, `state.py`, `main.py`, `.gitignore`, `requirements.txt`) | 6 | 5 | 1 (`main.py`) |
| Root `agents/` + `graph/` + `tools/` + `tests/` + `utils/` | 11 | 0 | 11 |
| Root `prompts/` | 2 | 1 | 1 |
| `ultimate-research-agent/**` | 25 | 4 | 21 |
| **Tracked total** | **44** | **10** | **34** |
| `.env` (untracked, on disk) | 1 | 1 | 0 |
| **Working-tree total** | **45** | **11** | **34** |

**The two numbers that matter: 11 files contain content; 34 files are 0 bytes.**




---

## 2. Intended Package Responsibilities (what each folder is for)

| Path | Intended role (inferred from naming + partial code) |
|---|---|
| `config.py` | Single source of truth for app metadata, model name/temperature, search settings. |
| `logger.py` | Shared configured `logging` handler used by every module. |
| `state.py` | The shared graph state object (`ResearchState`) passed between all nodes. |
| `llm.py` (nested only) | Builds and exports the one `ChatGoogleGenerativeAI` instance. |
| `agents/` | One module per graph node: the *behaviour* (prompt -> LLM -> state update). |
| `prompts/` | The *text* of each agent's instruction / system prompt, kept out of logic. |
| `graph/` | The LangGraph topology: node registration, edges, conditional routing, `compile()`. |
| `tools/` | External capabilities — Tavily web search, page fetching. |
| `utils/` | Cross-cutting helpers: output formatting, input validation. |
| `tests/` | Unit/integration tests for nodes, tools, and state transitions. |

---

## 3. Verbatim File Contents (the 11 non-empty files)

> Sections 3.1–3.7 are the root-layout files; 3.8–3.11 are the nested `ultimate-research-agent/`
> files. `.env` (3.1) is gitignored but present on disk, which is why 11 files contain content
> while only 10 are tracked.

### 3.1 `.env` — WARNING: plaintext secrets, please rotate

```dotenv
TAVILY_API_KEY="<redacted>"
GROQ_API_KEY="<redacted>"
MISTRAL_API_KEY="<redacted>"
GOOGLE_API_KEY="<redacted>"
LANGSMITH_API_KEY="<redacted>"
```

**Warnings you should act on:**
- These are **live-looking credentials**. `.env` is listed in `.gitignore`, so it is not
  tracked in commit `0189cb2` — but the values are exposed the moment this file is shared,
  pasted, or committed by accident. **Rotate all five keys** at Tavily / Groq / Mistral /
  Google AI Studio / LangSmith.
- The `GOOGLE_API_KEY` value does not look like a standard Google AI Studio key (those begin
  `AIza...`). It resembles an OAuth-style token, so the Gemini calls in `llm.py` may fail
  authentication even when the variable is present.
- `GROQ_API_KEY`, `MISTRAL_API_KEY` and `LANGSMITH_API_KEY` are currently **unused** anywhere.

### 3.2 `.gitignore`

```gitignore
.env
.venv/
__pycache__/
*.pyc
.DS_Store
venv/
.env.local
*.log
```

### 3.3 `config.py` (root) — verbatim

```python
#======================================================
#application information
#=====================================================
APP_NAME='The Ultimate Research Agent'
APP_VERSION='1.0.0'
#===================================================
#LLM CONFIGURATION
#======================================================
MODEL_NAME='gemini-2.5-flash'
TEMPERATURE=0.3
#===================================================
#TAVILY SEARCH 
#==================================================
MAX_SEARCH_RESULTS=5
SEARCH_DEAPTH="basic"
DEBUG=True
```

Notes: `SEARCH_DEAPTH` is a misspelling of "DEPTH"; `MAX_SEARCH_RESULTS` here is **5**, but the
nested `Config` class uses **10** — pick one value and share it.

### 3.4 `logger.py` (root) — verbatim

```python
import logging 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
level=logging.INFO
format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"

# --- the real logger.py ENDS on the line above; everything below is a SUGGESTION ---
# import logging
# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
# logger = logging.getLogger("research_agent")
```

Issues: it exposes **no logger object** (nothing can import it), and lines 6-7 are unused loose
variables that duplicate the `basicConfig` values. The commented lines above show the
conventional shape, not current content.

### 3.5 `state.py` (root) — verbatim

```python

from typing import Any, TypedDict


class ResearchState(TypedDict):

    # User Request
    query: str
    goal: str
    research_type: str
    constraints: dict[str, Any]
    output_requirements: dict[str, Any]

    # Planning
    plan: list[dict[str, Any]]
    tasks: list[dict[str, Any]]
    completed_tasks: list[str]
    current_task: dict[str, Any]

    # Sources
    sources: list[dict[str, Any]]
    source_metadata: list[dict[str, Any]]

    # Tools
    tool_calls: list[dict[str, Any]]
    tool_results: list[dict[str, Any]]
```

This is the **most complete design artifact in the repo** — 13 fields covering request,
planning, sourcing and tool-use. Gaps: there is **no `analysis` field** for the analyst node's
output, **no `final_report` / `report`** field for the synthesizer, **no `errors` / `messages`**
field for retries, and no `Annotated[..., add_messages]`-style reducer (so list fields are
replaced, not appended, on each node return). A `TypedDict` graph state also generally requires
every key to be supplied in the initial input dict.

### 3.6 `prompts/research_prompt.py` (root) — verbatim

```python
import json 
from state import ResearchState
from llm import llm 

def planner_agent(state:ResearchState) -> ResearchState:
    query=state["query"]
    constraints=state.get["constraints",()]
```

(Note: the real file has a **trailing whitespace line** after `constraints=state.get[...]`, which
is why it is 200 bytes. Trailing blank/whitespace lines are omitted here as they carry no meaning.)

Issues (this file is the clearest example of the work-in-progress state):
- Line 7 `state.get["constraints",()]` — **`get` is a method, so this raises `TypeError`**
  (should be `state.get("constraints", {})`; `()` is also the wrong default for a dict field).
- The function has **no return statement** and no body — it cannot satisfy its own
  `-> ResearchState` annotation.
- It imports `json` and `llm` but uses neither yet.
- A *planner* living in `prompts/research_prompt.py` (rather than in `agents/`) blurs the
  agents/prompts separation used by the nested copy.

### 3.7 `requirements.txt` (root) — verbatim

```text
altair==6.2.2
langchain-google-genai
python-dotenv
anyio==4.14.2
attrs==26.1.0
blinker==1.9.0
certifi==2026.7.22
charset-normalizer==3.4.9
click==8.4.2
gitdb==4.0.12
GitPython==3.1.57
h11==0.16.0
httptools==0.8.0
idna==3.18
itsdangerous==2.2.0
Jinja2==3.1.6
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
MarkupSafe==3.0.3
narwhals==2.24.0
numpy==2.5.1
packaging==26.2
pandas==3.0.5
pillow==12.3.0
protobuf==7.35.1
pyarrow==24.0.0
pydeck==0.9.3
python-dateutil==2.9.0.post0
python-multipart==0.0.32
referencing==0.37.0
requests==2.34.2
rpds-py==2026.6.3
six==1.17.0
smmap==5.0.3
starlette==1.3.1
streamlit==1.60.0
tenacity==9.1.4
toml==0.10.2
typing_extensions==4.16.0
urllib3==2.7.0
uvicorn==0.52.1
websockets==16.1.1
```

Important gaps: **`langgraph` is missing** even though `research_graph.py` imports it, and
**`tavily-python` (or `langchain-tavily`) is missing** even though `tools/` is built around
Tavily. The list also mixes direct dependencies with a large transitive/Streamlit stack
(`streamlit`, `altair`, `pandas`, `pyarrow`, `uvicorn`, `websockets`) — consistent with
`pip freeze` output rather than a curated file.

### 3.8 `ultimate-research-agent/main.py` — verbatim

```python
from llm import llm


def main():
    print("The Ultimate Research Agent")
    print("Tell me, how can I help you?")

    response = llm.invoke("Introduce yourself in one line")

    print("Response")
    print(response.content)


if __name__ == "__main__":
    main()
```

This is currently the **only executable entrypoint in the project**. It ignores the graph
entirely and simply asks the LLM to introduce itself. It also cannot run from the repo root
because `llm` is imported as a top-level module — you must `cd ultimate-research-agent` first
(or run it as a script from that directory).

### 3.9 `ultimate-research-agent/config.py` — verbatim

```python
"""Configuration settings for the Ultimate Research Agent."""

# LLM Configuration
MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.3


class Config:
    """Central configuration for the research agent pipeline."""

    def __init__(self):
        # Model configuration
        self.model_name = MODEL_NAME
        self.temperature = TEMPERATURE
        self.max_tokens = 4096

        # Search configuration
        self.search_engine = "tavily"
        self.max_search_results = 10
        self.search_timeout = 30

        # Pipeline configuration
        self.max_planning_iterations = 3
        self.enable_analyst = True

        # Logging configuration
        self.log_level = "INFO"
        self.log_file = "research_agent.log"
```

Note `max_planning_iterations` and `enable_analyst` imply a **conditional/looping graph** that
`research_graph.py` does not yet implement (its edges are strictly linear).

### 3.10 `ultimate-research-agent/llm.py` — verbatim

```python
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from config import MODEL_NAME, TEMPERATURE

# Load environment variables from .env file
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    api_key=os.getenv("GOOGLE_API_KEY")
)
```

`load_dotenv()` with no argument searches upward from the current working directory — so it
finds the root `.env` only when run from inside the repo. `max_tokens` from `Config` is never
passed here.

### 3.11 `ultimate-research-agent/graph/research_graph.py` — verbatim

```python
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
```

This file **cannot be imported today**: the four `agents.*` modules it imports are all empty,
so `planner_agent` (etc.) do not exist -> `ImportError`. It also never calls `builder.compile()`
and defines no `graph`/`app` object, so there is nothing for `main.py` to invoke.
`request_handler.py` exists in `agents/` and `prompts/` but is **not registered as a node** —
the intended entry node appears to be missing from the graph.

---

## 4. The Empty Files (34 files, all 0 bytes)

Every file below is **0 bytes** — present in the tree but containing nothing, not even a
newline. They are the scaffolding for the intended design:

| # | Path | What it is meant to hold |
|---|---|---|
| 1 | `main.py` | Root CLI/app entrypoint: build input state, invoke the compiled graph. |
| 2 | `agents/__init__.py` | Package marker; likely re-exports the agent callables. |
| 3 | `agents/research_agent.py` | Root-layout agent implementation. |
| 4 | `graph/__init__.py` | Package marker; likely exports `graph`/`app`. |
| 5 | `graph/builder.py` | `StateGraph(ResearchState)` construction + `compile()`. |
| 6 | `graph/edges.py` | Edge and conditional-routing definitions. |
| 7 | `graph/nodes.py` | Node registration / node-name constants. |
| 8 | `prompts/__init__.py` | Package marker. |
| 9 | `tools/__init__.py` | Package marker. |
| 10 | `tools/tavily_search.py` | Tavily client wrapper returning structured results. |
| 11 | `tests/__init__.py` | Test package marker (no test modules exist). |
| 12 | `utils/formatter.py` | Report/citation formatting helpers. |
| 13 | `utils/validator.py` | Input/state validation helpers. |
| 14 | `ultimate-research-agent/logger.py` | Shared logger for the nested package. |
| 15 | `ultimate-research-agent/state.py` | `ResearchState` for the nested package. |
| 16 | `ultimate-research-agent/requirements.txt` | Dependencies for the nested package. |
| 17 | `ultimate-research-agent/agents/__init__.py` | Package marker. |
| 18 | `ultimate-research-agent/agents/planner.py` | `planner_agent` — turns query into a task plan. |
| 19 | `ultimate-research-agent/agents/researcher.py` | `researcher_agent` — runs searches, gathers sources. |
| 20 | `ultimate-research-agent/agents/analyst.py` | `analyst_agent` — evaluates/critiques gathered evidence. |
| 21 | `ultimate-research-agent/agents/synthesizer.py` | `synthesizer_agent` — writes the final report. |
| 22 | `ultimate-research-agent/agents/request_handler.py` | Parses the raw user request (entry node, unregistered). |
| 23 | `ultimate-research-agent/graph/__init__.py` | Package marker. |
| 24 | `ultimate-research-agent/prompts/__init__.py` | Package marker. |
| 25 | `ultimate-research-agent/prompts/planner.py` | Planner prompt text. |
| 26 | `ultimate-research-agent/prompts/researcher.py` | Researcher prompt text. |
| 27 | `ultimate-research-agent/prompts/analyst.py` | Analyst prompt text. |
| 28 | `ultimate-research-agent/prompts/synthesizer.py` | Synthesizer prompt text. |
| 29 | `ultimate-research-agent/prompts/request_handler.py` | Request-handler prompt text. |
| 30 | `ultimate-research-agent/tools/__init__.py` | Package marker. |
| 31 | `ultimate-research-agent/tools/web_search.py` | Web search tool wrapper. |
| 32 | `ultimate-research-agent/tools/web_fetch.py` | Page fetch/scrape tool wrapper. |
| 33 | `ultimate-research-agent/utils/__init__.py` | Package marker. |
| 34 | `ultimate-research-agent/utils/helpers.py` | Shared helper functions. |

Also note: there is **no `utils/__init__.py` in the root `utils/`**, and there is **no
`ultimate-research-agent/tests/`** directory at all.

---

## 5. The Two Copies, Side by Side

The same architectural idea is expressed twice with different names and layouts:

| Concern | Root layout | Nested `ultimate-research-agent/` |
|---|---|---|
| State | `state.py` (13 fields, complete) | `state.py` (empty) |
| LLM client | `from llm import llm` (no `llm.py` exists!) | `llm.py` (implemented) |
| Config | `config.py` (constants only) | `config.py` (constants + `Config` class) |
| Entrypoint | `main.py` (empty) | `main.py` (LLM smoke test) |
| Graph | `graph/builder.py`, `edges.py`, `nodes.py` (all empty) | `graph/research_graph.py` (wired, uncompiled) |
| Agents | `agents/research_agent.py` + `planner_agent` misplaced in `prompts/` | `agents/{planner,researcher,analyst,synthesizer,request_handler}.py` (all empty) |
| Prompts | `prompts/research_prompt.py` (broken stub) | `prompts/{planner,researcher,analyst,synthesizer,request_handler}.py` (all empty) |
| Search | `tools/tavily_search.py` (empty) | `tools/web_search.py`, `web_fetch.py` (empty) |
| Utils | `utils/{formatter,validator}.py` (empty) | `utils/helpers.py` (empty) |

**Recommendation:** choose **one** layout. The nested copy has the cleaner separation
(agents vs. prompts, a real `llm.py`, a real `Config`) and is the better base — but the root
copy has the only complete `state.py`. The best starting point is the nested layout with the
root `state.py` moved into it.

---

## 6. Dependency & Import Graph (as currently resolvable)

```text
ultimate-research-agent/main.py
└── llm.py
    ├── config.py            (MODEL_NAME, TEMPERATURE)
    ├── dotenv.load_dotenv()
    └── langchain_google_genai.ChatGoogleGenerativeAI

ultimate-research-agent/graph/research_graph.py
├── langgraph.graph.{StateGraph, START, END}
├── state.py                 (EMPTY -> ResearchState undefined)      FAIL
├── agents.planner           (EMPTY -> planner_agent undefined)      FAIL
├── agents.researcher        (EMPTY -> researcher_agent undefined)   FAIL
├── agents.analyst           (EMPTY -> analyst_agent undefined)      FAIL
└── agents.synthesizer       (EMPTY -> synthesizer_agent undefined)  FAIL

prompts/research_prompt.py (root)
├── state.py                 (exists)
├── llm.py                   (DOES NOT EXIST in root)                FAIL
└── json                     (unused)
```

## 7. Intended Runtime Flow

As designed by `graph/research_graph.py` plus the `agents/` and `prompts/` module names:

```text
                 ┌─────────────────────────────────────────────┐
   user query →  │ (request_handler)  <- defined, NOT wired    │
                 └───────────────────┬─────────────────────────┘
                                     │  (missing edge)
                                     ▼
   START ──▶ planner ──▶ researcher ──▶ analyst ──▶ synthesizer ──▶ END
              │             │            │              │
              │             │            │              └─ writes final report
              │             │            └─ critiques / decides sufficiency
              │             └─ Tavily search + page fetch -> sources[]
              └─ query -> plan[] / tasks[]
```

Each node receives `ResearchState`, calls `llm`, and returns a **partial dict** that LangGraph
merges into the state. So the canonical node signature is
`def x_agent(state: ResearchState) -> dict:` (or `-> ResearchState` if returning the full state).

Config hints (`max_planning_iterations=3`, `enable_analyst=True`) suggest the analyst step was
meant to be able to **loop back** to the researcher — which requires
`builder.add_conditional_edges(...)`, absent today.

---

## 8. Honest Status: Gaps and Inconsistencies

### Blocking issues (nothing runs end-to-end today)
1. **34 of 45 files are empty**, including every `agents/*` module the graph imports -> `ImportError`.
2. **`langgraph` is not in `requirements.txt`**, though it is imported.
3. **`tavily-python` / `langchain-tavily` is not in `requirements.txt`**, though `tools/` targets Tavily.
4. **`prompts/research_prompt.py:7` is a guaranteed `TypeError`** (`state.get[...]` instead of `state.get(...)`).
5. **Root `prompts/research_prompt.py` imports `llm`, but no `llm.py` exists at the repo root.**
6. **`research_graph.py` never calls `.compile()`** and exposes no runnable app object.
7. **`request_handler` exists as a module but is never added as a node.**
8. **`state.py` has no `final_report` / `analysis` / `errors` fields**, so the analyst and
   synthesizer have nowhere to write their output.
9. **Two parallel project copies** with drifting constants (`MAX_SEARCH_RESULTS` = 5 vs. 10).
10. **No tests exist** (`tests/` contains only an empty `__init__.py`).

### Security / hygiene
11. **Five API keys sit in a plaintext `.env`.** Rotate them; keep `.env` untracked and commit a
    `.env.example` with placeholder values instead.
12. `GOOGLE_API_KEY` uses a non-standard token format, so Gemini auth likely fails.
13. `logger.py` exposes no logger object, so no module can log through it.
14. Root `utils/` is missing `__init__.py`, so `from utils.formatter import ...` will not resolve
    as a regular package.

### Naming / style inconsistencies
15. Mixed quoting (`'...'` in config, `"..."` elsewhere), mixed spacing (`builder=StateGraph`,
    `"researcher",'analyst'`), and inconsistent casing in `config.py`.
16. Typo: `SEARCH_DEAPTH`.
17. Root `prompts/` contains *logic* (`planner_agent`), contradicting the prompt-text vs.
    agent-logic separation used in the nested copy.

---

## 9. What a Working Skeleton Looks Like (smallest coherent target)

```text
ultimate-research-agent/
├── .env.example                 # placeholders only
├── requirements.txt             # langgraph, langchain-google-genai, tavily-python, python-dotenv
├── config.py                    # Config class (single source of constants)
├── logger.py                    # logger = logging.getLogger(...)
├── state.py                     # ResearchState (+ final_report, analysis, errors)
├── llm.py                       # configured ChatGoogleGenerativeAI
├── main.py                      # build input state -> app.invoke(state)
├── agents/
│   ├── request_handler.py       # parse the raw request into structured fields
│   ├── planner.py               # query -> plan[], tasks[]
│   ├── researcher.py            # tasks -> sources[], tool_results[]
│   ├── analyst.py               # sources -> analysis (sufficient? loop or continue)
│   └── synthesizer.py           # analysis + sources -> final_report
├── prompts/                     # pure prompt text, one module per agent
├── graph/
│   └── research_graph.py        # add nodes + conditional edges + app = builder.compile()
├── tools/
│   ├── web_search.py            # Tavily search
│   └── web_fetch.py             # page extraction
├── utils/
│   ├── formatter.py             # citations / markdown report assembly
│   └── validator.py             # input & state validation
└── tests/
    └── test_graph.py            # node-level + end-to-end smoke tests
```

---

## 10. Quick Reference — Commands That Should Work

```bash
# From the repo root
cd "/Users/sakshammangla/Documents/General Research agent"

# List every file with sizes (shows the empties instantly)
find . -type f -not -path './.git/*' -not -path './.venv/*' -not -path '*/__pycache__/*' \
  -exec wc -c {} \; | sort -k2

# The only currently runnable code (needs deps installed first)
cd ultimate-research-agent && python main.py     # prints a one-line LLM self-introduction

# Dependency install (note: langgraph and tavily are NOT in the current file)
pip install -r requirements.txt langgraph tavily-python
```

### Reproduce the numbers in this document

```bash
cd "/Users/sakshammangla/Documents/General Research agent"

# Every file on disk with its size — the 0-byte files are the empty scaffolding
find . -type f -not -path './.git/*' -not -path './.venv/*' \
  -not -path '*/__pycache__/*' -exec wc -c {} \; | sort -k2

# Totals
echo "tracked:  $(git ls-tree -r HEAD --name-only | wc -l)"
echo "on disk:  $(find . -type f -not -path './.git/*' -not -path './.venv/*' \
  -not -path '*/__pycache__/*' | wc -l)"
echo "empty:    $(find . -type f -not -path './.git/*' -not -path './.venv/*' \
  -not -path '*/__pycache__/*' -size 0 | wc -l)"

# Per-directory tracked / empty counts (as used in Section 1)
for d in agents graph prompts tools tests utils ultimate-research-agent; do
  n=$(git ls-tree -r HEAD --name-only -- "$d" | wc -l | tr -d ' ')
  e=$(for f in $(git ls-tree -r HEAD --name-only -- "$d"); do
        c=$(git show "HEAD:$f" | wc -c | tr -d ' '); [ "$c" = "0" ] && echo x
      done | wc -l | tr -d ' ')
  echo "$d | tracked=$n | empty=$e"
done

# Confirm the root import can never resolve (no llm.py at repo root)
ls llm.py 2>&1 || echo 'expected: root llm.py is missing but prompts/research_prompt.py imports it'
```

---

*Document generated from a full read of every file at commit `0189cb2`. All code blocks above
are reproduced exactly as they exist on disk; empty files are described rather than quoted.*
