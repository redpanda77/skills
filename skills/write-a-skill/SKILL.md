---
name: write-a-skill
description: Create agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, build, write, or author a new skill; when user mentions "skill", "SKILL.md", "agent capability", or asks how to make Claude follow specific workflows.
---

# Core Principles

Progressive disclosure is the most critical principle. Load only what is needed, when it is needed.
- **Level 1:** Frontmatter — name + description. Always loaded. Under 1024 chars.
- **Level 2:** SKILL.md — core workflow. Loaded when triggered. Under 100 lines (under 500 is the hard limit).
- **Level 3:** References — deep docs. Loaded only when needed. Never nest deeper than one level.

Less is more. Target 60–120 lines for a project file, under 30 for global, under 80 for monorepo root.
Imperatives over prose. Verifiable commands over descriptions.
High-priority rules first. Security, irreversibility, and out-of-scope rules in the first 40 lines.
IMPORTANT / YOU MUST sparingly. Reserve for the one or two truly critical rules.
Negative rules matter. Without explicit "nevers," the agent picks the most common pattern.
Don't duplicate the linter, the CI, or auto-memory. Delete anything tooling already enforces.
No secrets. Ever. Not in SKILL.md, not in CLAUDE.md, not in CLAUDE.local.md.

See references/principles.md for full rationale.

---

# When Asked to Create or Modify a Skill

Do not write anything before reading the reference for the step you are on. Use the checklist in references/process.md. Mark each item as done before proceeding.

## 1. Determine Scope

Ask one question: what is the use case?
- **Workflow / process** → sequential or iterative pattern. See references/patterns/.
- **MCP integration** → tool-first or problem-first framing. See references/invocation.md.
- **Domain expertise** → domain-specific pattern. See references/patterns/.
- **Multi-service** → multi-MCP or context-aware pattern. See references/patterns/.

## 2. Determine Invocation

How will the skill be triggered? See references/invocation.md.
- **Auto-triggered** → description must match user queries
- **Slash command** → user explicitly invokes with `/skill-name`
- **User-invocable** → user requests by name
- **Disable model invocation** → only explicit invocation

## 3. Determine Subagents

Does it delegate work to other agents? See references/subagents.md.
- Use `context: fork` for isolated work
- Use `skills:` in subagent frontmatter to preload skills
- Use `paths:` to restrict file access

## 4. Scaffold Frontmatter

See references/frontmatter.md.
- `name:` must be kebab-case, max 64 chars. Use gerund form: `processing-pdfs`, `analyzing-spreadsheets`.
- `description:` must be `[What it does]. Use when [triggers].` Under 1024 chars. Always write in third person ("Processes Excel files" not "I can help you process Excel files").
- `arguments:` if skill takes user input. See references/arguments.md.
- `allowed-tools:` if tool restriction needed. See references/permissions.md.

## 5. Write Instructions

See references/files-structure.md and references/principles.md.
- Keep SKILL.md under 100 lines for core workflow
- Move detailed schemas, examples, deep docs to `references/`
- Move deterministic operations to `scripts/`
- Include error handling and escape hatches
- Add negative rules explicitly

## 6. Configure Permissions

See references/permissions.md.
- Restrict `allowed-tools` to only what's needed
- Document side effects

## 7. Test

See references/testing.md.
- Triggering: verify it loads on relevant queries, not on unrelated ones
- Functional: verify each step produces correct output
- Edge cases: error handling, missing inputs, MCP failures

## 8. Review & Deliver

See references/process.md for the full checklist.
