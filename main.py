"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only; no network; no writes inside the repo.
"""

import os

MONOLOGUE = (
    "You stand before Malachar, King of the Ashen Reaches. "
    "The kneeling can wait; my knees have filed a complaint. "
    "Nine valleys bow to me still. Seven crowns I melted into this throne, "
    "and still the armrest wobbles. Tonight the Ninth Tithe comes due: "
    "one ember from every hearth, carried here by hand. "
    "My ravens counted them. Twice. And you \u2014 you come with a "
    "sword, a prophecy, and that look. Sit. No \u2014 stand. The doom will "
    "keep. It kept three hundred years; it can keep till moonrise. "
    "The moonrise can wait five more minutes. It has waited this long."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(MONOLOGUE)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
