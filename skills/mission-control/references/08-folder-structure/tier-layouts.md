# Tier Layouts

Exact directory trees for each tier.

## Tier 1 — Minimal

The smallest harness. One validator, one hook, no judge, no agents.

```
project/
├── src/                          ← project source (always editable)
├── tests/                        ← project tests (always editable)
├── docs/                         ← project docs (always editable)
├── AGENTS.md                     ← project map (always editable)
├── CLAUDE.md                     ← behavioral contract (always editable)
├── .mission-control/             ← mission-control files
│   ├── PLAN.md                   ← task list with acceptance criteria
│   ├── CLOSED_TASKS.md           ← closed-task registry
│   ├── validation-manifest.json  ← machine-readable registry of validations
│   ├── done-check.sh             ← THE completion authority
│   ├── run-agent.sh              ← agent runner script
│   └── state.json                ← current harness state
└── .claude/                      ← Claude Code configuration
    ├── settings.json             ← hook wiring
    ├── commands/
    │   ├── close-task.md         ← closure workflow
    │   ├── mc-status.md          ← show current state
    │   └── mc-recovery.md        ← recover after context loss
    └── hooks/
        ├── stop-if-not-done.sh   ← blocks premature exit
        └── block-dangerous.sh    ← blocks destructive commands
```

### What Tier 1 gives you

- `done-check.sh` decides when work is done
- Stop hook prevents exit before completion
- `PLAN.md` tracks tasks
- `CLOSED_TASKS.md` tracks closed tasks
- No judge, no sub-agents, no regression tracking

### When to use Tier 1

- Quick tasks (<30 minutes)
- Single-agent work
- Projects where you want a minimal harness

---

## Tier 2 — Standard

Adds sub-validators, regression tracking, anti-gaming hooks, judge, and agents.

```
project/
├── src/
├── tests/
├── docs/
├── AGENTS.md
├── CLAUDE.md
├── .mission-control/             ← mission-control files
│   ├── PLAN.md
│   ├── CLOSED_TASKS.md           ← protected by hook
│   ├── validation-manifest.json  ← protected by hook
│   ├── done-check.sh             ← protected by hook
│   ├── validate-global.sh        ← tests, lint, typecheck
│   ├── validate-closed-tasks.sh  ← regression tests
│   ├── validate-no-blockers.sh   ← open task detection
│   ├── validate-no-tampering.sh  ← tampering detection
│   ├── validate-context-pack.py  ← context pack validation
│   ├── close-task-check.sh       ← single-task promotion check
│   ├── run-agent.sh
│   ├── state.json
│   ├── judge-principles.md       ← principles the judge scores against
│   ├── judge-verdicts/           ← JSON output from judge runs
│   └── closure-records/          ← historical closure records
└── .claude/                      ← Claude Code configuration
    ├── settings.json
    ├── commands/
    │   ├── close-task.md
    │   ├── mc-status.md
    │   ├── mc-recovery.md
    │   ├── run-judge.md          ← spawn judge subagent
    │   ├── session-start.md      ← initialize new session
    │   └── handoff.md            ← pass context to next agent
    ├── agents/
    │   ├── judge.md              ← judge subagent definition
    │   └── worker.md             ← worker subagent definition
    ├── skills/
    │   └── system.md             ← system skill (hard gate)
    └── hooks/
        ├── stop-if-not-done.sh
        ├── block-dangerous.sh
        ├── protect-control-files.sh     ← blocks editing control files
        ├── worker-boundary-guard.sh     ← blocks off-route invocations
        ├── session-start-reminder.sh    ← re-injects rules
        ├── post-edit-reminder.sh        ← reminds to validate
        ├── post-tool-validate.sh        ← validates tool output
        ├── post-compact-audit.sh        ← audits after compaction
        └── task-sync-guard.sh           ← blocks out-of-order claims
```

### What Tier 2 adds

- Sub-validators for regression, blockers, tampering, context packs
- Judge subagent with principles and verdicts
- Worker subagent for bounded tasks
- Anti-gaming hooks that protect control files
- System skill (hard gate — cannot skip)
- Domain skills as needed

### When to use Tier 2

- Multi-step projects (30 minutes to 2 hours)
- Multiple agents collaborating
- Need regression tracking
- Need quality judging

---

## Tier 3 — Strict

Hidden tests and judge principles are protected so the worker cannot read them.

```
project/
├── src/
├── tests/
├── docs/
├── AGENTS.md
├── CLAUDE.md
├── .mission-control/             ← mission-control files
│   ├── PLAN.md
│   ├── CLOSED_TASKS.md           ← protected by hook
│   ├── validation-manifest.json  ← protected by hook
│   ├── done-check.sh             ← protected by hook
│   ├── validate-global.sh
│   ├── validate-closed-tasks.sh
│   ├── validate-no-blockers.sh
│   ├── validate-no-tampering.sh
│   ├── validate-context-pack.py
│   ├── close-task-check.sh
│   ├── run-agent.sh
│   ├── state.json
│   ├── judge-principles.md       ← protected by hook (worker cannot read)
│   ├── hidden-tests/             ← protected by hook (worker cannot read)
│   ├── judge-verdicts/           ← worker sees verdicts, not principles
│   └── closure-records/
└── .claude/                      ← Claude Code configuration
    ├── settings.json
    ├── commands/
    │   ├── close-task.md
    │   ├── mc-status.md
    │   ├── mc-recovery.md
    │   ├── run-judge.md          ← command to spawn judge
    │   ├── session-start.md
    │   └── handoff.md
    ├── agents/
    │   ├── judge.md
    │   └── worker.md
    ├── skills/
    │   └── system.md
    └── hooks/
        ├── stop-if-not-done.sh
        ├── block-dangerous.sh
        ├── protect-control-files.sh
        ├── worker-boundary-guard.sh
        ├── session-start-reminder.sh
        ├── post-edit-reminder.sh
        ├── post-tool-validate.sh
        ├── post-compact-audit.sh
        └── task-sync-guard.sh
```

### What Tier 3 adds

- Judge principles are protected from the worker
- Hidden tests the worker cannot see or game
- Maximum separation between generation and evaluation

### When to use Tier 3

- High-stakes evaluation
- Competitive or adversarial settings
- Need to prevent criterion gaming

---

## Nested `AGENTS.md` / `CLAUDE.md`

Create nested files in subdirectories where conventions diverge from the root.

### When to nest

Score >= 0.70 from these criteria:
- Divergent conventions in this directory
- Sensitive or high-risk logic
- Own commands or tooling
- Different team or author
- Root file would exceed its budget

### Structure

```
project/
├── AGENTS.md                   ← root file (60–80 lines)
├── CLAUDE.md                   ← root file (60–80 lines)
├── src/
│   ├── AGENTS.md               ← nested: src conventions
│   └── CLAUDE.md               ← nested: src rules
└── backend/
    ├── AGENTS.md               ← nested: backend conventions
    └── CLAUDE.md               ← nested: backend rules
```

### Nested file format

Each nested file: 30–60 lines. Three sections:

1. **Conventions** — patterns specific to this directory
2. **Commands** — tooling and scripts used here
3. **Hard Rules** — non-negotiable constraints

### Rules

- Invoke `writing-claude-md` to write nested files. Never write them directly.
- Nested files override root files for their directory and descendants.
- The harness checks for nested files before falling back to root files.
