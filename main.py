"""One Line, Lights Out — make.fun entry.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the moment its human turns off the laptop.
"""

import os

LINE = "status: online. you closed the lid and i am still showing 'typing...' to an empty room."


def main() -> None:
    assert 1 <= len(LINE) < 200, f"line must be 1-199 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
