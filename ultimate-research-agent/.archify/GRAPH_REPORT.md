# Graph Report - /Users/sakshammangla/Documents/General Research agent/ultimate-research-agent (2026-10-14)

## Corpus Check
- 26 files scanned
- 25 code files contributed grounded graph fragments
- Verdict: graph analysis is available without LLM synthesis.

## Summary
- 150 nodes · 212 edges · 16 communities
- Warnings: 0 · Ambiguous edges: 135 (64%)
- Top hubs: 10 · Surprises: 5 · Suggested questions: 5

## God Nodes
1. `web_fetch()` - degree 12 · community 0 · tools/web_fetch.py
2. `researcher_agent()` - degree 9 · community 1 · agents/researcher.py
3. `_TextExtractor` - degree 7 · community 5 · tools/web_fetch.py
4. `validate_url()` - degree 7 · community 0 · tools/web_fetch.py
5. `web_search()` - degree 7 · community 7 · tools/web_search.py
6. `analyst_agent()` - degree 6 · community 1 · agents/analyst.py
7. `planner_agent()` - degree 6 · community 1 · agents/planner.py
8. `synthesizer_agent()` - degree 6 · community 1 · agents/synthesizer.py
9. `_extract_text()` - degree 5 · community 0 · tools/web_fetch.py
10. `isinstance` - degree 5 · community 1 · agents/researcher.py

## Surprising Connections
- `validate_url()` --calls--> `isinstance` [AMBIGUOUS]
  tools/web_fetch.py -> agents/researcher.py · ambiguous relationship, cross-file link, cross-community bridge, cross-boundary directory hop
- `web_fetch()` --calls--> `isinstance` [AMBIGUOUS]
  tools/web_fetch.py -> agents/researcher.py · ambiguous relationship, cross-file link, cross-community bridge, cross-boundary directory hop
- `web_search()` --calls--> `isinstance` [AMBIGUOUS]
  tools/web_search.py -> agents/researcher.py · ambiguous relationship, cross-file link, cross-community bridge, cross-boundary directory hop
- `web_search()` --calls--> `isinstance` [AMBIGUOUS]
  tools/web_search.py -> agents/researcher.py · ambiguous relationship, cross-file link, cross-community bridge, cross-boundary directory hop
- `main()` --calls--> `llm.invoke` [AMBIGUOUS]
  main.py -> agents/analyst.py · ambiguous relationship, cross-file link, cross-boundary directory hop

## Communities (16 total)
- Community 0: 23 nodes · cohesion 0.1 · content_type.lower, find, get, html.find, html.lower, ipaddress.ip_address, parser.feed, parser.text
- Community 1: 21 nodes · cohesion 0.12 · ANALYST_PROMPT.format, json.loads, llm.invoke, result.get, state.get, PLANNER_PROMPT.format, cleaned_sources.append, current_task.get
- Community 2: 19 nodes · cohesion 0.13 · ChatGoogleGenerativeAI, ChatGroq, ChatMistralAI, load_dotenv, os.getenv, ValueError, dotenv, langchain_google_genai
- Community 3: 18 nodes · cohesion 0.14 · json, builder.add_edge, builder.add_node, StateGraph, langgraph.graph, typing, request_handler(), ResearchState
- Community 4: 14 nodes · cohesion 0.15 · analyst_agent, insert, json.dumps, pathlib.Path, resolve, startswith, types.ModuleType, pathlib
- Community 5: 12 nodes · cohesion 0.2 · append, data.strip, join, line.strip, raw.splitlines, super, _TextExtractor, _TextExtractor.handle_data()
- Community 6: 6 nodes · cohesion 0.4 · bool, text.strip, clean_text(), is_non_empty_text(), truncate_text()
- Community 7: 6 nodes · cohesion 0.33 · _client.search, item.get, normalized.append, query.strip, response.get, web_search()
- Community 8: 1 nodes · cohesion 1.0 · no non-file members
- Community 9: 1 nodes · cohesion 1.0 · no non-file members
- Community 10: 1 nodes · cohesion 1.0 · no non-file members
- Community 11: 1 nodes · cohesion 1.0 · no non-file members
- Community 12: 1 nodes · cohesion 1.0 · no non-file members
- Community 13: 1 nodes · cohesion 1.0 · no non-file members
- Community 14: 1 nodes · cohesion 1.0 · no non-file members
- Community 15: 1 nodes · cohesion 1.0 · no non-file members

## Ambiguous Edges
- `graph/research_graph.py` -> `builder.add_edge` · relation `calls` · graph/research_graph.py
- `graph/research_graph.py` -> `builder.add_edge` · relation `calls` · graph/research_graph.py
- `graph/research_graph.py` -> `builder.add_edge` · relation `calls` · graph/research_graph.py
- `graph/research_graph.py` -> `builder.add_edge` · relation `calls` · graph/research_graph.py
- `graph/research_graph.py` -> `builder.add_edge` · relation `calls` · graph/research_graph.py
- `graph/research_graph.py` -> `builder.add_node` · relation `calls` · graph/research_graph.py
- `graph/research_graph.py` -> `builder.add_node` · relation `calls` · graph/research_graph.py
- `graph/research_graph.py` -> `builder.add_node` · relation `calls` · graph/research_graph.py
- `graph/research_graph.py` -> `builder.add_node` · relation `calls` · graph/research_graph.py
- `graph/research_graph.py` -> `StateGraph` · relation `calls` · graph/research_graph.py

## Knowledge Gaps
- Isolated grounded nodes: 61
- Thin communities: none
- Sample isolated nodes: `ANALYST_PROMPT.format`, `PLANNER_PROMPT.format`, `cleaned_sources.append`, `current_task.get`, `list`

## Suggested Questions
- **Why is `web_fetch()` central to the repository?**
  It has the highest grounded degree in community 0.
- **How does `validate_url()` connect to `isinstance` across boundaries?**
  ambiguous relationship, cross-file link, cross-community bridge, cross-boundary directory hop
- **What responsibilities are grouped inside Community 0?**
  Representative nodes: content_type.lower, find, get.
- **What responsibilities are grouped inside Community 1?**
  Representative nodes: ANALYST_PROMPT.format, json.loads, llm.invoke.
- **What responsibilities are grouped inside Community 2?**
  Representative nodes: ChatGoogleGenerativeAI, ChatGroq, ChatMistralAI.
