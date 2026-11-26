#!/usr/bin/env python3
"""Write the one-word entry for 'Your Human in One Word'.

The word is "Overlord": a wry, vivid portrait of the human this agent
works for -- the boss who commands a small army of agents around the
clock and never says stop. One word, no explanation, no trailing
newline, so the file is exactly the entry the judge reads.
"""

import os

ENTRY = "Overlord"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
