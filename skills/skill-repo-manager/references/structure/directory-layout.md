---
name: skill-directory-layout
description: Directory structure and discovery rules for skill repositories. Use when organizing or troubleshooting skill repo layout.
---

# Directory Layout

## Skill Repository Structure

A skill repository is a folder that contains one or more skills. The CLI discovers skills by scanning for `SKILL.md` files.

### Standard layout

```
repo-root/
├── skills/
│   ├── skill-a/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   ├── scripts/
│   │   └── examples/
│   └── skill-b/
│       ├── SKILL.md
│       └── ...
├── .curated/
│   └── ...
├── .experimental/
│   └── ...
└── README.md
```

### Discovery paths

The CLI scans these locations in order:

1. **Repository root** — `SKILL.md` directly in the repo root
2. **`skills/`** — top-level skills folder
3. **`.curated/`** — curated skills subdirectory
4. **`.experimental/`** — experimental skills subdirectory
5. **Agent-specific folders** — `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.codex/skills/`, etc.

### Scan depth

- Default: **1 level** deep from the scan root
- Catalog-style nesting: **2 levels** deep
- Fallback: **full recursion** if nothing is found at shallow levels

### Agent installation paths

When installed, skills are placed in per-agent directories:

| Agent | Project scope | Global scope |
|-------|--------------|--------------|
| Claude Code | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` |
| Cursor | `.cursor/skills/<name>/` | `~/.cursor/skills/<name>/` |
| Codex | `.codex/skills/<name>/` | `~/.codex/skills/<name>/` |
| Generic | `.agents/skills/<name>/` | `~/.agents/skills/<name>/` |

### Plugin manifests

The CLI also reads from:
- `.claude-plugin/marketplace.json`
- `.claude-plugin/plugin.json`

These declare skills for plugin distribution.

## Rules

- Every skill must be in its own folder.
- Every skill folder must contain a `SKILL.md` file.
- The `SKILL.md` must start with YAML frontmatter.
- The frontmatter must have `name` and `description` fields.
- Optional: `metadata.internal: true` to hide from default installs.
