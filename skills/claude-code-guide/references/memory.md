---
source_urls:
  - https://code.claude.com/docs/en/memory
last_reviewed: 2026-05-13
---

# Memory: CLAUDE.md and auto memory

Claude Code starts each session with a fresh context window. Two mechanisms carry knowledge forward:

| Mechanism | Who writes | Contents | Loaded |
| --- | --- | --- | --- |
| **CLAUDE.md** (and hierarchy) | You | Instructions, conventions, architecture | Session start (plus on-demand nested files) |
| **Auto memory** | Claude | Learned preferences, commands, patterns | Session start (first ~200 lines or 25KB of `MEMORY.md`) |

Both are **context**, not enforced configuration. Be specific and concise for reliable adherence.

## Where `CLAUDE.md` lives (precedence: more specific wins)

Typical locations (see official doc for full OS paths):

- **Managed / org** — company-wide policy copies
- **Project** — `./CLAUDE.md` or `./.claude/CLAUDE.md` (team-shared)
- **User** — `~/.claude/CLAUDE.md` (personal defaults)
- **Local** — `./CLAUDE.local.md` (gitignored personal project prefs)

Nested `CLAUDE.md` files load when Claude works under those directories. Use **`.claude/rules/`** for path- or glob-scoped rules instead of one giant root file.

## Imports

`@path/to/file` in `CLAUDE.md` expands at launch (relative to the importing file). Recursive imports max depth **5**.

## Auto memory

Per-repo notes Claude maintains (with user steering). Subagents may use **`memory:`** in frontmatter for persistent agent memory directories — see [Subagents](https://code.claude.com/docs/en/sub-agents#enable-persistent-memory).

## Practical guidance

- Target **under ~200 lines** per root `CLAUDE.md`; split with rules or skills for large monorepos.
- Run **`/init`** to bootstrap project instructions (`CLAUDE_CODE_NEW_INIT=1` for multi-phase setup including skills/hooks prompts).
- Use **`/memory`** in-session to refine memory workflows (official Commands doc).

Official: [How Claude remembers your project](https://code.claude.com/docs/en/memory).
