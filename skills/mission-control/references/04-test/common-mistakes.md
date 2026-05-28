# Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|--------------|-----|
| Claude decides it's done | Memory is not evidence | `done-check.sh` is the only authority |
| Content quality in scripts | Scripts cannot judge semantics | Move to judge subagent |
| Skipping the system skill | Next session has no manual | Hard gate: invoke `write-a-skill` |
| Embedding prompts in commands | Commands cannot be versioned | `.claude/agents/*.md` with frontmatter |
| Writing CLAUDE.md directly | Misses behavioral contract | Always use `writing-claude-md` |
| Python script renders judge prompt | Bypasses harness, creates parallel system | Invoke judge directly via `Agent` tool |
| Python script pre-packages judge context | Judge reads packaged evidence, not raw | Pass evidence directly in prompt or let judge read raw |
| Script rewrites judge output | Erases judge reasoning | Treat malformed as `invalid`, re-run judge |
| Qualitative language in scripts | Scripts pretend to judge | Reclassify as `needs_judge` or `mechanical_blocker` |
| Missing `category_assessments` | Judge verdict is not actionable | Require per-category status and rationale |
| Missing `recommended_next` | Router cannot auto-route | Require top-level field |
| No shared judge-state ingestion | Ad-hoc loading is inconsistent | Implement shared module |
| Invoking subagents as `Agents()` | Wrong API, will fail | Use `Agent` tool with `subagent_type` |
| Missing subagent frontmatter | Harness cannot load agent | Require `name`, `description`, optional fields |
| Trying to build a custom harness | Claude Code already is the runtime | Configure native surfaces instead |
| One giant CLAUDE.md | Crowds context, rots quickly | Use AGENTS.md as a map, docs as territory |
| Manual review instead of constraints | Repeated corrections waste time | Encode rules into hooks, tests, linters |
| No feedback loops | Agent cannot self-correct | Add tests, app runners, logs, observability |
