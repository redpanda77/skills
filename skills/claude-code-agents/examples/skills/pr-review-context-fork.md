---
name: pr-review-context-fork
description: Use when reviewing a pull request in isolation so diffs and search noise stay out of the main conversation. Returns severity-ranked findings with evidence.
context: fork
---

# PR review (forked)

## Preconditions

- Branch name or PR number available
- Test command known or inferable

## Steps

1. Collect the smallest diff that answers the review (`git diff`, `gh pr diff`, or equivalent).
2. Cross-check touched areas for tests and docs updates.
3. Scan for security-sensitive edits (auth, crypto, parsing).

## Return format

- `Overview`
- `Findings` (severity, path, evidence, fix)
- `Tests / coverage gaps`
- `Suggested follow-ups`
