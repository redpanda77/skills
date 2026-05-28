---
name: skill-files-structure
description: Reference for skill directory layout, file naming, progressive disclosure, and what goes where. Use when scaffolding a new skill.
---

# File Structure

```
skill-name/
├── SKILL.md              # Required. Core workflow. Keep under 100 lines.
├── references/           # Optional. Deep docs, schemas, examples.
│   ├── topic-a.md
│   └── topic-b.md
├── scripts/              # Optional. Deterministic helpers.
│   └── validate.py
├── templates/            # Optional. Reusable templates.
│   └── report-template.md
├── examples/             # Optional. Concrete examples.
│   └── example-output.md
└── assets/               # Optional. Images, binaries.
```

## SKILL.md

- **Required.** Exactly `SKILL.md` (case-sensitive).
- **Content:** Frontmatter + core workflow only.
- **Length:** Under 100 lines. Under 60 is better. Under 500 is the hard limit.
- **What goes here:** The decision tree, the imperative steps, the critical rules.
- **What does NOT go here:** Deep explanations, long examples, schemas, troubleshooting, rationale.

## References

- **Optional but recommended.** Most skills need at least one.
- **Naming:** Descriptive, kebab-case. `api-patterns.md`, `troubleshooting.md`.
- **What goes here:**
  - Detailed schemas or API docs
  - Long examples or sample outputs
  - Troubleshooting guides
  - Deep dives on specific topics
  - Rationale for design decisions
- **Depth:** One level only. No `references/sub/dir/file.md`.

## Avoid Deeply Nested References

Claude may partially read files when they're referenced from other referenced files. When encountering nested references, Claude might use commands like `head -100` to preview content rather than reading entire files, resulting in incomplete information.

**Bad:**
```markdown
# SKILL.md
See [advanced.md](advanced.md)...

# advanced.md
See [details.md](details.md)...

# details.md
Here's the actual information...
```

**Good:**
```markdown
# SKILL.md
**Basic usage:** [instructions in SKILL.md]
**Advanced features:** See [advanced.md](advanced.md)
**API reference:** See [reference.md](reference.md)
**Examples:** See [examples.md](examples.md)
```

## Structure Longer Reference Files

For reference files longer than 100 lines, include a table of contents at the top. This ensures Claude can see the full scope even when previewing with partial reads.

```markdown
# API Reference

## Contents
- Authentication and setup
- Core methods (create, read, update, delete)
- Advanced features (batch operations, webhooks)
- Error handling patterns
- Code examples

## Authentication and setup
...
```

## Use Forward Slashes for Paths

Always use forward slashes in file paths, even on Windows. Unix-style paths work across all platforms.

- **Good:** `scripts/helper.py`, `reference/guide.md`
- **Avoid:** `scripts\helper.py`, `reference\guide.md`

## Scripts

- **Optional.** Only include if deterministic validation is needed.
- **What goes here:**
  - Validation scripts (check format, schema, etc.)
  - Data transformation helpers
  - Deterministic checks that are more reliable than natural language instructions
- **Why:** Code is deterministic. "Run `scripts/validate.py` and check exit code" is more reliable than "Make sure the JSON is valid."

### Scripts Best Practices

**Solve, don't punt.** Scripts should handle errors, not fail and let Claude figure it out.

- **Bad:** Script fails with a generic error. Claude has to debug.
- **Good:** Script catches errors, provides actionable messages, and returns gracefully.

**No voodoo constants.** Document why each value is what it is.

- **Bad:** `TIMEOUT = 47` with no explanation.
- **Good:** `REQUEST_TIMEOUT = 30` with a comment: "HTTP requests typically complete within 30 seconds."

**Provide utility scripts.** Even if Claude could write a script, pre-made scripts offer advantages:
- More reliable than generated code
- Save tokens (no need to include code in context)
- Save time (no code generation required)
- Ensure consistency across uses

**List dependencies.** If scripts need packages, state them explicitly. Don't assume packages are installed.

```markdown
Install required package: `pip install pypdf`

Then use it:
```python
from pypdf import PdfReader
reader = PdfReader("file.pdf")
```
```

**Make execution intent clear.** Tell Claude whether to execute or read the script:
- **Execute:** "Run `analyze_form.py` to extract fields"
- **Read as reference:** "See `analyze_form.py` for the extraction algorithm"

## Templates

- **Optional.** Reusable content the skill can copy and modify.
- **What goes here:**
  - Report templates
  - PR description templates
  - Configuration file templates

## Examples

- **Optional.** Concrete outputs showing what the skill should produce.
- **What goes here:**
  - Sample outputs
  - Before/after comparisons
  - Good vs bad examples

## Critical Rules

| Rule | Requirement |
|------|-------------|
| SKILL.md naming | Exactly `SKILL.md` (case-sensitive) |
| Folder naming | kebab-case: `skill-name` |
| No README.md | Don't include README.md inside skill folder |
| No XML in frontmatter | Forbidden: `< >` characters |
| No reserved names | Can't use "claude" or "anthropic" in name |
| References depth | One level only |
| No secrets | Never in any file |

## Progressive Disclosure

| Level | File | When Loaded | Content |
|-------|------|-------------|---------|
| 1 | Frontmatter | Always | Name + description with triggers |
| 2 | SKILL.md body | When triggered | Core step-by-step instructions |
| 3 | References | When needed | Deep docs, schemas, examples |
| 4 | Scripts | When called | Deterministic operations |

## What Goes Where

| Content | Location | Why |
|---------|----------|-----|
| Core workflow | SKILL.md | Always loaded when skill triggers |
| Detailed schemas | references/ | Only needed for specific steps |
| Usage examples | references/examples/ | Loaded when user asks for examples |
| Validation logic | scripts/ | Deterministic, executable |
| Troubleshooting | references/troubleshooting.md | Only needed when things break |
| Rationale | references/principles.md | Only needed when reasoning about design |

## MCP Tool References

If your skill uses MCP (Model Context Protocol) tools, always use fully qualified tool names.

**Format:** `ServerName:tool_name`

**Example:**
```markdown
Use the BigQuery:bigquery_schema tool to retrieve table schemas.
Use the GitHub:create_issue tool to create issues.
```

Without the server prefix, Claude may fail to locate the tool, especially when multiple MCP servers are available.

## Visual Analysis

When inputs can be rendered as images, have Claude analyze them visually.

```markdown
## Form layout analysis

1. Convert PDF to images:
   ```bash
   python scripts/pdf_to_images.py form.pdf
   ```

2. Analyze each page image to identify form fields
3. Claude can see field locations and types visually
```
