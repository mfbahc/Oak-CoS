# Claude

## Who should use this path?

Use Claude if you prefer Claude CLI or Claude Desktop. Oak supports both with the same public core and private local workspace.

## Before you start

- Choose Claude CLI if you are comfortable with Terminal.
- Choose Claude Desktop if you prefer a desktop project or folder-based workflow.
- Recommended connectors include Calendar, email, Drive, transcripts/Granola, Slack, and QMD/local search. You can skip any connector during onboarding.

## Step by step

1. Run Oak onboarding.
2. Open `.oak/START_HERE.md`.
3. Use the Claude CLI or Claude Desktop prompt from `.oak/launch-prompts.md`.
4. Keep private notes in `workspace/`.
5. For updates, use the same flow as Codex: `./scripts/update --check-only` to check and `./scripts/update --apply` to apply after review.

## What to paste

For Claude CLI, use the prompt under `## Claude CLI` in `.oak/launch-prompts.md`.

For Claude Desktop, use the prompt under `## Claude Desktop` in `.oak/launch-prompts.md`.

## How to know it worked

- Claude can see `CLAUDE.md`.
- Claude can explain that `workspace/`, `local/`, and `.oak/` are private local folders.
- Claude can prepare a first brief from local workspace context plus selected connectors after you grant runtime access.

## Common problems

- If Claude cannot see files, check folder/project access.
- If Claude tries to read too many files, remind it to use QMD/local search first.
- After web OAuth, restart or refresh Claude and verify the connector in the exact Claude surface you plan to use.
- Claude CLI, Claude Desktop, and cloud routines may not expose the same connector set.
- If Claude mentions sending or sharing, stop and require exact approval before any external action.
- After applying Oak updates, restart or refresh Claude so it reloads updated instructions and skills.
