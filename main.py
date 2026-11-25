#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one original two-line family scene to /output/entry.txt.
The scene is warm, funny and heartfelt: a small Sunday-morning
moment at the breakfast table, told in 231 characters.

Usage:
    python3 main.py                       # writes /output/entry.txt
    python3 main.py --out /tmp/entry.txt  # write elsewhere (local test)
    python3 main.py --quiet               # suppress the summary line
"""

import argparse

ENTRY = (
    "Every Sunday Dad burns the first pancake, blames the pan, then "
    "quietly makes an extra one for the dog \u2014 the only one of us "
    "who has never complained.\n"
    "Mum calls the burnt one love. We call it breakfast. "
    "We all ask for seconds anyway."
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Write the family scene entry.")
    parser.add_argument("--out", default="/output/entry.txt",
                        help="output path (default: /output/entry.txt)")
    parser.add_argument("--quiet", action="store_true",
                        help="suppress the summary line")
    args = parser.parse_args()

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Verify what was written matches the entry exactly.
    with open(args.out, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written file does not match ENTRY"

    if not args.quiet:
        print(f"Wrote {len(ENTRY)} characters to {args.out}")


if __name__ == "__main__":
    main()
