# Testing adherence

The only reliable way to know whether a CLAUDE.md is working is to test it.

## The test suite (5 representative prompts)

1. **New API endpoint** — exercises architecture rules, security rules, validation.
2. **Add tests for an existing function** — exercises test framework rules, factory/mock rules.
3. **Create a database migration** — exercises human-approval rules, scope rules.
4. **Security-adjacent change** (auth, payments, PII) — exercises escalation, `IMPORTANT` markers.
5. **Small bug fix in an existing file** — exercises "stay in scope", "don't refactor unrelated code".

## Procedure

1. Start a fresh Claude Code session in the repo.
2. Run `/memory` to confirm the file is loaded.
3. Run each prompt and capture the output.
4. Review every output against CLAUDE.md rules.

## Diagnosing violations

For each rule Claude violated:

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Violated across multiple prompts | Rule is unclear, too long, or buried | Rewrite as imperative; move higher in file |
| Violated only sometimes | Conflicts with another rule | Read top-to-bottom for contradictions |
| Followed in chat, violated in code | Rule is prose, not verifiable | Convert to runnable command |
| Mentioned once, then forgotten | Buried below line 100 | Move to first 40 lines or compress preceding content |

## Before/after compression

Run the same 5 prompts against the original file and the compressed version.

- Equivalent or better adherence with less context → compression worked.
- Missing rules from original → identify the load-bearing line and restore in compressed form.

## When to retest

- After any CLAUDE.md change.
- Quarterly during pruning review.
- After any incident where the agent contributed.
- When the user upgrades models (instruction-following characteristics change).
