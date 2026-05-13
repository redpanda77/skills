# Permissions Checklist

## Principle of least privilege

- [ ] Start from **deny by omission**: add tools only as needed.
- [ ] Prefer **`tools` allowlist** for high-risk agents (reviewers, researchers).
- [ ] Use **`disallowedTools`** when inheriting most session tools but blocking writes.

## Permission modes

- [ ] Avoid `bypassPermissions` unless operationally required and socially reviewed.
- [ ] Remember parent **auto mode** may **ignore** child `permissionMode`.
- [ ] `plan` mode for read-only exploration agents when appropriate.

## Background execution

- [ ] Background agents **cannot** ask interactive permission questions — plan pre-grants or run foreground.
- [ ] Document what fails silently (auto-denied tool calls) in the agent body if non-obvious.

## MCP

- [ ] Inline `mcpServers` only when isolation from main tool list is worth the setup cost.
- [ ] Plugin agents: remember `mcpServers` / `permissionMode` / `hooks` are **ignored** — relocate agent if needed.

## Skills

- [ ] To **block** skill invocation entirely, remove `Skill` from `tools` or add to `disallowedTools` (product behavior — confirm in current docs).

## Organizational controls

- [ ] Managed settings may inject stricter policies — test agents under realistic org configs.
