# Task Design

Good tasks make the control system work. Bad tasks make it fight you.

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
