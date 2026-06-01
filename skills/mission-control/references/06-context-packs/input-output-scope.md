# Input / Output Scope Discipline

## The Fundamental Asymmetry

Broad-scope work and deep-scope work have opposite context requirements. Mixing them is the primary cause of oversized packs and agent drift.

## Broad Scope: Plans, Grouping, Sequencing

**Rule:** Minimal detail. Only the spine.

A broad-scope agent sees:
- IDs of all units in its tier
- Boundaries and ordering rationale
- Risk flags and coverage gaps
- Compact member lists (not member details)

It does NOT see:
- Full content of downstream units
- Phrases, dialogues, examples
- Detailed metadata objects
- Raw source excerpts

**Why:** The agent's job is to decide how things group and sequence, not to generate or preview content. Extra detail distracts from the grouping decision and creates implicit pressure to evaluate or rewrite content.

## Deep Scope: Canonical Content

**Rule:** One unit at a time. Full detail.

A canonical worker sees:
- The exact target unit it must generate
- Relevant upstream context (prerequisites, dependencies)
- The schema and output contract
- Selected evidence, not the full upstream corpus

It does NOT see:
- The full plan for all other units
- The full corpus of other units
- Judge feedback for other units

**Why:** Generating detailed content requires focus. The agent must not try to harmonize across units or preview future work. One target, one output, done.

## Judging: Batched but Compact

**Rule:** Judges can evaluate batches, but the pack must be a compact evidence surface.

A judge pack contains:
- A spine of the units being judged (IDs, titles, minimal metadata)
- Risk rows with targeted evidence references
- Selected snippets, not full content
- The principle set and scoring rubric

It does NOT contain:
- Full content of every unit being judged
- Full downstream preview
- Raw source excerpts
- Arbitrary prose dumps

**Why:** A judge evaluates quality against principles. It needs enough evidence to score, but not so much that it re-reviews instead of scoring. The pack should surface the evidence that matters for the principle, not everything.

## The Context Window is Not Infinite

Even with large context windows, oversized packs cause:
- Slower reasoning
- Agent drift into irrelevant details
- Repeated evidence creating false confidence
- Confusion between plan and canonical content

**The budget is the contract.** If the pack exceeds the budget, the design is wrong — not the trimming logic.

## Applying the Discipline

1. **When designing a renderer:** decide the scope first. Is this broad or deep? Choose the pack kind and budget accordingly.
2. **When writing a prompt:** explicitly state what the agent must NOT do. Negative contracts are as important as positive ones.
3. **When validating:** check for forbidden fields. A plan containing canonical content is a schema violation, not a style issue.
4. **When routing:** send only the pack kind the agent expects. Do not send a full-context dump to a judge that expects a compact spine.
