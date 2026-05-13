# Mission Control Setup — Autonomous Loop

Guided setup for **autonomous loop** projects: Claude runs continuously, scripts decide when it's done, a Stop hook blocks premature exit.

Use `AskUserQuestion` for every question. Do not batch questions — ask one at a time.

## Standing rules

- **Always local.** Every file goes in the project's `.claude/` directory. Never write to `~/.claude/`.
- **Subagents as files.** Every subagent is a `.md` file in `.claude/agents/` with YAML frontmatter. Never embed prompts in shell scripts.
- **CLAUDE.md via skill.** Always invoke `writing-claude-md` to produce CLAUDE.md. Never write it directly.
- **System skill required.** Always invoke `write-a-skill` (Phase 6b). This is what makes the system usable in a fresh session. It has a hard checklist — do not skip it.

---

## Phase 0 — Orient the user

Print this before asking anything:

```
Mission Control (Autonomous Loop) sets up a system where Claude runs continuously
until scripts confirm the work is done.

The key idea: Claude implements, scripts decide when it's done.

Without this: Claude stops after subtasks, asks "should I continue?", or claims
completion while validation fails. With it, a Stop hook blocks premature stopping,
done-check.sh is the only completion authority, and run-agent.sh restarts Claude
if it crashes or sleeps.

Setup takes about 5 minutes.
```

Ask: "Does that sound right, or would you like me to explain more before we start?"

---

## Phase 1 — Project diagnosis

**Q1: Objective**
"What is the objective? One sentence — what needs to be built or fixed?"

Save as `OBJECTIVE`.

**Q2: Stack**
"What language and test framework does this project use? (e.g. TypeScript/Jest, Python/pytest, Go, Ruby/RSpec, shell scripts)"

Look at `package.json`, `Makefile`, `pyproject.toml`, `go.mod`, `Gemfile` to infer if unsure. Confirm with the user.

Save as `STACK` and `TEST_CMD`.

**Q3: Duration estimate**
"Roughly how long do you expect this to take if Claude runs without stopping — 15 minutes, an hour, several hours, or a full day?"

Save as `DURATION`.

**Q4: Risk level**
"Does this task touch production data, external APIs, deployments, billing, credentials, or anything that can't be easily undone?"

Save as `RISK` (`low` or `high`).

**Q5: Test suite confidence**
"How much do you trust the existing test suite? (a) good coverage, I trust it; (b) partial coverage, I'm not sure; (c) weak/no tests, Claude will be writing them from scratch."

Save as `TEST_CONFIDENCE`.

---

## Phase 2 — Recommend a tier

**Tier recommendation logic:**

```
If DURATION < 30 min AND RISK = low:
  Recommend Tier 1

If DURATION 30 min–2 hrs OR TEST_CONFIDENCE = partial:
  Recommend Tier 2

If DURATION > 2 hrs OR RISK = high OR TEST_CONFIDENCE = weak:
  Recommend Tier 3
```

Present the recommendation and show the tier table:

| Tier | Duration fit | What you get |
|------|-------------|--------------|
| **1 — Minimal** | < 30 min, low risk | PLAN.md + done-check.sh + Stop hook + run-agent.sh |
| **2 — Standard** | 30 min – 2 hrs | Tier 1 + regression tracking + tamper detection + anti-gaming hooks |
| **3 — Strict** | 2+ hrs, high risk | Tier 2 + judge layer + control files isolated outside repo |

Ask: "Does Tier [X] sound right, or do you want to choose a different one?"

Save as `TIER`.

**If Tier 2 or 3**, ask about layout:
"Do you want the control scripts inside the project or in a separate `agent-control/` directory next to it?"

Show the folder tree from `references/folder-structure.md` for both options.

Save as `LAYOUT` (`inline` or `external`).

---

## Phase 3 — Validation design

Read `references/validation-design.md` before proceeding.

Show the validation stack concept:

```
done-check.sh (top-level authority)
  └── validate-no-blockers.sh   — no BLOCKED_AGENT markers, no open tasks
  └── validate-global.sh        — typecheck + lint + test suite passes
  └── validate-closed-tasks.sh  — (Tier 2+) closed task regression tests still pass
  └── validate-no-tampering.sh  — (Tier 2+) no test weakening or config changes
```

Ask (multi-select): "Besides running your tests, what else should count as 'done'?"

Options:
- Typecheck must pass (`tsc --noEmit`, `mypy`, etc.)
- Lint must pass (`eslint`, `ruff`, `golint`, etc.)
- All open tasks in PLAN.md must be closed
- No TODO_AGENT / BLOCKED_AGENT markers in source
- Specific files must exist (they provide the command)
- Custom command must pass (they provide the command)

Save as `DONE_CRITERIA`.

Ask: "Should `done-check.sh` require ALL tasks in PLAN.md to be closed before passing?"

Save as `REQUIRE_ALL_TASKS_CLOSED`.

For Tier 2+, ask: "Do you want regression checks — re-running closed-task tests before a new task can close? Adds safety, requires registering each closed task's tests in `validation-manifest.json`."

Save as `USE_REGRESSION_CHECK`.

---

## Phase 4 — Hook selection

Explain:

```
Hooks run inside Claude Code and can block or allow actions.
The Stop hook connects them: when Claude tries to stop, it runs done-check.sh.
If done-check fails, Claude is blocked and receives the failure as its next input.
```

Present the three levels:

**Low** — Stop hook only. Good for short tasks.

**Medium** — Stop hook + dangerous command blocker + session-start reminder. Good for most tasks over 30 min.

**High** — All medium + control file protector + post-edit reminder. Good for Tier 2/3, multi-hour runs, tasks where Claude writes tests.

**Context warning (always recommend)** — Non-blocking Stop hook that fires once when transcript reaches ~60% context. Shows `/compact`, `/handoff`, `/clear` options. See `references/hooks.md` for template.

Ask: "Which level — Low, Medium, or High? And add context-warning hook? (Recommended: yes)"

Save as `HOOKS`.

---

## Phase 5 — Write files

Show summary before writing:

```
Files to create:
  PLAN.md                              task map (tasks populated in Phase 8)
  CLOSED_TASKS.md                      closed-task registry
  validation-manifest.json             closed-task test registry
  CLAUDE.md                            project-specific operating rules
  done-check.sh                        completion authority
  [validate-*.sh if Tier 2+]           sub-validators
  run-agent.sh                         wrapper loop
  .claude/commands/session-start.md    /session-start slash command
  .claude/commands/close-task.md       /close-task slash command
  .claude/commands/mc-status.md        /mc-status slash command
  .claude/commands/mc-recovery.md      /mc-recovery slash command
  .claude/commands/handoff.md          /handoff slash command
  [.claude/commands/run-judge.md]      /run-judge (if judge enabled)
  .claude/hooks/[selected].sh          hooks
  .claude/settings.json                hook wiring
  .mission-control/state.json          initial execution state
  [agent-control/ scripts]             (external layout only)
```

Ask: "Ready to write? I'll create these files in [current directory]."

### 5a. PLAN.md
Write from `templates/PLAN.md`. Fill in `OBJECTIVE`. Leave task list as placeholder — tasks are populated in Phase 8. Include phase headers with `> Skills:` callouts if domain skills are known.

### 5b. CLOSED_TASKS.md + validation-manifest.json
Write from `templates/CLOSED_TASKS.md` and `templates/validation-manifest.json`.

### 5c. CLAUDE.md
Always invoke `writing-claude-md`. Pass: `OBJECTIVE`, `STACK`, `TEST_CMD`, `TIER`, local commands list, subagent names, system skill name, real blockers, reference to `.mission-control/` state files, `## Project-local skills` section.

If CLAUDE.md already exists: read it, merge Mission Control block in. Preserve all existing content.

### 5d. .mission-control/ — initialize state
Create directory and write `state.json`:
```json
{
  "objective": "[OBJECTIVE]",
  "project_type": "autonomous",
  "scope_locked": true,
  "scope_file": null,
  "current_phase": null,
  "current_task": "T001",
  "last_completed_task": null,
  "last_verification": null,
  "last_verification_result": null,
  "session_name": "[slugified-OBJECTIVE]",
  "judge_required": false,
  "judge_trigger": null,
  "judge_confidence_threshold": 0.70,
  "last_judge_task": null,
  "last_judge_verdict": null,
  "blockers": []
}
```

Create: `.mission-control/judge-verdicts/` and `.mission-control/closure-records/`.
Add `.gitignore` entries for judge-verdicts and session-log.md.

### 5e. done-check.sh
Write from `templates/done-check.sh`. Fill in `TEST_CMD`, `DONE_CRITERIA`, `REQUIRE_ALL_TASKS_CLOSED`. For Tier 2+: add calls to `validate-closed-tasks.sh` and `validate-no-tampering.sh`. Add judge verdict check block (leave `JUDGE_REQUIRED=false` for now).

Make executable: `chmod +x done-check.sh`

### 5f. Sub-validators (Tier 2+)
Write from templates/: `validate-global.sh`, `validate-closed-tasks.sh`, `validate-no-tampering.sh`, `validate-no-blockers.sh`, `close-task-check.sh`. Make all executable.

### 5g. Local slash commands
See `references/local-skills.md` for full templates:
- `.claude/commands/session-start.md` — checks for handoff file first
- `.claude/commands/close-task.md` — fill in `TEST_CMD`, `JUDGE_REQUIRED`
- `.claude/commands/mc-status.md`
- `.claude/commands/mc-recovery.md`
- `.claude/commands/handoff.md`
- `.claude/commands/run-judge.md` (if judge enabled)

### 5h. Hooks
Write selected hooks to `.claude/hooks/`. For `stop-if-not-done.sh`: fill in correct path to `done-check.sh` (inline: `./done-check.sh`, external: `../agent-control/done-check.sh "$PWD"`).

### 5i. Wire hooks into settings.json
Read `.claude/settings.json` (create if needed). Merge selected hooks. Do not overwrite existing hooks without confirmation.

### 5j. run-agent.sh
Write from `templates/run-agent.sh`. Fill in session name. Make executable.

---

## Phase 6 — Judge layer (Tier 3, or opt-in for Tier 2)

Read `references/judge.md` before proceeding.

Ask: "Do you want a judge layer? Useful when test quality is uncertain or correctness of intent matters."

If yes (or `TIER == 3`), ask: judge types, trigger strategy, confidence threshold (default 0.70).

Write `.claude/agents/judge.md` as a subagent file (never a shell script calling `claude -p`). Write `.mission-control/judge-rubric-private.md`. Wire judge into `done-check.sh`. Update `run-agent.sh` to handle exit code 2.

Tell the user: "Complete the rubric in `judge-rubric-private.md`, then copy it into the judge subagent body."

---

## Phase 6b — System skill (REQUIRED — hard gate)

**Cannot be skipped.** Without this, a fresh agent in the next session has no operating context.

Invoke `write-a-skill` now. Do not write inline.

The skill must cover: project type + what it means for the agent, phase structure with skill callouts, task lifecycle (open → in-progress → acceptance criteria check → closure contract verification → closed), all slash commands (user-facing), done-check.sh criteria, user corrections protocol, real blockers, common mistakes.

**Checklist — do not proceed to Phase 7 until all pass:**
- [ ] `write-a-skill` invoked
- [ ] `.claude/skills/[skill-name]/SKILL.md` exists
- [ ] Skill referenced in CLAUDE.md under `## Project-local skills`

---

## Phase 7 — Git branch

Ask: "Create a git branch? Recommended."

If yes: `git checkout -b agent/[slugified-OBJECTIVE]`

---

## Phase 8 — Planning pass

**This step happens AFTER setup but BEFORE execution.**

Explain:

```
The control system is set up. PLAN.md only has placeholder tasks.

The planning pass produces the real task list. Claude reads the codebase,
understands the objective, and writes tasks with acceptance criteria and
closure contracts into PLAN.md. You review and approve — then execution starts.

Plan first, execute second. Do not mix them.
```

Print this planning prompt for the user:

```
Create the task list in PLAN.md for this objective: [OBJECTIVE]

For each task:
- Write a clear one-line name
- List acceptance criteria (verifiable, machine-checkable — commands, file existence, test results)
- Write a closure contract: what evidence proves this task is done?
  Evidence must be: test files added/updated, commands that pass, files that exist
- Estimate risk: which tasks might break existing behavior?

Do not implement anything yet. Produce the task map only.
Review the codebase first to understand current state.

Use the PLAN.md format already in place. See references/task-design.md
(Autonomous loop section) for acceptance criteria and closure contract patterns.
```

Tell the user: "Run that prompt in a Claude session in this project. Review PLAN.md and adjust task scope. Then run `./run-agent.sh`."

---

## Phase 9 — Orientation summary

```
Mission Control is set up (Autonomous Loop).

Tier [X] — [tier name]
Layout: [inline / external]
Hooks: [list]

Control files:
  PLAN.md                  task map — needs tasks before you run (see planning prompt above)
  CLOSED_TASKS.md          closed-task registry
  validation-manifest.json closed-task test registry
  done-check.sh            completion authority

Start (after populating PLAN.md):
  ./run-agent.sh

Resume after any interruption:
  ./run-agent.sh

What Claude can and cannot do:
  Can: edit product code, add tests, run validation, update PLAN.md
  Cannot: stop until done-check.sh passes (or real blocker)
  [If High aggressiveness]: Cannot edit hooks, validators, CLOSED_TASKS.md, validation-manifest.json

Real blockers (human required): production deploy, destructive deletion, credentials, ambiguous product decisions
```
