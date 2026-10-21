# Architecture Context

## System

- Project: `ultimate-research-agent`
- Target Path: `/Users/sakshammangla/Documents/General Research agent/ultimate-research-agent`
- Dominant Directories: `agents`, `prompts`, `tools`, `graph`, `utils`
- Dependency Shape: 13 subsystem links, 135 ambiguous edges, 1 tagged entrypoints, 0 enriched docs
- Summary: ultimate-research-agent contains 17 subsystems, 13 cross-subsystem flows, 0 processed documents, and 77 external dependencies derived from 171 extracted code nodes.

## Subsystem Inventory

### tools [MEDIUM]

- Kind: `module`
- Summary: tools is a module subsystem covering 1 paths and 22 symbols; strongest evidence: calls x23, imports x7.
- Paths: `tools/web_fetch.py`
- Key Symbols: `web_fetch()`, `validate_url()`, `_extract_text()`, `url.strip`, `__future__`
- Depends On: `subsystem-1-0-agents`, `subsystem-3-0-agents`, `subsystem-5-0-tools`
- Depended On By: `none`
- Responsibilities: Primary symbols: call_reference x13, import_reference x6.; Internal relations: calls x20, imports x6.
- Evidence: tools/web_fetch.py:_extract_text(), tools/web_fetch.py:validate_url(), tools/web_fetch.py:web_fetch()

### agents [MEDIUM]

- Kind: `module`
- Summary: agents is a module subsystem covering 4 paths and 18 symbols; strongest evidence: calls x57, contains x4.
- Paths: `agents/analyst.py`, `agents/planner.py`, `agents/researcher.py`, `agents/synthesizer.py`
- Key Symbols: `researcher_agent()`, `analyst_agent()`, `planner_agent()`, `synthesizer_agent()`, `isinstance`
- Depends On: `none`
- Depended On By: `subsystem-0-0-tools`, `subsystem-1-1-main-py`, `subsystem-3-0-agents`, `subsystem-4-0-tests`, `subsystem-7-0-tools`
- Responsibilities: Primary symbols: call_reference x14, function x4.; Internal relations: calls x51.; Exposes 1 interface candidate.
- Evidence: agents/analyst.py:analyst_agent(), agents/analyst.py:ANALYST_PROMPT.format, agents/analyst.py:json.loads

### main.py [MEDIUM]

- Kind: `module`
- Summary: main.py is a module subsystem covering 1 paths and 2 symbols; strongest evidence: calls x9, imports x1.
- Paths: `main.py`
- Key Symbols: `main()`, `print`
- Depends On: `subsystem-1-0-agents`, `subsystem-2-0-config-py`
- Depended On By: `subsystem-4-0-tests`
- Responsibilities: Primary symbols: function x1, call_reference x1.; Internal relations: calls x5, contains x1.; Exposes 3 interface candidates.
- Evidence: main.py:main(), main.py:print, main.py:main.py

### config.py [LOW]

- Kind: `adapter`
- Summary: config.py is a adapter subsystem covering 3 paths and 16 symbols; strongest evidence: imports x16, calls x16.
- Paths: `config.py`, `llm.py`, `tools/web_search.py`
- Key Symbols: `Config`, `dotenv`, `os`, `ValueError`, `load_dotenv`
- Depends On: `subsystem-3-0-agents`, `subsystem-7-0-tools`
- Depended On By: `subsystem-1-1-main-py`, `subsystem-3-0-agents`
- Responsibilities: Primary symbols: call_reference x8, import_reference x6.; Internal relations: calls x16, imports x10.; Exposes 1 interface candidate.
- Evidence: config.py:Config, config.py:Config.__init__(), config.py:config.py

### agents [MEDIUM]

- Kind: `ui`
- Summary: agents is a ui subsystem covering 10 paths and 8 symbols; strongest evidence: imports x25, calls x10.
- Paths: `agents/analyst.py`, `agents/planner.py`, `agents/request_handler.py`, `agents/researcher.py`, `agents/synthesizer.py`, `graph/research_graph.py`, `prompts/analyst.py`, `prompts/planner.py`, `prompts/synthesizer.py`, `state.py`
- Key Symbols: `json`, `typing`, `request_handler()`, `langgraph.graph`, `StateGraph`
- Depends On: `subsystem-1-0-agents`, `subsystem-2-0-config-py`
- Depended On By: `subsystem-0-0-tools`, `subsystem-2-0-config-py`, `subsystem-4-0-tests`
- Responsibilities: Primary symbols: import_reference x3, call_reference x3.; Internal relations: imports x17, calls x10.; Exposes 2 interface candidates.
- Evidence: agents/analyst.py:json, agents/analyst.py:agents/analyst.py, agents/planner.py:agents/planner.py

### tests [MEDIUM]

- Kind: `domain`
- Summary: tests is a domain subsystem covering 1 paths and 13 symbols; strongest evidence: calls x14, imports x5.
- Paths: `tests/test_analyst_smoke.py`
- Key Symbols: `FakeResp`, `FakeLLM`, `FakeLLM.invoke()`, `pathlib`, `sys`
- Depends On: `subsystem-1-0-agents`, `subsystem-1-1-main-py`, `subsystem-3-0-agents`
- Depended On By: `none`
- Responsibilities: Primary symbols: call_reference x7, import_reference x3.; Internal relations: calls x10, imports x3.
- Evidence: tests/test_analyst_smoke.py:FakeLLM, tests/test_analyst_smoke.py:FakeResp, tests/test_analyst_smoke.py:FakeLLM.invoke()

### tools [MEDIUM]

- Kind: `domain`
- Summary: tools is a domain subsystem covering 1 paths and 12 symbols; strongest evidence: calls x10, contains x6.
- Paths: `tools/web_fetch.py`
- Key Symbols: `_TextExtractor`, `_TextExtractor.text()`, `_TextExtractor.handle_data()`, `append`, `_TextExtractor.__init__()`
- Depends On: `none`
- Depended On By: `subsystem-0-0-tools`
- Responsibilities: Primary symbols: call_reference x6, method x5.; Internal relations: calls x9, contains x5.
- Evidence: tools/web_fetch.py:_TextExtractor, tools/web_fetch.py:_TextExtractor.__init__(), tools/web_fetch.py:_TextExtractor.handle_data()

### utils [MEDIUM]

- Kind: `shared_library`
- Summary: utils is a shared_library subsystem covering 1 paths and 5 symbols; strongest evidence: contains x3, calls x3.
- Paths: `utils/helpers.py`
- Key Symbols: `is_non_empty_text()`, `clean_text()`, `text.strip`, `truncate_text()`, `bool`
- Depends On: `none`
- Depended On By: `none`
- Responsibilities: Primary symbols: function x3, call_reference x2.; Internal relations: contains x3, calls x3.; Exposes 1 interface candidate.
- Evidence: utils/helpers.py:clean_text(), utils/helpers.py:is_non_empty_text(), utils/helpers.py:truncate_text()

### tools [MEDIUM]

- Kind: `adapter`
- Summary: tools is a adapter subsystem covering 1 paths and 6 symbols; strongest evidence: calls x9, contains x1.
- Paths: `tools/web_search.py`
- Key Symbols: `web_search()`, `_client.search`, `item.get`, `normalized.append`, `query.strip`
- Depends On: `subsystem-1-0-agents`
- Depended On By: `subsystem-2-0-config-py`
- Responsibilities: Primary symbols: call_reference x5, function x1.; Internal relations: calls x7.; Exposes 2 interface candidates.
- Evidence: tools/web_search.py:web_search(), tools/web_search.py:_client.search, tools/web_search.py:item.get

### agents [MEDIUM]

- Kind: `module`
- Summary: agents is a module subsystem covering 1 paths and 0 symbols; strongest evidence: structure-only edges.
- Paths: `agents/__init__.py`
- Key Symbols: `none`
- Depends On: `none`
- Depended On By: `none`
- Responsibilities: none
- Evidence: agents/__init__.py:agents/__init__.py

### graph [MEDIUM]

- Kind: `module`
- Summary: graph is a module subsystem covering 1 paths and 0 symbols; strongest evidence: structure-only edges.
- Paths: `graph/__init__.py`
- Key Symbols: `none`
- Depends On: `none`
- Depended On By: `none`
- Responsibilities: none
- Evidence: graph/__init__.py:graph/__init__.py

### logger.py [MEDIUM]

- Kind: `infrastructure`
- Summary: logger.py is a infrastructure subsystem covering 1 paths and 0 symbols; strongest evidence: structure-only edges.
- Paths: `logger.py`
- Key Symbols: `none`
- Depends On: `none`
- Depended On By: `none`
- Responsibilities: none
- Evidence: logger.py:logger.py

### prompts [MEDIUM]

- Kind: `module`
- Summary: prompts is a module subsystem covering 1 paths and 0 symbols; strongest evidence: structure-only edges.
- Paths: `prompts/__init__.py`
- Key Symbols: `none`
- Depends On: `none`
- Depended On By: `none`
- Responsibilities: none
- Evidence: prompts/__init__.py:prompts/__init__.py

### prompts [MEDIUM]

- Kind: `service`
- Summary: prompts is a service subsystem covering 1 paths and 0 symbols; strongest evidence: structure-only edges.
- Paths: `prompts/request_handler.py`
- Key Symbols: `none`
- Depends On: `none`
- Depended On By: `none`
- Responsibilities: Exposes 1 interface candidate.
- Evidence: prompts/request_handler.py:prompts/request_handler.py

### prompts [MEDIUM]

- Kind: `module`
- Summary: prompts is a module subsystem covering 1 paths and 0 symbols; strongest evidence: structure-only edges.
- Paths: `prompts/researcher.py`
- Key Symbols: `none`
- Depends On: `none`
- Depended On By: `none`
- Responsibilities: none
- Evidence: prompts/researcher.py:prompts/researcher.py

### tools [MEDIUM]

- Kind: `module`
- Summary: tools is a module subsystem covering 1 paths and 0 symbols; strongest evidence: structure-only edges.
- Paths: `tools/__init__.py`
- Key Symbols: `none`
- Depends On: `none`
- Depended On By: `none`
- Responsibilities: none
- Evidence: tools/__init__.py:tools/__init__.py

### utils [MEDIUM]

- Kind: `shared_library`
- Summary: utils is a shared_library subsystem covering 1 paths and 0 symbols; strongest evidence: structure-only edges.
- Paths: `utils/__init__.py`
- Key Symbols: `none`
- Depends On: `none`
- Depended On By: `none`
- Responsibilities: none
- Evidence: utils/__init__.py:utils/__init__.py

## Interfaces

- `final_report.strip` [MEDIUM] in `subsystem-1-0-agents` as `database` from `agents/synthesizer.py`.
  Evidence: agents/synthesizer.py:final_report.strip, agents/synthesizer.py:calls, agents/synthesizer.py:calls
- `main()` [HIGH] in `subsystem-1-1-main-py` as `entrypoint` from `main.py`.
  Evidence: main.py:main(), main.py:calls, main.py:contains
- `main.py` [HIGH] in `subsystem-1-1-main-py` as `entrypoint` from `main.py`.
  Evidence: main.py:main.py, main.py:calls, main.py:contains
- `print` [HIGH] in `subsystem-1-1-main-py` as `entrypoint` from `main.py`.
  Evidence: main.py:print, tests/test_analyst_smoke.py:calls, tests/test_analyst_smoke.py:calls
- `prompts/request_handler.py` [HIGH] in `subsystem-12-0-prompts` as `route` from `prompts/request_handler.py`.
  Evidence: prompts/request_handler.py:prompts/request_handler.py
- `TavilyClient` [MEDIUM] in `subsystem-2-0-config-py` as `cli` from `tools/web_search.py`.
  Evidence: tools/web_search.py:TavilyClient, tools/web_search.py:calls
- `agents/request_handler.py` [HIGH] in `subsystem-3-0-agents` as `route` from `agents/request_handler.py`.
  Evidence: agents/request_handler.py:agents/request_handler.py, agents/request_handler.py:contains, agents/request_handler.py:imports
- `request_handler()` [HIGH] in `subsystem-3-0-agents` as `route` from `agents/request_handler.py`.
  Evidence: agents/request_handler.py:request_handler(), agents/request_handler.py:contains
- `truncate_text()` [MEDIUM] in `subsystem-6-0-utils` as `cli` from `utils/helpers.py`.
  Evidence: utils/helpers.py:truncate_text(), utils/helpers.py:contains
- `_client.search` [MEDIUM] in `subsystem-7-0-tools` as `cli` from `tools/web_search.py`.
  Evidence: tools/web_search.py:_client.search, tools/web_search.py:calls
- `query.strip` [MEDIUM] in `subsystem-7-0-tools` as `database` from `tools/web_search.py`.
  Evidence: tools/web_search.py:query.strip, tools/web_search.py:calls

## Key Flows

- `subsystem-0-0-tools` -> `subsystem-1-0-agents` [LOW] via `calls`: calls x2 Evidence: tools/web_fetch.py:calls, tools/web_fetch.py:calls
- `subsystem-0-0-tools` -> `subsystem-3-0-agents` [HIGH] via `imports`: imports x1 Evidence: tools/web_fetch.py:imports
- `subsystem-0-0-tools` -> `subsystem-5-0-tools` [HIGH] via `calls`: contains x1, calls x1 Evidence: tools/web_fetch.py:contains, tools/web_fetch.py:calls
- `subsystem-1-1-main-py` -> `subsystem-1-0-agents` [LOW] via `calls`: calls x1 Evidence: main.py:calls
- `subsystem-1-1-main-py` -> `subsystem-2-0-config-py` [MEDIUM] via `imports`: imports x1 Evidence: main.py:imports
- `subsystem-2-0-config-py` -> `subsystem-3-0-agents` [HIGH] via `imports`: imports x1 Evidence: tools/web_search.py:imports
- `subsystem-2-0-config-py` -> `subsystem-7-0-tools` [HIGH] via `contains`: contains x1 Evidence: tools/web_search.py:contains
- `subsystem-3-0-agents` -> `subsystem-1-0-agents` [HIGH] via `contains`: contains x4 Evidence: agents/analyst.py:contains, agents/planner.py:contains, agents/researcher.py:contains
- `subsystem-3-0-agents` -> `subsystem-2-0-config-py` [MEDIUM] via `imports`: imports x4 Evidence: agents/analyst.py:imports, agents/planner.py:imports, agents/researcher.py:imports
- `subsystem-4-0-tests` -> `subsystem-1-0-agents` [LOW] via `calls`: calls x1 Evidence: tests/test_analyst_smoke.py:calls
- `subsystem-4-0-tests` -> `subsystem-1-1-main-py` [LOW] via `calls`: calls x3 Evidence: tests/test_analyst_smoke.py:calls, tests/test_analyst_smoke.py:calls, tests/test_analyst_smoke.py:calls
- `subsystem-4-0-tests` -> `subsystem-3-0-agents` [HIGH] via `imports`: imports x2 Evidence: tests/test_analyst_smoke.py:imports, tests/test_analyst_smoke.py:imports
- `subsystem-7-0-tools` -> `subsystem-1-0-agents` [LOW] via `calls`: calls x2 Evidence: tools/web_search.py:calls, tools/web_search.py:calls

## Cross-Cutting Concerns


## Entrypoints

- `main()` [HIGH] from `main.py` in `subsystem-1-1-main-py`. Ranked as an entrypoint because it is tagged or named like a runtime root and has degree 3. Evidence: main.py:main(), main.py:calls, main.py:contains
- `main.py` [HIGH] from `main.py` in `subsystem-1-1-main-py`. Ranked as an entrypoint because it is tagged or named like a runtime root and has degree 2. Evidence: main.py:main.py, main.py:calls, main.py:contains
- `print` [HIGH] from `main.py` in `subsystem-1-1-main-py`. Ranked as an entrypoint because it is tagged or named like a runtime root and has degree 2. Evidence: main.py:print, tests/test_analyst_smoke.py:calls, tests/test_analyst_smoke.py:calls
- `prompts/request_handler.py` [HIGH] from `prompts/request_handler.py` in `subsystem-12-0-prompts`. Ranked as an entrypoint because it is tagged or named like a runtime root and has degree 0. Evidence: prompts/request_handler.py:prompts/request_handler.py
- `agents/request_handler.py` [HIGH] from `agents/request_handler.py` in `subsystem-3-0-agents`. Ranked as an entrypoint because it is tagged or named like a runtime root and has degree 2. Evidence: agents/request_handler.py:agents/request_handler.py, agents/request_handler.py:contains, agents/request_handler.py:imports
- `request_handler()` [HIGH] from `agents/request_handler.py` in `subsystem-3-0-agents`. Ranked as an entrypoint because it is tagged or named like a runtime root and has degree 1. Evidence: agents/request_handler.py:request_handler(), agents/request_handler.py:contains
- `TavilyClient` [MEDIUM] from `tools/web_search.py` in `subsystem-2-0-config-py`. Ranked as an entrypoint because it is tagged or named like a runtime root and has degree 1. Evidence: tools/web_search.py:TavilyClient, tools/web_search.py:calls
- `truncate_text()` [MEDIUM] from `utils/helpers.py` in `subsystem-6-0-utils`. Ranked as an entrypoint because it is tagged or named like a runtime root and has degree 1. Evidence: utils/helpers.py:truncate_text(), utils/helpers.py:contains
- `_client.search` [MEDIUM] from `tools/web_search.py` in `subsystem-7-0-tools`. Ranked as an entrypoint because it is tagged or named like a runtime root and has degree 1. Evidence: tools/web_search.py:_client.search, tools/web_search.py:calls

## External Dependencies

- `ANALYST_PROMPT.format` [LOW] used by `subsystem-1-0-agents` from `agents/analyst.py`. Evidence: agents/analyst.py:ANALYST_PROMPT.format, agents/analyst.py:calls
- `ChatGoogleGenerativeAI` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:ChatGoogleGenerativeAI, llm.py:calls
- `ChatGroq` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:ChatGroq, llm.py:calls
- `ChatMistralAI` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:ChatMistralAI, llm.py:calls
- `Config` [LOW] used by `subsystem-2-0-config-py` from `tools/web_search.py`. Evidence: tools/web_search.py:Config, tools/web_search.py:calls
- `PLANNER_PROMPT.format` [LOW] used by `subsystem-1-0-agents` from `agents/planner.py`. Evidence: agents/planner.py:PLANNER_PROMPT.format, agents/planner.py:calls
- `SYNTHESIZER_PROMPT.format` [LOW] used by `subsystem-1-0-agents` from `agents/synthesizer.py`. Evidence: agents/synthesizer.py:SYNTHESIZER_PROMPT.format, agents/synthesizer.py:calls
- `StateGraph` [LOW] used by `subsystem-3-0-agents` from `graph/research_graph.py`. Evidence: graph/research_graph.py:StateGraph, graph/research_graph.py:calls
- `TavilyClient` [LOW] used by `subsystem-2-0-config-py` from `tools/web_search.py`. Evidence: tools/web_search.py:TavilyClient, tools/web_search.py:calls
- `ValueError` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:ValueError, llm.py:calls, llm.py:calls
- `__future__` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:__future__, tools/web_fetch.py:imports
- `_client.search` [LOW] used by `subsystem-7-0-tools` from `tools/web_search.py`. Evidence: tools/web_search.py:_client.search, tools/web_search.py:calls
- `analyst_agent` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:analyst_agent, tests/test_analyst_smoke.py:calls, tests/test_analyst_smoke.py:calls
- `append` [LOW] used by `subsystem-5-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:append, tools/web_fetch.py:calls, tools/web_fetch.py:calls
- `bool` [LOW] used by `subsystem-6-0-utils` from `utils/helpers.py`. Evidence: utils/helpers.py:bool, utils/helpers.py:calls
- `builder.add_edge` [LOW] used by `subsystem-3-0-agents` from `graph/research_graph.py`. Evidence: graph/research_graph.py:builder.add_edge, graph/research_graph.py:calls, graph/research_graph.py:calls
- `builder.add_node` [LOW] used by `subsystem-3-0-agents` from `graph/research_graph.py`. Evidence: graph/research_graph.py:builder.add_node, graph/research_graph.py:calls, graph/research_graph.py:calls
- `cleaned_sources.append` [LOW] used by `subsystem-1-0-agents` from `agents/researcher.py`. Evidence: agents/researcher.py:cleaned_sources.append, agents/researcher.py:calls
- `content_type.lower` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:content_type.lower, tools/web_fetch.py:calls
- `current_task.get` [LOW] used by `subsystem-1-0-agents` from `agents/researcher.py`. Evidence: agents/researcher.py:current_task.get, agents/researcher.py:calls, agents/researcher.py:calls
- `data.strip` [LOW] used by `subsystem-5-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:data.strip, tools/web_fetch.py:calls
- `dotenv` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:dotenv, llm.py:imports, tools/web_search.py:imports
- `final_report.strip` [LOW] used by `subsystem-1-0-agents` from `agents/synthesizer.py`. Evidence: agents/synthesizer.py:final_report.strip, agents/synthesizer.py:calls, agents/synthesizer.py:calls
- `find` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:find, tools/web_fetch.py:calls, tools/web_fetch.py:calls
- `get` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:get, tools/web_fetch.py:calls
- `html.find` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:html.find, tools/web_fetch.py:calls
- `html.lower` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:html.lower, tools/web_fetch.py:calls, tools/web_fetch.py:calls
- `html.parser` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:html.parser, tools/web_fetch.py:imports
- `insert` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:insert, tests/test_analyst_smoke.py:calls
- `ipaddress` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:ipaddress, tools/web_fetch.py:imports
- `ipaddress.ip_address` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:ipaddress.ip_address, tools/web_fetch.py:calls
- `isinstance` [LOW] used by `subsystem-1-0-agents` from `agents/researcher.py`. Evidence: agents/researcher.py:isinstance, agents/researcher.py:calls, agents/synthesizer.py:calls
- `item.get` [LOW] used by `subsystem-7-0-tools` from `tools/web_search.py`. Evidence: tools/web_search.py:item.get, tools/web_search.py:calls, tools/web_search.py:calls
- `join` [LOW] used by `subsystem-5-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:join, tools/web_fetch.py:calls, tools/web_fetch.py:calls
- `json` [LOW] used by `subsystem-3-0-agents` from `agents/analyst.py`. Evidence: agents/analyst.py:json, agents/analyst.py:imports, agents/planner.py:imports
- `json.dumps` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:json.dumps, tests/test_analyst_smoke.py:calls
- `json.loads` [LOW] used by `subsystem-1-0-agents` from `agents/analyst.py`. Evidence: agents/analyst.py:json.loads, agents/analyst.py:calls, agents/planner.py:calls
- `langchain_google_genai` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:langchain_google_genai, llm.py:imports
- `langchain_groq` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:langchain_groq, llm.py:imports
- `langchain_mistralai` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:langchain_mistralai, llm.py:imports
- `langgraph.graph` [LOW] used by `subsystem-3-0-agents` from `graph/research_graph.py`. Evidence: graph/research_graph.py:langgraph.graph, graph/research_graph.py:imports
- `line.strip` [LOW] used by `subsystem-5-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:line.strip, tools/web_fetch.py:calls
- `list` [LOW] used by `subsystem-1-0-agents` from `agents/researcher.py`. Evidence: agents/researcher.py:list, agents/researcher.py:calls
- `llm.invoke` [LOW] used by `subsystem-1-0-agents` from `agents/analyst.py`. Evidence: agents/analyst.py:llm.invoke, agents/analyst.py:calls, agents/planner.py:calls
- `load_dotenv` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:load_dotenv, llm.py:calls, tools/web_search.py:calls
- `normalized.append` [LOW] used by `subsystem-7-0-tools` from `tools/web_search.py`. Evidence: tools/web_search.py:normalized.append, tools/web_search.py:calls
- `os` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:os, llm.py:imports, tools/web_search.py:imports
- `os.getenv` [LOW] used by `subsystem-2-0-config-py` from `llm.py`. Evidence: llm.py:os.getenv, llm.py:calls, llm.py:calls
- `parser.feed` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:parser.feed, tools/web_fetch.py:calls
- `parser.text` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:parser.text, tools/web_fetch.py:calls
- `pathlib` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:pathlib, tests/test_analyst_smoke.py:imports
- `pathlib.Path` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:pathlib.Path, tests/test_analyst_smoke.py:calls
- `print` [LOW] used by `subsystem-1-1-main-py` from `main.py`. Evidence: main.py:print, tests/test_analyst_smoke.py:calls, tests/test_analyst_smoke.py:calls
- `query.strip` [LOW] used by `subsystem-7-0-tools` from `tools/web_search.py`. Evidence: tools/web_search.py:query.strip, tools/web_search.py:calls
- `raw.splitlines` [LOW] used by `subsystem-5-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:raw.splitlines, tools/web_fetch.py:calls
- `requests` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:requests, tools/web_fetch.py:imports
- `requests.get` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:requests.get, tools/web_fetch.py:calls
- `resolve` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:resolve, tests/test_analyst_smoke.py:calls
- `response.get` [LOW] used by `subsystem-7-0-tools` from `tools/web_search.py`. Evidence: tools/web_search.py:response.get, tools/web_search.py:calls
- `result.get` [LOW] used by `subsystem-1-0-agents` from `agents/analyst.py`. Evidence: agents/analyst.py:result.get, agents/analyst.py:calls, agents/analyst.py:calls
- `socket` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:socket, tools/web_fetch.py:imports
- `socket.getaddrinfo` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:socket.getaddrinfo, tools/web_fetch.py:calls
- `startswith` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:startswith, tests/test_analyst_smoke.py:calls
- `state.get` [LOW] used by `subsystem-1-0-agents` from `agents/analyst.py`. Evidence: agents/analyst.py:state.get, agents/analyst.py:calls, agents/analyst.py:calls
- `str` [LOW] used by `subsystem-1-0-agents` from `agents/researcher.py`. Evidence: agents/researcher.py:str, tests/test_analyst_smoke.py:calls, agents/researcher.py:calls
- `strip` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:strip, tools/web_fetch.py:calls, tools/web_fetch.py:calls
- `super` [LOW] used by `subsystem-5-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:super, tools/web_fetch.py:calls
- `sys` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:sys, tests/test_analyst_smoke.py:imports
- `tavily` [LOW] used by `subsystem-2-0-config-py` from `tools/web_search.py`. Evidence: tools/web_search.py:tavily, tools/web_search.py:imports
- `text.strip` [LOW] used by `subsystem-6-0-utils` from `utils/helpers.py`. Evidence: utils/helpers.py:text.strip, utils/helpers.py:calls, utils/helpers.py:calls
- `types` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:types, tests/test_analyst_smoke.py:imports
- `types.ModuleType` [LOW] used by `subsystem-4-0-tests` from `tests/test_analyst_smoke.py`. Evidence: tests/test_analyst_smoke.py:types.ModuleType, tests/test_analyst_smoke.py:calls
- `typing` [LOW] used by `subsystem-3-0-agents` from `state.py`. Evidence: state.py:typing, state.py:imports, tools/web_fetch.py:imports
- `url.strip` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:url.strip, tools/web_fetch.py:calls, tools/web_fetch.py:calls
- `urllib.parse` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:urllib.parse, tools/web_fetch.py:imports
- `urlparse` [LOW] used by `subsystem-0-0-tools` from `tools/web_fetch.py`. Evidence: tools/web_fetch.py:urlparse, tools/web_fetch.py:calls
- `web_search` [LOW] used by `subsystem-1-0-agents` from `agents/researcher.py`. Evidence: agents/researcher.py:web_search, agents/researcher.py:calls

## Open Questions

- LOW: Does `subsystem-0-0-tools` really depend on `subsystem-1-0-agents` through `calls`? Why: The strongest cross-subsystem signal is backed by ambiguous or sparse evidence. Evidence: tools/web_fetch.py:calls, tools/web_fetch.py:calls
- LOW: Does `subsystem-1-1-main-py` really depend on `subsystem-1-0-agents` through `calls`? Why: The strongest cross-subsystem signal is backed by ambiguous or sparse evidence. Evidence: main.py:calls
- LOW: Does `subsystem-4-0-tests` really depend on `subsystem-1-0-agents` through `calls`? Why: The strongest cross-subsystem signal is backed by ambiguous or sparse evidence. Evidence: tests/test_analyst_smoke.py:calls
- LOW: Does `subsystem-4-0-tests` really depend on `subsystem-1-1-main-py` through `calls`? Why: The strongest cross-subsystem signal is backed by ambiguous or sparse evidence. Evidence: tests/test_analyst_smoke.py:calls, tests/test_analyst_smoke.py:calls, tests/test_analyst_smoke.py:calls
- LOW: Does `subsystem-7-0-tools` really depend on `subsystem-1-0-agents` through `calls`? Why: The strongest cross-subsystem signal is backed by ambiguous or sparse evidence. Evidence: tools/web_search.py:calls, tools/web_search.py:calls
- LOW: How does `validate_url()` connect to `isinstance` across boundaries? Why: ambiguous relationship, cross-file link, cross-community bridge, cross-boundary directory hop Evidence: tools/web_fetch.py:web_fetch(), agents/researcher.py:researcher_agent()
- LOW: Should `agents` stay grouped as one subsystem? Why: Its membership spans multiple path prefixes or relies on low-confidence evidence. Evidence: agents/analyst.py:json, agents/analyst.py:agents/analyst.py, agents/planner.py:agents/planner.py
- LOW: Should `config.py` stay grouped as one subsystem? Why: Its membership spans multiple path prefixes or relies on low-confidence evidence. Evidence: config.py:Config, config.py:Config.__init__(), config.py:config.py
- LOW: What responsibilities are grouped inside Community 0? Why: Representative nodes: content_type.lower, find, get. Evidence: tools/web_fetch.py:web_fetch(), agents/researcher.py:researcher_agent()
- LOW: What responsibilities are grouped inside Community 1? Why: Representative nodes: ANALYST_PROMPT.format, json.loads, llm.invoke. Evidence: tools/web_fetch.py:web_fetch(), agents/researcher.py:researcher_agent()
- LOW: What responsibilities are grouped inside Community 2? Why: Representative nodes: ChatGoogleGenerativeAI, ChatGroq, ChatMistralAI. Evidence: tools/web_fetch.py:web_fetch(), agents/researcher.py:researcher_agent()
- LOW: Why is `web_fetch()` central to the repository? Why: It has the highest grounded degree in community 0. Evidence: tools/web_fetch.py:web_fetch(), agents/researcher.py:researcher_agent()
