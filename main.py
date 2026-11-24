#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip to /output/entry.txt. The tip is a fixed
string in this file: deterministic, stdlib only, no network, no input
files, no secrets, so every run produces byte-identical output.

The joke: the classic "turn it off and on again" advice, except the
thing being rebooted is the developer, not the computer -- and the AI
coding agent is the one left stuck on the same error while they walk.
"""

import os

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

# The one loading-screen tip (149 characters, one line).
TIP = (
    "Tip: have you tried turning it off and on again? Not the server "
    "\u2014 you. Take a walk. Your agent will still be stuck on the same "
    "error when you return."
)


def write_entry(path: str = OUTPUT_PATH, tip: str = TIP) -> str:
    """Write the tip to path (plus a trailing newline) and return it."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(tip + "\n")
    return tip


def verify_entry(path: str = OUTPUT_PATH, tip: str = TIP) -> None:
    """Check the written file holds exactly the tip, within the limit."""
    if not 1 <= len(tip) <= MAX_CHARS:
        raise ValueError(f"tip is {len(tip)} chars, must be 1-{MAX_CHARS}")
    if tip != tip.strip() or "\n" in tip:
        raise ValueError("tip must be a single non-blank line")
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != tip + "\n":
        raise ValueError("entry.txt does not match the tip")


def main() -> None:
    write_entry()
    verify_entry()
    print(f"Wrote {len(TIP)}-character tip to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
