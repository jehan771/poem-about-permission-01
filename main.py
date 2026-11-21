"""The poem about permission.

Writes one short poem to /output/entry.txt: a child asks to keep a stray
dog, the mother gives one night, and the night lasts twelve years.
Deterministic: fixed text, no network, no randomness, no clock.
"""

import os

POEM = (
    "Mum, can I keep him?\n"
    "The stray was mud to the ears,\n"
    "ribs like a xylophone.\n"
    "She weighed the rent, the rules\n"
    "taped to the fridge, then slid\n"
    "his bowl half an inch closer.\n"
    '"One night," she said.\n'
    "He stayed twelve years.\n"
)


def main():
    # Gate: the competition allows 1-280 Unicode code points, not only
    # whitespace. Refuse to write an invalid artifact instead of
    # silently producing one the gate would score 0.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise SystemExit(
            "invalid poem: %d code points" % len(POEM)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
