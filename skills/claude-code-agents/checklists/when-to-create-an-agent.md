# When to Create an Agent

Create an agent when **at least two** are true:

- The task repeatedly appears across projects or sessions.
- The task benefits from a specialized role prompt.
- The task should not pollute the main context.
- The task needs restricted tools.
- The task should use a different model.
- The task produces lots of intermediate output.
- The task can return a compact summary.
- The task is safe to delegate with clear boundaries.

## Do not create an agent when

- A short prompt is enough.
- A **skill** would better capture reusable instructions (especially without isolation).
- A **hook** is needed because behavior must happen **deterministically** at lifecycle or tool boundaries.
- The task needs ongoing back-and-forth with the user in one shared thread.

## Quick alternatives

| Signal | Prefer |
| --- | --- |
| Repeatable procedure, slash command | Skill (optional `context: fork`) |
| Must run every time on tool use | Hook |
| One-off Q&A on current context | Main thread or `/btw` |
