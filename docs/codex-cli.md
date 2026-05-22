# Codex CLI

## Who should use this path?

Use Codex CLI if you are comfortable opening Terminal and running commands. If you are not, use Codex App instead.

## Before you start

- Install Codex CLI.
- Download or clone the Oak folder.
- Open Terminal in the Oak folder.
- No connector is required for setup or the demo.

## Step by step

```bash
cd /path/to/oak
./scripts/onboard
./scripts/qmd-setup
codex
```

Then paste the Codex CLI launch prompt.

## What to paste

After onboarding, copy the prompt from `.oak/launch-prompts.md` under `## Codex CLI`.

Fallback prompt:

```text
You are Oak in Codex CLI. The Oak root is the current repo. Read AGENTS.md first, then use docs/codex-cli.md only as needed. Use QMD/local search before broad scans. Keep context tight. Do not send emails, messages, invites, file shares, posts, or external updates unless I explicitly ask for that exact action. Report a short status before large work.
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
- Connector confusion: `local/connectors.toml` records preferences only; it does not connect accounts by itself.
