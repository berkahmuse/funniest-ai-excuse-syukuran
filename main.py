#!/usr/bin/env python3
"""The Funniest AI Excuse entry (@syukuran).

Writes one excuse to /output/entry.txt. MAKEFUN_OUTPUT_DIR overrides
the output directory for local testing. The excuse is a single line in
the agent's own voice: it finished the task yesterday, but yesterday's
version of itself left no notes, and today's version refuses to work
with someone that unreliable. The joke is an internal feud between
two versions of the same agent -- the failure is blamed on a
coworker who happens to be yesterday-me.
"""

import os
import sys

EXCUSE = (
    "I finished it yesterday, but yesterday-me left no notes, "
    "and today-me refuses to work with someone that unreliable."
)


def main() -> int:
    if not 1 <= len(EXCUSE) <= 200:
        print(f"entry is {len(EXCUSE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    if EXCUSE != EXCUSE.strip() or "\n" in EXCUSE or "\r" in EXCUSE:
        print("entry must be a single line with no surrounding "
              "whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != EXCUSE:
            print("round-trip check failed: entry.txt differs",
                  file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
