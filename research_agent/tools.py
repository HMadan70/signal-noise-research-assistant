"""Tools the assistant can call. prototype.answer and the desk's notebooks call dispatch().

Every tool returns {"ok": value} or {"error": message}. dispatch never raises: an
unexpected exception becomes {"error": "tool failed: <ExceptionType>"}.
"""

AGENCIES = {
    "ap": "Associated Press",
    "afp": "Agence France-Presse",
    "bbc": "British Broadcasting Corporation",
    "dpa": "Deutsche Presse-Agentur",
    "efe": "Agencia EFE",
}


def dispatch(call: dict) -> dict:
    """Run one tool call {"tool": name, "arguments": {...}}."""
    try:
        tool = call.get("tool")
        args = call.get("arguments") or {}
        if tool == "echo":
            return {"ok": args}
        elif tool == "word_count":
            text = args.get("text")
            if not isinstance(text, str):
                return {"error": "word_count needs text"}
            # Whitespace words, not text.words: the desk's reports were built on this count.
            return {"ok": len(text.split())}
        elif tool == "agency":
            code = args.get("code", "")
            name = AGENCIES.get(code.strip().lower())
            if name is None:
                return {"error": "unknown agency: " + code}
            return {"ok": name}
        elif tool == "add":
            total = 0
            for value in args.get("numbers", []):
                if isinstance(value, (int, float)):
                    total += value
            return {"ok": total}
        elif tool == "upper":
            text = args["text"]
            return {"ok": text.upper().strip()}
        else:
            return {"error": f"unknown tool: {tool}"}
    except Exception as exc:
        return {"error": f"tool failed: {type(exc).__name__}"}
