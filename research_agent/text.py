"""Shared text rules for the whole package. Fixed: no task changes this file.

A word is a run of ASCII letters and digits. Case is ignored when matching and words are
returned lowercased, so "BBC's" gives ["bbc", "s"] and "café" gives ["caf"].
"""

import re

WORD = re.compile(r"[a-z0-9]+", re.ASCII | re.IGNORECASE)


def words(text: str) -> list[str]:
    """The canonical tokenizer: every word of `text`, lowercased, in order."""
    return [match.group().lower() for match in WORD.finditer(text)]


def word_spans(text: str) -> list[tuple[int, int]]:
    """(start, end) character offsets of every word in the ORIGINAL text: text[start:end]
    is the word as written (not lowercased)."""
    return [match.span() for match in WORD.finditer(text)]
