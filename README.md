# The Ultimate Research Agent

A multi-agent research pipeline built with **LangGraph** and **LangChain**. Give it a question and it plans the research, searches the web, analyzes the gathered sources, and synthesizes a cited final report.

- **LLM:** Google Gemini 2.5 Flash (default), with Mistral and Groq as alternates
- **Search:** Tavily web search + page fetch tools
- **Pipeline:** `planner → researcher → analyst → synthesizer`

## Project Layout

This repository contains two copies of the project:

```text
General Research agent/                  <- repo root (early scaffolding)
├── config.py, logger.py, state.py, main.py
├── agents/  graph/  prompts/  tools/  utils/  tests/   (mostly empty stubs)
│
└── ultimate-research-agent/             <- active, working implementation
    ├── main.py                # entrypoint / LLM smoke test
    ├── llm.py                 # ChatGoogleGenerativeAI / ChatMistralAI / ChatGroq
    ├── config.py              # Config class — single source of settings
    ├── state.py               # ResearchState TypedDict
    ├── agents/
    │   ├── request_handler.py # parse raw request into structured state
    │   ├── planner.py         # query -> plan[], tasks[]
    │   ├── researcher.py      # tasks -> sources[], tool_results[]
    │   ├── analyst.py         # sources -> analysis (sufficient? loop or continue)
    │   └── synthesizer.py     # analysis + sources -> final_report
    ├── prompts/               # one prompt module per agent
    ├── graph/research_graph.py# nodes, edges, compiled app
    ├── tools/                 # web_search.py (Tavily), web_fetch.py
    ├── utils/                 # helpers
    └── tests/                 # smoke tests
```

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for a full file-by-file reference.

## Pipeline

| Node | Responsibility |
|------|----------------|
| `request_handler` | Normalize the raw query into `ResearchState` |
| `planner` | Break the query into a plan and concrete research tasks |
| `researcher` | Execute tasks with Tavily search/fetch, collect `sources` |
| `analyst` | Judge whether sources are sufficient; request more if not |
| `synthesizer` | Produce the final cited report (`final_report`) |

State flows linearly: `START → planner → researcher → analyst → synthesizer → END`.

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt
pip install langgraph tavily-python langchain-mistralai langchain-groq
```

### Environment Variables

Create a `.env` file in the repo root (it is gitignored — never commit it):

```bash
GOOGLE_API_KEY=your_google_api_key      # required (default model)
MISTRAL_API_KEY=your_mistral_api_key    # required by llm.py at import time
GROQ_API_KEY=your_groq_api_key          # required by llm.py at import time
TAVILY_API_KEY=your_tavily_api_key      # required by tools/web_search.py
```

> **Note:** `llm.py` validates all three LLM keys at import time, so all of the
> above must be set even if you only use the default Gemini model.

## Usage

```bash
cd ultimate-research-agent
python main.py
```

This runs a one-line LLM smoke test. To run the full graph, compile
`graph/research_graph.py` and invoke it with an initial state built by
`agents/request_handler.py`.

## Configuration

Edit `ultimate-research-agent/config.py`:

```python
DEFAULT_MODEL = "gemini"        # "gemini" | "mistral" | "groq"
GEMINI_MODEL = "gemini-2.5-flash"
GROQ_MODEL = "llama-3.3-70b-versatile"
MISTRAL_MODEL = "mistral-large-latest"
MODEL_TEMPERATURE = 0.3
```

The `Config` class additionally exposes search settings (`max_search_results`,
`search_timeout`), pipeline settings (`max_planning_iterations`,
`enable_analyst`), and logging settings.

## Tests

```bash
cd ultimate-research-agent
python -m pytest tests/
```

## License

No license file has been added yet.
