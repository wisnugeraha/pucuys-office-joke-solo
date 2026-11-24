#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes exactly one line (1-200 characters) to /output/entry.txt:
a one-line joke about office life.
"""
import os

LINE = "IT's new password policy: 8 chars, one symbol, no dictionary words. I set it to 'correct!' — the exclamation mark is the symbol. They haven't caught on yet."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line is {len(text)} chars (must be 1-200)")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
