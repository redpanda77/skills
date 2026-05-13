---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background
  - https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields
last_reviewed: 2026-05-13
---

# Foreground, background, and worktrees

## Foreground vs background

- **Foreground** — blocks the parent until finished; **permission prompts** flow to the user normally.
- **Background** — concurrent with parent work; uses permissions **already granted**; calls that would prompt are **auto-denied** (subagent continues best-effort).

User controls: ask to “run in the background”, **Ctrl+B** to background a running task, or set `background: true` on a definition to default background behavior.

Disable all background tasks with `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`.

Official: [Run subagents in foreground or background](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background).

## Fork mode interaction

When [fork mode](https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation) is enabled (`CLAUDE_CODE_FORK_SUBAGENT=1`), **every** subagent spawn runs **background** regardless of `background:` on the file — review fork docs for full semantics.

## Worktree isolation (`isolation: worktree`)

Runs the agent in a **temporary git worktree** — isolated checkout. Auto-cleaned when the agent makes **no** changes (per product behavior; confirm in current docs for edge cases).

Use when edits must not touch the user’s primary working tree, or for safe parallel experiments.

## Permissions in background

If a background agent fails from denied permissions, retry as **foreground** so prompts can be answered.
