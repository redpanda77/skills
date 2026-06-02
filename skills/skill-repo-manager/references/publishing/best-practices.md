---
name: skill-best-practices
description: Best practices for managing skill repositories. Use when organizing, reviewing, or improving a skill repo.
---

# Best Practices

## Skill Design

- **One concern per skill** — A skill should do one thing well. Don't bundle unrelated workflows.
- **Progressive disclosure** — Keep `SKILL.md` under 100 lines. Push deep docs to `references/`.
- **Router pattern** — For complex skills, use `SKILL.md` as a router with a lookup table.
- **Self-contained** — Every skill should work independently. Don't assume another skill is installed.

## Repository Hygiene

- **Version control** — Track skills in git. Use semantic versioning for releases.
- **Testing** — Verify with `npx skills add ./repo --list` before pushing.
- **No secrets** — Never commit API keys, tokens, or credentials in skill files.
- **Clean structure** — One folder per skill. No orphaned files at the repo root.

## Naming

- Use kebab-case for skill names: `my-skill`, not `mySkill` or `my_skill`.
- Use gerund form for action-oriented skills: `processing-pdfs`, `analyzing-logs`.
- Be specific: `kubernetes-debugging` is better than `debugging`.

## Descriptions

- Write in third person: "Processes Excel files" not "I can help you process Excel files".
- Include the trigger: `Use when the user asks about X`.
- Keep under 1024 characters.
- Be specific about what the skill does and when to use it.

## Updates

- **Backward compatible** — Don't break existing users' workflows.
- **Deprecation** — If removing a skill, document it in the README and keep the folder for one release cycle.
- **Update frequently** — Run `npx skills update` periodically to refresh installed skills.

## Multi-Agent Support

- The CLI supports dozens of agents (Claude Code, Cursor, Codex, etc.).
- Use standard paths so the CLI can auto-detect: `skills/<name>/SKILL.md`.
- Avoid agent-specific features unless necessary.

## Error Handling

- Document common failures in the skill's references.
- Provide escape hatches: "If X fails, try Y."
- Don't assume the user's environment matches yours.
