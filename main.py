#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes the one-line elevator pitch a city pigeon gives investors for its
startup to /output/entry.txt. Standard library only.
"""

import os

PITCH = (
    "Coo.ly is Yelp for statues, written by the pigeons who've been "
    "reviewing every monument in the city for centuries \u2014 five stars, "
    "one splat at a time. Seed round's open."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"Wrote {len(PITCH)} characters to {path}")


if __name__ == "__main__":
    main()
