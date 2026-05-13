Read `.plan/CONTEXT.md` if it exists. Use its terminology throughout — never invent synonyms.

Read the codebase for relevant context before asking anything.

Use `AskUserQuestion` to ask which feature this PRD is for if not specified in $ARGUMENTS.

Then interview the user with 3–5 questions using `AskUserQuestion` (one at a time). Cover: problem being solved, who it affects, what's in scope, what's explicitly out, and key constraints or decisions with tradeoffs.

Draft the PRD using the format in `.claude/commands/` (or ask Claude to use the PRD structure: Problem, Goal, Scope In/Out, Key decisions, Success criteria, Open questions).

Save to `.plan/features/[feature-name]/prd.md`. Create the folder if it doesn't exist.

After saving, ask via `AskUserQuestion`:
> "What next?"
> Options: "Break into tasks now (/prd-to-tasks)" | "Review PRD first" | "Done for now"
