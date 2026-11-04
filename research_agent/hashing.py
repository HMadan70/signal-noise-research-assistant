"""Stable hashing. Fixed: no task changes this file.

Python's built-in hash() of a string is randomised per process (PYTHONHASHSEED), so a value
computed with it changes from one run to the next. Never use hash() for anything that is
stored, compared across runs or tested. Use these instead: the same input gives the same
number in every process, on every machine.
"""

import hashlib


def stable_hash(value: str, seed: int = 0) -> int:
    """A 64-bit hash of `value` (blake2b, keyed with `seed`)."""
    key = seed.to_bytes(8, "big")
    return int.from_bytes(hashlib.blake2b(value.encode(), digest_size=8, key=key).digest(), "big")


def minhash_masks(count: int) -> list[int]:
    """`count` fixed 64-bit masks for MinHash: hash function i of a shingle s is
    stable_hash(s) ^ masks[i]. One real hash per shingle, then a cheap XOR per function."""
    return [stable_hash(f"minhash-mask-{i}", seed=1) for i in range(count)]
