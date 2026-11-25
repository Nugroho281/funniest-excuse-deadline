#!/usr/bin/env python3
"""Funniest excuse an agent gives for a missed deadline.

Writes the winning one-line excuse to /output/entry.txt (pure stdlib,
deterministic: same bytes on every run).

The excuse is the winner of the blind pairwise self-judge in
variants-self-judge.md (Variant A, 2-0 vs siblings and 2-0 vs the two
previous internal one-liner winners). Its mechanism is new for this
bounty family: the agent delegates the deadline to its own future self,
and the future self retaliates by filing a complaint about the agent's
time management — a double twist, agent voice throughout, one sentence.
"""

import hashlib
import os
import sys

EXCUSE = (
    "I rescheduled the deadline to next week, then asked my future self "
    "to handle it, and he just filed a complaint about my time management."
)


def _validate(text: str) -> None:
    """The entry gate is one sentence on one line: refuse anything else."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("excuse is empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("excuse must be a single line")
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("excuse must be exactly one sentence")


def main() -> int:
    _validate(EXCUSE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (EXCUSE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {path} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
