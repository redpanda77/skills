---
name: skill-publishing
description: How to publish and share a skill repository. Use when preparing a skill repo for distribution.
---

# Publishing

## Sharing a Skill Repository

The `npx skills` CLI can install from any GitHub repo, git URL, or local path. To publish:

1. **Host on GitHub** — Push your repo to a public GitHub repository.
2. **Use the standard layout** — `skills/` folder with one folder per skill.
3. **Verify with `--list`** — Test before telling others:
   ```bash
   npx skills add ./your-repo --list
   ```
4. **Share the install command**:
   ```bash
   npx skills add owner/repo
   ```

## Visibility

| Visibility | How |
|------------|-----|
| Public | Default. Anyone can install with `npx skills add owner/repo`. |
| Internal | Set `metadata.internal: true` in `SKILL.md`. Hidden unless `INSTALL_INTERNAL_SKILLS=1`. |
| Private | Private GitHub repos work if the user has access. |

## Registry

Public listing on [skills.sh](https://skills.sh) is driven by install telemetry when users run `npx skills add <owner/repo>`. There is no separate registry submission.

## README

Your repo README should include:
- What the skill repo contains
- Install command
- List of skills with one-line descriptions
- Optional: skill table (name, source, what it does)

## Example README snippet

```markdown
## Install

```bash
npx skills add owner/repo
```

## Skills

| Skill | What it does |
|-------|--------------|
| `my-skill` | Description here |
```
