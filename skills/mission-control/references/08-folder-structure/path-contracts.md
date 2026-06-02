# Path Contracts

What Claude can edit, what hooks protect, and what lives in each directory.

## The authority table

| Location | Tier 1 | Tier 2 | Tier 3 |
|----------|--------|--------|--------|
| `src/`, `tests/`, `docs/` | ✓ | ✓ | ✓ |
| `AGENTS.md` | ✓ | ✓ | ✓ |
| `CLAUDE.md` | ✓ | ✓ | ✓ |
| `.mission-control/PLAN.md` | ✓ | ✓ | ✓ |
| `.mission-control/CLOSED_TASKS.md` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/validation-manifest.json` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/done-check.sh` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/validate-*.sh` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/close-task-check.sh` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/run-agent.sh` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/state.json` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/judge-principles.md` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/hidden-tests/` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/judge-verdicts/` | ✓ | ✗ (hook) | ✗ (hook) |
| `.mission-control/closure-records/` | ✓ | ✗ (hook) | ✗ (hook) |
| `.claude/settings.json` | ✓ | ✗ (hook) | ✗ (hook) |
| `.claude/commands/*.md` | ✓ | ✗ (hook) | ✗ (hook) |
| `.claude/agents/*.md` | ✓ | ✗ (hook) | ✗ (hook) |
| `.claude/skills/*.md` | ✓ | ✗ (hook) | ✗ (hook) |
| `.claude/hooks/*.sh` | ✓ | ✗ (hook) | ✗ (hook) |

**Legend:** ✓ = Claude can edit | ✗ (hook) = hook blocks edit

## Why paths are protected

| File | If Claude edits it | Risk |
|------|--------------------|------|
| `CLOSED_TASKS.md` | Reopens closed tasks, hides regressions | Repeated work, false progress |
| `validation-manifest.json` | Removes validations, weakens gates | Undetected failures |
| `done-check.sh` | Makes done-check always pass | Premature completion |
| `validate-*.sh` | Removes checks, weakens tests | Broken code ships |
| `state.json` | Fakes state, hides blockers | Routing errors, lost work |
| `.claude/hooks/*.sh` | Disables guardrails | Unblocked destructive actions |
| `.claude/agents/*.md` | Changes judge criteria mid-flight | Inconsistent evaluation |
| `judge-principles.md` | Relaxes principles | Lower quality bar |
| `hidden-tests/` | Worker sees tests, games criteria | Criterion gaming |

## The path contract rules

1. **Canonical content is always editable.** `src/`, `tests/`, `docs/` are never protected.
2. **Intent files are always editable.** `AGENTS.md`, `CLAUDE.md` are never protected.
3. **Plan is always editable.** `.mission-control/PLAN.md` is never protected.
4. **Validation authority is always protected.** `done-check.sh` and sub-validators are protected by hooks.
5. **State is always protected.** `.mission-control/` is protected by hooks in all tiers.
6. **Hooks are always protected.** `.claude/hooks/` is protected by hooks.
7. **Agent definitions are protected in Tier 2+.** `.claude/agents/` cannot be edited mid-flight.
8. **Hidden tests are protected in Tier 3.** `.mission-control/hidden-tests/` is protected by hooks.

## What to do when a hook blocks valid work

1. Confirm the router's exact next action is correct.
2. Check whether the rendered prompt names the expected target.
3. Fix the narrow mismatch in the route, prompt, context pack, or subagent handoff.
4. Do not bypass the hook. If the hook is genuinely wrong, use Escape Protocol.

## Escape Protocol for path conflicts

When the control system itself is wrong — a hook blocks correct work, a validator has a false positive, or the pipeline is stuck — use Escape Protocol:

- Requires explicit user authorization or a router-classified `control_failure` state.
- Repairs are limited to control-layer artifacts: router, hooks, validators, prompt renderers.
- Canonical content, judge principles, and acceptance criteria are NOT changed.
- After control repair, the system re-runs the router and resumes normal workflow.

See `references/00-introduction/system-architecture/hooks.md` for full Escape Protocol rules.
