"""Tool-call envelopes. Model providers and our old notebooks send tool calls in different
shapes; everything after this module should only ever see ONE shape."""


def normalize_call(call: dict) -> dict:
    """Today: turns a call into our OLD envelope {"name": ..., "args": {...}}."""
    if "name" in call:
        return {"name": call["name"], "args": call.get("args", {})}
    return {"name": call.get("tool"), "args": call.get("arguments", {})}
