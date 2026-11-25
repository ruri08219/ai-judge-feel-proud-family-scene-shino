"""make.fun entry: Make the AI Judge Feel Proud — A Family Scene.

Writes one short family scene (one line, <= 280 chars) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "Every Sunday, Dad inspects Mum's roast like a general, carves one slice, "
    "nods once, and says, 'Not bad' — which in our house means he loved it "
    "so much he went back for thirds."
)

MAX_CHARS = 280


def validate(text):
    """Return True only if text passes the competition gate."""
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if len(text.splitlines()) > 2:
        return False
    if any(ord(ch) < 0x20 and ch not in "\n" for ch in text):
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
