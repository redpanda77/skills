# 10-point CLAUDE.md audit checklist

Run for every audit.

- [ ] Root file is under 120 lines and readable in under 90 seconds.
- [ ] All build, test, lint, and migration commands are current and runnable. (Ask the user to verify each.)
- [ ] Security rules are stated as imperatives. `IMPORTANT` markers only on the truly critical ones.
- [ ] "Human Approval Required" section exists as an explicit checklist.
- [ ] No secrets, tokens, API keys, or environment-specific values anywhere in the file.
- [ ] Architecture section reflects current state — not historical, deprecated, or aspirational.
- [ ] Folder-specific rules live in nested `CLAUDE.md` files, not the root.
- [ ] `CLAUDE.local.md` is gitignored and referenced in onboarding docs.
- [ ] Reviewed and pruned within the last 90 days; `/memory` run and duplicates removed.
- [ ] If multi-tool: tool-specific files (Copilot, Cursor, Windsurf) sync with canonical `AGENTS.md`.

## Per-line test

For every line in CLAUDE.md, ask:

> If I removed this line, would Claude make a specific mistake I have actually seen?

- **Yes** → keep.
- **No / maybe** → delete or move to a reference doc.

## Per-rule tests

- **Testable?** Can you tell from a PR whether Claude followed it?
- **Imperative?** Direct command, not suggestion?
- **Specific?** Names the file/folder/command, not a vague concept?
- **Non-contradictory?** No other rule in the file says the opposite?
