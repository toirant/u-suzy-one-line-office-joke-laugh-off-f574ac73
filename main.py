#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only
whitespace, on a single line.
"""

import os

JOKE = "My manager told me to bring my whole self to work, so I brought my resignation letter too."


def main():
    # The gate rejects anything outside 1..200 chars, blank text,
    # or more than one line, so validate before writing.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert "\n" not in JOKE.strip(), "joke must be a single line"
    assert JOKE.strip(), "joke must not be blank"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
