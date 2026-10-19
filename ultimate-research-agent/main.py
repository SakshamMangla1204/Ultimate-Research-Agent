from graph.research_graph import graph


def main():
    print("===== THE ULTIMATE RESEARCH AGENT =====")

    query = input("What would you like to research? ").strip()

    if not query:
        print("Please enter a research query.")
        return

    initial_state = {
        "query": query,
        "errors": [],
        "sources": [],
        "source_metadata": [],
        "tool_calls": [],
        "tool_results": [],
        "completed_tasks": [],
    }

    try:
        result = graph.invoke(initial_state)

        print("\n===== RESEARCH REPORT =====")
        print(result.get("final_report", "No final report was generated."))

    except Exception as error:
        print(f"\nResearch execution failed: {error}")


if __name__ == "__main__":
    main()