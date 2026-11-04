from research_agent.chunking import chunk_text


def test_short_text_is_one_chunk_with_original_offsets():
    assert chunk_text("Storm, hits") == [{"start": 0, "end": 11, "text": "Storm, hits"}]
