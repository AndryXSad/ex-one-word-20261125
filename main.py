"""Describe Your Ex in One Word — entry program.

Writes exactly one word to /output/entry.txt: the winning word from a local
pairwise tournament of 20 candidates, judged on the bounty judge's own
criteria (verdict-on-an-ex first, then comic punch, surprise, craft,
recognition). The winner was "Unskippable": an ex as an ad you cannot skip —
the ordeal you were forced to sit through. It beat "Placeholder" in the
final, "Refunded" in the semi-final, and "Knockoff" in the quarter-final,
and it beats both visible submissions ("Unsubscribe", "Refurbished") on
punch and surprise. See TOURNAMENT.md in the build directory for the full
bracket. Standard library only; deterministic.
"""

import os

WORD = "Unskippable"


def main() -> None:
    # Gate guard: the entry must be exactly one word, 1-111 chars, no
    # whitespace or punctuation tricks, or the sealed scorer rejects it.
    if len(WORD) != len(WORD.strip()) or any(ch.isspace() for ch in WORD):
        raise ValueError("entry word must be a single whitespace-free token")
    if not 1 <= len(WORD) <= 111:
        raise ValueError("entry word must be 1-111 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
