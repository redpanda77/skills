# Hooks

Guardrails that enforce constraints and prevent off-protocol actions.

## Purpose

Block premature exit, dangerous commands, off-route work, and scope violations. Hooks are part of the control system, not obstacles to bypass.

## What they are

Shell scripts wired to Claude Code events:

| Event | Hook | Purpose |
|-------|------|---------|
| Stop | `stop-if-not-done.sh` | Blocks exit until `done-check.sh` passes |
| PreToolUse | `block-dangerous.sh` | Blocks destructive commands |
| PreToolUse | `protect-control-files.sh` | Blocks editing `.claude/`, `PLAN.md`, etc. |
| PreToolUse | `worker-boundary-guard.sh` | Blocks off-route agent invocations |
| SessionStart | `session-start-reminder.sh` | Re-injects rules |
| PostToolUse | `post-tool-validate.sh` | Validates tool output |
| PostCompact | `post-compact-audit.sh` | Audits after context compaction |
| TaskSync | `task-sync-guard.sh` | Blocks out-of-order task claims |

## Rules

- If a hook blocks a tool call, assume the attempted action is off-protocol until proved otherwise
- Do not switch to shell reads, inline Python, direct writes, or ad-hoc scripts to get past a block
- If a hook blocks valid work:
  1. Confirm the router's exact next action
  2. Check whether the rendered prompt names the expected target
  3. Fix the narrow mismatch in the route, prompt, context pack, or subagent handoff
  4. Do not allow broad off-route probing or protected writes
- Do not edit hooks or settings during normal execution
- Hook changes are control-layer maintenance; they require explicit user request or Escape Protocol

## Failure Mode

If hooks are broken or bypassed:
- Destructive commands run unblocked
- Agents exit prematurely before validation
- Off-route work pollutes the project
- Control files are edited directly, breaking the harness
- Scope violations cause cascading failures

## Escape Protocol

When the control system itself is broken — the router loops, the hook is wrong, the validator has a false positive, or the pipeline is stuck with no legal action — the system enters Escape Protocol.

Escape Protocol is the only path that repairs the control system without weakening the quality gates.

Rules:
- Escape Protocol requires explicit user authorization or a router-classified `control_failure` state
- Repairs are limited to control-layer artifacts: router, hooks, validators, prompt renderers
- Canonical content, judge principles, and acceptance criteria are NOT changed during Escape Protocol
- Control repair workers have restricted tool access and cannot write canonical artifacts
- After control repair, the system re-runs the router and resumes normal workflow
- Escape Protocol is not a license to bypass hooks or skip validation

## Repair Authority

- Hook blocks valid work → fix the route/prompt/pack, not the hook
- Hook is genuinely wrong → control-layer maintenance via Escape Protocol
- Never bypass a hook to complete a task
