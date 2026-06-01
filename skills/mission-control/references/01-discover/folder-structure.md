# Folder Structure

## What this skill is vs. what it produces

The **mission-control skill** lives in `~/.claude/skills/mission-control/`. It contains principles and workflow guidance.

The skill **produces control files** inside your project:

- `PLAN.md`, `AGENTS.md`, `CLAUDE.md`
- `done-check.sh`, `run-agent.sh`
- `.claude/agents/*.md`, `.claude/skills/*`, `.claude/hooks/*.sh`
- `.mission-control/state.json`, `.mission-control/judge-verdicts/`

## Tier 1 — Minimal

```
project/
├── PLAN.md
├── CLOSED_TASKS.md
├── validation-manifest.json
├── done-check.sh
├── run-agent.sh
├── AGENTS.md
├── CLAUDE.md
├── .mission-control/
│   └── state.json
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
├── PLAN.md, CLOSED_TASKS.md, validation-manifest.json
├── done-check.sh, validate-*.sh, close-task-check.sh, run-agent.sh
├── .mission-control/
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

## Tier 2 — External

Control scripts live outside repo. Physical isolation.

```
parent/
├── project/                 # Claude's workspace
│   ├── PLAN.md, CLAUDE.md
│   ├── .mission-control/
│   └── .claude/
└── agent-control/           # outside Claude's workspace
    ├── done-check.sh
    ├── validate-*.sh
    ├── close-task-check.sh
    ├── run-agent.sh
    └── hooks/
```

## Tier 3 — Strict

Judge rubric moves outside project. Worker cannot read criteria.

```
parent/
├── project/
│   └── .claude/commands/run-judge.md
└── agent-control/
    ├── judge-principles-private.md
    └── hidden-tests/
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

| Location | T1 | T2 inline | T2 external | T3 |
|----------|----|-----------|-------------|----|
| `src/`, `tests/` | ✓ | ✓ | ✓ | ✓ |
| `PLAN.md` | ✓ | ✓ | ✓ | ✓ |
| `.mission-control/` | ✓ | ✓ | ✓ | ✓ |
| `CLOSED_TASKS.md` | ✓ | ✗ (hook) | ✓ | ✗ |
| `validation-manifest.json` | ✓ | ✗ (hook) | ✓ | ✗ |
| `done-check.sh`, `validate-*.sh` | ✓ | ✗ (hook) | ✗ (outside) | ✗ (outside) |
| `.claude/hooks/` | ✓ | ✗ (hook) | ✗ (outside) | ✗ (outside) |

## Rules

- Invoke `writing-claude-md` to write `AGENTS.md` and `CLAUDE.md`. Never write them directly.
- Invoke `claude-code-hooks` for hook design. Never write hooks manually.
- Invoke `write-a-skill` for skill creation. Never write skills manually.
