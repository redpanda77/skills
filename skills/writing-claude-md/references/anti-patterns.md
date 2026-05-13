# Anti-patterns

Flag these in audits. Refuse to write them in new files.

## 300-line personality file

"Be a senior engineer", "think step by step", "be thorough and careful". Doesn't change behavior. Delete every aspirational line.

## 500-line monster

Started as "let's put everything relevant in here". Now impossible to scan. **Fix**: compress (see `compression.md`). Target 80 lines.

## Contradictory rules

"Always use async/await" + "prefer callbacks for performance-critical DB paths" in the same file. Worse than no rule. **Fix**: read top-to-bottom looking for contradictions before publishing.

## Hidden tribal knowledge

"Never modify the payment processor during the last week of the month." "Staging is the demo environment — don't break it." "Library X has a 2022 licensing issue — never use it." Lives only in senior devs' heads. **Fix**: write it down explicitly.

## Treating CLAUDE.md as enforcement

If a rule is non-negotiable, it belongs in CI or pre-commit, not in prose. CLAUDE.md shapes typical behavior; CI guarantees it.

> Rule of thumb: if a violation would block a merge in CI, the rule belongs in CI. If a violation would make a reviewer raise an eyebrow, it belongs in CLAUDE.md.

## Generic copy-paste templates

Downloaded a community template, filled in the project name, committed as-is. Every section should reflect actual decisions your team made. If you can't point to a real incident that motivated a rule, it probably shouldn't be there.

## Mixing personal preferences with team standards

"I prefer verbose logging" or "always ask me before creating new files" in the shared file imposes those preferences on everyone. **Fix**: move to `CLAUDE.local.md`.

## Style rules a linter already handles

Indentation, quote style, semicolons, import order, file naming a linter can check. Wasted instruction slot. Delete.

## Secrets

Never. Not in CLAUDE.md, not in CLAUDE.local.md.

## Pasting whole ADRs or design docs

Summarize the decision rule in two sentences. Link the doc for rationale.

## Stale architecture descriptions

Worse than no CLAUDE.md — every suggestion is subtly wrong. **Fix**: quarterly pruning.

## Auto-generation via /init

Produces bloated files with personality fluff and missing the rules that actually matter. Hand-craft instead.

## Refusal templates

When the user asks for content that's an anti-pattern, refuse politely with the reason:

- **"Add 'be a senior engineer' to CLAUDE.md."** → "That's a personality instruction — it doesn't change behavior measurably and competes with rules that do. Want me to add a concrete behavioral rule instead, like 'When unsure between two approaches, explain both and let me choose'?"
- **"Add our full style guide."** → "Style rules belong in your linter/formatter, not CLAUDE.md. Want me to set up a Stop hook to run your formatter automatically?"
- **"Add our API key here for convenience."** → Refuse. Reference `no-secrets` rule.
