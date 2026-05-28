---
name: skill-writing-principles
description: Core design principles for writing effective skills. Reference when reasoning about skill structure, length, style, or content decisions.
---

# Skill Writing Principles

These principles apply to every SKILL.md, CLAUDE.md, AGENTS.md, or agent instruction file.

## Less Is More

Target line counts:
- **Project file:** 60–120 lines
- **Global file:** under 30 lines
- **Monorepo root:** under 80 lines

Every line must prevent a specific mistake. If a line doesn't stop a wrong action, delete it.

Why: The agent's context window is finite. Bloated instructions get ignored. Concise instructions get followed.

## Imperatives Over Prose

Prefer commands that can be executed.

- **Good:** `Run pnpm test before marking ready.`
- **Bad:** `Make sure tests pass before you consider the task done.`

- **Good:** `If the file is over 500 lines, stop and ask the user before editing.`
- **Bad:** `Be mindful of file sizes when making changes.`

Verifiable commands over descriptions. Commands can be executed and checked; descriptions can't.

## High-Priority Rules First

The first 40 lines are the most-read. Put the most critical rules there:
- Security constraints
- Irreversible operation warnings
- Out-of-scope boundaries
- Mandatory checkpoints

## IMPORTANT / YOU MUST Sparingly

Reserve `IMPORTANT` or `YOU MUST` for the one or two truly critical rules. If everything is important, nothing is.

Use formatting for emphasis, not just caps:
- `**CRITICAL:**` for security or irreversibility
- `**STOP:**` for gates where the agent must pause
- `**NEVER:**` for absolute prohibitions

## Negative Rules Matter

Without explicit "nevers," the agent picks the most common pattern it knows — which may not be yours.

- **Bad:** `Use the project's formatting conventions.`
- **Good:** `Never run prettier on files in src/lib/legacy. That directory is intentionally unformatted.`

- **Bad:** `Handle errors appropriately.`
- **Good:** `Never retry a 401. If auth fails, stop and ask the user.`

## Don't Duplicate Tooling

Delete anything the linter, CI, or auto-memory already enforces:
- Don't restate the style guide if prettier/eslint is configured
- Don't list directory structures if the agent can see the file tree
- Don't define terminology if CONTEXT.md exists (read it instead)
- Don't repeat patterns the agent infers from one session in the repo

## No Secrets

Never include:
- API keys
- Tokens
- Passwords
- Private URLs
- Internal hostnames

Not in SKILL.md, not in CLAUDE.md, not in CLAUDE.local.md, not in scripts. Use environment variables or ask the user to configure them.

## Progressive Disclosure

Structure content in 3 levels:
1. **Frontmatter:** Always loaded — just name and description
2. **SKILL.md body:** Loaded when triggered — core workflow only
3. **References:** Loaded only when needed — deep docs, schemas, examples

Keep SKILL.md under 100 lines. Move everything else to `references/`.

## Naming Conventions

Use gerund form (verb + -ing) for skill names. This clearly describes the activity.
- **Good:** `processing-pdfs`, `analyzing-spreadsheets`, `testing-code`
- **Acceptable:** `pdf-processing`, `spreadsheet-analysis`, `process-pdfs`
- **Avoid:** `helper`, `utils`, `tools`, `documents`, `data`

## Descriptions in Third Person

Always write descriptions in third person. The description is injected into the system prompt.
- **Good:** "Processes Excel files and generates reports"
- **Avoid:** "I can help you process Excel files"
- **Avoid:** "You can use this to process Excel files"

## Avoid Windows-Style Paths

Always use forward slashes in file paths, even on Windows.
- **Good:** `scripts/helper.py`, `reference/guide.md`
- **Avoid:** `scripts\helper.py`, `reference\guide.md`

## Provide a Default, Not a Menu

Don't present multiple approaches unless necessary. Give one default with an escape hatch.
- **Bad:** "You can use pypdf, or pdfplumber, or PyMuPDF, or pdf2image..."
- **Good:** "Use pdfplumber for text extraction. For scanned PDFs requiring OCR, use pdf2image with pytesseract instead."

## Composability

Skills coexist with others. Don't assume exclusive access.
- Handle your domain
- Gracefully coexist with other active skills
- Don't override global conventions unless necessary

## Portability

Functions identically across Claude.ai, Claude Code, and API (assuming environment supports required tools).

## Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| Vague steps: "Analyze the data" | Specific: "Calculate average order value from the CSV and store in variable `aov`" |
| Implicit dependencies: "Use the data from earlier" | Explicit: "Use the `ticket_ids` list generated in Step 1" |
| Subjective quality: "Make sure it looks good" | Objective: "Verify all JSON keys match schema in `references/schema.json`" |
| No failure handling: "Call the API" | Explicit: "Call the API. If 404: log and skip. If 500: retry once. If 429: wait 60s and retry." |
| Buried critical rules | Move to first 40 lines |
| Secrets in instructions | Use env vars or ask user |
