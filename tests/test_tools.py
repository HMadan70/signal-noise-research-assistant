from research_agent.tools import dispatch


def test_word_count_counts_whitespace_words():
    assert dispatch({"tool": "word_count", "arguments": {"text": "Storm hits the coast"}}) == {"ok": 4}
    assert dispatch({"tool": "nope", "arguments": {}}) == {"error": "unknown tool: nope"}
