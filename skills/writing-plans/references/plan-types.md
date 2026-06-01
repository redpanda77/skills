# Plan Types

Different types of plans require different structures and emphases. Choose the type that matches your project.

## Reorganization Plan

For restructuring code, moving files, consolidating directories, and establishing boundaries.

**Key characteristics:**
- Heavy on KOs (knockout files) for mechanical moves
- Requires deletion ledgers for every deleted path
- Requires impact analysis before any move
- Validates with build/lint commands

**Example structure:**
- P{NN}-K01: Foundation components
- P{NN}-K02: Feature extraction
- P{NN}-K03: Storage infrastructure
- P{NN}-K04: Import boundary enforcement

**See:** `references/reorganization-plan.md`

## Theming Plan

For migrating colors, design tokens, typography, spacing, or visual systems.

**Key characteristics:**
- Heavy on audit and coverage mapping
- Requires token taxonomy before component migration
- Validates with visual audits (light mode identity, dark mode legibility)
- Requires lint rules for drift detection

**Example structure:**
- P{NN}-00: Audit baseline and scope
- P{NN}-01: Theme contract (tokens)
- P{NN}-02: Runtime infrastructure
- P{NN}-03: Core tokens and primitives
- P{NN}-04: Feature surface migration

**See:** `references/theming-plan.md`

## Feature Plan

For adding new functionality, APIs, or user-facing features.

**Key characteristics:**
- Heavy on design documents and acceptance criteria
- Requires API contracts and type definitions
- Validates with functional tests and user acceptance criteria
- May include A/B test plans or rollout strategies

**Example structure:**
- P{NN}-00: Requirements and scope
- P{NN}-01: Design and API contract
- P{NN}-02: Core implementation
- P{NN}-03: Integration and edge cases
- P{NN}-04: Testing and validation
- P{NN}-05: Rollout and monitoring

**See:** `references/feature-plan.md`

## Audit Plan

For code quality audits, security reviews, or technical debt assessments.

**Key characteristics:**
- Heavy on findings and evidence
- Requires severity classification (Critical, High, Medium, Low)
- Validates with remediation verification
- May include recurring checks

**Example structure:**
- P{NN}-00: Audit scope and methodology
- P{NN}-01: Findings by category
- P{NN}-02: Remediation plan
- P{NN}-03: Verification and sign-off

**See:** `references/audit-plan.md`

## Rules

- Choose the plan type before writing the goal
- The plan type determines the KO structure and validation approach
- Reorganization plans require deletion ledgers and impact analysis
- Theming plans require token taxonomy and visual audits
- Feature plans require acceptance criteria and rollout plans
- Audit plans require severity classification and evidence
