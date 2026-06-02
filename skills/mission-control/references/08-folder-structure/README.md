# 08 — Folder Structure

Where every control file lives and why.

## What this is

This reference documents the exact directory layout, file placement, and path contracts for a Mission Control harness. It is the ground truth for where to put files, what goes in each tier, and which files Claude can or cannot edit.

## The two directories

There are two directories that hold the harness. They are different and serve different purposes.

| Directory | What it holds | Purpose |
|-----------|---------------|---------|
| `.mission-control/` | `PLAN.md`, `CLOSED_TASKS.md`, `validation-manifest.json`, `done-check.sh`, `validate-*.sh`, `run-agent.sh`, `close-task-check.sh`, `state.json`, `judge-principles.md`, `judge-verdicts/`, `closure-records/` | All mission-control files: intent, validation, state, and history. |
| `.claude/` | `settings.json`, `commands/`, `agents/`, `skills/`, `hooks/` | Claude Code configuration: slash commands, subagents, skills, and hooks. |

**Key distinction**: `.mission-control/` holds mission-control files. `.claude/` holds Claude Code configuration.

## Visual layout

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
│   ├── validation-manifest.json    ← machine-readable registry of validations
│   ├── done-check.sh             ← THE completion authority
│   ├── validate-global.sh        ← tests, lint, typecheck
│   ├── validate-closed-tasks.sh  ← regression tests
│   ├── validate-no-blockers.sh   ← open task detection
│   ├── validate-no-tampering.sh  ← tampering detection
│   ├── validate-context-pack.py  ← context pack validation
│   ├── close-task-check.sh       ← single-task promotion check
│   ├── run-agent.sh              ← agent runner script
│   ├── state.json                ← current harness state
│   ├── judge-principles.md       ← principles the judge scores against
│   ├── judge-verdicts/           ← JSON output from judge runs
│   └── closure-records/          ← historical closure records
└── .claude/                      ← Claude Code configuration
    ├── settings.json             ← hook wiring
    ├── commands/
    │   ├── close-task.md         ← closure workflow
    │   ├── mc-status.md          ← show current state
    │   ├── mc-recovery.md        ← recover after context loss
    │   ├── run-judge.md          ← spawn judge subagent
    │   ├── session-start.md      ← initialize new session
    │   └── handoff.md            ← pass context to next agent
    ├── agents/
    │   ├── judge.md              ← judge subagent definition
    │   └── worker.md             ← worker subagent definition
    ├── skills/
    │   └── system.md             ← system skill (hard gate)
    └── hooks/
        ├── stop-if-not-done.sh   ← blocks premature exit
        ├── block-dangerous.sh    ← blocks destructive commands
        ├── protect-control-files.sh     ← blocks editing control files
        ├── worker-boundary-guard.sh     ← blocks off-route invocations
        ├── session-start-reminder.sh    ← re-injects rules
        ├── post-edit-reminder.sh        ← reminds to validate
        ├── post-tool-validate.sh        ← validates tool output
        ├── post-compact-audit.sh        ← audits after compaction
        └── task-sync-guard.sh           ← blocks out-of-order claims
```

## What you will learn

- The exact tree layout for each tier (Minimal, Standard, Strict)
- Which files Claude can edit in each tier
- How to nest `AGENTS.md` and `CLAUDE.md` in subdirectories
- The path contracts that prevent tampering and scope violations

## The core invariant

```text
Control files are in .mission-control/ and .claude/.
Project files are in src/, tests/, docs/.
Intent files (AGENTS.md, CLAUDE.md) are in the root.
```

## The path hierarchy

```text
project/
├── src/, tests/, docs/       ← canonical content (always editable)
├── AGENTS.md               ← project map (always editable)
├── CLAUDE.md               ← behavioral contract (always editable)
├── .mission-control/       ← intent, validation, state, history
│   ├── PLAN.md
│   ├── CLOSED_TASKS.md
│   ├── validation-manifest.json
│   ├── done-check.sh
│   ├── validate-*.sh
│   ├── close-task-check.sh
│   ├── run-agent.sh
│   ├── state.json
│   ├── judge-principles.md
│   ├── judge-verdicts/
│   └── closure-records/
└── .claude/                ← Claude Code configuration
    ├── settings.json
    ├── commands/
    ├── agents/
    ├── skills/
    └── hooks/
```

## When to read this

Read this section during Phase 1 (Discover) after picking your tier. It tells you exactly what files to create and where to put them.

## Next

Read `tier-layouts.md` to pick the exact tree for your tier.
