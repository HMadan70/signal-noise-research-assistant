"""Citation markers. A draft answer cites a source as [@source_id]; render_citations turns
the markers into numbers and builds the reference list. prototype.answer calls it."""

import re

MARKER = re.compile(r"\[@([A-Za-z0-9_-]+)\]")


def render_citations(text: str, sources: list[dict]) -> dict:
    """Replace each [@id] in `text` with [n] and list the references.

    sources: [{"id": ..., "title": ...}, ...]. Returns {"text": ..., "references": [...]},
    each reference "[n] Title". A marker for an id that is not a source becomes [?].
    """
    numbers = {source["id"]: i + 1 for i, source in enumerate(sources)}
    titles = {source["id"]: source["title"] for source in sources}

    def replace(match: re.Match) -> str:
        number = numbers.get(match.group(1))
        return f"[{number}]" if number else "[?]"

    rendered = MARKER.sub(replace, text)
    references = [f"[{numbers[source_id]}] {titles[source_id]}" for source_id in numbers]
    return {"text": rendered, "references": references}
