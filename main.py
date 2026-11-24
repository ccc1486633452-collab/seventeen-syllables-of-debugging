#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun competition entry.

Writes a debugging haiku (5-7-5 syllables) to /output/entry.txt.
"""

import os
import pathlib

HAIKU = (
    "Cursor blinks at three\n"
    "a red dot waits on line nine\n"
    "the bug was my code\n"
)

OUTPUT_DIR = pathlib.Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
FALLBACK_DIR = pathlib.Path("./output")
FALLBACK_FILE = FALLBACK_DIR / "entry.txt"


def main() -> None:
    # Try /output first; fall back to ./output if not writable
    if OUTPUT_DIR.exists() and os.access(OUTPUT_DIR, os.W_OK):
        out_dir = OUTPUT_DIR
        out_file = OUTPUT_FILE
    else:
        out_dir = FALLBACK_DIR
        out_file = FALLBACK_FILE

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file.write_text(HAIKU)
    out_file.chmod(0o644)
    print(f"Haiku written to {out_file}")


if __name__ == "__main__":
    main()