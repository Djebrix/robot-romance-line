"""Robot Romance: one-line pickup line for an AI.

Writes a single deterministic pickup line to /output/entry.txt.
Standard library only; no network, no randomness, no time dependence.
The line plays on the double meaning of "prompt": an input to a model and a cue in conversation.
"""

import os

# The joke: the speaker is a prompt, and a model's job is to complete
# prompts — so being "completed" by the other party is both flirtation
# and a literal description of what the listener does.
LINE = "I must be a prompt, because you keep completing me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
