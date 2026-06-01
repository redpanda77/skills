# Worker Class Contracts

Scoped evidence language by worker class. Every agent reads a bounded evidence surface appropriate to its role.

## The core invariant

```text
Scope must be explicit, typed, and worker-class appropriate.
```

## The cross-surface invariant

```text
The files a worker is told to read, the files hooks authorize,
and the files the agent base prompt expects must be the same files.
```

Any mismatch is a pipeline bug. A scope change is incomplete until every surface is updated:

```text
renderer script -> authorization sidecar -> hook expectations -> routed handoff prompt -> subagent base prompt -> skill docs -> mirror sync -> tests
```

## Worker classes

| Worker Class | Read Scope | Write Scope | Evidence Surface |
|--------------|-----------|-------------|------------------|
| **Judge** | One typed context pack | One judgment file | `context_pack_v2` rows, indexes, risks |
| **Artifact** | Rendered prompt + one target-local context pack | One canonical artifact | Typed context pack |
| **Repair** | Rendered prompt + bounded repair evidence | One repaired artifact | Repair context pack + target artifact |
| **Planning** | Rendered prompt + compact source/catalog evidence | One plan artifact | Compact upstream evidence |
| **Escape** | Authorized control-layer files only | One control-layer patch | Router/hook/validator scripts |
| **Audit** | Read-only state and logs | One audit report | State, ledger, logs |

## Judge workers

Expected scope:

```text
read: one typed context pack
write: one judgment file
```

Allowed evidence:

- `context_pack_v2` rows
- indexes
- risks
- validation
- output contract
- context hash

Required language:

```text
Read exactly the context pack named by the routed prompt.
If required evidence is missing, return blocked_upstream and name the renderer
field that must be added. Do not browse raw artifacts, sidecars, source_paths,
plans, runtime state, hooks, settings, or sibling judgments.
```

Required hook/authorization alignment:

```text
read_scope: [the exact context pack path]
write_scope: [the exact judgment path]
```

## Artifact workers (canonical content)

Expected scope:

```text
read: rendered worker prompt + one target-local typed context pack
write: one canonical artifact
```

Mechanical pre-read of the output target is allowed only when the tool requires it before overwrite. That pre-read is not evidence.

Required language:

```text
Use the required typed context pack as the evidence surface.
Provenance source_paths are not a read list.
If the pack does not contain enough evidence to write the target, return
blocked_upstream and name the missing renderer field.
```

Required hook/authorization alignment:

```text
read_scope: [the exact typed context pack path]
mechanical_read_scope: [the output target, only if overwrite tooling requires it]
write_scope: [the exact output target]
```

## Repair workers

Expected scope:

```text
read: rendered repair prompt + bounded repair evidence
write: one repaired artifact
```

Repair workers may need more evidence than a judge or content worker. That evidence must be explicitly scoped by the renderer.

Allowed repair evidence examples:

- current target artifact
- bounded repair context pack
- compact failure summary
- schema skeleton and field type rows
- target plan row
- relevant child summaries
- immediate neighbor summaries
- a bounded scaffold file for legality checks

Forbidden by default:

- full raw plans
- full source catalogs
- full graph views
- full canonical sibling directories
- raw diagnostics logs
- runtime state
- authorization sidecars
- hooks and settings

Required language:

```text
Read exactly the files listed by the rendered repair prompt.
Repair prompts may include a bounded repair context pack and, when needed, the
target artifact or bounded scaffold file.
Do not browse raw plans, sibling artifacts, diagnostics, source_paths, or
runtime files unless the rendered prompt lists that exact file.
If listed evidence is insufficient, return blocked_upstream and name the missing
repair context field.
```

## Planning workers

Expected scope:

```text
read: rendered prompt + compact source/catalog evidence or typed planning pack
write: one plan artifact
```

Planning happens before many downstream packs exist, so planning workers may need compact upstream source evidence. This does not authorize downstream canonical browsing.

Required language:

```text
Use compact source/catalog evidence and typed planning rows as the planning
surface. Write a thin grouping/ordering contract. Do not generate downstream
canonical content inside the plan.
```

## Escape workers

Expected scope:

```text
read: authorized control-layer files only
write: one control-layer patch
```

Escape workers run only during Escape Protocol. They cannot write canonical artifacts, judge principles, or acceptance criteria.

Allowed:

- router scripts
- hook scripts
- validator scripts
- prompt renderers
- authorization sidecars

Forbidden:

- canonical artifacts
- judge principles
- acceptance criteria
- runtime state (unless fixing state corruption)

## Parent orchestrator

Expected scope:

```text
read: router card only
execute: routed run field
delegate: exact subagent and handoff prompt
```

The parent must not inspect worker prompts, context packs, sidecars, targets, or diagnostics to construct delegation. The router decides the next action; the parent executes it.

## Rules

- Bounded evidence != always one file
- Bounded evidence != raw artifact browsing
- Missing evidence is a renderer/handoff defect, not a worker failure
- Workers do not discover raw files by prose reasoning
- Workers do not work around hooks by reading adjacent files
- Every scope change must update all contract surfaces in the same change set
