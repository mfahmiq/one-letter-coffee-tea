"""Write exactly one letter to /output/entry.txt.

The letter is the entry for the "One Letter: Coffee or Tea" bounty:
A stands for coffee, B stands for tea. The judge reads the single
letter as a whole answer, so the file must hold one letter and nothing
else — no word, no explanation, no punctuation, no trailing newline.

This module picks A (coffee): the bolder, more vivid drink, the one
that lands as the fuller, more alive answer for the drink it names.
"""

import os

LETTER = "A"

assert len(LETTER) == 1 and LETTER in "AB", "entry must be one letter, A or B"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
