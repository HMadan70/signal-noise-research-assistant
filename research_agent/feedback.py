"""Query expansion from the first results (pseudo-relevance feedback)."""

from research_agent.formats import Index


def expand_and_rerank(index: Index, terms: list[str]) -> dict:
    raise NotImplementedError("Write expand_and_rerank - see your task in Darbni")
