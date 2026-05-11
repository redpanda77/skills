# Tolaria file format

The contract that every Tolaria-compatible note follows. Tool-agnostic — works in plain Obsidian, vanilla markdown viewers, or the Tolaria app.

## Atomic rules

1. **One Markdown note per file.** No exceptions.
2. **YAML frontmatter** between `---` fences at the top of every note. Even minimal: `type:` alone is fine.
3. **First H1 in the body is the display title.** Don't add `title:` to new notes (legacy fallback only).
4. **Filenames are kebab-case.** Stable IDs for cross-linking — never rename casually.
5. **`type:` is required.** Every note declares its type.

## Frontmatter format

```yaml
---
type: <TypeName>                       # Required. Capitalized.
date: YYYY-MM-DD                       # Where applicable
status: <StatusValue>                  # Where applicable
related_to:                            # Multi-value relationships → YAML list
  - "[[other-note]]"
  - "[[another-note]]"
owner: "[[person]]"                    # Single-value relationship → quoted string
url: https://example.com               # Bare strings for non-relationship scalars
---
```

Rules:
- Wikilinks **in frontmatter** must be quoted: `"[[name]]"`.
- Wikilinks in the body are bare: `[[name]]`.
- Lists with `-` indentation for multi-value.
- Scalars unquoted unless they contain colons, brackets, or wikilinks.
- Dates always `YYYY-MM-DD` (ISO).

## Wikilinks

- `[[filename]]` — link by the target's filename (no `.md` extension).
- `[[Note Title]]` — link by the H1 display title.
- `[[filename|display text]]` — link with alternate label.

Works in both frontmatter (quoted) and body (bare). Don't use markdown links (`[text](path.md)`) for vault-internal references.

## Underscore-prefixed keys

Frontmatter keys starting with `_` are **Tolaria-managed app state**. Examples:

- `_organized: true` — Tolaria's internal sort flag
- `_icon: rocket` — type display icon
- `_color: "#3b82f6"` — type display color
- `_order: 0` — type ordering in sidebars
- `_list_properties_display:` — which fields appear in list view
- `_sort: "property:onboarding:asc"` — default sort for views of this type

**Never modify underscore keys unless explicitly editing type-definition or view config.** They round-trip through the app and your edits will be overwritten.

## Type definitions

Type-definition files live at the **vault root**. They are regular notes with `type: Type` set in their own frontmatter.

```yaml
---
type: Type
_icon: rocket
_color: "#3b82f6"
_order: 0
_list_properties_display:
  - status
  - owner
  - related_to
_sort: "property:status:asc"
---

# Initiative

Epic-level product work spanning multiple features.
```

The H1 is the type name. The body explains the type's purpose.

When editing an existing type file, **preserve the key style already used** (underscored or not) — don't mass-normalize.

## Views

Saved views live in `views/*.yml`. The filename is the stable view ID — use kebab-case (`active-initiatives.yml`).

```yaml
name: Active Initiatives
icon: null
color: null
sort: "property:priority:asc"
filters:
  all:
    - field: type
      op: equals
      value: Initiative
    - field: status
      op: equals
      value: Active
```

Rules:

- `name` is **required**. `icon`, `color`, `sort` are optional.
- `filters` root must be **exactly one** `all:` group or `any:` group.
- Each condition: `field`, `op`, `value`.
- `field` can target built-ins (`type`, `status`, `title`, `favorite`, `body`) or any frontmatter key in the vault.
- Operators: `equals`, `not_equals`, `contains`, `not_contains`, `any_of`, `none_of`, `is_empty`, `is_not_empty`, `before`, `after`.
- `any_of` / `none_of` expect `value:` to be a YAML list.
- `regex: true` works with `equals`, `not_equals`, `contains`, `not_contains`.
- Relationship filters can use wikilinks in `value:` — e.g., `value: "[[tolaria]]"`.
- **Sort `option:direction`** — built-ins: `modified`, `created`, `title`, `status`. Custom: `property:<key>:<asc|desc>`.
- **Never** create `.view.json` files — Tolaria reads `.yml` only.

## Attachments

Files in `attachments/` are **assets**, not notes. Reference them from notes:

```markdown
![Diagram](attachments/system-diagram.png)

[Spec PDF](attachments/spec-v2.pdf)
```

Never give attachments a `.md` extension or treat them as notes.

## File header for vault-meta notes

Notes that are vault-meta (a roster, an index, a template) sometimes use a leading underscore:

```
people/_roster.md
initiatives/_focus-areas.md
daily/_template.md
```

These are still regular notes — kebab-case filename, frontmatter, H1. The underscore just signals "meta, not content."

## What violates the format

Refuse / fix when encountered:

- Frontmatter without `---` fences.
- Missing `type:`.
- Multiple H1s in one note (`#` headings; use `##` for sub-sections).
- File extensions other than `.md` for notes.
- Markdown links for vault-internal references (use wikilinks).
- Bare wikilinks in frontmatter strings (must be quoted).
- Spaces or CamelCase in filenames.
- Modifying `_`-prefixed keys without explicit config-editing intent.
