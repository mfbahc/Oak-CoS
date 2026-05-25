# Codex App

## Who should use this path?

Use Codex App if you want to open the Oak folder and ask Codex to help you run setup. This is the easiest Codex path for someone who does not want to manage a terminal session by hand.

## Before you start

- Download or clone the Oak folder.
- Use a dedicated Oak folder; do not open an existing Claude, Codex, OpenClaw, or other assistant workspace unless you are intentionally migrating it.
- Open the folder in Codex App.
- Recommended connectors include Calendar, email, Drive, transcripts/Granola, Slack, and QMD/local search. You can skip any connector during onboarding.
- Oak will create private local files in `workspace/`, `local/`, and `.oak/`.

## Step by step

1. Open the Oak folder in Codex App.
2. Ask Codex: `Please help me set up Oak. Read README.md and run ./scripts/onboard. Explain each choice in plain English.`
3. When onboarding finishes, ask Codex to run `./scripts/qmd-setup`.
4. Open `.oak/START_HERE.md`.
5. Use the Codex App launch prompt shown there.

To check for updates later, ask Codex: `Check for Oak updates.` Codex should run `./scripts/update --check-only`. To apply updates, ask: `Update Oak.` Codex should run `./scripts/update --apply`.

## What to paste

After onboarding, use the prompt in `.oak/launch-prompts.md` under `## Codex App`.

You can also paste:

```text
You are Oak in Codex App. The Oak root is this workspace. Read AGENTS.md first, then read workspace/context/assistant-identity.md if it exists. Use docs/codex.md only as needed. Use QMD/local search before broad scans. Treat manifests as maps. Keep private state in workspace/, local/, or .oak/. If I ask to check for updates or update Oak, use the same safe ./scripts/update flow documented in core/skills/oak-update/SKILL.md. Do not send or publish externally unless I explicitly ask for the exact action. Give me a short status and ask what I want to work on.
```

## How to know it worked

- `.oak/START_HERE.md` exists.
- `.oak/launch-prompts.md` contains a Codex App prompt.
- `workspace/` exists for private notes.
- Oak can prepare a first brief from local workspace context plus selected connectors after you grant runtime access.

## Common problems

- If Codex says it cannot find scripts, make sure the Oak folder itself is open.
- If Codex seems influenced by another assistant setup, confirm the Oak folder is the workspace root and tell Codex not to use outside memories, skills, or tools unless you approve migration.
- If onboarding feels too technical, ask Codex to explain each question before answering.
- If a connector is mentioned, remember that documented or selected does not mean connected. You can skip any connector or keep it read-only/draft-only.
- After browser OAuth or connector authorization, refresh Codex App and verify a read-only request in Codex before saying that connector is connected in Codex.
- A connector that works in another runtime may not work in Codex App; record the runtime-specific status.
- If a script fails, ask Codex to run `./scripts/doctor` and explain the result.
- After applying Oak updates, restart or refresh Codex App so it reloads the updated public core.
