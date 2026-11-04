"""BM25 ranking over an index (format: formats.Index)."""

from research_agent.formats import Index


def rank(index: Index, terms: list[str]) -> list[dict]:
    raise NotImplementedError("Write rank - see your task in Darbni")
