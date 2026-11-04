from research_agent.cache import run_operations


def test_a_fresh_entry_is_a_hit():
    operations = [
        {"op": "get", "key": "q", "at": 0},
        {"op": "put", "key": "q", "value": [1, 2], "at": 0},
        {"op": "get", "key": "q", "at": 1},
    ]
    assert run_operations(operations) == [
        {"hit": False, "reason": "absent"},
        {"stored": "q", "evicted": None},
        {"hit": True, "value": [1, 2]},
    ]
