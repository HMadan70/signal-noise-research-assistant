from research_agent.agent import run_agent


def test_one_tool_then_an_answer():
    call = {"id": "c1", "tool": "search", "arguments": {"q": "flood"}}
    script = {
        "responses": [{"tokens": 1, "calls": [call]}, {"tokens": 1, "final": "Done."}],
        "results": {"c1": {"ok": ["doc-1"]}},
    }
    assert run_agent(script) == {
        "status": "final",
        "answer": "Done.",
        "steps": 2,
        "tokens": 2,
        "calls": 1,
        "trace": [{"step": 1, "id": "c1", "tool": "search", "result": {"ok": ["doc-1"]}}],
    }
