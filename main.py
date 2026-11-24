import os

TEXT = (
    "Drizzlewick: light rain, 14°, and the clouds have agreed to queue "
    "politely behind the bus shelter. Umbrellas optional, dignity intact."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate self-check: 1-140 chars, not whitespace only, one line, no
    # leading/trailing spaces (per RULES.txt sealed scorer).
    assert 1 <= len(TEXT) <= 140, f"text is {len(TEXT)} chars"
    assert TEXT.strip(), "text is whitespace only"
    assert "\n" not in TEXT and "\r" not in TEXT, "text must be one line"
    assert TEXT == TEXT.strip(), "text has leading/trailing spaces"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Post-write verification: prove the bytes on disk are exactly the
    # intended text, so a silent write failure or encoding slip fails
    # loudly here instead of reaching the judge.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == TEXT, "round-trip text mismatch"
    assert raw == TEXT.encode("utf-8"), "round-trip bytes mismatch"
    assert len(raw) == len(TEXT.encode("utf-8")), "round-trip length mismatch"
    print(TEXT)


if __name__ == "__main__":
    main()
