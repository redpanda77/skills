# System Components

A multi-agent pipeline is a compiler, not a chat. It has a data layer, an orchestration layer, an execution layer, a control layer, and a communication protocol between them.

## The Core Components

```
Source/Graph           ← evidence layer (input)
    ↓
Router                 ← orchestration brain
    ↓
Agents                 ← model execution
    ├── Workers          → generate artifacts
    └── Judges           → evaluate quality
    ↓
Validation             ← deterministic checks
State/Ledger           ← tracking and manifests
    ↓
Export/Render          ← output materialization
```

**Control:** Hooks enforce route, worker, and protected-path rules.
**Entrypoint:** Skills and commands define the operator contract (`/curriculum`, etc.).
**Protocol:** Context packs are the typed communication interface between router, agents, and validation.

## The Data Flow

In the system's own language:

```
Sources
  → normalized facts
  → planning hypothesis (model-authored)
  → planning judgment (agent-evaluated)
  → tiered graph views (deterministic normalization)
  → tiered plans
  → canonical units
  → judge decisions
  → consumer-facing output
  → audit / acceptance
```

Every phase produces an artifact that the next phase consumes. The router decides which phase runs next.

## Why each component exists

| Component | Purpose | If it fails |
|-----------|---------|-------------|
| **Source/Graph** | Provides the evidence and facts that feed the pipeline | The router has nothing to route; agents hallucinate |
| **Router** | Decides the next legal action; prevents agent improvisation | Agents wander, skip steps, or loop |
| **Workers** | Generate one bounded artifact at a time | Scope creep; agents try to write the whole pipeline |
| **Judges** | Evaluate quality against principles | Bad output passes; no feedback loop |
| **Validation** | Check mechanical facts deterministically | Schema violations, missing files, broken hashes |
| **State/Ledger** | Track what passed, what failed, what's next | Repeated work, stale artifacts, lost progress |
| **Export/Render** | Materialize the final output | No deliverable; build artifacts are invisible |
| **Hooks** | Enforce constraints and guardrails | Destructive commands, premature exit, off-route work |
| **Skills/Commands** | Define the operator contract and entrypoint | No way to invoke the system; inconsistent protocol |
| **Context Packs** | *Protocol*, not component. Typed, bounded evidence interface between router, agents, and validation | Oversized dumps, repeated objects, agent confusion |

## The Bounded Decision Test

A good design passes this test:

- Can an agent understand the next action in under 30 lines of context?
- Can a human find the final output without opening build artifacts?
- Can a judge evaluate one target without reading the whole project?
- Can a repair change one bounded unit without rewriting huge files?
- Can the project be audited from summaries and pointers?

If any answer is no, the harness is missing a component or a boundary.

## Component vs. Protocol

Components are systems. Protocols are interfaces between them.

- **Router**, **Agents**, **Validation**, **State**, **Export** are components.
- **Context Packs** are the protocol that carries evidence between them. They are not a standalone system; they are the typed interface that makes the components composable.

## Detailed Breakdown

Read the detailed architecture documents in `system-architecture/`:

- [`system-architecture/source-and-graph.md`](system-architecture/source-and-graph.md) — the evidence layer
- [`system-architecture/router.md`](system-architecture/router.md) — orchestration and routing
- [`system-architecture/agents.md`](system-architecture/agents.md) — workers and judges
- [`system-architecture/validation.md`](system-architecture/validation.md) — deterministic checks
- [`system-architecture/state-and-ledger.md`](system-architecture/state-and-ledger.md) — tracking and manifests
- [`system-architecture/export-and-render.md`](system-architecture/export-and-render.md) — output materialization
- [`system-architecture/hooks.md`](system-architecture/hooks.md) — guardrails and constraints
- [`system-architecture/entrypoints.md`](system-architecture/entrypoints.md) — skills and commands

Read the protocol documentation in `06-context-packs/`:

- [`06-context-packs/README.md`](../06-context-packs/README.md) — context pack discipline overview
- [`06-context-packs/typed-context-packs.md`](../06-context-packs/typed-context-packs.md) — schema standard
- [`06-context-packs/planning-content-boundaries.md`](../06-context-packs/planning-content-boundaries.md) — plan vs canonical content
- [`06-context-packs/input-output-scope.md`](../06-context-packs/input-output-scope.md) — broad vs deep scope
- [`06-context-packs/validation-and-budgets.md`](../06-context-packs/validation-and-budgets.md) — hard rules and budgets
- [`06-context-packs/content-evidence-pattern.md`](../06-context-packs/content-evidence-pattern.md) — row-local evidence, ID alignment, and migration rules
