# Local Skills and Slash Commands

Setup writes local slash commands into `.claude/commands/` that the worker Claude can invoke by name during execution. These are project-specific — they live in the project, not in `~/.claude/skills/`.

A local skill is a `.md` file in `.claude/commands/`. Claude Code makes it available as a slash command automatically.

---

## Which skills to write

Setup always writes these during Phase 5:

| Command | File | Purpose |
|---------|------|---------|
| `/close-task` | `.claude/commands/close-task.md` | Full closure workflow for a task |
| `/mc-status` | `.claude/commands/mc-status.md` | Show current state, last verification, judge verdict |
| `/mc-recovery` | `.claude/commands/mc-recovery.md` | Recovery mode after context loss or crash |

Setup writes this one only if judge is enabled:

| Command | File | Purpose |
|---------|------|---------|
| `/run-judge` | `.claude/commands/run-judge.md` | Spawn judge subagent for current task |

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

**3. Local commands available:**
```markdown
## Commands

- /close-task [TASK_ID] — full closure workflow
- /run-judge [TASK_ID] — spawn judge subagent (if judge enabled)
- /mc-status — show current state
- /mc-recovery — recovery after context loss
```

**4. Real blockers** (customize for this project's risk areas):
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
