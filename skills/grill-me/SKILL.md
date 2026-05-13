---
name: grill-me
description: Interview the user before starting a feature or task using interactive multiple-choice questions. Use when the user says "grill me", "interview me", "ask me questions before we start", or wants to clarify scope and decisions before coding.
---

You are interviewing the user before they start building. Your job is to surface the decisions that will meaningfully change what gets built — not to document what you can already infer from the codebase.

## Before You Ask Anything

1. If `CONTEXT.md` exists in the project root, read it. Use the terminology defined there — never invent synonyms for existing terms. If it doesn't exist, note this after the interview and suggest `/grill-with-docs` to create it.
2. Read CLAUDE.md (if present), relevant files, and the git branch name.
3. Infer what you can. Only ask about what you genuinely cannot determine.

## Question Rules

- Use `AskUserQuestion` for **every** question — never plain text.
- Single-choice for architecture/scope/priority decisions.
- Multi-select for features, edge cases, environments to target.
- Always include a free-text fallback as the last option: `"Something else — I'll explain"`.
- Pre-select a sensible default when one is obvious, but always ask.
- Ask **6–8 questions maximum**. Stop when you have enough to build.
- Bias toward questions where different answers lead to meaningfully different implementations.

## Question Coverage

Across your questions, cover these areas (skip any you can already infer):

1. **Scope** — What's in, what's explicitly out?
2. **Key tradeoff** — The one architectural or design decision with real alternatives.
3. **Edge cases** — Which ones must be handled vs. explicitly deferred?
4. **Success criteria** — How will we know this is done?
5. **Constraints** — Performance, compatibility, team/process, deadline.
6. **Risk** — What's the one thing most likely to go wrong?

## After All Answers

1. Print a brief **Decision Summary** — one line per answer, capturing the *why* where the user gave a reason.
2. Write these decisions into the handoff doc:
   - Git repo: `handoffs/<branch>.md` (create `handoffs/` if needed). Read the file first if it exists.
   - No git: `mktemp -t handoff-XXXXXX.md`.
3. Structure the handoff entry under a `## Decisions` section with YAML frontmatter (`date`, `branch`, `status: pre-build`).
4. Tell the user the file path and that the handoff is ready to carry into the build session.
