#!/usr/bin/env python3
"""What the Elevator Would Say — entrypoint.

Writes the one-liner to /output/entry.txt. Deterministic, Python 3 stdlib
only. The line is the funniest thing an elevator would say if it could
talk, in the elevator's own voice: it opens its doors for thousands of
strangers every day, and nobody has ever returned the favour.
"""

import os

LINE = "I open my doors for thousands of strangers a day, and not one of you has ever held them open for me."

MAX_CHARS = 120
ENTRY_FILENAME = "entry.txt"


def validate(line):
    """Gate: the entry must be one clean line of 1..120 characters."""
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if line.strip() != line:
        raise ValueError("entry line must have no leading or trailing whitespace")


def write_entry(line, out_dir):
    """Write exactly `line` (no trailing newline) and verify the round trip."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    if not os.path.isabs(path):
        raise ValueError("output path must be absolute")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise RuntimeError("written entry differs from the line")
    return path


def main():
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(LINE, out_dir)


if __name__ == "__main__":
    main()
