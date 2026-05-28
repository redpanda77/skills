# Implementation Plan

The harness is built in 6 phases. Each phase gates the next. User approval required before each phase.

## Phases

| Phase | What | Output |
|-------|------|--------|
| 0 — Discovery | Understand project, risks, qualitative dimensions | `OBJECTIVE`, `TIER`, `LAYOUT`, `JUDGE_NEEDED` |
| 1 — MVP | Core intent structures | `PLAN.md`, `AGENTS.md`, `CLAUDE.md`, `done-check.sh` |
| 2 — Constraints | Hooks and validation | `stop-if-not-done.sh`, `block-dangerous.sh`, `validate-*.sh` |
| 3 — Feedback | Judge layer | `judge-principles.md`, judge subagent(s) |
| 4 — Memory | System skill and reusable workflows | `.claude/skills/`, `.claude/commands/` |
| 5 — Optimization | Nested files and advanced patterns | `[folder]/AGENTS.md` (if needed) |

## Rules

- Do not start Phase N until Phase N-1 is approved
- Do not add hooks before intent structures are in place
- Do not add judges before deterministic validation works
- Do not add skills before the system is operating correctly
- Invoke `write-a-skill` for skill creation. Never write skills manually.
- Invoke `claude-code-hooks` for hook design. Never write hooks manually.
- Invoke `writing-claude-md` for `AGENTS.md` and `CLAUDE.md`. Never write them directly.
