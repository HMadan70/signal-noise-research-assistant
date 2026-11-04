"""A small cache for repeated tool calls, on a fake clock."""


class LruTtlCache:
    def __init__(self, capacity: int, ttl: float) -> None:
        raise NotImplementedError("Write LruTtlCache - see your task in Darbni")


def run_operations(operations: list[dict]) -> list[dict]:
    raise NotImplementedError("Write run_operations - see your task in Darbni")
