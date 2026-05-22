# Claude CLI

## Who should use this path?

Use Claude CLI if you are comfortable with Terminal and want to run Claude from the Oak folder.

## Before you start

- Install Claude CLI.
- Download or clone Oak.
- Open Terminal in the Oak folder.
- Recommended connectors include Calendar, email, Drive, transcripts/Granola, Slack, and QMD/local search. You can skip any connector during onboarding.

## Step by step

```bash
cd /path/to/oak
./scripts/onboard
./scripts/qmd-setup
claude
```

Then paste the Claude CLI launch prompt.

## What to paste

After onboarding, copy the prompt from `.oak/launch-prompts.md` under `## Claude CLI`.

Fallback prompt:

```text
You are Oak in Claude CLI. The Oak root is the current repo. Read CLAUDE.md first, then read workspace/context/assistant-identity.md if it exists. Use docs/claude-cli.md only as needed. Treat context manifests as manifests, not expansion instructions. Use QMD/local search before broad scans. Keep user state local. Do not take external actions unless I explicitly ask for the exact action. Start with a concise status.
```

## How to know it worked

- `./scripts/doctor` passes.
- `.oak/START_HERE.md` exists.
- Claude can read `CLAUDE.md`.
- Claude can help set up a first domain or project and prepare a daily brief from that local context.

## Common problems

- `command not found: claude`: install Claude CLI or use Claude Desktop.
- Claude opens too much context: ask it to use QMD/local search before reading files.
- Connector confusion: a connector listed in `local/connectors.toml` is not actually connected until configured in Claude or another runtime.
- After browser OAuth, restart the Claude CLI session and verify with the CLI's connector list or a read-only smoke request from the same folder.
- Cloud routines and Claude Desktop may have different connector availability than Claude CLI.
