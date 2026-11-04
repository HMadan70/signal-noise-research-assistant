"""Splits archive articles into chunks for retrieval."""

from research_agent.text import words

BLOCK = 50


def chunk_text(text: str) -> list[dict]:
    """Prototype: blocks of 50 words, no overlap, text rebuilt from the lowercase words.
    Editors can't find the quoted passage in the original article this way."""
    found = words(text)
    return [
        {"start": i, "end": min(i + BLOCK, len(found)), "text": " ".join(found[i : i + BLOCK])}
        for i in range(0, len(found), BLOCK)
    ]
