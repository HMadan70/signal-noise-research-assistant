from research_agent.evaluation import evaluate, score_query


def test_a_perfect_ranking():
    judgments = {"a": 3, "b": 0}
    assert score_query(["a", "b"], judgments) == {"recall": 1.0, "ndcg": 1.0}
    assert evaluate({"q": ["a"]}, {"q": judgments}) == {"queries": 1, "recall": 1.0, "ndcg": 1.0, "skipped": []}
