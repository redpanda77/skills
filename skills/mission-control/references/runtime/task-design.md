# Task Design

Good tasks make the control system work. Bad tasks make it fight you.

**Two fundamentally different task models depending on project type:**

| | Autonomous loop | Human-in-the-loop / Evaluation |
|-|----------------|-------------------------------|
| Completion decided by | `done-check.sh` script | Human review + `/close-task` |
| Acceptance criteria | Machine-checkable commands | File existence + human sign-off |
| Closure contract | Evidence scripts can verify | Evidence agent can surface; human confirms |
| Milestone gates | Not applicable | Explicit planned review points |
| Stale task recovery | Re-run from first open task | Re-open in state.json; delete stale outputs |

Read the relevant section below for your project type.

---

## Autonomous loop — Task design

## What makes a bad task

**Too large:** "Implement the authentication system" is not a task. It's a project. Claude will implement something, claim it's done, and the done-check will fail in opaque ways.

**Acceptance criteria that aren't checkable:** "The code should be clean and well-structured." How does done-check.sh verify that? It can't. Either it becomes a judge criterion, or it's dropped.

**Missing closure contract:** If there's no contract, Claude will mark tasks closed based on conversational memory ("I said I finished it, so it's finished"). The system degrades to the old model.

**Circular tasks:** "T005: Fix any remaining issues" — remaining issues from what? When does it end? Infinite loop guaranteed.

## What makes a good task

**Scoped to a verifiable outcome:** The task produces something that either exists or doesn't.

**Acceptance criteria are commands:** "The tests pass" → `npm test`. "The endpoint returns 200" → `curl -s localhost:3000/health | jq '.status' == "ok"`. "The file exists" → `[ -f src/config.ts ]`.

**Closure contract specifies evidence:** What test file was added? What command passes? What artifact was created? If you can't describe the evidence in 1-3 lines, the task scope is too large.

**One thing at a time:** Not "implement feature X and add tests and update docs." That's three tasks.

## Task sizing guide

| Time to implement | Right size? |
|------------------|-------------|
| < 5 minutes | Too small — merge with adjacent task |
| 10–45 minutes | Good |
| 45–90 minutes | Borderline — consider splitting |
| > 90 minutes | Too large — split |

If you can't estimate implementation time, the task is too vague.

## Acceptance criteria patterns

**File must exist:**
```
- [ ] src/auth/token.ts exists and exports TokenService
```
Verifiable with: `[ -f src/auth/token.ts ]`

**Command must pass:**
```
- [ ] npm test passes with no failures
- [ ] tsc --noEmit exits 0
```
Verifiable with the command itself.

**Behavior must be true:**
```
- [ ] POST /auth/login with valid credentials returns { token: string }
- [ ] POST /auth/login with invalid credentials returns 401
```
Verifiable with: `npm test -- tests/auth.test.ts`

**No regressions:**
```
- [ ] All previously passing tests still pass
```
Verifiable with `validate-closed-tasks.sh`.

**Avoid:**
```
- [ ] Code is readable and maintainable     (not checkable)
- [ ] Implementation follows best practices  (not checkable)
- [ ] Claude reviewed the changes            (tautological)
```
These belong in the judge rubric, not in acceptance criteria.

## Closure contract patterns

**Simple task (add a function):**
```
Closure Contract:
- Evidence required:
  - tests/auth/token.test.ts added (or updated)
  - npm test passes
  - TokenService is exported from src/auth/index.ts
```

**Refactoring task:**
```
Closure Contract:
- Evidence required:
  - All existing tests still pass (no regressions)
  - Old function name no longer exported
  - New function name used in all call sites (grep confirms)
  - CLOSED_TASKS.md entry added
```

**Investigation task (no code changes):**
```
Closure Contract:
- Evidence required:
  - Summary written to PLAN.md under T001 results
  - Relevant files listed
  - Recommended next task identified
```

## Registering a closed task

When Claude closes a task (Tier 2+), it must:

1. Update PLAN.md: change `Status: open` → `Status: closed`
2. Add an entry to `CLOSED_TASKS.md` with:
   - What was accepted
   - Which test files protect it
   - The invariant that must remain true
3. Add an entry to `validation-manifest.json`:
   ```json
   {
     "id": "T002",
     "name": "Short task name",
     "status": "closed",
     "tests": ["tests/auth/token.test.ts"],
     "invariants": ["TokenService.create() returns a signed JWT"],
     "protected_files": ["tests/auth/token.test.ts"]
   }
   ```
4. Run `close-task-check.sh T002` to verify the closure is valid
5. Git commit: `git commit -m "Close T002: [task name]"`

If `protect-control-files.sh` is installed, Claude cannot do steps 2–3 directly. Either use a closure script, or handle those steps from outside Claude Code.

---

## Human-in-the-loop / Evaluation — Task design

Tasks in human-in-the-loop and evaluation projects do not run against a `done-check.sh`. Completion is decided by the human after reviewing outputs. The agent's job is to produce artifacts and surface them clearly — not to assert completion autonomously.

### What makes a bad human-in-the-loop task

**No output to review:** "Explore clustering options" with no artifact produced. The human can't review nothing. Every task must produce a file, chart, summary, or logged decision that the human can read.

**Acceptance criteria require running code the human doesn't have:** "Tests must pass" — there may be no test suite. Criteria must be things the human can inspect: file exists, row counts match, output looks sane.

**Skipping the scope lock:** Running Phase 1 tasks without T000 (foundations) closed. All downstream tasks depend on the scope being fixed.

**Overwriting outputs without logging:** Producing a new version of a file without recording what changed and why in the session log.

### Task format for human-in-the-loop projects

```markdown
### T007: Feature engineering

Status: open
Phase: phase_1__eda_clustering

> Skills: quik-analytics-query-writer · quik-persona-process

What to do:
Derive the behavioral feature matrix from B1/B2/B3 outputs. One row per customer.

Outputs:
- phases/phase_1__eda_clustering/output/feature_matrix.csv

Acceptance Criteria:
- [ ] feature_matrix.csv exists and is non-empty
- [ ] All 10 behavioral dimensions present as columns
- [ ] No customer_id NULLs
- [ ] Row count within 5% of B1 customer count

Closure Contract:
- Evidence required:
  - phases/phase_1__eda_clustering/output/feature_matrix.csv (non-empty, correct columns)
  - Notes section filled in with row count and any anomalies
- Human closes with /close-task T007 after review

Notes:
```

Key differences from autonomous tasks:
- `Phase:` field on every task (which phase it belongs to)
- `> Skills:` callout at phase header so agent knows what to load
- `Outputs:` explicit list (agent produces these; human reviews them)
- Closure contract ends with "Human closes with /close-task TXXX after review" — not automated
- Notes section is mandatory to fill before closing

### Registering a closed human-in-the-loop task

When the human runs `/close-task TXXX`:

1. Verify all output files in Closure Contract exist and are non-empty
2. Fill in Notes section in PLAN.md — row counts, anomalies, observations
3. Update `state.json`: `current_task`, `last_completed_task`, `current_phase`
4. Write closure record to `.mission-control/closure-records/TXXX-closure.json`
5. Advance to next task — do not start work until user confirms

For human-in-the-loop projects: no `validation-manifest.json` or `CLOSED_TASKS.md` unless there's a test suite. Replace with a notes-based closure record.

---

## Milestone gate tasks (human-in-the-loop and evaluation projects)

A milestone gate is a planned human review point — not triggered by failure, but by design. Use it when the next phase requires a judgment call that can't be automated.

**Signs you need a milestone gate:**
- Phase N produces output that a human must review before Phase N+1 makes sense (e.g. cluster quality review, enrichment decision)
- The decision at the boundary has multiple valid paths (enrich vs. proceed, expand scope vs. cut)
- A domain expert needs to sign off on an intermediate artifact

**Milestone gate task format:**
```markdown
### T011b: Enrichment Assessment Gate

Status: open
Type: milestone-gate

Purpose:
Human reviews cluster quality and decides whether to enrich before calibration.

What to review:
- Cluster profile output at phases/phase_1__eda/output/cluster_profiles.json
- Dimension sparsity — which dimensions have < 30% signal?
- Whether enrichment would materially improve persona separation

Decision required:
- [ ] Human reviewed cluster quality and enrichment readiness
- [ ] Decision logged: proceed as-is OR enrich (specify which dimensions)

Closure Contract:
- Evidence required:
  - /log-decision "enrichment decision: [proceed|enrich] — [reason]"
  - If enrichment: enrichment tasks added to PLAN.md before T012

Notes:
```

Milestone gates have no code output and no test command. Their closure contract is: "human reviewed and decided, decision logged." The agent's job is to surface the information the human needs, then wait.

---

## User corrections protocol

When the user steers mid-project — changes scope, redefines a task, adjusts a threshold, or invalidates completed work — follow this protocol. Do not apply corrections silently.

1. **Log the decision first** — run `/log-decision "what changed and why"` before making any edits.
2. **Update the operating manual skill** — if the correction affects methodology, personas, dimensions, or process, update the relevant section of the project's operating manual skill (in `.claude/skills/`). Skills must stay in sync with how the project is actually running.
3. **Update CLAUDE.md or quik-progress** — if the correction changes phase structure, task scope, or common-mistake patterns, update those.
4. **Re-open affected tasks** — update `task_status` in `state.json` from `"closed"` back to `"open"` for any task now invalidated. Delete or overwrite stale output files.
5. **Note in PLAN.md** — add a dated note to the affected task's Notes section explaining what changed and why.

User corrections are not exceptions — they are part of the process. If only the first N steps are applied and skills/CLAUDE.md drift from reality, the next session starts from a wrong baseline.

---

## Planning pass guidance (what to tell Claude)

When running the planning pass, Claude should:

1. **Read the codebase first** — don't plan blindly. Understand what already exists.
2. **Start with an investigation task** — T001 is always "inspect current state." This gives Claude a low-risk task to establish baseline understanding and note what's already working.
3. **Order by dependency** — if T003 depends on T002, that must be reflected. Don't create tasks that assume later tasks have already run.
4. **Estimate risk in each task** — which tasks change existing behavior? Which add new behavior? Which are pure additions? Risk affects how tight the closure contract needs to be.
5. **Don't plan more than 10 tasks up front** — for long objectives, plan the first 5–7 tasks in detail and leave later tasks as rough stubs. They'll be refined as earlier tasks complete and the picture becomes clearer.

## Example: well-formed task list

```markdown
### T001: Inspect current state

Status: open

Acceptance Criteria:
- [ ] Current auth implementation reviewed
- [ ] Existing test coverage noted
- [ ] Files that will change identified

Closure Contract:
- Evidence required:
  - Notes written to PLAN.md under T001 results
  - List of files to change
  - Confirmation of current test pass/fail status

---

### T002: Add TokenService class

Status: open

Acceptance Criteria:
- [ ] src/auth/token.ts created
- [ ] TokenService.create(userId) returns a signed JWT
- [ ] TokenService.verify(token) returns userId or throws
- [ ] npm test passes

Closure Contract:
- Must add: tests/auth/token.test.ts
- Tests must cover: create happy path, verify happy path, verify invalid token throws
- Must register in validation-manifest.json
- Must run close-task-check.sh T002

---

### T003: Wire TokenService into login endpoint

Status: open

Acceptance Criteria:
- [ ] POST /auth/login uses TokenService.create
- [ ] Response includes { token: string }
- [ ] Existing login tests still pass

Closure Contract:
- Must update: tests/auth/login.test.ts
- validate-closed-tasks.sh must pass (T002 regression)
- Must register in validation-manifest.json
```
