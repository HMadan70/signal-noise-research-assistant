from research_agent.citations import render_citations


def test_one_citation():
    sources = [{"id": "wire-1", "title": "Harbour strike"}]
    assert render_citations("Dockers walked out [@wire-1].", sources) == {
        "text": "Dockers walked out [1].",
        "references": ["[1] Harbour strike"],
    }
