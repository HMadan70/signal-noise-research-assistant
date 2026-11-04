"""Splits archive articles into chunks for retrieval, with offsets into the original text."""

from research_agent.text import word_spans

SIZE = 10  # words per chunk
STEP = 7   # a new chunk starts 7 words after the previous one (3 words are shared)


def chunk_text(text: str) -> list[dict]:
    spans = word_spans(text)
    n = len(spans)
    if n == 0:
        return []

    # Index of the first word of every chunk.
    starts = [0]
    while starts[-1] + SIZE < n:  # the last chunk does not reach the last word yet
        starts.append(starts[-1] + STEP)

    # A short last chunk (and more than one chunk): move its start back so it has SIZE words.
    if len(starts) > 1 and n - starts[-1] < SIZE:
        starts[-1] = n - SIZE

    chunks = []
    for first in starts:
        last = min(first + SIZE, n) - 1
        start = spans[first][0]
        end = spans[last][1]
        chunks.append({"start": start, "end": end, "text": text[start:end]})
    return chunks