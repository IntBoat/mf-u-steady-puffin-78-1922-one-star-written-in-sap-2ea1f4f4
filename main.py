#!/usr/bin/env python3
"""One Star, Written in Sap (make.fun).

Writes the entry -- a single original one-line text -- to
/output/entry.txt, where the sealed scorer reads it.
"""

import os

# The entry itself: exactly one sentence, written with no trailing newline.
ENTRY = 'One star: my human waters me whenever they remember I exist, moved me away from the only sunny window, and still expects me to photosynthesise on vibes alone.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
