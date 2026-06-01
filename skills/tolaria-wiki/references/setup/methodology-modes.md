# Tolaria Wiki Methodology Modes

The default Tolaria folder structure is opinionated but simple. For users who want a different organizational philosophy, three optional methodology modes are available. These are setup-time choices, not runtime changes.

## Default Mode

The standard folder structure (see `references/setup/setup.md`):

```
meetings/
initiatives/
features/
research/
decisions/
people/
daily/
Raw/
summaries/
logs/
attachments/
views/
```

Best for: Teams, project-oriented work, meeting-heavy environments.

## PARA Mode

Based on the PARA method (Projects, Areas, Resources, Archives).

```
1-projects/
  - active-project-a/
  - active-project-b/
2-areas/
  - health/
  - finance/
  - career/
3-resources/
  - research/
  - books/
  - courses/
4-archives/
  - completed-projects/
  - old-areas/
Raw/
summaries/
logs/
attachments/
views/
```

### Type Mapping

| Default Type | PARA Location |
|--------------|---------------|
| Meeting | Inside the relevant project or area |
| Initiative | `1-projects/<name>/` |
| Feature | `1-projects/<name>/` |
| Decision | `1-projects/<name>/` or `2-areas/<name>/` |
| Research | `3-resources/research/` |
| Person | `3-resources/people/` |
| Note | `2-areas/<name>/` or `3-resources/<name>/` |
| Summary | `summaries/` |

### Rules

1. Everything is a project or belongs to an area.
2. Projects have a goal and a deadline. Areas have a standard to maintain.
3. Resources are reference material. Archives are completed or inactive.
4. Notes are filed by context, not by type.

## Zettelkasten Mode

Based on the Zettelkasten method (Fleeting, Literature, Permanent, Index).

```
fleeting/
literature/
permanent/
index/
Raw/
summaries/
logs/
attachments/
views/
```

### Type Mapping

| Default Type | Zettelkasten Location |
|--------------|----------------------|
| Meeting | `fleeting/` (if unprocessed) or `permanent/` (if synthesized) |
| Initiative | `permanent/` |
| Feature | `permanent/` |
| Decision | `permanent/` |
| Research | `literature/` |
| Person | `permanent/` |
| Note | `fleeting/` (if unprocessed) or `permanent/` (if synthesized) |
| Summary | `index/` (as a Map of Content) or `permanent/` |

### Rules

1. Fleeting notes are quick captures. They are processed into permanent notes.
2. Literature notes are about sources (books, articles, talks).
3. Permanent notes are atomic ideas, one idea per note.
4. Index notes are Maps of Content (MOCs) that link to permanent notes.
5. Every permanent note should link to at least one other permanent note.

## LYT Mode

Based on the Linking Your Thinking method (Maps of Content, structured linking).

```
0-inbox/
1-mocs/
2-notes/
3-sources/
4-people/
5-projects/
Raw/
summaries/
logs/
attachments/
views/
```

### Type Mapping

| Default Type | LYT Location |
|--------------|--------------|
| Meeting | `0-inbox/` (if unprocessed) or `2-notes/` (if synthesized) |
| Initiative | `5-projects/` |
| Feature | `5-projects/` |
| Decision | `2-notes/` |
| Research | `3-sources/` |
| Person | `4-people/` |
| Note | `2-notes/` |
| Summary | `1-mocs/` (as a Map of Content) |

### Rules

1. MOCs (Maps of Content) are the primary navigation mechanism.
2. MOCs link to notes, not the other way around.
3. Notes are atomic and linked.
4. Sources are preserved in their original form.
5. People are linked from notes and MOCs.

## How to Choose

| User Profile | Recommended Mode |
|--------------|------------------|
| Team, project-oriented, meeting-heavy | Default |
| Personal productivity, goal-oriented | PARA |
| Researcher, writer, thinker | Zettelkasten |
| Content creator, knowledge worker | LYT |

## How to Switch

Switching modes is a setup-time decision. To switch after setup:

1. Read the new mode's folder structure.
2. Create the new folders.
3. Move existing notes to the new structure.
4. Update `AGENTS.md` and `CLAUDE.md` with the new folder structure.
5. Run a health check to verify all links are intact.

## Rules

1. Pick one mode at setup time. Don't mix modes.
2. The mode is a folder structure, not a type system. Types are universal across all modes.
3. The mode is a setup choice, not a runtime change. The agent doesn't switch modes during operation.
4. The mode is documented in `AGENTS.md` and `CLAUDE.md` so the agent knows which structure to use.
