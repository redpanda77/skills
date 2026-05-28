---
name: skill-distribution
description: Reference for skill distribution — plugin, personal, project, and bundled skills. Use when deciding how to package and deploy a skill.
---

# Distribution

Where a skill lives and how it gets to users.

## Skill Types

### Plugin Skills

Installed via a plugin system (e.g., Claude Code plugins, VS Code extensions).

- **Managed by:** Plugin author / package manager
- **Scope:** Available wherever the plugin is installed
- **Updates:** Automatic via plugin updates
- **Example:** A company-wide skill distributed through an internal plugin

### Personal Skills

Installed by an individual user for their own use.

- **Location:** `~/.claude/skills/` (Claude Code) or uploaded via settings (Claude.ai)
- **Scope:** Only for that user
- **Updates:** Manual upload/replacement
- **Best for:** Individual workflows, personal preferences, experimentation

### Project Skills

Stored in a project repository and shared with the team.

- **Location:** `.claude/skills/` in the project root
- **Scope:** Only when working in that project
- **Updates:** Via git (version controlled)
- **Best for:** Team conventions, project-specific workflows, codebase-specific knowledge

### Bundled Skills

Multiple skills packaged together as a single unit.

- **Use when:** A set of related skills that should be installed together
- **Structure:** Parent folder with subfolders per skill
- **Example:** A "DevOps" bundle with skills for deployment, monitoring, and incident response

## Packaging

### Individual Skill

```
skill-name/
├── SKILL.md
├── references/
├── scripts/
└── (optional extras)
```

Zip the folder for upload, or place directly in the skills directory.

### Multiple Skills

```
skills/
├── skill-a/
│   └── SKILL.md
├── skill-b/
│   └── SKILL.md
└── skill-c/
    └── SKILL.md
```

Each skill is an independent folder with its own SKILL.md.

## Installation

### Claude Code

1. Place skill folder in `~/.claude/skills/` (personal) or project `.claude/skills/` (project)
2. Restart Claude Code or wait for change detection
3. Verify with: `What skills do you have available?`

### Claude.ai

1. Go to Settings > Capabilities > Skills
2. Upload the skill folder (or zip)
3. Verify by asking a trigger question

### API

Skills are not directly loaded via API. Use system prompts or prompt engineering instead.

## Recommended Approach

1. **Host on GitHub** (public or private repo)
   - Clear repo-level README (NOT inside skill folders)
   - Installation instructions
   - Version tags

2. **For teams:**
   - Project skills: commit `.claude/skills/` to the repo
   - Personal skills: share via internal wiki or script

3. **For plugins:**
   - Follow the plugin platform's packaging format
   - Include manifest.json if required

## Legacy Commands

Some platforms support legacy command formats:

- **Slash commands:** `/command` (platform-specific, may be deprecated)
- **Custom prompts:** Pre-skill system for injecting prompts

Prefer the skill format over legacy commands. Skills are:
- Version controllable
- Composable
- Portable across platforms
- More explicit about their scope
