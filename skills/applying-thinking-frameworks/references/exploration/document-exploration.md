---
name: document-exploration
description: Strategy for exploring documents before applying a thinking framework. Reference when the problem involves a codebase or existing documentation.
---

# Document Exploration

## When to Explore

Before applying a framework to a codebase problem, explore the relevant documents. This prevents applying models in a vacuum.

| Situation | What to Read |
|-----------|-------------|
| Problem references existing code | Key source files, tests, configs |
| Problem references a system | Architecture docs, diagrams, API specs |
| Problem involves domain terminology | CONTEXT.md, AGENTS.md, glossary |
| Problem involves a bug | Logs, error traces, recent commits |
| Problem involves a decision | ADRs, design docs, meeting notes |

## Exploration Order

1. **Read project context** — `CLAUDE.md`, `AGENTS.md`, `CONTEXT.md` (if present)
2. **Read the relevant files** — Source files, tests, configs mentioned in the problem
3. **Check recent history** — Git log, recent commits, PRs
4. **Check existing documentation** — `docs/`, `README.md`, `docs/adr/`

## What to Look For

- **Terminology** — Don't invent synonyms for existing terms
- **Assumptions** — What does the codebase already assume?
- **Constraints** — What are the hard limits?
- **Patterns** — What patterns are already in use?
- **Recent changes** — What changed recently that might be relevant?

## Exploration Rules

- Only read what you need. Don't read the entire codebase.
- Use `grep` to find relevant files quickly.
- Use `Read` to read the files you find.
- If a file is too long, read the first 100 lines and the last 50 lines.
- If `CONTEXT.md` exists, use its terminology — never invent synonyms.

## After Exploration

1. Summarize what you found in 2–3 sentences.
2. Identify any gaps — what do you still not know?
3. If gaps remain, decide if you need to grill the user or if you can proceed.
4. Route to the right framework with the context you have.
