# Cross-tool: AGENTS.md + adapters

## When to use

User operates two or more of: Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Windsurf, Zed, OpenCode.

## The unified model

Maintain a single canonical `AGENTS.md` at the repo root. Each tool-specific file imports or copies from it and adds only what's tool-specific.

```
repo/
├── AGENTS.md                            # canonical, tool-agnostic
├── CLAUDE.md                            # @AGENTS.md + Claude-specific
├── .github/copilot-instructions.md      # AGENTS.md content + Copilot tweaks
├── .cursor/rules/*.mdc                  # AGENTS.md content split into scoped rules
└── .windsurfrules                       # AGENTS.md content + Windsurf-specific
```

## What goes where

Empirically: 70–80% shared core, 20–30% adapter.

| Shared (AGENTS.md) | Tool-specific adapter |
|---------------------|------------------------|
| Architecture map | Claude `/memory` debug notes |
| Security rules | Cursor pattern scoping |
| Build/test/lint commands | Copilot inline-suggestion hints |
| Escalation requirements | `CLAUDE.local.md` conventions |
| Hard rules | Windsurf-specific phrasing |

## Tool reference (verify against current docs)

| Tool | File | Loading |
|------|------|---------|
| Claude Code | `CLAUDE.md` | Directory walk + concat, on-demand subdir, @imports, auto-memory, `/memory` |
| OpenAI Codex | `AGENTS.md` | Root + nested subdir files |
| GitHub Copilot | `.github/copilot-instructions.md` (+ `.github/instructions/*.instructions.md`) | Workspace-global, file-pattern scoped |
| Cursor | `.cursor/rules/*.mdc` | Directory of rule files, always-on or pattern-scoped |
| Windsurf | `.windsurfrules` | Single flat root file |

## CI sync check

Recommend a lightweight CI script that reads `AGENTS.md` and verifies that **core rules** (security mandates, escalation requirements) appear in each tool-specific file. Adapters can rephrase but cannot silently omit mandates.

## Migration path

If the user has one CLAUDE.md and wants to add other tools:

1. Extract tool-agnostic content from CLAUDE.md into `AGENTS.md`.
2. Replace that content in CLAUDE.md with `@AGENTS.md`.
3. Add only Claude-specific bits (Claude.local.md conventions, /memory references) to CLAUDE.md.
4. Create stub files for each other tool referencing `AGENTS.md`.
