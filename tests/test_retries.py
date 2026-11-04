from research_agent.retries import run_script


def test_success_on_the_first_attempt():
    script = {"seed": 1, "deadline": 10.0, "outcomes": [{"ok": "rows", "duration": 0.25}]}
    assert run_script(script) == {
        "status": "ok",
        "value": "rows",
        "attempts": 1,
        "elapsed": 0.25,
        "waits": [],
    }
