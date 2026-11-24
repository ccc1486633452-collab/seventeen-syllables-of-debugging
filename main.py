#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — a make.fun competition entry."""

import os
import stat

HAIKU = (
    "Cursor blinks at three\n"
    "a red dot waits on line nine\n"
    "the bug was my code"
)


def main() -> None:
    # Pick writable output path: prefer /output, fall back to ./output
    target_dir = "/output"
    try:
        os.makedirs(target_dir, exist_ok=True)
        probe = os.path.join(target_dir, ".probe")
        with open(probe, "w") as fh:
            fh.write("")
        os.remove(probe)
    except (PermissionError, OSError):
        target_dir = "./output"

    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, "entry.txt")

    with open(path, "w") as fh:
        fh.write(HAIKU + "\n")

    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

    print(f"Haiku written to {path}")


if __name__ == "__main__":
    main()