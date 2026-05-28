# Skills Setup

How to create the system skill and domain skills.

## What skills are

Skills are reusable operating manuals. They encode:
- Project-specific conventions
- Workflows (how to close a task, how to run the judge)
- Domain knowledge

## Types

| Type | Purpose | Example |
|---|---|---|
| **System skill** | Operating manual for the project | How to use this harness |
| **Domain skill** | Specialized domain knowledge | How to write React components in this repo |

## Rules

- Every project MUST produce a system skill. Hard gate.
- Keep `SKILL.md` under 100 lines. Move deep docs to `references/`.
- The system skill should list available domain skills and when to use them.
- Skills can invoke other skills and agents.
- Use `skills:` in subagent frontmatter to inject domain knowledge.
- Invoke `write-a-skill` to create skills. Do not write them manually.
