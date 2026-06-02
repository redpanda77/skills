---
source_urls:
  - https://code.claude.com/docs/en/permission-modes
last_reviewed: 2026-05-13
---

# Permission modes

Modes control **how often** Claude Code prompts before tools like `Edit`, `Bash`, or network calls. They are selected via **UI / CLI / settings**, not by asking Claude in chat.

## Mode summary

| Mode | Runs without asking (high level) | Typical use |
| --- | --- | --- |
| `default` | Reads | onboarding, sensitive work |
| `acceptEdits` | Reads + in-scope file edits + limited safe filesystem bash | iterate locally, review via `git diff` |
| `plan` | Reads (+ read-only shell where allowed) | explore before edits |
| `auto` | Broad auto-approval with classifier safety checks | long tasks; availability per account/policy |
| `dontAsk` | Only pre-approved tools | locked-down CI |
| `bypassPermissions` | Skips permission layer (still circuit-breakers on catastrophic rm) | **containers / VMs only** |

Except in `bypassPermissions`, **protected paths** still guard sensitive areas — see [permissions](https://code.claude.com/docs/en/permissions).

## Switching

- **CLI:** `Shift+Tab` cycles a subset (`default` → `acceptEdits` → `plan`, plus optional modes). `claude --permission-mode <mode>` at startup; `permissions.defaultMode` in settings for persistence.
- **VS Code / Desktop / Web:** mode picker (labels differ; web/cloud may subset modes — official doc has tables).

## Interaction with rules

Modes set baseline; **`permissions.allow` / `ask` / `deny`** and **hooks** refine behavior. `bypassPermissions` skips the permission layer entirely — do not use on developer laptops with valuable repos.

Official: [Choose a permission mode](https://code.claude.com/docs/en/permission-modes).
