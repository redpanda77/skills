# Philosophy

## The Harness Mindset

When the agent fails, ask: **what is missing from the harness?**

```
Agent failure
    |
    v
Ask: what was missing?
    |
    ├── missing context?      → add docs / AGENTS.md map / rules
    ├── missing tool?         → add script / MCP / validate.sh
    ├── missing constraint?   → add hook / permission / linter
    ├── missing feedback?     → add judge / test / CI
    └── repeated mistake?     → encode as skill / rule / cleanup task
```

## Core beliefs

1. **Humans steer; agents execute.** The engineer's job is setting goals, defining acceptance criteria, and improving the harness — not manually writing every line.
2. **The environment matters more than the prompt.** If the agent fails, the fix is not "prompt harder." The fix is: what tool, test, doc, or constraint is missing?
3. **Make everything legible to the agent.** Agents can only use what they can see. Code, docs, schemas, tests, and plans should live where the agent can access them.
4. **The repo becomes the system of record.** Use a short `AGENTS.md` as a map, not a giant manual. Put detailed architecture, specs, plans, and rules in structured repo docs.
5. **Prefer progressive disclosure.** Do not overload the agent with all context upfront. Give it a stable entry point (`CLAUDE.md`), then clear paths to deeper information when needed.
6. **Constraints beat taste comments.** Do not rely on repeated human review. Encode architecture, naming, logging, and quality rules into linters, tests, hooks, and repo-local tooling.
7. **Enforce invariants, not implementation details.** Be strict about boundaries, correctness, and observability. Allow flexibility inside those boundaries.
8. **Feedback loops create leverage.** Agents improve when they can run validation, inspect state, read logs, reproduce failures, and iterate without waiting for humans.
9. **Scripts are the completion authority.** `done-check.sh` decides when work is done. Claude does not decide.
10. **Scripts = deterministic only. Judge = qualitative only.** No overlap. No exceptions.
11. **Entropy is automatic; cleanup must be automatic too.** Agents copy existing patterns, including bad ones. Without recurring cleanup, drift compounds.
12. **High throughput + weak harness = chaos. High throughput + strong harness = leverage.**
