# tasks.md Format

```markdown
# Tasks: [Feature Name]
Status: 0/N complete

## Backlog
- [ ] TASK-001 | [title] | [S/M/L]
  Done when: [specific, testable criteria — one sentence]

- [ ] TASK-002 | [title] | [S/M/L]
  Done when: [criteria]

## In Progress

## Done
```

Rules:
- Size: S = under 2h, M = half-day, L = full session
- "Done when" must be testable — not "it works" but "endpoint returns 200 with payload X"
- Move tasks between sections as they progress; update the Status counter
- Never delete tasks — completed ones move to Done
