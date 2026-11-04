from research_agent.incremental import final_index, run_updates


def empty():
    return {"docs": {}, "postings": {}, "lengths": {}, "total_length": 0}


def test_insert_then_delete():
    operations = [{"op": "insert", "id": "a", "terms": ["storm", "storm"]}, {"op": "delete", "id": "a"}]
    assert run_updates(empty(), operations) == [{"ok": "inserted"}, {"ok": "deleted"}]
    assert final_index(empty(), operations[:1]) == {
        "docs": {"a": ["storm", "storm"]},
        "postings": {"storm": {"a": [0, 1]}},
        "lengths": {"a": 2},
        "total_length": 2,
    }
