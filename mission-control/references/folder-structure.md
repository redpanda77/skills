# Folder Structure

## Tier 1 — Minimal (inline)

```
project/
├── PLAN.md                          task map
├── CLOSED_TASKS.md                  closed-task registry (human-readable)
├── validation-manifest.json         closed-task test registry (machine-readable)
├── done-check.sh                    completion authority
├── run-agent.sh                     wrapper loop
│
├── .mission-control/                runtime state (gitignore or commit — your choice)
│   ├── state.json                   current task, last verification, session info
│   └── session-log.md               running event log (optional)
│
├── .claude/
│   ├── settings.json                hook wiring
│   ├── commands/                    local slash commands
│   │   ├── close-task.md            /close-task — full closure workflow
│   │   ├── mc-status.md             /mc-status — show current state
│   │   └── mc-recovery.md           /mc-recovery — recovery after context loss
│   └── hooks/
│       ├── stop-if-not-done.sh      blocks premature stopping
│       └── block-dangerous.sh       blocks destructive commands
│
├── CLAUDE.md                        project-specific operating rules
├── src/
└── tests/
```

---

## Tier 2 — Standard (inline)

Adds sub-validators, anti-gaming hooks, and regression tracking.

```
project/
├── PLAN.md
├── CLOSED_TASKS.md
├── validation-manifest.json
│
├── done-check.sh                    calls sub-validators
├── validate-global.sh               typecheck + lint + tests
├── validate-closed-tasks.sh         regression tests for closed tasks
├── validate-no-tampering.sh         detects test weakening or config changes
├── validate-no-blockers.sh          detects open tasks and blocker markers
├── close-task-check.sh              verifies a single task can be promoted
├── run-agent.sh
│
├── .mission-control/
│   ├── state.json
│   ├── judge-rubric.md              (if judge enabled)
│   ├── judge-verdicts/
│   │   ├── T001.json
│   │   └── latest.json
│   ├── closure-records/
│   │   └── T001-closure.json
│   └── session-log.md
│
├── .claude/
│   ├── settings.json
│   ├── commands/
│   │   ├── close-task.md
│   │   ├── mc-status.md
│   │   ├── mc-recovery.md
│   │   └── run-judge.md             (if judge enabled)
│   └── hooks/
│       ├── stop-if-not-done.sh
│       ├── block-dangerous.sh
│       ├── session-start-reminder.sh
│       └── protect-control-files.sh  blocks Claude from editing validators/hooks
│
├── CLAUDE.md
├── src/
└── tests/
```

`protect-control-files.sh` blocks Claude from editing `*.sh` scripts, `.claude/hooks/`, `.claude/settings.json`, `CLOSED_TASKS.md`, and `validation-manifest.json`. Claude can still read `.mission-control/` and update it (since closure records and judge verdicts must be writable by the worker).

---

## Tier 2 — Standard (external agent-control)

Control scripts live outside the repo. Physical isolation — no hook needed to protect them.

```
parent-directory/
│
├── project/                          Claude's workspace
│   ├── PLAN.md
│   ├── CLOSED_TASKS.md
│   ├── validation-manifest.json
│   ├── CLAUDE.md
│   │
│   ├── .mission-control/
│   │   ├── state.json
│   │   ├── judge-rubric.md           (if judge enabled — stays inside project)
│   │   ├── judge-verdicts/
│   │   └── closure-records/
│   │
│   ├── .claude/
│   │   ├── settings.json             hook commands point to ../agent-control/hooks/
│   │   └── commands/
│   │       ├── close-task.md
│   │       ├── mc-status.md
│   │       ├── mc-recovery.md
│   │       └── run-judge.md
│   │
│   ├── src/
│   └── tests/
│
└── agent-control/                    outside Claude's workspace
    ├── done-check.sh                 accepts repo path: ./done-check.sh ../project
    ├── validate-global.sh
    ├── validate-closed-tasks.sh
    ├── validate-no-tampering.sh
    ├── validate-no-blockers.sh
    ├── close-task-check.sh
    ├── run-agent.sh
    └── hooks/
        ├── stop-if-not-done.sh
        ├── block-dangerous.sh
        ├── session-start-reminder.sh
        └── protect-control-files.sh
```

**Hook path wiring** in `.claude/settings.json`:
```json
{
  "hooks": {
    "Stop": [{ "hooks": [{ "type": "command", "command": "../agent-control/hooks/stop-if-not-done.sh" }] }],
    "PreToolUse": [
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": "../agent-control/hooks/block-dangerous.sh" }] },
      { "matcher": "Write|Edit|MultiEdit", "hooks": [{ "type": "command", "command": "../agent-control/hooks/protect-control-files.sh" }] }
    ]
  }
}
```

`stop-if-not-done.sh` must call done-check with the repo path:
```bash
if ../agent-control/done-check.sh "$PWD" >/dev/null 2>&1; then exit 0; fi
```

---

## Tier 3 — Strict (external + judge + private rubric)

Judge rubric moves outside the project. Worker cannot read criteria.

```
parent-directory/
│
├── project/                          Claude's workspace (same as Tier 2 external)
│   ├── ...
│   ├── .mission-control/
│   │   ├── state.json
│   │   ├── judge-verdicts/           verdicts written here by worker after subagent returns
│   │   └── closure-records/
│   └── .claude/commands/
│       └── run-judge.md              spawns judge subagent; reads rubric from ../agent-control/
│
└── agent-control/
    ├── done-check.sh
    ├── validate-*.sh
    ├── close-task-check.sh
    ├── run-agent.sh
    │
    ├── judge-rubric-private.md       worker CANNOT read this — only passed to judge subagent
    ├── hidden-tests/                 additional tests Claude cannot modify
    │   └── [test files]
    │
    └── hooks/
        └── ...
```

In Tier 3, the `run-judge.md` slash command reads the rubric from `../agent-control/judge-rubric-private.md`. The worker passes it to the judge subagent but does not process or summarize it — it passes the raw file content.

---

## What Claude can and cannot edit — by configuration

| Location | T1 | T2 inline | T2 external | T3 |
|----------|----|-----------|-------------|----|
| `src/`, `tests/` | ✓ | ✓ | ✓ | ✓ |
| `PLAN.md` | ✓ | ✓ | ✓ | ✓ |
| `.mission-control/state.json` | ✓ | ✓ | ✓ | ✓ |
| `.mission-control/judge-verdicts/` | ✓ | ✓ | ✓ | ✓ |
| `.mission-control/closure-records/` | ✓ | ✓ | ✓ | ✓ |
| `.mission-control/judge-rubric.md` | ✓ | ✓ | ✓ (inline) | ✗ (in agent-control) |
| `CLOSED_TASKS.md` | ✓ | ✗ (hook) | ✓ (inside project) | ✗ |
| `validation-manifest.json` | ✓ | ✗ (hook) | ✓ (inside project) | ✗ |
| `done-check.sh`, `validate-*.sh` | ✓ | ✗ (hook) | ✗ (outside) | ✗ (outside) |
| `.claude/hooks/` | ✓ | ✗ (hook) | ✗ (outside) | ✗ (outside) |
| `.claude/settings.json` | ✓ | ✗ (hook) | ✓ | ✓ |
| `.claude/commands/` | ✓ | ✓ | ✓ | ✓ |
| `agent-control/` | n/a | n/a | ✗ (unreachable) | ✗ (unreachable) |

**Note:** `.claude/commands/` (local skills) are intentionally writable. The worker may need to update its own slash commands during long tasks. If you want to lock them, add them to the `protect-control-files.sh` pattern list.

**Note on CLOSED_TASKS.md and validation-manifest.json at Tier 2 inline:** These are blocked by `protect-control-files.sh`. The closure workflow (`/close-task`) must either: (a) be run while the hook is temporarily disabled, or (b) write through a dedicated script that is itself not protected. The simplest solution: add a `close-task.sh` script that updates both files, and list it as the permitted update path. Claude invokes the script; the hook only blocks direct file edits.

---

## .gitignore recommendations

```gitignore
# Mission Control runtime state — exclude verdicts and session logs
.mission-control/judge-verdicts/
.mission-control/session-log.md

# Keep in version control:
# .mission-control/state.json       (track current task across machines)
# .mission-control/closure-records/ (durable evidence)
# .mission-control/judge-rubric.md  (unless using Tier 3 private rubric)
```
