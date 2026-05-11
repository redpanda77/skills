# Prompts

Use short prompts. Enforcement lives in hooks and scripts.

## Planning prompt

```
Create PLAN.md for this project.

Objective: [state it]

The plan must include:
- Objective
- Global Definition of Done
- Task list (each task gets: acceptance criteria, closure contract, expected evidence)
- Blocker policy

Do not implement yet. Produce the task map first.
```

## Execution prompt (use with run-agent.sh or manual resume)

```
You are in execution mode.

Use PLAN.md as the task map.
Use CLOSED_TASKS.md and validation-manifest.json as the closed-work baseline.
Use done-check.sh as the completion authority.

Work from the first incomplete task.

For each task:
1. Implement the task.
2. Run local validation.
3. Add or update regression protection.
4. Run closed-task regression validation.
5. Run global validation.
6. Record closure evidence in PLAN.md.
7. Move immediately to the next incomplete task.

Do not ask whether to continue.
Do not stop after a completed subtask.
Stop only if done-check.sh passes or a real blocker exists.
```

## Recovery prompt (after context loss or crash)

```
Continue from the current repo state.

Read PLAN.md, CLOSED_TASKS.md, and validation-manifest.json.
Run git status and git log --oneline -10.
Identify the first incomplete task or failed validation.
Continue from there.

Do not rely on conversation history.
Do not ask whether to continue.
Stop only when done-check.sh passes or a real blocker exists.
```

## Closure prompt (for a single task)

```
Attempt to close the current task.

Before marking it closed:
- verify acceptance criteria
- add or update regression protection
- update closure evidence in PLAN.md
- ensure all closed-task validations still pass
- ensure global validation passes
- update CLOSED_TASKS.md and validation-manifest.json

If any check fails, do not close the task. Continue fixing.
```
