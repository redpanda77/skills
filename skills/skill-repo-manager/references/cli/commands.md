---
name: skills-cli-commands
description: Complete reference for the npx skills CLI commands. Use when installing, listing, finding, removing, updating, or initializing skills.
---

# CLI Commands

The `npx skills` CLI distributes reusable guidance sets for AI coding agents (Claude Code, Cursor, Codex, etc.).

## Install

```bash
npx skills add <source> [options]
```

Sources:
- GitHub repo: `owner/repo`
- Full git address: `https://github.com/owner/repo.git`
- Local path: `./path/to/repo`

Options:
| Flag | Description |
|------|-------------|
| `-g` | Install globally (in `~/.claude/skills/` or equivalent) |
| `-a <agent>` | Target a specific agent (e.g., `claude`, `cursor`, `codex`) |
| `-s <skill>` | Install only the named skill from the repo |
| `-l` | Preview without installing (list only) |
| `-y` | Bypass prompts, auto-confirm |
| `--copy` | Duplicate files instead of symlinking |
| `--all` | Install all skills found, not just the default set |

Examples:
```bash
npx skills add redpanda77/skills
npx skills add redpanda77/skills --skill mission-control
npx skills add redpanda77/skills -g
npx skills add ./local-repo --copy
```

## List

```bash
npx skills list [options]
```

Shows installed skills. Aliases: `ls`.

Options:
| Flag | Description |
|------|-------------|
| `-g` | List globally installed skills |
| `-a <agent>` | List skills for a specific agent |

## Find

```bash
npx skills find <query>
```

Search for skills by name or description across installed sources.

## Remove

```bash
npx skills remove <skill> [options]
```

Uninstall a skill. Aliases: `rm`.

Options:
| Flag | Description |
|------|-------------|
| `-g` | Remove from global scope |
| `-a <agent>` | Remove from a specific agent |

## Update

```bash
npx skills update [source] [options]
```

Refresh installed skills from their sources.

Options:
| Flag | Description |
|------|-------------|
| `-p` | Limit to current project (skip global) |
| `-g` | Limit to global scope |
| `-y` | Auto-confirm |

## Init

```bash
npx skills init [options]
```

Scaffold a new skill repository or skill.

Options:
| Flag | Description |
|------|-------------|
| `-s <name>` | Initialize a specific skill folder |
| `--dir <path>` | Target directory |

## Test before publishing

```bash
npx skills add ./local-repo --list
```

Verify what skills would be installed without actually installing.
