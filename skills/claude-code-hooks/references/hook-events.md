---
source_urls:
  - https://code.claude.com/docs/en/hooks#hook-events
last_reviewed: 2026-05-13
---

# Hook events (catalog)

The authoritative list — with **when each event fires**, **input JSON**, and **decision / blocking** behavior — is on the official page:

**[Hooks reference → Hook events](https://code.claude.com/docs/en/hooks#hook-events)**

## Summary table (from official docs)

| Event | When it fires |
| --- | --- |
| `SessionStart` | Session begins or resumes |
| `Setup` | `--init-only`, or `--init` / `--maintenance` in `-p` mode |
| `UserPromptSubmit` | Prompt submitted, before Claude processes it |
| `UserPromptExpansion` | User-typed command expands into a prompt (can block expansion) |
| `PreToolUse` | Before a tool runs (can block) |
| `PermissionRequest` | Permission dialog |
| `PermissionDenied` | Tool denied by auto classifier (`retry: true` supported) |
| `PostToolUse` | After tool succeeds |
| `PostToolUseFailure` | After tool fails |
| `PostToolBatch` | After a batch of parallel tool calls resolves |
| `Notification` | Claude Code sends a notification |
| `SubagentStart` / `SubagentStop` | Subagent spawned / finishes |
| `TaskCreated` / `TaskCompleted` | Task lifecycle |
| `Stop` / `StopFailure` | Turn completes / API error ends turn |
| `TeammateIdle` | Agent-team teammate about to go idle |
| `InstructionsLoaded` | `CLAUDE.md` or `.claude/rules/*.md` loaded |
| `ConfigChange` | Config file changes mid-session |
| `CwdChanged` | Working directory changes |
| `FileChanged` | Watched file changes |
| `WorktreeCreate` / `WorktreeRemove` | Git worktree lifecycle |
| `PreCompact` / `PostCompact` | Before / after compaction |
| `Elicitation` / `ElicitationResult` | MCP elicitation flows |
| `SessionEnd` | Session terminates |

For each event, the reference documents **matcher support** (some events ignore matchers), **stdin fields**, and **allowed JSON responses**. Always verify against the live docs before relying on blocking semantics.
