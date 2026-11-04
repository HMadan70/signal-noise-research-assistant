"""The positional inverted index (format: formats.Index)."""

from research_agent.formats import Index


def build_index(documents: list[dict]) -> Index | dict:
    raise NotImplementedError("Write build_index - see your task in Darbni")


def lookup(index: Index, term: str) -> list[dict]:
    raise NotImplementedError("Write lookup - see your task in Darbni")
