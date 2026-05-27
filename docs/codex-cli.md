# Codex CLI

## Who should use this path?

Use Codex CLI if you are comfortable opening Terminal and running commands. If you are not, use Codex App instead.

## Before you start

- Install Codex CLI.
- Download or clone the Oak folder.
- Use a dedicated Oak folder; do not run Codex from an existing Claude, Codex, OpenClaw, or other assistant workspace unless you are intentionally migrating it.
- Open Terminal in the Oak folder.
- Recommended connectors include Calendar, email, Drive, transcripts/Granola, Slack, and QMD/local search. You can skip any connector during onboarding.

## Step by step

```bash
cd /path/to/oak
./scripts/onboard
./scripts/qmd-setup
codex
```

Then paste the Codex CLI launch prompt.

To check for updates later, ask Codex or run:

```bash
./scripts/update --check-only
```

To apply updates after review:

```bash
./scripts/update --apply
```

## What to paste

After onboarding, copy the prompt from `.oak/launch-prompts.md` under `## Codex CLI`.

Fallback prompt:

```text
You are Oak in Codex CLI. The Oak root is the current repo. Read AGENTS.md first, then read workspace/context/assistant-identity.md and workspace/context/current-actions.md if they exist. Use docs/codex-cli.md only as needed. Use QMD/local search before broad scans. Keep context tight. If I ask to check for updates or update Oak, use the same safe ./scripts/update flow documented in core/skills/oak-update/SKILL.md. Do not send emails, messages, invites, file shares, posts, or external updates unless I explicitly ask for that exact action. Report a short status before large work.
```

## How to know it worked

- `./scripts/doctor` passes.
- `.oak/START_HERE.md` exists.
- Codex can read `AGENTS.md`.
- Oak can answer: `Help me set up my first Oak domain or project, then prepare my first daily brief from that local context.`

## Common problems

- `permission denied`: run `chmod +x scripts/*` from the Oak folder.
- `command not found: codex`: install or open Codex App instead.
- Prompt confusion: use `.oak/START_HERE.md` first, then `.oak/launch-prompts.md`.
- Existing assistant context: if Codex seems to rely on another setup, restart from the dedicated Oak folder and treat outside memories, skills, or tools as read-only unless you approve migration.
- Connector confusion: `local/connectors.toml` records preferences only; it does not connect accounts by itself.
- After web OAuth, restart the CLI session and verify a read-only connector request from the same Oak folder before claiming the connector is connected.
- Runtime settings edits must preserve the whole settings file and existing permission rules.
- After applying Oak updates, restart Codex CLI from the Oak folder so it reloads the updated public core.
