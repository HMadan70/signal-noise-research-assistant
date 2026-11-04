"""The archive desk's prototype: answers a question from a handful of documents.

The desk's notebook and the nightly digest job import answer(): keep it working while the
real assistant is built around it.
"""

from research_agent.citations import render_citations
from research_agent.text import words
from research_agent.tools import dispatch

LIMIT = 3


def keyword_search(documents: list[dict], question: str) -> list[str]:
    """Ids of the documents sharing the most distinct words with the question."""
    asked = set(words(question))
    scored = [(len(asked & set(words(doc["text"]))), doc["id"]) for doc in documents]
    ranked = sorted(scored, key=lambda pair: (-pair[0], pair[1]))
    return [doc_id for score, doc_id in ranked if score > 0][:LIMIT]


def answer(question: str, documents: list[dict]) -> dict:
    """documents: [{"id", "title", "text"}]. A draft answer citing the best documents."""
    hits = keyword_search(documents, question)
    draft = " ".join(f"See [@{doc_id}]." for doc_id in hits) or "No sources found."
    sources = [{"id": doc["id"], "title": doc["title"]} for doc in documents]
    rendered = render_citations(draft, sources)
    counted = dispatch({"tool": "word_count", "arguments": {"text": question}})
    return {
        "answer": rendered["text"],
        "references": rendered["references"],
        "question_words": counted.get("ok"),
    }
