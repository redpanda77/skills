# Local File Structure

## Clean Repo Layout

```
repo/
  .agents/
    skills/
      pr-review/
        SKILL.md
        references/
          review-rubric.md
        scripts/
          collect_diff.sh
        assets/

      bug-repro/
        SKILL.md
        scripts/
          repro.sh

  .codex/
    config.toml

    agents/
      pr_explorer.toml
      reviewer.toml
      test_planner.toml
      docs_researcher.toml

    hooks.json
    hooks/
      pre_tool_use_policy.py
      post_tool_use_review.py
      stop_validate.py
      subagent_start_context.py
```

## Path Separation

| Layer | Path | Purpose |
|-------|------|---------|
| Skills | `.agents/skills/*` | Reusable workflows |
| Agents | `.codex/agents/*.toml` | Custom subagent definitions |
| Hooks | `.codex/hooks.json` | Lifecycle scripts config |
| Hook scripts | `.codex/hooks/*` | Hook implementation code |
| Config | `.codex/config.toml` | Codex config, agent and hook settings |

## Discovery Rules

- **Skills:** Scanned from cwd upward to repo root in `.agents/skills/`, plus `~/.agents/skills/`, `/etc/codex/skills/`, and bundled system skills.
- **Agents:** Loaded from `repo/.codex/agents/*.toml` and `~/.codex/agents/*.toml`.
- **Hooks:** Loaded from active config layers: `repo/.codex/hooks.json`, `repo/.codex/config.toml`, `~/.codex/hooks.json`, `~/.codex/config.toml`.

## Important Notes

- Use absolute paths or `git rev-parse --show-toplevel` in hook commands. Avoid fragile relative paths because Codex may start from a subdirectory.
- Skills themselves do not bypass Codex permissions. Scripts run only if the sandbox and approval settings allow the relevant command.
