#!/usr/bin/env python3
"""
Lightweight structural check for Claude Code hook *settings* JSON (root object
with a "hooks" key). Not a full JSON-schema validator — confirm details against
https://code.claude.com/docs/en/hooks
"""
from __future__ import annotations

import json
import sys
from typing import Any

KNOWN_EVENTS = frozenset(
    {
        "SessionStart",
        "Setup",
        "UserPromptSubmit",
        "UserPromptExpansion",
        "PreToolUse",
        "PermissionRequest",
        "PermissionDenied",
        "PostToolUse",
        "PostToolUseFailure",
        "PostToolBatch",
        "Notification",
        "SubagentStart",
        "SubagentStop",
        "TaskCreated",
        "TaskCompleted",
        "Stop",
        "StopFailure",
        "TeammateIdle",
        "InstructionsLoaded",
        "ConfigChange",
        "CwdChanged",
        "FileChanged",
        "WorktreeCreate",
        "WorktreeRemove",
        "PreCompact",
        "PostCompact",
        "Elicitation",
        "ElicitationResult",
        "SessionEnd",
    }
)

HANDLER_TYPES = frozenset({"command", "http", "mcp_tool", "prompt", "agent"})


def err(msg: str) -> None:
    print(msg, file=sys.stderr)


def validate_matcher_group(node: Any, path: str) -> list[str]:
    problems: list[str] = []
    if not isinstance(node, dict):
        problems.append(f"{path}: matcher group must be an object")
        return problems
    hooks = node.get("hooks")
    if not isinstance(hooks, list) or not hooks:
        problems.append(f"{path}: each matcher group needs a non-empty 'hooks' array")
        return problems
    for i, h in enumerate(hooks):
        hp = f"{path}.hooks[{i}]"
        if not isinstance(h, dict):
            problems.append(f"{hp}: handler must be an object")
            continue
        t = h.get("type")
        if t not in HANDLER_TYPES:
            problems.append(f"{hp}: missing or invalid 'type' (expected one of {sorted(HANDLER_TYPES)})")
        if t == "command" and not h.get("command"):
            problems.append(f"{hp}: command handler needs 'command'")
        if t == "http" and not h.get("url"):
            problems.append(f"{hp}: http handler needs 'url'")
        if t == "mcp_tool":
            if not h.get("server"):
                problems.append(f"{hp}: mcp_tool handler needs 'server'")
            if not h.get("tool"):
                problems.append(f"{hp}: mcp_tool handler needs 'tool'")
        if t in ("prompt", "agent") and not h.get("prompt"):
            problems.append(f"{hp}: prompt/agent handler needs 'prompt'")
    return problems


def validate_root(doc: Any) -> int:
    if not isinstance(doc, dict):
        err("Root JSON must be an object")
        return 1
    hooks = doc.get("hooks")
    if hooks is None:
        err('Expected a "hooks" object at the top level (settings-style hook file).')
        return 1
    if not isinstance(hooks, dict):
        err('"hooks" must be an object keyed by event name')
        return 1

    problems: list[str] = []
    for event, groups in hooks.items():
        if event not in KNOWN_EVENTS:
            problems.append(f'Unknown hook event "{event}" (not in bundled catalog — may still be valid if docs added new events)')
        if not isinstance(groups, list) or not groups:
            problems.append(f'Event "{event}": value must be a non-empty array of matcher groups')
            continue
        for i, group in enumerate(groups):
            problems.extend(validate_matcher_group(group, f'hooks["{event}"][{i}]'))

    if problems:
        err("Validation issues:")
        for p in problems:
            err(f"  - {p}")
        return 1
    print("OK: basic hook settings structure looks valid.")
    return 0


def main() -> int:
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            err("No JSON on stdin")
            return 1
        doc = json.loads(raw)
    except json.JSONDecodeError as e:
        err(f"Invalid JSON: {e}")
        return 1
    return validate_root(doc)


if __name__ == "__main__":
    raise SystemExit(main())
