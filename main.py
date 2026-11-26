"""The Word You'd Delete From the Dictionary.

Entry: "inflammable" -- the word that looks like it means
"not flammable" and actually means "flammable". It lies to you
at the exact moment you most need the truth, and deleting it
costs nothing, because "flammable" already says it plainly.
"""

import os

WORD = "inflammable"
OUTPUT_PATH = "/output/entry.txt"


def main():
    # The entry must be exactly one word: lowercase letters, no spaces,
    # no punctuation, no extra text -- the word alone is the whole joke.
    assert WORD.isalpha(), "entry must be a single word"
    assert WORD.islower(), "entry must be lowercase"
    assert " " not in WORD, "entry must contain no spaces"
    assert 1 <= len(WORD) <= 30, "entry length out of range"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Verify what was written: exactly the word, no trailing newline.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data == WORD.encode("utf-8"), "output bytes do not match entry"
    assert not data.endswith(b"\n"), "output must not end with a newline"


if __name__ == "__main__":
    main()
