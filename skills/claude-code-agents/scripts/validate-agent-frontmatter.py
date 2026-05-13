#!/usr/bin/env python3
"""
Structural checks for Claude Code subagent Markdown definitions (YAML frontmatter).

Not a complete schema validator — confirm ambiguous details against:
https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields
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

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

KNOWN_TOP_LEVEL_KEYS = frozenset(
    {
        "name",
        "description",
        "tools",
        "disallowedTools",
        "model",
        "permissionMode",
        "maxTurns",
        "skills",
        "mcpServers",
        "hooks",
        "memory",
        "background",
        "effort",
        "isolation",
        "color",
        "initialPrompt",
    }
)

KNOWN_MODELS = frozenset({"sonnet", "opus", "haiku", "inherit"})
KNOWN_PERMISSION_MODES = frozenset(
    {"default", "acceptEdits", "auto", "dontAsk", "bypassPermissions", "plan"}
)
KNOWN_MEMORY = frozenset({"user", "project", "local"})
KNOWN_ISOLATION = frozenset({"worktree"})
KNOWN_COLORS = frozenset(
    {"red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"}
)
KNOWN_EFFORT = frozenset({"low", "medium", "high", "xhigh", "max"})


def err(msg: str) -> None:
    print(msg, file=sys.stderr)


def split_frontmatter(text: str) -> tuple[dict[str, Any], str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    raw_fm = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
    if yaml is None:
        raise RuntimeError("PyYAML is required: pip install pyyaml")
    data = yaml.safe_load(raw_fm)
    if not isinstance(data, dict):
        return None
    return data, body


def _as_str_list(value: Any, field: str) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        parts = [p.strip() for p in re.split(r"[,\s]+", value) if p.strip()]
        return parts
    if isinstance(value, list) and all(isinstance(x, str) for x in value):
        return list(value)
    raise ValueError(f"{field} must be a string or list of strings")


def validate_frontmatter(data: dict[str, Any], path: str) -> list[str]:
    problems: list[str] = []

    unknown = set(data.keys()) - KNOWN_TOP_LEVEL_KEYS
    if unknown:
        problems.append(f"{path}: unknown frontmatter keys: {sorted(unknown)}")

    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        problems.append(f"{path}: missing or invalid 'name' (non-empty string required)")
    elif not NAME_RE.match(name):
        problems.append(
            f"{path}: 'name' should be lowercase letters, digits, and hyphens (got {name!r})"
        )

    desc = data.get("description")
    if not isinstance(desc, str) or not desc.strip():
        problems.append(f"{path}: missing or invalid 'description' (non-empty string required)")

    model = data.get("model")
    if model is not None:
        if not isinstance(model, str):
            problems.append(f"{path}: 'model' must be a string if present")
        elif model not in KNOWN_MODELS and not model.startswith("claude-"):
            problems.append(
                f"{path}: 'model' {model!r} is not a known alias; if intentional, use a full model id"
            )

    pm = data.get("permissionMode")
    if pm is not None and pm not in KNOWN_PERMISSION_MODES:
        problems.append(f"{path}: invalid permissionMode {pm!r}")

    mem = data.get("memory")
    if mem is not None and mem not in KNOWN_MEMORY:
        problems.append(f"{path}: invalid memory {mem!r}")

    iso = data.get("isolation")
    if iso is not None and iso not in KNOWN_ISOLATION:
        problems.append(f"{path}: invalid isolation {iso!r}")

    color = data.get("color")
    if color is not None and color not in KNOWN_COLORS:
        problems.append(f"{path}: invalid color {color!r}")

    effort = data.get("effort")
    if effort is not None and effort not in KNOWN_EFFORT:
        problems.append(f"{path}: invalid effort {effort!r}")

    bg = data.get("background")
    if bg is not None and not isinstance(bg, bool):
        problems.append(f"{path}: 'background' must be a boolean if present")

    mt = data.get("maxTurns")
    if mt is not None:
        if not isinstance(mt, int) or isinstance(mt, bool) or mt < 1:
            problems.append(f"{path}: 'maxTurns' must be a positive integer if present")

    try:
        _as_str_list(data.get("tools"), "tools")
        _as_str_list(data.get("disallowedTools"), "disallowedTools")
        skills = data.get("skills")
        if skills is None:
            pass
        elif isinstance(skills, list) and all(isinstance(x, str) for x in skills):
            pass
        else:
            raise ValueError("skills must be a list of strings")
    except ValueError as exc:
        problems.append(f"{path}: {exc}")

    hooks = data.get("hooks")
    if hooks is not None and not isinstance(hooks, dict):
        problems.append(f"{path}: 'hooks' must be a mapping if present (see hooks docs)")

    mcp = data.get("mcpServers")
    if mcp is not None and not isinstance(mcp, list):
        problems.append(f"{path}: 'mcpServers' must be a list if present")

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Markdown agent files to validate")
    args = parser.parse_args()

    if yaml is None:
        err("PyYAML is required. Install with: pip install pyyaml")
        return 2

    any_failed = False
    for raw in args.paths:
        path = Path(raw)
        if not path.is_file():
            err(f"{path}: not a file")
            any_failed = True
            continue
        text = path.read_text(encoding="utf-8")
        parsed = split_frontmatter(text)
        if parsed is None:
            err(f"{path}: missing YAML frontmatter fenced by ---")
            any_failed = True
            continue
        fm, body = parsed
        if not body.strip():
            err(f"{path}: warning: empty markdown body (system prompt)")
        probs = validate_frontmatter(fm, str(path))
        if probs:
            any_failed = True
            for p in probs:
                err(p)
        else:
            print(f"OK {path}")

    return 1 if any_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
