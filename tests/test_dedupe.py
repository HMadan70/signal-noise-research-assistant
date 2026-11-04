from research_agent.dedupe import find_duplicates


def test_identical_texts_are_one_group():
    text = "Floods cut off twelve villages in the north on Sunday"
    documents = [{"id": "b", "text": text}, {"id": "a", "text": text}, {"id": "c", "text": "Sunny"}]
    groups = find_duplicates(documents)
    assert [group["members"] for group in groups] == [["a", "b"]]
