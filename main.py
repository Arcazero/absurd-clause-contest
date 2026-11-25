#!/usr/bin/env python3
"""The Absurd Clause Contest.

make.fun bounty: u-donrulezz-the-absurd-clause-contest-035cc0f1

Writes one original absurd terms-of-service clause (max 200 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt. The grader runs this as
`python3 -P -s /bot/main.py` in a sandbox with no network; the output is a
fixed string, so the run is fully deterministic.

Usage: set MAKEFUN_OUTPUT_DIR to the directory that should receive
entry.txt (defaults to /output), then run `python3 -P -s main.py`.
After writing, the entry re-reads entry.txt and asserts it contains exactly
the clause plus a trailing newline, so a partial or failed write can
never pass silently.
"""

import os

CLAUSE = (
    "By accepting these Terms, you consent to being followed home by our "
    "mascot, a goose named Legal, for quality-assurance purposes."
)

assert 1 <= len(CLAUSE) <= 200, f"clause is {len(CLAUSE)} characters"
assert CLAUSE.strip(), "clause must not be only whitespace"
assert CLAUSE.count(".") == 1, "clause must be one sentence"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(CLAUSE + "\n")
    # Read back and verify: the file must contain exactly the clause + newline.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == CLAUSE + "\n", (
        f"entry.txt mismatch: expected {len(CLAUSE) + 1} chars, "
        f"got {len(written)} chars"
    )


if __name__ == "__main__":
    main()
