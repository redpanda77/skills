# PRD Format

```markdown
# PRD: [Feature Name]

## Problem
One paragraph. What breaks or is missing without this feature? Who feels it?

## Goal
One sentence. What does success look like from the user's perspective?

## Scope
### In
- [What this feature covers]

### Out
- [What is explicitly deferred — important for keeping tasks focused]

## Key decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| [topic]  | [what we chose] | [why, esp. what we rejected] |

## Success criteria
- [ ] [Specific, testable outcome]
- [ ] [Another outcome]

## Open questions
- [Unresolved item that may affect scope]
```

- Use only terminology from `.plan/CONTEXT.md`
- Keep it under 400 tokens — enough to brief Claude, not a design doc
- "Out of scope" is as important as "in scope" — it prevents scope creep in tasks
