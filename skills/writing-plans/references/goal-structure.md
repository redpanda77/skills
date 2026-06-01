# Goal Structure

The `goal.md` file is the execution contract for a plan. It is the single source of truth for scope, boundaries, and completion criteria.

## Structure

```markdown
<goal>
The task is complete only when:
1. Phase 1: ...
2. Phase 2: ...
</goal>

<context>
Repository:
  /path/to/repo

Important files/directories:
  - docs/plans/P{NN}-<name>/index.md (master plan)
  - docs/plans/P{NN}-<name>/P{NN}-AUDIT.md (current state audit)

Reference patterns:
  - Pattern name — brief description

Known current state:
  - Fact 1
  - Fact 2
</context>

<scope>
Phase 1 — Name

Allowed:
  - List of allowed changes

Not allowed:
  - List of forbidden changes

All phases:
  - Global constraints (e.g., "No committing without explicit request")
</scope>

<mandatory_first_steps>
Before editing:
1. Confirm working directory is `/path/to/repo`.
2. Inspect git status to protect unrelated local changes.
3. Read project guidance: `AGENTS.md` and `CLAUDE.md`.
4. Read this file (`goal.md`) as the execution contract.
5. Read `index.md` for execution order, KO links, and progress tracker.
6. Read the specific KO plan file before editing that KO.
</mandatory_first_steps>

<progress_tracking>
Use the "Execution Spine / Progress Tracker" table in `index.md`.

Before starting a KO:
  - Read that KO's plan file.
  - Identify the KO goal, scope, allowed changes, validation criteria.
  - Mark the KO status as `In progress` in the tracker.

Before checking off a KO:
  - Re-read that KO's validation section.
  - Run the KO's required validation commands.
  - Mark the KO checkbox only after the exit gate is satisfied.

If a KO cannot be completed:
  - Mark it `Blocked`.
  - Record the blocker in `DEVIATIONS.md` before moving on.
</progress_tracking>

<refactoring_protocol>
Execute each KO as a sequence of small green-to-green steps:

1. Baseline:
   - Record current git status.
   - Run the narrowest relevant baseline check.
   - If baseline fails, document whether failure is pre-existing.

2. Classify:
   - Label the next step: mechanical, boundary, or behavioral.

3. Map Impact:
   - For files with >5 consumers, run impact analysis.
   - Search for imports, dynamic imports, route references, tests, configs.
   - Identify update order: interfaces/types first, implementations second, callers third.

4. Change:
   - Make one coherent move at a time.
   - Update imports in the same change set as the file move.
   - Do not introduce compatibility wrappers unless explicitly required.

5. Verify:
   - Run narrowest check after each high-blast-radius move.
   - Any runtime behavior change is a failure unless the KO explicitly allows it.

6. Ledger:
   - Record moved, merged, deleted paths in the KO deletion ledger.
   - Record deviations in `DEVIATIONS.md`.

7. Repeat until the KO acceptance criteria pass.
</refactoring_protocol>

<implementation_requirements>
The agent must:
  - Treat deletion as the final step of a move, not the first step
  - Run impact analysis on any file with >5 consumers before moving
  - Move files atomically: update imports in the same operation
  - Preserve all runtime functionality for mechanical KOs
  - Document any deviation in `DEVIATIONS.md`

Do not:
  - Change business logic, function signatures, or component props
  - Delete non-empty directories based only on target tree expectations
  - Create empty directories just to match a template
  - Skip the pre-commit check
</implementation_requirements>

<deletion_safety_gate>
Before any deletion can be considered complete, produce a deletion ledger:

| Path | Action | Replacement / New Owner | Reference Check | Validation |
|------|--------|--------------------------|-----------------|------------|
| `old/path` | moved / merged / deleted-empty / deleted-dead | `new/path` or `none` | Search result | Command result |

Rules:
  - `deleted-empty`: only when `find <path> -type f` returns no files
  - `deleted-dead`: only when search shows zero consumers AND the KO explicitly lists the deletion
  - `moved`: new file must exist and old imports must resolve to new path
  - `merged`: requires side-by-side diff or written rationale
</deletion_safety_gate>

<verification_requirements>
The agent must verify completion with:
  - Build command — must pass or document pre-existing failures
  - Lint command — must pass with zero issues (or only documented pre-existing issues)
  - Impact analysis — must be run for all modified symbols
  - Deletion ledger — every deleted path has a replacement or zero-consumer proof
  - Manual inspection — verify structural correctness

If a command fails:
  - Determine whether it is caused by the agent's changes, pre-existing code, or missing environment.
  - Fix failures caused by the agent's changes immediately.
  - Document pre-existing or environment failures with exact output.
</verification_requirements>

<completion_contract>
The agent may stop only when:
1. All expected files exist / code changes are complete for the requested KO scope
2. All acceptance criteria for the specific KO pass
3. Verification commands have run and results are reported
4. Any blockers are documented with exact evidence
5. Final response contains required summary
</completion_contract>

<final_response_format>
Return:
  - Result: [SUCCESS / PARTIAL / BLOCKED]
  - Files changed: [list of moved/created/deleted files]
  - Verification run: [commands executed and their results]
  - Remaining blockers: [any issues that prevented full completion, with evidence]
  - Recommended next command: [what the user or next agent should do]
</final_response_format>
```

## Rules

- Every section must be present. Do not omit sections.
- The `<goal>` tag is the acceptance criteria. It is the contract.
- The `<context>` tag is the shared understanding. It prevents the agent from rediscovering known facts.
- The `<scope>` tag is the boundary. It prevents scope creep.
- The `<mandatory_first_steps>` tag is the pre-flight checklist.
- The `<refactoring_protocol>` tag is the how. Every KO must follow the same protocol.
- The `<implementation_requirements>` tag is the hard rules.
- The `<deletion_safety_gate>` tag is the safety check.
- The `<verification_requirements>` tag is the exit gate.
- The `<completion_contract>` tag is the stop condition.
- The `<final_response_format>` tag is the output format.
