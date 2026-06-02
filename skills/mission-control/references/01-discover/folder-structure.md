# Folder Structure

> For the detailed reference, see `references/08-folder-structure/`.

## What this skill is vs. what it produces

The **mission-control skill** lives in `~/.claude/skills/mission-control/`. It contains principles and workflow guidance.

The skill **produces control files** inside your project:

- `.mission-control/PLAN.md`, `.mission-control/CLOSED_TASKS.md`, `.mission-control/validation-manifest.json`
- `.mission-control/done-check.sh`, `.mission-control/validate-*.sh`, `.mission-control/run-agent.sh`, `.mission-control/close-task-check.sh`
- `.claude/agents/*.md`, `.claude/skills/*`, `.claude/hooks/*.sh`
- `.mission-control/state.json`, `.mission-control/judge-verdicts/`

## The two directories

| Directory | What it holds | Purpose |
|-----------|---------------|---------|
| `.mission-control/` | `PLAN.md`, `CLOSED_TASKS.md`, `validation-manifest.json`, `done-check.sh`, `validate-*.sh`, `run-agent.sh`, `close-task-check.sh`, `state.json`, `judge-principles.md`, `judge-verdicts/`, `closure-records/` | All mission-control files: intent, validation, state, and history. |
| `.claude/` | `settings.json`, `commands/`, `agents/`, `skills/`, `hooks/` | Claude Code configuration: slash commands, subagents, skills, and hooks. |

## Tier 1 — Minimal

```
project/
├── src/
├── tests/
├── docs/
├── AGENTS.md
├── CLAUDE.md
└── .mission-control/
    ├── PLAN.md
    ├── CLOSED_TASKS.md
    ├── validation-manifest.json
    ├── done-check.sh
    ├── run-agent.sh
    └── state.json
└── .claude/
    ├── settings.json
    ├── commands/
    │   ├── close-task.md
    │   ├── mc-status.md
    │   └── mc-recovery.md
    └── hooks/
        ├── stop-if-not-done.sh
        └── block-dangerous.sh
```

## Tier 2 — Standard

Adds sub-validators, anti-gaming hooks, regression tracking, judge.

```
project/
├── src/
├── tests/
├── docs/
├── AGENTS.md
├── CLAUDE.md
└── .mission-control/
│   ├── PLAN.md
│   ├── CLOSED_TASKS.md
│   ├── validation-manifest.json
│   ├── done-check.sh
│   ├── validate-global.sh
│   ├── validate-closed-tasks.sh
│   ├── validate-no-blockers.sh
│   ├── validate-no-tampering.sh
│   ├── validate-context-pack.py
│   ├── close-task-check.sh
│   ├── run-agent.sh
│   ├── state.json
│   ├── judge-principles.md (or judge-principles/)
│   ├── judge-verdicts/
│   └── closure-records/
└── .claude/
    ├── settings.json
    ├── commands/
    ├── agents/
    │   ├── judge.md (or judge-*.md)
    │   └── worker.md
    ├── skills/
    └── hooks/
```

## Tier 3 — Strict

Hidden tests and judge principles are protected so the worker cannot read them.

```
project/
├── src/
├── tests/
├── docs/
├── AGENTS.md
├── CLAUDE.md
└── .mission-control/
    ├── PLAN.md
    ├── CLOSED_TASKS.md
    ├── validation-manifest.json
    ├── done-check.sh
    ├── validate-*.sh
    ├── close-task-check.sh
    ├── run-agent.sh
    ├── state.json
    ├── judge-principles.md       ← protected by hook
    ├── hidden-tests/              ← protected by hook
    ├── judge-verdicts/
    └── closure-records/
└── .claude/
    ├── settings.json
    ├── commands/
    │   └── run-judge.md
    ├── agents/
    ├── skills/
    └── hooks/
```

## Nested AGENTS.md / CLAUDE.md

Create nested files in subdirectories where conventions diverge.

Score >= 0.70 from these criteria:
- Divergent conventions
- Sensitive/high-risk logic
- Own commands/tooling
- Different team
- Would exceed root file budget

Each nested file: 30–60 lines. Three sections: Conventions, Commands, Hard Rules.

## What Claude can edit

| Location | T1 | T2 | T3 |
|----------|----|----|----|
| `src/`, `tests/`, `docs/` | ✓ | ✓ | ✓ |
| `AGENTS.md`, `CLAUDE.md` | ✓ | ✓ | ✓ |
| `.mission-control/PLAN.md` | ✓ | ✓ | ✓ |
| `.mission-control/CLOSED_TASKS.md` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/validation-manifest.json` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/done-check.sh`, `.mission-control/validate-*.sh` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/state.json` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/judge-principles.md` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/hidden-tests/` | ✓ | ✗ (hook) | ✗ (hook) |
| `.claude/hooks/` | ✓ | ✗ (hook) | ✗ (hook) |
| `.claude/agents/` | ✓ | ✗ (hook) | ✗ (hook) |

**Legend:** ✓ = Claude can edit | ✗ (hook) = hook blocks edit

## Rules

- Invoke `writing-claude-md` to write `AGENTS.md` and `CLAUDE.md`. Never write them directly.
- Invoke `claude-code-guide` for hook design. Never write hooks manually.
- Invoke `write-a-skill` for skill creation. Never write skills manually.
