from research_agent.research import research


def test_no_retrievals_means_no_evidence():
    request = {"retrievals": [], "passages": {}, "budget": 100, "model": []}
    assert research(request) == {
        "status": "no_evidence",
        "evidence": [],
        "claims": [],
        "failed_retrievals": [],
        "cached": 0,
        "attempts": 0,
    }
