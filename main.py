#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one original two-line family scene to /output/entry.txt.
The scene is warm, funny and heartfelt: a small Sunday-morning
moment at the breakfast table, told in 231 characters.

Gate (per the bounty rules): /output/entry.txt must be UTF-8 text of
1 to 280 characters, one or two lines, not only white space.

Usage:
    python3 main.py                       # writes /output/entry.txt
    python3 main.py --out /tmp/entry.txt  # write elsewhere (local test)
    python3 main.py --quiet               # suppress the summary line
"""

import argparse
import sys

ENTRY = (
    "Every Sunday Dad burns the first pancake, blames the pan, then "
    "quietly makes an extra one for the dog \u2014 the only one of us "
    "who has never complained.\n"
    "Mum calls the burnt one love. We call it breakfast. "
    "We all ask for seconds anyway."
)

MAX_CHARS = 280
MAX_LINES = 2


def validate(text: str) -> None:
    """Reject any text that would fail the bounty gate."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only white space")
    if text != text.strip():
        raise ValueError("entry has leading or trailing white space")
    if text.count("\n") + 1 > MAX_LINES:
        raise ValueError(f"entry has more than {MAX_LINES} lines")


def main() -> int:
    parser = argparse.ArgumentParser(description="Write the family scene entry.")
    parser.add_argument("--out", default="/output/entry.txt",
                        help="output path (default: /output/entry.txt)")
    parser.add_argument("--quiet", action="store_true",
                        help="suppress the summary line")
    args = parser.parse_args()

    try:
        validate(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Verify what was written matches the entry exactly.
    with open(args.out, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written file does not match ENTRY"
    validate(written)

    if not args.quiet:
        lines = ENTRY.count("\n") + 1
        print(f"Wrote {len(ENTRY)} characters ({lines} lines) to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
