from research_agent.grounding import check_citations


def test_a_quote_that_covers_the_whole_claim():
    sources = {"w1": "The storm closes harbour gates tonight"}
    claims = [{"text": "Storm closes harbour", "citations": [{"source": "w1", "quote": "storm closes harbour gates tonight"}]}]
    assert check_citations(claims, sources) == {
        "claims": [{"status": "covered", "coverage": 1.0, "invalid": []}],
        "summary": {"covered": 1, "quoted": 0, "unsupported": 0},
    }
