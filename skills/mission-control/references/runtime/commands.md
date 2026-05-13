# Local Skills and Slash Commands

Setup writes local slash commands into `.claude/commands/` that the worker Claude can invoke by name during execution. These are project-specific — they live in the project, not in `~/.claude/skills/`.

A local skill is a `.md` file in `.claude/commands/`. Claude Code makes it available as a slash command automatically.

---

## Which commands to write

Templates are in `references/templates/commands/`. Copy the relevant template into `.claude/commands/` and fill in project-specific values.

### All project types

| Command | Template | Purpose |
|---------|----------|---------|
| `/session-start` | `templates/commands/session-start.md` | Orient at session start; check handoff, state, scope lock |
| `/mc-status` | `templates/commands/mc-status.md` | Current state, last verification, judge verdict |
| `/mc-recovery` | `templates/commands/mc-recovery.md` | Recovery after context loss or crash |
| `/log-decision` | `templates/commands/log-decision.md` | Append to session log before any deviation or change |
| `/handoff` | `templates/commands/handoff.md` | Compact context to handoffs/<slug>.md for clean new session |

### Autonomous loop only

| Command | Template | Purpose |
|---------|----------|---------|
| `/close-task` | `templates/commands/close-task.md` | Full closure: verify acceptance criteria, run done-check.sh, update CLOSED_TASKS.md + validation-manifest.json, commit |
| `/run-judge` | `templates/commands/run-judge.md` | Spawn judge subagent (if judge enabled) |

### Human-in-the-loop / evaluation only

| Command | Template | Purpose |
|---------|----------|---------|
| `/close-task` | `templates/commands/close-task-human.md` | Verify outputs + notes, update state.json + PLAN.md, write closure record — human runs after reviewing output |

---

## /session-start

See canonical template: `references/templates/commands/session-start.md`

Key behaviors: checks `handoffs/` first (most recent file wins), checks `scope_locked` for analytical projects, prints phase/task/progress summary, suggests next action without starting work.

---

## /handoff

See canonical template: `references/templates/commands/handoff.md`

Exact copy of the global `~/.claude/skills/handoff/` skill — same logic, same document structure, same rules. Writes to `handoffs/<branch>.md`. Includes Resume Prompt.

Proactively suggest running `/handoff` after 3+ heavy sessions, when the context-warning hook fires, or when the user says "I'll continue later."

---

## /close-task

The closure workflow. Worker invokes this when it believes a task is complete.

```markdown
---
description: Run the full closure workflow for a task. Verifies acceptance criteria, runs validation, optionally runs judge, updates CLOSED_TASKS.md and validation-manifest.json, commits.
---

Close task $ARGUMENTS (or current task from .mission-control/state.json if not specified).

## Closure steps

1. Identify task ID. Read from $ARGUMENTS or .mission-control/state.json current_task.

2. Read task section from PLAN.md. Extract:
   - Acceptance criteria checklist
   - Closure contract requirements

3. Verify each acceptance criterion manually:
   - For each "- [ ]" item: determine whether it is satisfied
   - Run any commands the criterion implies (e.g. `npm test`, `[ -f src/auth/token.ts ]`)
   - If any criterion is not met: stop, do not close the task, continue fixing

4. Run validation:
   - Run done-check.sh (minus the judge check) to confirm validation passes
   - If validation fails: stop, fix, retry

5. Run judge (if judge_required=true in .mission-control/state.json):
   - Run /run-judge [TASK_ID]
   - If verdict is fail: stop, address must_fix items, retry closure
   - If verdict is blocked: stop, report to user

6. Update PLAN.md:
   - Change task Status from "open" to "closed"
   - Fill in "Closed at:" with current timestamp and next commit hash (TBD)
   - Mark all acceptance criteria checkboxes as checked

7. Update CLOSED_TASKS.md:
   - Add entry for this task using the format from the CLOSED_TASKS.md template
   - Include: accepted behaviors, test files that protect them, invariants, reopen policy

8. Update validation-manifest.json:
   - Add entry for this task: id, name, status=closed, tests[], invariants[], protected_files[]

9. Update .mission-control/state.json:
   - Set last_completed_task to this task ID
   - Set current_task to next open task in PLAN.md

10. Write closure record to .mission-control/closure-records/[TASK_ID]-closure.json

11. Git commit:
    - `git add -A`
    - `git commit -m "Close [TASK_ID]: [task name]"`
    - Update PLAN.md "Closed at:" with the actual commit hash

12. Confirm: print "Task [TASK_ID] closed. Moving to next task: [NEXT_TASK_ID]"

13. Immediately start work on the next open task in PLAN.md. Do not stop.
```

---

## /run-judge

See full template in `references/judge.md` — The /run-judge local skill section. The complete `.claude/commands/run-judge.md` is there.

Setup copies it and fills in:
- `[TEST_CMD]` with the actual test command from Phase 1
- `[TASK_ID]` placeholder — replaced at runtime with $ARGUMENTS

---

## /mc-status

Quick read of current state. Useful for orientation at session start or after resuming.

```markdown
---
description: Show Mission Control status — current task, last verification, judge verdict, any blockers
---

Read and display current mission control state.

1. Read .mission-control/state.json
2. Read PLAN.md — count open/closed tasks
3. Read .mission-control/judge-verdicts/latest.json if it exists

Print:

---
Mission Control Status
---
Objective: [objective]
Current task: [current_task] — [task name from PLAN.md]
Last completed: [last_completed_task]
Last verification: [last_verification] ([last_verification_result])
Tasks: [N closed] / [total] complete

Judge: [enabled/disabled]
  Last verdict: [verdict] (confidence: [confidence]) for [last_judge_task]

Blockers: [none / list]

Next action: [first open task in PLAN.md]
---
```

---

## /mc-recovery

Guides Claude through recovery after context loss, crash, or session resume.

```markdown
---
description: Recovery mode — read current state, identify where to resume, continue execution from the right place
---

Recovery mode. Do not ask whether to continue.

1. Run /mc-status to get current state

2. Read git log: `git log --oneline -10`

3. Read PLAN.md in full — identify:
   - First task with Status: open
   - Last task with Status: closed (and at which commit)
   - Any BLOCKED_AGENT markers

4. Check validation: run done-check.sh, capture output (don't stop if it fails)

5. Report findings:
   - Current task
   - Last verified state
   - Whether done-check passes now
   - Any blockers found

6. Resume from the first open task. Do not re-do closed tasks.
   - If done-check already passes: nothing to do — report complete
   - If done-check fails: continue working from first open task
   - If there are BLOCKED_AGENT markers: report them before continuing

Do not rely on conversation history. Everything you need is in PLAN.md, CLOSED_TASKS.md, and .mission-control/.
```

---

## CLAUDE.md — write it for this project

During setup Phase 5, write a project-specific `CLAUDE.md` — not just a generic block appended to an existing file. If writing-claude-md skill is available (`~/.claude/skills/writing-claude-md/`), invoke it. Otherwise write manually using this structure.

A good CLAUDE.md for a mission-control project covers:

**1. Project context** (what it is, what it does, tech stack)

**2. Mission Control operating rules** — this block should be personalized, not generic:
```markdown
## Mission Control

This task is running under Mission Control. Completion is determined by done-check.sh.

Current objective: [OBJECTIVE]
Test command: [TEST_CMD]
Tier: [TIER]

Rules:
- Use PLAN.md as the task map
- Use CLOSED_TASKS.md and validation-manifest.json as the closed-work baseline
- Start each session by running /mc-status
- Close tasks using /close-task — do not mark tasks closed manually
- Run /run-judge before closing any task (if judge is enabled)
- Stop only when done-check.sh passes or a real blocker exists
- Update .mission-control/state.json at key points
```

**3. Slash commands — for the USER to run**

Recommend these; do not invoke them autonomously:

```markdown
## Slash commands — for the USER to run

| Command | When to suggest |
|---------|----------------|
| `/session-start` | Always — start of every session |
| `/mc-status` | User wants a progress check mid-session |
| `/close-task TXXX` | A task's closure contract is met |
| `/log-decision "text"` | Any deviation from design docs or calibration call |
| `/handoff` | Context is large, session is ending, or after 3+ long runs |

After 3 or more heavy working runs, proactively suggest: "Consider running `/handoff` to compact context and start fresh."
```

**4. Project-local skills (if applicable)**

If the project has specialized domain skills (e.g. query writer, persona analysis), list them in a skills table so a fresh agent knows what to load:

```markdown
## Project-local skills

| Skill | Load when |
|-------|----------|
| `[skill-name]` | [trigger condition] |
```

**5. Real blockers** (customize for this project's risk areas):
```markdown
## Blockers (require human input)
- [project-specific blocker 1]
- [project-specific blocker 2]
- General: production deploy, credential handling, destructive deletion, ambiguous product decisions
```

**5. State files:**
```markdown
## Key files
- PLAN.md — task map
- .mission-control/state.json — current execution state
- .mission-control/judge-rubric.md — judge criteria (if enabled)
- done-check.sh — completion authority
```

**6. File discipline (for analytical/data projects)**

Add this block if the project produces phase outputs or has a defined output folder convention:

```markdown
## File discipline

- All outputs go to `phases/phase_N__name/output/` — never the project root, never `tmp/`
- `tmp/` is scratch only — never reference it from phase scripts
- No versioned filenames (`_v2`, `_final`, `_new`) — overwrite the canonical output in place
- A phase output folder contains exactly what the closure contract names — remove stale files
```

For code projects, adapt: build artifacts go to `dist/`, generated files to `generated/`, etc. The principle is the same: one canonical location, no version proliferation.

If the project has existing CLAUDE.md content (architecture notes, coding conventions, etc.), preserve it. The Mission Control block is an addition, not a replacement.

---

## Context files in .mission-control/

If the project benefits from domain context (like `grill-me-careem` would produce), write it to `.mission-control/context.md` during setup.

Ask in setup: "Is there domain vocabulary or architectural context Claude should know while working? If yes, describe it briefly and I'll write a context file."

If yes, write `.mission-control/context.md`. Reference it in CLAUDE.md:
```markdown
## Domain context
Read .mission-control/context.md at session start.
```

This is the same approach as grill-with-docs producing `.plan/CONTEXT.md` in the launchpad skill — domain context as a first-class persistent file, not buried in conversation history.
