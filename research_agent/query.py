"""Search queries typed by editors."""

from research_agent.formats import ParsedQuery


def parse_query(text: str) -> ParsedQuery | dict:
    raise NotImplementedError("Write parse_query - see your task in Darbni")
