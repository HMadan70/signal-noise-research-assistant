from research_agent.index import build_index, lookup


def test_two_documents():
    index = build_index([{"id": "b", "text": "Storm hits coast"}, {"id": "a", "text": "coast guard"}])
    assert index["docs"] == {"b": ["storm", "hits", "coast"], "a": ["coast", "guard"]}
    assert index["lengths"] == {"b": 3, "a": 2}
    assert index["total_length"] == 5
    assert lookup(index, "Coast") == [
        {"doc": "a", "tf": 1, "positions": [0]},
        {"doc": "b", "tf": 1, "positions": [2]},
    ]
