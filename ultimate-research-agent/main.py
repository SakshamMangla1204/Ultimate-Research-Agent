
import traceback

from graph.research_graph import graph


def main():
    print("\n===== THE ULTIMATE RESEARCH AGENT =====\n")

    query = input("What would you like to research? ").strip()

    if not query:
        print("Please enter a research query.")
        return

    # Initialize the shared state for this research run.
    initial_state = {
        "query": query,
        "errors": [],
        "sources": [],
        "source_metadata": [],
        "tool_calls": [],
        "tool_results": [],
        "completed_tasks": [],
    }

    print("\nStarting research...")
    print("-" * 45)

    try:
        # Execute the LangGraph workflow.
        result = graph.invoke(
            initial_state,
            config={"recursion_limit": 30},
        )

        print("\n" + "=" * 45)
        print("RESEARCH REPORT")
        print("=" * 45 + "\n")

        final_report = result.get("final_report")

        if final_report:
            print(final_report)
        else:
            print("No final report was generated.")

            errors = result.get("errors", [])
            if errors:
                print("\nReported errors:")
                for error in errors:
                    print(f"- {error}")

        print("\n" + "=" * 45)
        print("RESEARCH EXECUTION COMPLETED")
        print("=" * 45)

    except Exception as error:
        print("\n" + "=" * 45)
        print("RESEARCH EXECUTION FAILED")
        print("=" * 45)

        print(f"\nError type: {type(error).__name__}")
        print(f"Error message: {error}")

        print("\nFull traceback:")
        traceback.print_exc()


if __name__ == "__main__":
    main()
