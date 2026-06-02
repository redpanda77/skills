---
name: skill-repo-manager
description: Manage a skill repository using the npx skills CLI. Use when installing, listing, updating, removing, or publishing skills. Covers the skill format, directory structure, CLI commands, and publishing best practices for the open agent skills ecosystem.
---

# Skill Repository Manager

Route to the right topic based on user intent. Three areas: **CLI commands** (install, list, update), **Repository structure** (skill format, directory layout), and **Publishing** (sharing, versioning, best practices).

## Quick Router

| User intent | Topic | Start here |
| --- | --- | --- |
| "Install a skill", "add a skill", "npx skills add" | CLI | `references/cli/commands.md` |
| "List my skills", "what skills do I have?" | CLI | `references/cli/commands.md` |
| "Find a skill", "search for a skill" | CLI | `references/cli/commands.md` |
| "Remove a skill", "uninstall a skill" | CLI | `references/cli/commands.md` |
| "Update skills", "refresh skills" | CLI | `references/cli/commands.md` |
| "Scaffold a new skill", "create a skill" | CLI | `references/cli/commands.md` |
| "How do I structure a skill repo?" | Structure | `references/structure/directory-layout.md` |
| "What goes in SKILL.md?" | Format | `references/format/skill-md.md` |
| "How do I publish skills?" | Publishing | `references/publishing/publishing.md` |
| "Best practices for skill repos" | Publishing | `references/publishing/best-practices.md` |

## Workflow

1. **Identify user intent** — What operation or question do they have?
2. **Route to topic** — CLI, Structure, or Publishing
3. **Load the reference** — Read the corresponding file
4. **Execute or explain** — Follow the CLI commands or apply the guidance

## Rules

- Always use the `npx skills` CLI for installation and management — never manually copy files.
- If the user is creating a new skill, verify the SKILL.md frontmatter is valid before publishing.
- If installing from a GitHub repo, use the full `owner/repo` format.
- Prefer global installation (`-g`) for skills used across projects; project scope for repo-specific skills.
- If a skill is experimental or internal, mark it with `metadata.internal: true`.

## Error Handling

- CLI not found: Ensure Node.js is installed and `npx` is available.
- No skills found: Check the directory structure matches the expected layout.
- Invalid SKILL.md: Validate frontmatter with `name` and `description` fields.
- Conflicts on install: Use `--copy` instead of symlinks, or remove the existing skill first.
