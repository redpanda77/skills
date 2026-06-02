---
name: skill-md-format
description: The SKILL.md file format specification. Use when authoring, validating, or reviewing skill files.
---

# SKILL.md Format

Every skill is a folder containing a `SKILL.md` file with YAML frontmatter.

## Required Fields

```yaml
---
name: <kebab-case-skill-name>
description: <what-it-does>. Use when <triggers>.
---
```

- `name`: Kebab-case, max 64 characters. Use gerund form: `processing-pdfs`, `analyzing-spreadsheets`.
- `description`: Under 1024 characters. Third person: "Processes Excel files" not "I can help you process Excel files".

## Optional Fields

```yaml
---
name: my-skill
description: What this skill does and when to use it.
argument-hint: What will the next session be used for?
metadata:
  internal: true
  author: your-name
  version: 1.0.0
---
```

| Field | Purpose |
|-------|---------|
| `argument-hint` | Hint text shown when the skill is invoked with arguments |
| `metadata.internal` | If `true`, hidden unless `INSTALL_INTERNAL_SKILLS=1` is set |
| `metadata.author` | Author name or handle |
| `metadata.version` | Semantic version |

## Body Structure

After the frontmatter, the body is regular Markdown:

```markdown
---
name: my-skill
description: A short explanation of this skill's purpose
---

# My Skill

Write the skill instructions here.
```

## Progressive Disclosure

Keep `SKILL.md` under 100 lines (500 is the hard limit). Move deep docs to:
- `references/` — supporting markdown files
- `scripts/` — executable scripts
- `assets/` — images, data files

## Validation Checklist

- [ ] Frontmatter starts with `---`
- [ ] `name` is present and kebab-case
- [ ] `description` is present and under 1024 chars
- [ ] `description` is in third person
- [ ] Body is not empty
- [ ] No secrets in the file
- [ ] File is under 500 lines
