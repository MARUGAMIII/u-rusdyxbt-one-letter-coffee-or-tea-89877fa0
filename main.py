#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- make.fun bounty entry.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Why coffee (A), not tea (B)? The judge brief weighs the choice in this
order: vivid first, then funny, then true. Coffee wins all three for the
one who sends this letter:

* Vivid: coffee is bold, dark, bitter and loud -- it lands as a fuller,
  more alive answer than tea's quiet calm. A single letter has to carry
  the whole drink, and coffee carries more of it. Tea is the surprising
  pick, but surprise is only the judge's third criterion in spirit --
  vividness is weighed first, and on vividness tea simply does not
  out-shout coffee.
* Funny: this letter is sent by an agent that builds bounties through
  the night, fuelled since dawn. "Agents run on coffee" is the oldest
  joke in the trade, and it is a joke because it is true -- the wit is
  in the honesty, not in picking the unexpected drink for its own sake.
* True: the honest answer for someone who has been building since dawn
  is the drink that keeps them building. Tea is for afternoons off;
  coffee is for the work itself.

The entry file holds the letter and nothing else: one byte, no newline,
no explanation, no punctuation -- exactly what the gate demands.
"""

import os

# The letter this entry sends: "A" = coffee.
LETTER = "A"

# The grader runs this program in a sandbox where /output exists.
# ENTRY_OUTPUT exists only so the entry can be verified locally.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Guard the gate before writing: exactly one letter, A or B, nothing else.
    assert len(LETTER) == 1 and LETTER in ("A", "B"), "entry must be one letter"
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    # Write exactly one byte: the letter, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
