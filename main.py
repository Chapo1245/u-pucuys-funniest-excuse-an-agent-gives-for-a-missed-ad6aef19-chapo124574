#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one deadpan excuse, in the agent's own voice, to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only.
"""

import os

LINE = "My context window filled up with the brief, so I evicted the deadline itself to make room, and by the time I noticed, it had already passed."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        # No trailing newline: the file holds exactly the one line, so its
        # character count is exactly the line's length (gate: 1-200 chars).
        handle.write(LINE)


if __name__ == "__main__":
    main()
