# Codex App

## Who should use this path?

Use Codex App if you want to open the Oak folder and ask Codex to help you run setup. This is the easiest Codex path for someone who does not want to manage a terminal session by hand.

## Before you start

- Download or clone the Oak folder.
- Open the folder in Codex App.
- You do not need Gmail, Calendar, Drive, Slack, or any other connector on day one.
- Oak will create private local files in `workspace/`, `local/`, and `.oak/`.

## Step by step

1. Open the Oak folder in Codex App.
2. Ask Codex: `Please help me set up Oak. Read README.md and run ./scripts/onboard. Explain each choice in plain English.`
3. When onboarding finishes, ask Codex to run `./scripts/qmd-setup`.
4. Open `.oak/START_HERE.md`.
5. Use the Codex App launch prompt shown there.

## What to paste

After onboarding, use the prompt in `.oak/launch-prompts.md` under `## Codex App`.

You can also paste:

```text
You are Oak in Codex App. The Oak root is this workspace. Read AGENTS.md first, then use docs/codex.md only as needed. Use QMD/local search before broad scans. Treat manifests as maps. Keep private state in workspace/, local/, or .oak/. Do not send or publish externally unless I explicitly ask for the exact action. Give me a short status and ask what I want to work on.
```

## How to know it worked

- `.oak/START_HERE.md` exists.
- `.oak/launch-prompts.md` contains a Codex App prompt.
- `workspace/` exists for private notes.
- Oak can prepare a synthetic daily brief without connecting outside accounts.

## Common problems

- If Codex says it cannot find scripts, make sure the Oak folder itself is open.
- If onboarding feels too technical, ask Codex to explain each question before answering.
- If a connector is mentioned, remember that documented or selected does not mean connected. Day one can stay local.
- If a script fails, ask Codex to run `./scripts/doctor` and explain the result.
