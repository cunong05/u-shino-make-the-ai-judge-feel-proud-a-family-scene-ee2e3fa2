#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one original two-line family scene to /output/entry.txt.
The scene is warm, funny and heartfelt: a small Sunday-morning
moment at the breakfast table, told in 231 characters.
"""

ENTRY = (
    "Every Sunday Dad burns the first pancake, blames the pan, then "
    "quietly makes an extra one for the dog \u2014 the only one of us "
    "who has never complained.\n"
    "Mum calls the burnt one love. We call it breakfast. "
    "We all ask for seconds anyway."
)


def main() -> None:
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {out_path}")


if __name__ == "__main__":
    main()
