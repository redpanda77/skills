# Mission Control Setup — Human-in-the-Loop / Evaluation

Guided setup for **human-in-the-loop** and **evaluation/analysis** projects: work proceeds phase by phase with the human reviewing between phases. The agent recommends `/close-task`; the human decides when a task is done. No autonomous run loop.

Use `AskUserQuestion` for every question. Do not batch questions — ask one at a time.

## Standing rules

- **Always local.** Every file goes in the project's `.claude/` directory. Never write to `~/.claude/`.
- **CLAUDE.md via skill.** Always invoke `writing-claude-md` to produce CLAUDE.md. Never write it directly.
- **System skill required.** Always invoke `write-a-skill` (Phase 5b). Hard gate — do not proceed to Phase 6 until the checklist passes.
- **No run-agent.sh.** No blocking Stop hook. No done-check.sh. Completion is human-decided.
- **Scope before queries.** If this is an analytical/data project, T000 (foundations) must close before any phase work starts.

---

## Phase 0 — Orient the user

Print this before asking anything:

```
Mission Control (Human-in-the-Loop) sets up a phase-gate tracking system.

The key idea: you review and close tasks; the agent surfaces work and waits.

The agent produces outputs, verifies file existence and non-emptiness, fills in
Notes sections, and recommends /close-task — but never closes a task itself.
You review the output, decide it's good, and run /close-task to advance.

This is different from the autonomous loop mode: there is no done-check.sh
blocking Claude, no run-agent.sh wrapper. The agent works session by session
with you in the loop at every phase boundary.

Setup takes about 5 minutes.
```

Ask: "Does that sound right, or would you like me to explain more?"

---

## Phase 1 — Project diagnosis

**Q1: Objective**
"What is the objective? One sentence."

Save as `OBJECTIVE`.

**Q2: Project subtype**
"Is this closer to: (a) analytical / data pipeline — SQL, Python scripts, outputs are CSVs or JSON; (b) research / evaluation — document analysis, scoring, coverage targets; (c) mixed — some code, some human judgment?"

Save as `SUBTYPE`.

**Q3: Domain scope capture**
"Does this project have domain-specific parameters that need to be locked before work starts? (e.g. date ranges, cohort definitions, metric definitions, data sources, coverage targets)"

If yes: run scope interview now (use `grill-me` or `grill-with-docs` if available, or ask the parameters manually). Write results to:
- `shared/config/scope.md` — human-readable
- `shared/config/scope.json` — machine-readable

Add a T000 foundations task to PLAN.md. Its closure contract: scope.md and scope.json written, reviewed, and approved by the human. After T000 closes, scope is read-only — any changes require re-opening T000 and logging the decision.

Save `SCOPE_LOCKED` = `true` if scope was captured now, `false` if T000 will be first task.

**Q4: Phase structure**
"How many phases does this project have? What are they? Give me a rough list."

This becomes the phase header structure in PLAN.md. Phases group tasks — all tasks in Phase N must close before Phase N+1 starts.

Save as `PHASES` (list of phase names).

**Q5: Skills needed**
"Are there specialized domain skills the agent should load for each phase? (e.g. query-writer for SQL phases, persona-analysis for analysis phases)"

This becomes the `> Skills:` callout on each phase header in PLAN.md.

Save as `PHASE_SKILLS` (map of phase → skills list).

**Q6: Duration / sessions**
"Roughly how many working sessions will this take? One session, a few, or many over days/weeks?"

This drives whether the context-warning hook and /handoff are critical (they are for multi-session projects).

---

## Phase 2 — Validation approach

For human-in-the-loop projects, "done" is decided by the human, but the agent should verify what it can before recommending /close-task.

Ask: "For each task, what should the agent verify before recommending /close-task?"

Options (multi-select):
- Output files exist and are non-empty
- Row/record counts match expected ranges
- No NULLs in key ID fields
- Summary/notes written to PLAN.md task Notes section
- A specific data validation script passes (they provide it)
- Nothing automated — human judgment only

Save as `VERIFICATION_APPROACH`.

Ask: "Should all tasks in a phase be closed before the next phase starts? (Recommended: yes — phase gates prevent forward progress on incomplete foundations.)"

Save as `STRICT_PHASE_GATES`.

---

## Phase 3 — Milestone gates

Ask: "Are there planned human review points between phases — where you need to assess output quality before deciding whether to proceed, enrich, or change direction?"

Examples: cluster quality review after EDA before calibration; enrichment decision after item-level analysis; stakeholder sign-off before dashboard build.

For each milestone gate identified, add it as a `Type: milestone-gate` task at the phase boundary in PLAN.md. See `references/task-design.md` — Milestone gate tasks section for the format.

Save as `MILESTONE_GATES` (list of gate task descriptions and their positions).

---

## Phase 4 — Hooks

For human-in-the-loop projects, hooks are lighter — no blocking Stop hook needed.

**Always include:**
- `context-warning.sh` — fires once when transcript is ~60% full. Non-blocking. Essential for multi-session projects. See `references/hooks.md` for template.

**Optional:**
- `session-start-reminder.sh` — re-injects operating rules at session start / after compaction. Recommended for projects that run across many sessions.
- `block-dangerous.sh` — blocks `rm -rf`, force push, etc. Recommended if agent runs bash commands.

Ask: "Which optional hooks do you want?"

Save as `HOOKS`.

---

## Phase 5 — Write files

Show summary before writing:

```
Files to create:
  PLAN.md                              phase + task map (with milestone gates)
  CLAUDE.md                            project-specific operating rules
  shared/config/scope.md               scope definition (if captured)
  shared/config/scope.json             machine-readable scope
  .claude/commands/session-start.md    /session-start slash command
  .claude/commands/close-task.md       /close-task slash command
  .claude/commands/mc-status.md        /mc-status slash command
  .claude/commands/log-decision.md     /log-decision slash command
  .claude/commands/handoff.md          /handoff slash command
  .claude/hooks/context-warning.sh     context fill warning
  [.claude/hooks/session-start-reminder.sh]
  [.claude/hooks/block-dangerous.sh]
  .claude/settings.json                hook wiring
  .mission-control/state.json          initial state
  .mission-control/session-log/log.md  append-only decision log
```

Ask: "Ready to write?"

### 5a. PLAN.md
Write from `templates/PLAN.md`. Use phase header format:

```markdown
## Phase N — [Phase Name]

> Skills: [skill-name] · [skill-name]

### T00N: [Task name]

Status: open
Phase: phase_N__[name]

Outputs:
- [path/to/output.csv]

Acceptance Criteria:
- [ ] [output file exists and is non-empty]
- [ ] [specific verifiable condition — row count, column presence, etc.]
- [ ] Notes section filled in with observations

Closure Contract:
- Evidence required:
  - [output file] exists, non-empty, correct shape
  - Notes written to this task's Notes section
- Human closes with /close-task T00N after review

Notes:
```

Include T000 (foundations) if `SCOPE_LOCKED = false`. Include milestone gate tasks at phase boundaries. Add `> Skills:` callouts from `PHASE_SKILLS`.

### 5b. CLAUDE.md
Always invoke `writing-claude-md`. Pass: `OBJECTIVE`, `SUBTYPE`, `PHASES`, slash commands list, system skill name, scope file path, real blockers, `## Project-local skills` section.

Include in CLAUDE.md:
- Handoff check at session start: `ls handoffs/ 2>/dev/null`
- Slash commands framed as "for the USER to run"
- User corrections 5-step protocol
- File discipline rules (output locations, no versioned filenames, tmp/ is scratch only)
- Phase gate rule: all tasks in Phase N closed before Phase N+1

### 5c. state.json
```json
{
  "objective": "[OBJECTIVE]",
  "project_type": "human-in-the-loop",
  "scope_locked": [SCOPE_LOCKED],
  "scope_file": "shared/config/scope.md",
  "current_phase": "[first phase name or 'setup']",
  "current_task": "[T000 or T001]",
  "last_completed_task": null,
  "last_verification": null,
  "last_verification_result": null,
  "session_name": "[slugified-OBJECTIVE]",
  "judge_required": false,
  "judge_trigger": null,
  "judge_confidence_threshold": null,
  "last_judge_task": null,
  "last_judge_verdict": null,
  "blockers": []
}
```

Create: `.mission-control/closure-records/` and `.mission-control/session-log/`.
Write empty `.mission-control/session-log/log.md` with header.

### 5d. Local slash commands
See `references/local-skills.md` for full templates:
- `.claude/commands/session-start.md` — checks `handoffs/` first; checks `scope_locked`; reads state; prints orientation
- `.claude/commands/close-task.md` — verifies outputs exist, notes written; updates state.json; writes closure record; advances current_task
- `.claude/commands/mc-status.md`
- `.claude/commands/log-decision.md` — appends to `.mission-control/session-log/log.md`
- `.claude/commands/handoff.md`

### 5e. Hooks
Write selected hooks to `.claude/hooks/`. Wire into `.claude/settings.json`.

---

## Phase 5b — System skill (REQUIRED — hard gate)

**Cannot be skipped.** This is the operating manual a fresh agent loads at session start.

Invoke `write-a-skill` now. Do not write inline.

The skill must cover: project type + what it means for the agent, phase structure with skills callouts per phase, task lifecycle for human-in-the-loop (open → agent produces output → agent verifies → agent recommends /close-task → human reviews → /close-task), all slash commands (user-facing), user corrections 5-step protocol, scope lock meaning, milestone gate handling, file discipline rules, common mistakes.

**Checklist — do not proceed to Phase 6 until all pass:**
- [ ] `write-a-skill` invoked
- [ ] `.claude/skills/[skill-name]/SKILL.md` exists
- [ ] Skill referenced in CLAUDE.md under `## Project-local skills`

---

## Phase 6 — Git branch (optional)

Ask: "Create a git branch for this project?"

If yes: `git checkout -b project/[slugified-OBJECTIVE]`

---

## Phase 7 — Planning pass

**This step happens AFTER setup but BEFORE any phase work.**

Explain:

```
The system is set up. PLAN.md has a phase structure but placeholder tasks.

The planning pass produces the real task list. The agent reads existing
documentation and data sources, understands the objective, and writes tasks
with acceptance criteria and closure contracts into PLAN.md.

You review and approve — then Phase 0 / T000 starts.

Important for human-in-the-loop: acceptance criteria are file-based and
verifiable (outputs exist, non-empty, correct shape) not test-suite based.
Closure contracts end with "Human closes with /close-task after review."
```

Print this planning prompt for the user:

```
Create the task list in PLAN.md for this objective: [OBJECTIVE]

For each task, use the human-in-the-loop task format:
- Phase header with > Skills: callout
- Outputs: list of files the task produces
- Acceptance Criteria: file existence, non-empty, correct shape, notes filled in
  (No test commands — this is a human-reviewed project)
- Closure Contract: output files listed + "Human closes with /close-task TXXX after review"
- Notes section: empty, to be filled when closing

Include milestone gate tasks at phase boundaries where human review is needed.
For T000 (if scope not yet locked): closure contract is scope.md + scope.json written and reviewed.

Do not start any analysis yet. Produce the task map only.
Read any existing documentation, design docs, or data source info first.

See references/task-design.md (Human-in-the-loop section) for format examples.
```

Tell the user: "Review PLAN.md and adjust phase structure and task scope. T000 (scope lock) must close before any other task starts."

---

## Phase 8 — Orientation summary

```
Mission Control is set up (Human-in-the-Loop).

Project type: [SUBTYPE]
Scope locked: [yes / no — T000 must close first]
Phases: [list]
Hooks: [list]

Slash commands (USER runs these — agent recommends them):
  /session-start    — always first; checks for handoff file
  /close-task TXXX  — after reviewing a task's output
  /mc-status        — mid-session progress check
  /log-decision     — any deviation or calibration call
  /handoff          — when context is large or session is ending

Phase gate rule: all tasks in Phase N must be closed before Phase N+1 starts.

Start: run /session-start, then ask the agent to begin T000 (scope foundations).

Real blockers (require human input): scope changes, data source gaps,
methodology decisions, enrichment choices, persona redefinitions.
```
