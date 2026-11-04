"""Measures retrieval quality against editors' relevance judgments."""


def score_query(ranked: list[str], judgments: dict[str, int]) -> dict:
    raise NotImplementedError("Write score_query - see your task in Darbni")


def evaluate(runs: dict[str, list[str]], judgments: dict[str, dict[str, int]]) -> dict:
    raise NotImplementedError("Write evaluate - see your task in Darbni")
