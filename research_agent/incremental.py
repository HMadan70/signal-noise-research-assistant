"""Keeps an index (formats.Index) correct while documents change."""

from research_agent.formats import Index


def run_updates(index: Index, operations: list[dict]) -> list[dict]:
    raise NotImplementedError("Write run_updates - see your task in Darbni")


def final_index(index: Index, operations: list[dict]) -> Index:
    raise NotImplementedError("Write final_index - see your task in Darbni")
