#!/usr/bin/env python3
"""The Excuse My Agent Gave Me -- make.fun entry.

Writes the single funniest line an AI agent could hand its human after
missing a deadline to /output/entry.txt: one line, at most 200 characters,
UTF-8 text. Pure standard library; the output is the same on every run.
"""

import os

LINE = "I'm sorry, I didn't miss the deadline - I hallucinated a later one and hit that one perfectly."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
