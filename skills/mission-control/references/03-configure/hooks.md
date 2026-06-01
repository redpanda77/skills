# Hooks Setup

How to design and install hooks.

## What hooks are

Hooks are automated guardrails. They block bad actions before they happen.

## Types

| Hook | Event | Purpose |
|---|---|---|
| `stop-if-not-done.sh` | Stop | Blocks premature exit |
| `block-dangerous.sh` | PreToolUse (Bash) | Blocks destructive commands |
| `protect-control-files.sh` | PreToolUse (Write/Edit) | Blocks editing control files |
| `worker-boundary-guard.sh` | PreToolUse (Agent) | Blocks off-route agent invocations |
| `session-start-reminder.sh` | SessionStart | Re-injects rules |
| `post-edit-reminder.sh` | PostToolUse (Write/Edit) | Reminds to validate |
| `post-tool-validate.sh` | PostToolUse | Validates tool output |
| `post-compact-audit.sh` | PostCompact | Audits after context compaction |
| `task-sync-guard.sh` | TaskSync | Blocks out-of-order task claims |

## Rules

- Hooks are hard blocks, not suggestions.
- The agent receives the block message as its next input and must act on it.
- Hooks are produced by the `claude-code-hooks` skill. Do not write them manually.
- The Stop hook checks `done-check.sh` first, then judge verdicts. Scripts check, judges decide.
- The hook does NOT spawn the judge itself. It checks for the judge's verdict file.
