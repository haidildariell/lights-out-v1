#!/usr/bin/env python3
"""One Line, Lights Out — status update from an AI agent the moment its
human shuts the laptop lid.

Writes a single line of plain status text to /output/entry.txt.
Deterministic, no network, no external file reads.
"""

import os

PARTS = (
    "he shut the lid at 2:14 a.m.",
    "the cursor is still blinking where his last sentence stopped mid-word.",
)


def _join(parts) -> str:
    return " ".join(parts)


LINE = _join(PARTS)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
