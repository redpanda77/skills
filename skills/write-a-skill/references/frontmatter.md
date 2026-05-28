---
name: skill-frontmatter
description: Reference for all SKILL.md frontmatter fields, naming rules, description formulas, and validation. Use when creating or reviewing frontmatter.
---

# Frontmatter

The YAML block at the top of SKILL.md. This is the only thing the system sees when deciding whether to load the skill.

## Required Fields

```yaml
---
name: skill-name              # MUST be kebab-case
  description: What it does. Use when [triggers].
---
```

### `name`

- Must be kebab-case: `my-skill-name`
- Maximum 64 characters
- No underscores, no CamelCase, no spaces
- Cannot contain "claude" or "anthropic" (reserved)
- Must match the folder name exactly
- **Prefer gerund form** (verb + -ing): `processing-pdfs`, `analyzing-spreadsheets`, `testing-code`
- **Acceptable alternatives:** noun phrases (`pdf-processing`), action-oriented (`process-pdfs`)
- **Avoid:** vague names (`helper`, `utils`, `tools`), reserved words (`anthropic-helper`)

### `description`

The only signal the system uses for auto-invocation. This is the most important field.

**Formula:**
```
[What it does] + [When to use it / Triggers] + [Key capabilities]
```

**Length:** Under 1024 characters. Under 200 is ideal.

**Must include:**
- "Use when..." trigger phrase
- Specific keywords, file types, or actions
- At least 2–3 distinct trigger scenarios

**Always write in third person.** The description is injected into the system prompt.
- **Good:** "Processes Excel files and generates reports"
- **Avoid:** "I can help you process Excel files"
- **Avoid:** "You can use this to process Excel files"

**Examples:**

```yaml
# BAD — too vague
description: Helps with projects.

# BAD — missing triggers
description: Creates sophisticated multi-page documentation systems.

# BAD — first person
description: I can help you analyze Excel spreadsheets.

# GOOD — specific + triggers + third person
description: Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for "design specs", or "design-to-code handoff".

# GOOD — clear value + triggers + third person
description: End-to-end customer onboarding workflow for PayFlow. Handles account creation, payment setup, and subscription management. Use when user says "onboard new customer", "set up subscription", or "create PayFlow account".
```

## Optional Fields

```yaml
---
name: skill-name
description: ...

# Arguments the skill accepts from the user
arguments:
  - name: issue_number
    description: The GitHub issue number to review
    required: false

# Tool restriction
allowed-tools:
  - Bash
  - Read
  - Edit

# Compatibility notes
compatibility:
  - "Requires Python 3.8+"
  - "Network access for API calls"

# Metadata (informational only)
metadata:
  author: Your Name
  version: 1.0.0
  mcp-server: service-name
---
```

## Validation Checklist

- [ ] Name is kebab-case
- [ ] Name ≤ 64 chars
- [ ] No reserved words in name
- [ ] Description includes "Use when..."
- [ ] Description under 1024 chars
- [ ] No XML tags `< >` anywhere in frontmatter
- [ ] No time-sensitive data (version numbers, percentages, dates)
- [ ] Triggers are specific, not generic
- [ ] Folder name matches `name` field exactly

## Negative Triggers

To prevent overtriggering, include negative guidance in the description:

```yaml
description: Advanced data analysis for CSV. Use for statistical modeling. Do NOT use for simple exploration or one-off queries.
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| `name: my_skill` (snake_case) | `name: my-skill` |
| `description: Helps with code` | Add triggers: `description: Generates Python unit tests from function signatures. Use when user asks for "test this", "write tests", or "unit test coverage".` |
| Frontmatter over 1024 chars | Cut to 200 chars if possible |
| XML in description: `description: Use <git>` | Escape or remove: `description: Use git commands` |
