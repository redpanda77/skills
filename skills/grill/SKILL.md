---
name: grill
description: Interview and stress-test the user before building. Use when user says "grill me", "interview me", "ask me questions before we start", or wants to clarify scope, decisions, or stress-test a plan against existing documentation. Routes to the right grilling mode based on intent.
---

# Grill

Route to the right grilling mode based on user intent. Two modes: **pre-build interview** (surface decisions before coding) and **plan stress-test** (challenge a plan against the domain model and existing docs).

## Quick Router

| User intent | Mode | Start here |
| --- | --- | --- |
| "grill me", "interview me", "ask me questions before we start" | Pre-build interview | `references/workflows/grill-me.md` |
| "what should I build?", "help me scope this" | Pre-build interview | `references/workflows/grill-me.md` |
| "stress-test my plan", "challenge my design" | Plan stress-test | `references/workflows/grill-with-docs.md` |
| "does this match our domain model?" | Plan stress-test | `references/workflows/grill-with-docs.md` |
| "update our glossary / ADRs" | Plan stress-test | `references/workflows/grill-with-docs.md` |
| "how do I write a CONTEXT.md?" | Formats | `references/formats/context.md` |
| "how do I write an ADR?" | Formats | `references/formats/adr.md` |

## Workflow

1. **Identify user intent** — Are they starting something new or stress-testing an existing plan?
2. **Route to mode** — Pre-build interview or plan stress-test
3. **Load the workflow** — Read the corresponding reference file
4. **Follow the process** — Ask questions, explore codebase, update docs
5. **Capture decisions** — Write to handoff doc or update CONTEXT.md/ADR as decisions crystallise

## When to Combine Modes

- **Interview then stress-test**: First grill the user on scope, then stress-test the resulting plan against existing docs
- **Stress-test then interview**: If the plan has gaps, switch to interview mode to fill them
- **Both + formats**: When building in a new domain, interview for scope, then create/update CONTEXT.md and ADRs

## Rules

- Never skip the grilling phase if the user explicitly asks for it.
- If the user is vague, default to pre-build interview first.
- If a plan exists and the user wants validation, default to plan stress-test.
- If `CONTEXT.md` exists, always load it before asking terminology questions.
- Always ask one question at a time, waiting for feedback before continuing.
- If a question can be answered by exploring the codebase, explore instead of asking.
- When decisions crystallise, write them down immediately — don't batch.

## Error Handling

- Missing CONTEXT.md: Note the gap and suggest creating one during the session.
- User resists questions: Explain that ambiguous scope is the #1 source of rework.
- Contradiction found in code vs docs: Surface it immediately and ask which is correct.
- Term too vague to define: Ask for a concrete scenario that uses it.
