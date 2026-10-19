import json
import sys
import pathlib

# Ensure the project root is importable (same layout as the rest of the package).
_ROOT = str(pathlib.Path(__file__).resolve().parent.parent)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from prompts.planner import PLANNER_PROMPT


def test_planner_prompt_renders_all_five_placeholders():
    """PLANNER_PROMPT must accept query, goal, research_type, constraints, output_requirements."""
    sample = {
        "query": "BMW",
        "goal": "Explain the performance and design of BMW",
        "research_type": "general",
        "constraints": {"budget": "Medium"},
        "output_requirements": {"length": "2 paragraphs", "sources": 3},
    }

    rendered = PLANNER_PROMPT.format(**sample)

    # Every intended placeholder must be substituted (no leftover {key}).
    for key in ("query", "goal", "research_type", "constraints", "output_requirements"):
        assert "{" + key + "}" not in rendered, f"placeholder '{{{key}}}' was not substituted"

    # The five intended placeholders must be present in the template itself.
    for key in ("query", "goal", "research_type", "constraints", "output_requirements"):
        assert "{" + key + "}" in PLANNER_PROMPT


def test_planner_prompt_json_example_rows_are_balanced():
    """The JSON example must have balanced braces so str.format() can parse it.

    The example uses literal {} empty objects and a surrounding JSON object; each
    literal { must be {{ and each literal } must be }} so that str.format() does
    not try to interpret them as replacement fields.
    """
    opens = PLANNER_PROMPT.count("{")
    closes = PLANNER_PROMPT.count("}")
    assert opens == closes, f"template braces unbalanced: {{ {opens} }} != {{ {closes} }}"


def test_planner_prompt_json_example_still_valid_after_escaping():
    """The rendered prompt must keep the JSON example intact (escaped braces) and
    substitute all five placeholders.

    This asserts the exact failure mode fixed here: str.format() must not raise a
    KeyError while building the prompt for a real user request.
    """
    sample = {
        "query": "BMW",
        "goal": "Explain the performance and design of BMW",
        "research_type": "general",
        "constraints": {"budget": "Medium"},
        "output_requirements": {"length": "2 paragraphs", "sources": 3},
    }

    rendered = PLANNER_PROMPT.format(**sample)

    # The JSON example is the block that starts after the 'Use the following structure:'
    # header and ends at the '}}xx' terminator (which renders to a single '} + 'xx').
    start = rendered.find("Use the following structure:\n\n{")
    end = rendered.find("}xx")
    assert start != -1, "JSON example start not found in rendered prompt"
    assert end != -1, "JSON example terminator '}xx' not found in rendered prompt"

    # Verify all five labels still appear as labels (not as substituted values).
    for label in (
        "Query:",
        "Goal:",
        "Research Type:",
        "Constraints:",
        "Output Requirements:",
    ):
        assert label in rendered, f"expected label '{label}' missing from rendered prompt"

    # The rendered JSON example must contain the expected keys and balanced structure.
    json_snippet = rendered[start + len("Use the following structure:\n\n{"):end]
    for key in ("goal", "research_type", "constraints", "output_requirements", "plan", "tasks"):
        assert json_snippet.find('"' + key + '"') != -1, f"JSON example missing key '{key}'"
    assert json_snippet.count("{") == json_snippet.count("}"), (
        "JSON example braces unbalanced in rendered prompt"
    )


if __name__ == "__main__":
    test_planner_prompt_renders_all_five_placeholders()
    print("PASS: test_planner_prompt_renders_all_five_placeholders")

    test_planner_prompt_json_example_rows_are_balanced()
    print("PASS: test_planner_prompt_json_example_rows_are_balanced")

    test_planner_prompt_json_example_still_valid_after_escaping()
    print("PASS: test_planner_prompt_json_example_still_valid_after_escaping")

    print("ALL_TESTS_PASSED")

