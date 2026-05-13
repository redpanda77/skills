# Authoring — create, classify, file, cross-link

For creating any new note in an existing vault. Full type table and schemas live in `types-reference.md`; this file is the **procedure**.

## The 7-step procedure

1. **Classify the note.** Determine `type` from user intent + content. See `types-reference.md` § "How to choose between similar types".
2. **Pick the destination folder.** See `types-reference.md` § "Folder routing".
3. **Pick the filename.** See `types-reference.md` § "Filename conventions". Always kebab-case, `.md`.
4. **Build frontmatter** using the type-specific schema. Required fields per type listed in `types-reference.md`.
5. **Cross-link** with `[[wikilinks]]`. See § "Cross-linking" below.
6. **Write the body** with the first H1 as the display title.
7. **If the note represents a structural change** (new initiative, new feature, new person, decision), append a line to `logs/maintenance-log.md`.

## Cross-linking

After choosing the type, add `related_to` (and type-specific relationship keys) to frontmatter:

- **Meeting** → `attendees:` list of `[[person]]`, `related_to:` initiatives or features discussed
- **Decision** → `related_to:` whatever this decision affects
- **Initiative** → `owner: "[[person]]"`, optionally `related_to:` research that motivates it
- **Feature** → `initiative: "[[parent-initiative]]"`, `owner: "[[person]]"`
- **Research** → `source:` URL or `[[raw-note]]`, `related_to:` initiatives or features that consume it
- **Raw** → `source:` path or URL of the upstream artifact

Rules:
- Don't link to people via `related_to` — use `attendees`, `owner`, or a dedicated relationship key.
- Don't link to a file that doesn't exist unless you're also creating it in this operation.
- Don't link to `attachments/` — reference inline with markdown image/link syntax instead.

## When to ask

Use AskUserQuestion only when context can't resolve the choice:

- Type is ambiguous (could be Note vs Research vs Initiative — content fits all).
- Meeting category unclear (Data vs Engineering vs Design — attendees span teams).
- Owner missing on an action item, especially in meeting notes.
- Confidentiality unclear on stakeholder material — default confidential if the meeting includes leadership / exec / external parties unless told otherwise.

Default to proceeding autonomously when:
- Clear meeting transcript with attendees and topic.
- Obvious feature/initiative description.
- Filename or path the user provided implies the type.

## Common authoring tasks

### Create a meeting note

User says: "Create a meeting note for today's data sync with [people]."

1. type=Meeting, date=today, category=Data (heuristic: people are DS).
2. Folder: `meetings/data/`.
3. Filename: `YYYY-MM-<topic>.md` — e.g., `2026-05-data-sync.md`.
4. Frontmatter with `attendees:` list.
5. Body skeleton with sections: `## Topics`, `## Decisions`, `## Action items` (with `- [ ]` checkboxes and owners), `## Next steps`.

### Create a decision

User says: "Record the decision to use X for Y."

1. type=Decision, date=today, status=Accepted (or Proposed if not yet ratified).
2. Folder: `decisions/`.
3. Filename: `kebab-case-of-decision.md` — descriptive, not dated.
4. Body: `## Context`, `## Options considered`, `## Decision`, `## Consequences`, `## Related`.
5. Append to maintenance log.

### Create an initiative

User says: "Start tracking the X initiative."

1. type=Initiative, status=Active, priority (ask if unclear), owner, timeline.
2. Folder: `initiatives/`.
3. Filename: `<descriptive>-initiative.md` (suffix optional, common in practice).
4. Body: `## Goal`, `## Scope`, `## Out of scope`, `## Milestones`, `## Open questions`.
5. Append to maintenance log.

### Create a person note

User says: "Add a note for [person]."

1. type=Person, role, team.
2. Folder: `people/`.
3. Filename: `firstname-lastname.md`.
4. Body: `## Role`, `## Working on`, `## Communication`, `## Notes`. Keep it light — facts you want quick access to.

### Add a daily note

User says: "Daily note for today."

1. type=Note, date=today.
2. Folder: `daily/`.
3. Filename: `YYYY-MM-DD.md`.
4. If `daily/_template.md` exists, use it. Otherwise: `## Yesterday`, `## Today`, `## Blockers`, `## Notes`.

## Filing a Raw note into a structured note

When the user has a Raw note and wants the structured version:

1. Read the Raw note. Check `category:` and content.
2. Determine destination type from category + content (see `types-reference.md` § "Raw → destination mapping").
3. Apply the relevant authoring task above.
4. After writing the structured note, update the Raw note:
   - `status: Processed`
   - `processed_date: YYYY-MM-DD`
   - `processed_to: "[[path/to/structured-note]]"`
5. Move the Raw file: `Raw/X.md` → `Raw/archive/X.md`.
6. Append to `logs/maintenance-log.md`.

This procedure is also the main subject of `maintenance.md` — see there for batch processing and recording imports.

## After authoring

End every authoring task with:

- File path created.
- One-line summary of the note's contents.
- Linked targets that don't yet exist (offer to stub them).
- Any unanswered ambiguity (e.g., "the owner of action item 3 wasn't named — ask me").

Never claim the note is "complete" — knowledge-base notes accrete. Just confirm it's filed correctly.
