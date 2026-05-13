# redpanda77 skills

Agent skills for Claude Code and compatible agents: planning (launchpad), controlled execution (mission-control), documentation workflows (grill-me, grill-with-docs), handoffs, Tolaria vaults, skill authoring, and CLAUDE.md / AGENTS.md writing.

## Install

Install all skills (project scope is detected automatically; use `-g` for global):

```bash
npx skills add redpanda77/skills
```

List available skills without installing:

```bash
npx skills add redpanda77/skills --list
```

Install one skill:

```bash
npx skills add redpanda77/skills --skill mission-control
```

Install globally:

```bash
npx skills add redpanda77/skills --skill mission-control -g
```

If `npx` on your Node version prefers `npm exec`, equivalent invocations use `npm exec --yes -- skills …` with the same arguments after `skills`.

## Layout

Skills live under `skills/<skill-name>/` with a `SKILL.md` (YAML frontmatter plus body). Optional folders: `references/`, `scripts/`, `assets/`.

## Test before publishing

From outside this repo (or with a path to it):

```bash
npx skills add ./skills-repo --list
```

After pushing to GitHub:

```bash
npx skills add redpanda77/skills --list
npx skills add redpanda77/skills --skill grill-me -y
```

Public listing on [skills.sh](https://skills.sh) is driven by install telemetry when users run `npx skills add <owner/repo>`; there is no separate registry submission for the leaderboard.

## License

MIT — see [LICENSE](LICENSE).
