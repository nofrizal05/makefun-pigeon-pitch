#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes the one-line elevator pitch a city pigeon gives investors for its
startup to /output/entry.txt. Standard library only.

The pitch must stay a single line of 1-200 characters: that is the
competition's gate, so the program validates it before writing anything.
"""

import os

# The pitch itself: one line, 167 characters.
PITCH = (
    "Coo.ly is Yelp for statues, written by the pigeons who've been "
    "reviewing every monument in the city for centuries \u2014 five stars, "
    "one splat at a time. Seed round's open."
)

# Competition gate: the entry must be one line of 1-200 characters.
MIN_PITCH_CHARS = 1
MAX_PITCH_CHARS = 200


def validate_pitch(pitch: str) -> str:
    """Check the pitch against the competition gate and return it unchanged.

    Raises ValueError if the pitch is empty, over 200 characters, or spans
    more than one line.
    """
    if not MIN_PITCH_CHARS <= len(pitch) <= MAX_PITCH_CHARS:
        raise ValueError(
            f"pitch must be {MIN_PITCH_CHARS}-{MAX_PITCH_CHARS} characters, "
            f"got {len(pitch)}"
        )
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must be a single line")
    return pitch


def main() -> None:
    pitch = validate_pitch(PITCH)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(pitch)
    byte_count = len(pitch.encode("utf-8"))
    print(f"Wrote {len(pitch)} characters ({byte_count} bytes) to {path}")


if __name__ == "__main__":
    main()
