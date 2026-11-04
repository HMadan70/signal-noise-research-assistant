from research_agent.feedback import expand_and_rerank

INDEX = {
    "docs": {"a": ["flood", "barrier"], "b": ["sunny", "day"], "c": ["barrier", "repair"]},
    "postings": {
        "flood": {"a": [0]},
        "barrier": {"a": [1], "c": [0]},
        "sunny": {"b": [0]},
        "day": {"b": [1]},
        "repair": {"c": [1]},
    },
    "lengths": {"a": 2, "b": 2, "c": 2},
    "total_length": 6,
}


def test_the_matching_document_comes_first():
    assert expand_and_rerank(INDEX, ["flood"])["results"][0]["id"] == "a"
    assert expand_and_rerank(INDEX, ["zebra"]) == {"expansion": [], "results": []}
