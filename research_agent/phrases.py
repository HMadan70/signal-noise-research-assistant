"""Phrase search over an index (formats.Index) for a parsed query (formats.ParsedQuery)."""

from research_agent.formats import Index, ParsedQuery


def search(index: Index, query: ParsedQuery) -> list[dict]:
    raise NotImplementedError("Write search - see your task in Darbni")


def search_batch(index: Index, queries: list[ParsedQuery]) -> list[list[dict]]:
    raise NotImplementedError("Write search_batch - see your task in Darbni")
