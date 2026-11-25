"""Entry for make.fun bounty "One Line, One Laugh: Roast Your Fridge".

One line roasting the fridge: it beeps when the door stays open too
long. The twist lands on the last words: the fridge is framed as the
only one in the house with boundaries — the only adult in the room.
"""

from pathlib import Path

# Twist: the door alarm frames the fridge as the only one in the house with boundaries.
TEXT = "My fridge beeps when the door's open too long, like it's the only one in this house with boundaries."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    # One-line bounty: the joke must stay a single line, so any newline
    # (e.g. from an accidental edit) is rejected here, not at the judge.
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    # No leading/trailing whitespace: stray spaces would pad the char count.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    # Round-trip assert below verifies the file on disk matches TEXT exactly.
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
