"""Reads the tool calls a model wrote in its reply."""

import json


def parse_calls(text: str, tools: dict) -> dict:
    """Prototype: assumes the whole reply is {"calls": [...]} and trusts it."""
    return {"calls": json.loads(text)["calls"]}
