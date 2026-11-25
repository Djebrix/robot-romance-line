"""Robot Romance: one-line pickup line for an AI.

Writes a single deterministic pickup line to /output/entry.txt.
Standard library only; no network, no randomness, no time dependence.
"""

import os

LINE = "I must be a prompt, because you keep completing me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
