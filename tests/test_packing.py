from research_agent.packing import pack_evidence


def test_nothing_fits_an_empty_budget():
    passages = [{"id": "p1", "tokens": 5, "relevance": 3, "fresh": False}]
    assert pack_evidence(passages, 0) == {"ids": [], "utility": 0, "tokens": 0}
    assert pack_evidence([], 50) == {"ids": [], "utility": 0, "tokens": 0}
