from research_agent.prototype import answer


def test_answer_cites_the_matching_document():
    documents = [
        {"id": "wire-1", "title": "Harbour strike", "text": "Dockers strike at the harbour"},
        {"id": "wire-2", "title": "Weather", "text": "Sunny weekend ahead"},
    ]
    result = answer("Why are dockers on strike?", documents)
    assert result["answer"] == "See [1]."
    assert result["references"][0] == "[1] Harbour strike"
    assert result["question_words"] == 5
