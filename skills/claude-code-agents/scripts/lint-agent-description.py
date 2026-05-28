#!/usr/bin/env python3
"""
Heuristic linter for Claude Code subagent `description` fields.

Encourages delegation-friendly text. This is not a correctness proof.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore[assignment]


def err(msg: str) -> None:
    print(msg, file=sys.stderr)


def split_frontmatter(text: str) -> dict[str, Any] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    raw_fm = text[3:end].strip()
    if yaml is None:
        raise RuntimeError("PyYAML is required: pip install pyyaml")
    data = yaml.safe_load(raw_fm)
    return data if isinstance(data, dict) else None


def lint_description(desc: str, path: str) -> list[str]:
    warnings: list[str] = []
    d = desc.strip()
    if len(d) < 80:
        warnings.append(f"{path}: description is short (<80 chars); consider more routing detail")
    if len(d) > 600:
        warnings.append(f"{path}: description is very long (>600 chars); move detail to body")

    lower = d.lower()
    if "use when" not in lower and "use after" not in lower and "use for" not in lower:
        warnings.append(f"{path}: consider starting with a trigger phrase like 'Use when…'")

    if not re.search(r"\breturns?\b|\bsummary\b|\bfindings\b|\breport\b", lower):
        warnings.append(f"{path}: mention what the agent returns (summary, findings, etc.)")

    vague = ("help", "assistant", "handles tasks", "does stuff", "various")
    if any(v in lower for v in vague) and "use when" not in lower:
        warnings.append(f"{path}: description may be too vague for reliable delegation")

    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Markdown agent files to lint")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any warnings are emitted",
    )
    args = parser.parse_args()

    if yaml is None:
        err("PyYAML is required. Install with: pip install pyyaml")
        return 2

    had_warnings = False
    for raw in args.paths:
        path = Path(raw)
        if not path.is_file():
            err(f"{path}: not a file")
            had_warnings = True
            continue
        fm = split_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            err(f"{path}: could not parse YAML frontmatter")
            had_warnings = True
            continue
        desc = fm.get("description")
        if not isinstance(desc, str) or not desc.strip():
            err(f"{path}: missing description")
            had_warnings = True
            continue
        msgs = lint_description(desc, str(path))
        if msgs:
            had_warnings = True
            for w in msgs:
                err(w)
        else:
            print(f"OK {path}")

    if args.strict and had_warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
