"""Shared data formats. Fixed: no task changes this file.

Several modules pass these structures to each other. Their shape is defined HERE, not by
whoever wrote the producing module: a function that takes an Index works with any Index
in this shape, including ones it did not build itself. Darbni's tests build these inputs
directly, so your function is always tested on exactly this format.
"""

from typing import TypedDict


class Index(TypedDict):
    """A positional inverted index over documents (each document has a string id).

    docs:         {doc_id: [term, ...]}  the indexed terms of each document, in order.
                  Every indexed document is a key, even one with no terms ([]).
    postings:     {term: {doc_id: [position, ...]}}  where each position p means
                  docs[doc_id][p] == term. Positions are strictly increasing. A term maps
                  only to documents that contain it; a term in no document is not a key.
    lengths:      {doc_id: len(docs[doc_id])}, for every document.
    total_length: the sum of all lengths.

    The number of documents is len(docs); the average length is total_length / len(docs).
    """

    docs: dict[str, list[str]]
    postings: dict[str, dict[str, list[int]]]
    lengths: dict[str, int]
    total_length: int


class ParsedQuery(TypedDict):
    """A search query after parsing (see query.py).

    terms:    single words that should appear, in first-seen order, no duplicates.
    phrases:  each phrase is its words in order (one or more words); no duplicate phrases.
    excluded: words that must not appear, in first-seen order, no duplicates.
    All words are lowercase canonical words (text.words).
    """

    terms: list[str]
    phrases: list[list[str]]
    excluded: list[str]


class ToolCall(TypedDict):
    """The canonical tool-call envelope.

    id:        a non-empty string, unique within one model response.
    tool:      the tool's name.
    arguments: a JSON object (dict) of argument name -> value.
    """

    id: str
    tool: str
    arguments: dict
