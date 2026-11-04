from research_agent.query import parse_query


def test_terms_phrase_and_exclusion():
    assert parse_query('storm "coast guard" -rumour') == {
        "terms": ["storm"],
        "phrases": [["coast", "guard"]],
        "excluded": ["rumour"],
    }
