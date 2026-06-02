---
name: when-to-grill
description: Decision guide for when to invoke grill-me or grill-with-docs before applying a thinking framework. Reference when the problem is vague or needs validation.
---

# When to Grill

## Invoke `grill-me` When

The problem is vague or underspecified. Use `grill-me` to clarify scope before applying any framework.

| Trigger | Why |
|---------|-----|
| User says "grill me" or "interview me" | Explicit request for clarification |
| Problem statement is one sentence | Need more detail to route correctly |
| No success criteria mentioned | Cannot evaluate if framework worked |
| Multiple competing interpretations | Need to narrow down |
| User says "I don't know where to start" | Clarify scope before routing |

**What `grill-me` does:**
- Asks 6–8 targeted questions via `AskUserQuestion`
- Covers scope, key tradeoffs, edge cases, success criteria, constraints, risks
- Writes a decision summary to `handoffs/<branch>.md`

**After grilling:** Read the handoff doc and route to the right framework.

## Invoke `grill-with-docs` When

A plan or design exists and needs validation against existing documentation.

| Trigger | Why |
|---------|-----|
| User says "grill this plan" or "stress-test this" | Explicit request for validation |
| Plan contradicts existing terminology | Need to align with domain model |
| Plan references concepts not in codebase | Need to check if they exist |
| User wants to create CONTEXT.md or ADRs | Documentation needs to be validated |
| Complex design with many dependencies | Need to resolve dependencies one-by-one |

**What `grill-with-docs` does:**
- Explores codebase and documentation
- Challenges against glossary and existing ADRs
- Sharps fuzzy language
- Stress-tests with concrete scenarios
- Updates CONTEXT.md and creates ADRs inline

**After grilling:** Apply the validated plan with the right framework.

## Don't Grill When

| Situation | Why |
|-----------|-----|
| Problem is clear and well-defined | Grilling adds friction without value |
| User just wants to apply a known framework | Direct application is faster |
| Emergency or time-critical | Apply framework immediately, grill later |
| User already provided a detailed handoff | Read the handoff, route directly |

## Workflow

```
User asks a question
    |
    Is the problem vague? → yes → Invoke grill-me
    |
    Is there a plan to validate? → yes → Invoke grill-with-docs
    |
    Is there a codebase? → yes → Explore documents first
    |
    Route to framework
```
