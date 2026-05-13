#!/usr/bin/env python3
"""Print a fixture JSON file to stdout for manual hook testing."""
from __future__ import annotations

import argparse
import pathlib
import sys


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("fixture", type=pathlib.Path, help="Path to a JSON fixture file")
    args = p.parse_args()
    if not args.fixture.is_file():
        print(f"Not a file: {args.fixture}", file=sys.stderr)
        return 1
    text = args.fixture.read_text(encoding="utf-8")
    sys.stdout.write(text)
    if not text.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
