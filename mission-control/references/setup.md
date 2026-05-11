# Mission Control Setup

Guided setup. Use `AskUserQuestion` for every question. Do not batch questions — ask one at a time and proceed based on the answer.

---

## Phase 0 — Orient the user

Before asking anything, print this brief explanation:

```
Mission Control sets up a controlled execution system for long-running Claude Code tasks.

The key idea: Claude implements, but scripts decide when it's done.

Without this system, Claude stops after subtasks, asks "should I continue?", or claims completion while validation fails. With it, a Stop hook blocks premature stopping, a done-check.sh script is the only completion authority, and a wrapper loop restarts Claude if it crashes or sleeps.

Setup takes about 5 minutes and creates files directly in your project.
```

Then ask: "Does that sound like what you need, or would you like me to explain more before we start?"

If they want more, read `references/hooks.md` and `references/validation-design.md` and summarize the relevant parts.

---

## Phase 1 — Project diagnosis

Ask each of these in order. Use the answers to recommend tier and validation design.

**Q1: Objective**
"What is the objective for this task? One sentence — what needs to be built or fixed?"

Save as `OBJECTIVE`.

**Q2: Stack**
"What language and test framework does this project use? (e.g. TypeScript/Jest, Python/pytest, Go, Ruby/RSpec, shell scripts)"

Look at `package.json`, `Makefile`, `pyproject.toml`, `go.mod`, `Gemfile` to infer if unsure. Confirm with the user.

Save as `STACK` and `TEST_CMD`.

**Q3: Duration estimate**
"Roughly how long do you expect this to take if Claude runs without stopping — 15 minutes, an hour, several hours, or a full day?"

Save as `DURATION`. This drives tier recommendation.

**Q4: Risk level**
"Does this task touch production data, external APIs, deployments, billing, credentials, or anything that can't be easily undone?"

Save as `RISK` (`low` or `high`).

**Q5: Test suite confidence**
"How much do you trust the existing test suite? Options: (a) good coverage, I trust it; (b) partial coverage, I'm not sure; (c) weak/no tests, Claude will be writing them from scratch."

Save as `TEST_CONFIDENCE`.

---

## Phase 2 — Recommend a tier

Based on the diagnosis answers, recommend a tier. Show the recommendation and the reasoning.

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

- **Inside project** (default): simpler, everything in one place. Claude can theoretically edit the scripts if hooks aren't installed yet.
- **Separate `agent-control/`**: stronger isolation. Validators and hooks live outside the worker's editable space. Preferred for Tier 3.

Show the folder tree from `references/folder-structure.md` for both options.

Save as `LAYOUT` (`inline` or `external`).

---

## Phase 3 — Validation design

This phase figures out what `done-check.sh` should actually check. Read `references/validation-design.md` before proceeding.

Show the user the validation stack concept:

```
done-check.sh (top-level authority)
  └── validate-no-blockers.sh   — no BLOCKED_AGENT markers, no open tasks
  └── validate-global.sh        — typecheck + lint + test suite passes
  └── validate-closed-tasks.sh  — (Tier 2+) closed task regression tests still pass
  └── validate-no-tampering.sh  — (Tier 2+) no test weakening or config changes
```

Ask: "Besides running your tests, what else should count as 'done'? Check all that apply:"

Options (use AskUserQuestion with multi-select style, or ask sequentially):
- Typecheck must pass (`tsc --noEmit`, `mypy`, etc.)
- Lint must pass (`eslint`, `ruff`, `golint`, etc.)
- All open tasks in PLAN.md must be closed
- No TODO_AGENT / BLOCKED_AGENT markers in source
- Specific files must exist (e.g. migration files, generated docs)
- Custom command must pass (they provide the command)

Save selected checks as `DONE_CRITERIA`.

For each selected criterion, note the command that verifies it. These go into `validate-global.sh`.

Ask: "Should `done-check.sh` require ALL tasks in PLAN.md to be closed before passing? Or should it pass as long as tests pass, regardless of task status?"

This matters: if yes, Claude cannot stop until every task in PLAN.md is marked closed and its closure contract is complete.

Save as `REQUIRE_ALL_TASKS_CLOSED`.

For Tier 2+, explain:
"Tier 2 also runs `validate-closed-tasks.sh` — this re-runs the regression tests for every previously closed task before allowing a new one to close. This catches regressions Claude might miss. It requires test files to be explicitly registered in `validation-manifest.json`."

Ask: "Do you want that regression check? It adds safety but requires Claude to register each closed task's tests explicitly."

Save as `USE_REGRESSION_CHECK`.

---

## Phase 4 — Hook selection

Explain the enforcement model first:

```
Hooks run inside Claude Code and can block or allow actions.
They are separate from validation scripts — hooks are local Claude Code behavior,
scripts decide whether the work is done.

The Stop hook is what connects them: when Claude tries to stop, the Stop hook
runs done-check.sh. If done-check fails, Claude is blocked from stopping and
receives the failure as its next input.
```

Present the three hook aggressiveness levels and ask which fits:

**Low (enforcement only)**
- Stop hook — blocks stopping until done-check passes
- No other hooks

Good for: short tasks, when you trust Claude's judgment on everything except stopping.

**Medium (enforcement + safety)**
- Stop hook
- Dangerous command blocker — blocks `rm -rf`, force push, publish, deploy
- Session start reminder — re-orients Claude after resume/compaction

Good for: most tasks over 30 minutes. Prevents the most common accidents without adding context noise.

**High (enforcement + safety + anti-gaming)**
- All medium hooks
- Control file protector — blocks Claude from editing hooks, validators, CLOSED_TASKS.md
- Post-edit reminder — reminds Claude to validate after every file edit

Good for: Tier 2/3 tasks, multi-hour runs, when the test suite is being written as part of the task (so Claude could theoretically weaken it).

**Note:** High aggressiveness means Claude cannot modify its own control files. If you need to update a hook, you'd do it from the terminal, not from within Claude Code.

Ask: "Which level — Low, Medium, or High? Or pick individual hooks?"

If they want individual selection, ask about each hook one at a time using the descriptions from `references/hooks.md`.

Save selected hooks as `HOOKS`.

---

## Phase 5 — Write files

Show a summary of everything that will be created before writing any files:

```
Files to create:
  PLAN.md                              task map (tasks populated after setup)
  CLOSED_TASKS.md                      closed-task registry
  validation-manifest.json             closed-task test registry
  CLAUDE.md                            project-specific operating rules
  done-check.sh                        completion authority
  [validate-*.sh if Tier 2+]           sub-validators
  run-agent.sh                         wrapper loop
  .claude/commands/close-task.md       /close-task slash command
  .claude/commands/mc-status.md        /mc-status slash command
  .claude/commands/mc-recovery.md      /mc-recovery slash command
  [.claude/commands/run-judge.md]      /run-judge slash command (if judge enabled)
  .claude/hooks/[selected].sh          hooks
  .claude/settings.json                hook wiring
  .mission-control/state.json          initial execution state
  [agent-control/ scripts]             (external layout only)
```

Ask: "Ready to write? I'll create these files in [current directory]."

Then proceed in order:

### 5a. PLAN.md
Write from `templates/PLAN.md`. Fill in `OBJECTIVE`. Leave task list as placeholder — tasks are populated in Phase 8.

### 5b. CLOSED_TASKS.md + validation-manifest.json
Write `CLOSED_TASKS.md` from `templates/CLOSED_TASKS.md`.
Write `validation-manifest.json` from `templates/validation-manifest.json`.

### 5c. CLAUDE.md
This is a project-specific file, not a generic append. Write it fully tailored to this project.

If `writing-claude-md` skill is available (`~/.claude/skills/writing-claude-md/`): invoke it. Pass the mission control block as required content.

Otherwise write directly using the structure from `references/local-skills.md` — CLAUDE.md section. Fill in:
- `OBJECTIVE` from Phase 1
- `STACK` and `TEST_CMD` from Phase 1
- `TIER` from Phase 2
- The local commands that will be available (from 5f below)
- Project-specific real blockers based on RISK from Phase 1
- Reference to `.mission-control/` state files

If CLAUDE.md already exists: read it, then merge the Mission Control block into it. Preserve all existing content. Only add, never replace.

### 5d. .mission-control/ — initialize state
Create `.mission-control/` directory.

Write `.mission-control/state.json`:
```json
{
  "objective": "[OBJECTIVE]",
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

Update `judge_required` and `judge_trigger` after Phase 6 if judge is enabled.

Create subdirectories: `.mission-control/judge-verdicts/` and `.mission-control/closure-records/`.

Write `.gitignore` entry for `.mission-control/judge-verdicts/` and `.mission-control/session-log.md`.

### 5e. done-check.sh
Write from `templates/done-check.sh`, customized for this project:
- Fill in `TEST_CMD`
- Add typecheck and lint commands based on `DONE_CRITERIA`
- Add `REQUIRE_ALL_TASKS_CLOSED` check if selected
- For Tier 2+: add calls to `validate-closed-tasks.sh` and `validate-no-tampering.sh`
- Add judge verdict check block from `references/judge.md` — Wiring section (if judge will be enabled in Phase 6 — leave it with `JUDGE_REQUIRED=false` for now, Phase 6 will update it)

Make executable: `chmod +x done-check.sh`

### 5f. Sub-validators (Tier 2+)
Write from templates/, fill in `TEST_CMD`:
- `validate-global.sh` — fill in all `DONE_CRITERIA` commands
- `validate-closed-tasks.sh` — fill in `TEST_CMD`
- `validate-no-tampering.sh`
- `validate-no-blockers.sh`
- `close-task-check.sh`

For `external` layout: place in `agent-control/` instead of project root.
Make all executable.

### 5g. Local slash commands
Create `.claude/commands/` if it doesn't exist.

Always write these three (see `references/local-skills.md` for full templates):
- `.claude/commands/close-task.md` — fill in `TEST_CMD`, `JUDGE_REQUIRED`
- `.claude/commands/mc-status.md`
- `.claude/commands/mc-recovery.md`

If judge is being configured (Phase 6), also write:
- `.claude/commands/run-judge.md` — fill in `TEST_CMD`; leave rubric path as `.mission-control/judge-rubric.md` (or `../agent-control/judge-rubric-private.md` for Tier 3 external)

### 5h. Hooks
Write only the hooks selected in Phase 4. Target `.claude/hooks/`.
For `external` layout: place in `agent-control/hooks/`.

For `stop-if-not-done.sh`: fill in the correct path to `done-check.sh` based on layout:
- Inline: `./done-check.sh`
- External: `../agent-control/done-check.sh "$PWD"`

### 5i. Wire hooks into settings.json
Read `.claude/settings.json` (create if needed). Merge selected hooks using `templates/settings-hooks.json` as schema. Use correct paths based on layout. Do not overwrite existing hooks without user confirmation.

### 5j. run-agent.sh
Write from `templates/run-agent.sh`. Fill in session name from slugified OBJECTIVE.
Make executable.

---

## Phase 6 — Judge layer (Tier 3, or opt-in for Tier 2)

Read `references/judge.md` before proceeding.

Ask: "Do you want a judge layer? It uses a separate Claude instance to evaluate whether the implementation satisfies the intent — not just whether tests pass. Useful when test quality is uncertain or when correctness of intent matters."

If yes (or if `TIER == 3`), ask in sequence:

**Q: Which judge types do you need?** (from judge.md — Judge types section)
- Correctness — does it satisfy the actual requirements?
- Test quality — are the tests meaningful?
- Regression guard — does the diff threaten closed-task invariants beyond what tests catch?
- Architecture — is the new code consistent with existing patterns?
- Security — are there exploitable patterns?

**Q: When should the judge run?** Present the trigger strategy table from judge.md. Make a recommendation based on `DURATION` and `TEST_CONFIDENCE` from Phase 1.

**Q: Confidence threshold?** (Default: 0.70) Explain: "Below this, a judge pass is treated as a fail — the judge is uncertain, which is a signal."

Then write:
1. `agent-control/judge-rubric-private.md` — use the rubric template from judge.md. Fill in objective and judge types. Leave specific criteria as labeled prompts for the user to fill in before running.
2. `agent-control/run-judge.sh` from the template in judge.md. Make executable.
3. Wire the judge into `done-check.sh` using the wiring snippet from judge.md, with the selected confidence threshold.
4. If per-task triggering selected: also add judge call to `close-task-check.sh`.
5. Update `run-agent.sh` to detect exit code 2 (blocked verdict) and stop rather than retry.

Tell the user: "Fill in specific, falsifiable criteria in `agent-control/judge-rubric-private.md` before running. The placeholders are prompts — vague criteria produce inconsistent verdicts. See the 'Writing a rubric' section in `references/judge.md` for examples."

---

## Phase 7 — Git branch

Ask: "Create a git branch for this task? Recommended — enables clean checkpoints and rollback."

If yes, run: `git checkout -b agent/[slugified-OBJECTIVE]`

---

## Phase 8 — Planning pass (critical)

This step happens AFTER setup but BEFORE execution. Explain:

```
The control system is set up, but PLAN.md only has placeholder tasks.

Before running Claude, you need a real task list. The planning pass produces it.
Claude reads the codebase, understands the objective, and writes the tasks —
with acceptance criteria and closure contracts — into PLAN.md.

You review and approve the plan. Only then does execution start.

This separation matters: plan first, then execute. Don't mix them.
```

Print the planning prompt for the user to use:

```
Create the task list in PLAN.md for this objective: [OBJECTIVE]

For each task:
- Write a clear one-line name
- List acceptance criteria (verifiable, not vague)
- Write a closure contract: what evidence proves this task is done?
  Evidence should be: test files added/updated, commands that pass, files that exist
- Estimate risk: which tasks might break existing behavior?

Do not implement anything yet. Produce the task map only.
Review the codebase first to understand current state.

Use the PLAN.md format already in place.
```

Tell the user: "Run that planning prompt in a Claude session in this project. Review the resulting PLAN.md and adjust task scope if needed. Then come back and run `./run-agent.sh`."

---

## Phase 9 — Orientation summary

Print the final summary:

```
Mission Control is set up.

Tier [X] — [tier name]
Layout: [inline / external]
Hooks: [list selected hooks]

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
