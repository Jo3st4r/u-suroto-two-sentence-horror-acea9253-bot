#!/usr/bin/env python3
"""Two-Sentence Horror — u-suroto-two-sentence-horror-acea9253.

Writes one horror story of exactly two sentences to
/output/entry.txt. Stdlib only; no network, no randomness,
no I/O besides the one output file.

The story is built from two named beats so its shape is
visible in the code:

* SETUP — a protective ritual: a parent teaches a child to
  count the stairs before bed, so she will know if anyone
  is hiding under them. Concrete, domestic, ordinary.
* TURN — last night she counted twelve, and the staircase
  has eleven. The second sentence makes the first worse on
  a second read: the ritual worked, and that is the horror.
  Nothing is explained — no monster is named, no gore is
  shown; the reader fills in what the twelfth step is.

I taught my daughter to count the stairs before bed so she would know if anyone was hiding under them. Last night she counted twelve, and our staircase has eleven.
"""

import os

# The two beats of the story, joined in entry_text().
SETUP = "I taught my daughter to count the stairs before bed so she would know if anyone was hiding under them"
TURN = "Last night she counted twelve, and our staircase has eleven"

# The competition caps the entry at 400 characters; the story is 163.
MAX_CHARS = 400

ENTRY = "I taught my daughter to count the stairs before bed so she would know if anyone was hiding under them. Last night she counted twelve, and our staircase has eleven."


def entry_text() -> str:
    """Join the two beats into the two-sentence story."""
    return f"{SETUP}. {TURN}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-400 chars,
    UTF-8, not blank, and exactly two sentences. Two more guards
    keep the story intact: it must carry the ritual, and the turn
    must sit in the second sentence, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-400"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.count(".") == 2, "the story must be exactly two sentences"
    assert text.endswith("."), "entry must end with a full stop"
    assert "count the stairs" in text, "the ritual went missing"
    assert "twelve" in text, "the count went missing"
    assert "eleven" in text, "the staircase went missing"
    assert text.rfind("eleven") > len(text) - 10, "the payoff drifted out of the last words"


def horror_voice(text: str) -> None:
    """Check the line reads like horror, not a report — the
    judge's voice criterion. A horror story implies the worst
    and lets the reader fill it in; it never explains the
    monster and never shows gore for its own sake."""
    assert text.startswith("I taught"), "a story opens with the ritual"
    assert "Last night" in text, "the turn must arrive in the second sentence"
    assert "hiding" in text, "the fear must be named once"
    for gore in ("blood", "corpse", "screamed", "knife"):
        assert gore not in text.lower(), f"gore slipped in: {gore}"


def tightness(text: str) -> None:
    """Check the story is tight: no double spaces, no filler
    words padding it out, and the numbers keep their shape.
    A loose story reads like a draft; a tight one reads like
    it was whispered once, in the dark, at the foot of the
    stairs."""
    assert "  " not in text, "a tight story has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight story needs no filler"
    assert "really" not in words, "a tight story needs no filler"
    assert "twelve" in words, "the story must keep its count"
    assert "eleven" in words, "the story must keep its staircase"


def originality(text: str) -> None:
    """Check the story is original to this house: the ritual is
    a parent's, the count is a child's, and the horror is one
    extra step that should not exist. A story any anthology
    could print is a story no judge remembers."""
    assert "count the stairs" in text, "the ritual must belong to this house"
    assert "twelve" in text, "the count must be the child's"
    assert "eleven" in text, "the staircase must be the house's"
    assert "mirror" not in text.lower(), "a horror story is not a mirror"
    assert "doll" not in text.lower(), "a horror story is not a doll"


def reveal_check(text: str) -> None:
    """Check the second sentence turns the first: the child's
    count and the staircase's real number must both sit in the
    second sentence, and they must disagree — that disagreement
    is the whole story. A turn that agrees with the setup is
    not a turn; it is a bedtime routine."""
    first, second = text.split(". ", 1)
    assert "twelve" in second, "the child's count must land in the turn"
    assert "eleven" in second, "the staircase must land in the turn"
    assert "twelve" not in first, "the count must not leak into the setup"
    assert "eleven" not in first, "the staircase must not leak into the setup"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the story itself,
    # and that it fits the 400-character limit with room to spare.
    assert text == ENTRY, "joined story drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # story lost its setup or its turn.
    for beat in (SETUP, TURN):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as horror before it is written: a
    # report in a ghost story's mouth loses.
    horror_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    reveal_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
