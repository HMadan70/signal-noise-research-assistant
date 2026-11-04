from research_agent.tool_schema import normalize_call


def test_errors_that_do_not_depend_on_ids():
    assert normalize_call({"tool": "Search", "arguments": {}}) == {"error": "bad tool"}
    assert normalize_call({"tool": "search", "name": "search"}) == {"error": "ambiguous"}
    assert normalize_call({"function": {"name": "search", "arguments": "{oops"}}) == {
        "error": "bad arguments"
    }
