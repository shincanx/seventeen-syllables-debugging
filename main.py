#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one original haiku about debugging (5-7-5, at most 200
characters) to /output/entry.txt. Deterministic: the same bytes on
every run.
"""

import os

HAIKU = """Three a.m. cursor
still blinks on the breakpoint line
and the bug was me
"""

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def validate(text: str) -> None:
    """Guard the bounty gate: 3 lines, 1-200 characters, not blank."""
    lines = text.splitlines()
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} outside 1-{MAX_CHARS}"
    assert text.strip(), "haiku must not be only whitespace"


def main() -> None:
    validate(HAIKU)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
