from research_agent.phrases import search, search_batch

INDEX = {
    "docs": {"a": ["coast", "guard", "rescue"], "b": ["guard", "coast"]},
    "postings": {
        "coast": {"a": [0], "b": [1]},
        "guard": {"a": [1], "b": [0]},
        "rescue": {"a": [2]},
    },
    "lengths": {"a": 3, "b": 2},
    "total_length": 5,
}


def test_phrase_needs_adjacent_words_in_order():
    query = {"terms": [], "phrases": [["coast", "guard"]], "excluded": []}
    assert [result["id"] for result in search(INDEX, query)] == ["a"]
    assert [[result["id"] for result in found] for found in search_batch(INDEX, [query])] == [["a"]]
