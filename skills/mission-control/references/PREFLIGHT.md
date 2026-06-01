# Preflight Checklist

Run this before every session or before any significant work. The preflight is the validator's first line of defense — it catches harness corruption, stale state, and misconfiguration before they compound into failures.

## What this is

A checklist that verifies the harness is in a known-good state. Not a substitute for `done-check.sh` or the judge. This is the **environment health check**.

## When to run

- Start of every session
- After any harness configuration change
- After any crash or recovery
- Before spawning a judge or worker subagent
- When context packs seem wrong or oversized

---

## 1. Context Pack Integrity

Context packs are the protocol interface. If they are broken, everything downstream is broken.

- [ ] `schema_version` is `context_pack_v2` on every pack
- [ ] `pack_kind` is one of the allowed kinds (`plan_worker`, `plan_grouping_judge`, `unit_judge`, `batch_judge`, `scope_judge`)
- [ ] Root keys are exactly the allowed set (no unknown keys)
- [ ] Every pack is under its kind's hard budget (see `06-context-packs/validation-and-budgets.md`)
- [ ] Nesting depth is within the kind's limit
- [ ] No repeated embedded entities (`rows[].member_details[]` or similar must fail)
- [ ] No canonical content in plan artifacts (no `dialogues`, `exercises`, `examples`, `member_details`)
- [ ] `rows` + `indexes` pattern is used (no scattered ID maps, no full-content rows)
- [ ] `input_hashes.source_paths` and `source_hashes` are present on every pack
- [ ] `context_pack_hash` is present and matches the content
- [ ] File paths follow the organization invariant (`pack_kind/target_id.json`)
- [ ] No stale packs (source hash matches current file)
- [ ] Closed packs have not been bulk-regenerated (judge hashes are stable)

## 2. Router Health

The router is the workflow authority. If it is broken, agents wander.

- [ ] Router script exists and is executable
- [ ] Router produces valid JSON output
- [ ] `action` field is one of `delegate | validate | repair | render | accept`
- [ ] `target` field is present and references a real artifact
- [ ] `requires_worker` matches an existing agent
- [ ] `prompt_path` and `context_pack_path` exist and are readable
- [ ] No `loop_risk` classifications are active
- [ ] No `control_failure` state unless Escape Protocol is authorized
- [ ] The `then` field is an observation command, not permission to continue
- [ ] The router does not chain multiple actions in one output

## 3. Agent Contracts

Workers and judges must have bounded, correct contracts.

- [ ] All worker subagents have YAML frontmatter with `name`, `description`, `tools`
- [ ] All worker subagents declare read surfaces and write surfaces
- [ ] All worker subagents have a forbidden-write list
- [ ] All judge subagents have `principles` defined
- [ ] Judge principles are 5-10 per judge, each falsifiable
- [ ] Judge output format matches the contract (`verdict`, `confidence`, `principle_scores`, `must_fix`, `should_fix`, `evidence`, `concerns`)
- [ ] Judge `threshold` is present and consistent across all judges
- [ ] No worker is also a judge (no collapsed roles)
- [ ] Worker authorization sidecar exists (prompt path, hash, allowed reads, write path)
- [ ] `subagent_type` is used for custom agents, not generic prompts

## 4. State and Ledger

State tracks what passed, what failed, what's next. If it is corrupted, work repeats or is lost.

- [ ] `state.json` exists and is valid JSON
- [ ] `current_task` is present and references a real open task
- [ ] `last_completed_task` is present and references a closed task
- [ ] `last_verification` timestamp is recent (not stale)
- [ ] `last_verification_result` is `pass` or `fail`
- [ ] `blockers` array is empty or contains actionable items
- [ ] Delegation ledger exists and is append-only
- [ ] Acceptance manifest exists and records all passed tasks
- [ ] Scope registry shows correct status for each scope (open, closed, blocked)
- [ ] No closed scope has been reopened without router authorization
- [ ] Closed batch hashes match the judge hashes that approved them

## 5. Validation Stack

Validators are deterministic and must be complete.

- [ ] `done-check.sh` exists and is executable
- [ ] `validate-global.sh` exists (tests, lint, typecheck)
- [ ] `validate-no-blockers.sh` exists
- [ ] `validate-closed-tasks.sh` exists (Tier 2+)
- [ ] `validate-no-tampering.sh` exists (Tier 2+)
- [ ] `validate-context-pack.py` exists (Tier 2+)
- [ ] `close-task-check.sh` exists
- [ ] All validators produce silent success, loud failure
- [ ] No qualitative heuristics in any validator script
- [ ] Validator stack is wired correctly in `done-check.sh`

## 6. Hooks and Constraints

Hooks enforce the rules. If they are missing or broken, the system is unprotected.

- [ ] `stop-if-not-done.sh` is installed and active
- [ ] `block-dangerous.sh` is installed and active
- [ ] `protect-control-files.sh` is installed and active (Tier 2+)
- [ ] `worker-boundary-guard.sh` is installed and active (Tier 2+)
- [ ] `session-start-reminder.sh` is installed and active
- [ ] `post-compact-audit.sh` is installed (Tier 2+)
- [ ] `task-sync-guard.sh` is installed (Tier 2+)
- [ ] Hooks are wired in `.claude/settings.json`
- [ ] No hook has been bypassed or edited during normal execution
- [ ] No hook has been disabled without Escape Protocol authorization

## 7. Source and Graph

The evidence layer is the ground truth. If it is broken, the pipeline hallucinates.

- [ ] Source files exist and are readable
- [ ] Graph views are deterministic and up to date
- [ ] Source hashes match the current files
- [ ] No source file has been edited without regenerating dependent packs
- [ ] Element graph is consistent with source graph
- [ ] Scope graph shows complete coverage
- [ ] No orphaned elements (elements in source but not in any graph view)

## 8. Export and Output

The final output must be materialized and consistent.

- [ ] `build/canonical/` directory exists with canonical units
- [ ] `build/plans/` directory exists with grouping contracts
- [ ] `out/` directory exists with consumer-facing output
- [ ] Output is deterministic (not model-authored)
- [ ] Output format is consistent and complete
- [ ] No stale build artifacts are mistaken for final output
- [ ] Human-readable output is findable without opening build artifacts

## 9. Skills and Commands

The operator interface must be consistent. Skills encode knowledge; commands invoke it.

### Skills

- [ ] **System skill** exists in `.claude/skills/` — the operating manual for the harness itself
- [ ] **Domain skill(s)** exist in `.claude/skills/` — specialized knowledge for the actual work domain (e.g., React, curriculum, data pipelines)
- [ ] System skill lists available domain skills and when to use them
- [ ] Domain skills are loaded on demand via `skills:` in subagent frontmatter
- [ ] Skills are not a replacement for docs; they are the docs, encoded

### Commands

- [ ] All commands exist in `.claude/commands/`
- [ ] Commands are thin shims (load skills, not duplicate logic)
- [ ] `/close-task` loads the system skill
- [ ] `/run-judge` spawns the judge subagent via `Agent` tool
- [ ] `/mc-status` shows current state
- [ ] `/mc-recovery` handles crash recovery

### The difference

| | System Skill | Domain Skill |
|---|---|---|
| **What it teaches** | How to use this harness | How to do the actual work |
| **When it loads** | Every session | On demand per task |
| **What it contains** | Commands, rules, workflows, preflight | Domain patterns, conventions, procedures |
| **Can it invoke agents?** | Yes (router, judge, worker) | Yes (specialized subagents) |
| **Is it a hard gate?** | Yes — never skip | No — create as needed |
| **Example** | "How to close a task in this repo" | "How to write a React component in this repo" |

## 10. Escape Protocol Readiness

The control system must be able to repair itself.

- [ ] Escape Protocol is documented and known to operators
- [ ] Control repair workers are defined (restricted tool access)
- [ ] Router can classify `control_failure` state
- [ ] Doctor script exists and is deterministic
- [ ] No control system repair has been attempted without authorization
- [ ] All control-layer changes are logged and auditable

---

## Running the Preflight

Run each section in order. If any item fails, do not proceed. Fix the issue first.

```bash
# Example: preflight script
python3 preflight.py \
  --context-packs-dir .context-packs/ \
  --state-file .mission-control/state.json \
  --validators-dir scripts/ \
  --hooks-dir .claude/hooks/
```

## Failure Handling

| Failure | Action |
|---------|--------|
| Context pack fails schema | Stop. Fix renderer. Do not trim to pass. |
| Context pack exceeds budget | Stop. Fix renderer. The budget is the contract. |
| Router produces invalid JSON | Stop. Fix router script. |
| `loop_risk` active | Stop. Run Escape Protocol. |
| State file corrupted | Stop. Run recovery from traces. |
| Judge hash mismatch | Stop. Do not re-judge closed packs. Audit the change. |
| Hook missing or bypassed | Stop. Reinstall via `claude-code-hooks` skill. |
| Validator missing | Stop. Create validator before proceeding. |
| Source hash mismatch | Stop. Regenerate dependent packs. |

## Rule

**The preflight is not optional.** If you skip it and the system fails, the failure was predictable. Every skipped check is a failure mode you chose to ignore.
