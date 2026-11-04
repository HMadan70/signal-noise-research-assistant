from research_agent.bm25 import rank

INDEX = {
    "docs": {"a": ["flood", "warning"], "b": ["sunny", "day"]},
    "postings": {"flood": {"a": [0]}, "warning": {"a": [1]}, "sunny": {"b": [0]}, "day": {"b": [1]}},
    "lengths": {"a": 2, "b": 2},
    "total_length": 4,
}


def test_only_documents_with_a_query_term():
    assert [result["id"] for result in rank(INDEX, ["flood"])] == ["a"]
    assert rank(INDEX, ["zebra"]) == []
