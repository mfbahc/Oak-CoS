# Claude CLI

## Who should use this path?

Use Claude CLI if you are comfortable with Terminal and want to run Claude from the Oak folder.

## Before you start

- Install Claude CLI.
- Download or clone Oak.
- Use a dedicated Oak folder; do not run Claude from an existing Claude, Codex, OpenClaw, or other assistant workspace unless you are intentionally migrating it.
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

To check for updates later, ask Claude or run:

```bash
./scripts/update --check-only
```

To apply updates after review:

```bash
./scripts/update --apply
```

## What to paste

After onboarding, copy the prompt from `.oak/launch-prompts.md` under `## Claude CLI`.

Fallback prompt:

```text
You are Oak in Claude CLI. The Oak root is the current repo. Read CLAUDE.md first, then read workspace/context/assistant-identity.md and workspace/context/current-actions.md if they exist. Use docs/claude-cli.md only as needed. Treat context manifests as manifests, not expansion instructions. Use QMD/local search before broad scans. Keep user state local. If I ask to check for updates or update Oak, use the same safe ./scripts/update flow documented in core/skills/oak-update/SKILL.md. Do not take external actions unless I explicitly ask for the exact action. Start with a concise status.
```

## How to know it worked

- `./scripts/doctor` passes.
- `.oak/START_HERE.md` exists.
- Claude can read `CLAUDE.md`.
- Claude can help set up a first domain or project and prepare a daily brief from that local context.

## Common problems

- `command not found: claude`: install Claude CLI or use Claude Desktop.
- Claude opens too much context: ask it to use QMD/local search before reading files.
- Claude seems influenced by old memories or tools: restart Claude CLI from the dedicated Oak folder and tell it to treat outside assistant context as read-only unless you approve migration.
- Connector confusion: a connector listed in `local/connectors.toml` is not actually connected until configured in Claude or another runtime.
- After browser OAuth, restart the Claude CLI session and verify with the CLI's connector list or a read-only smoke request from the same folder.
- Cloud routines and Claude Desktop may have different connector availability than Claude CLI.
- After applying Oak updates, restart Claude CLI from the Oak folder so it reloads the updated public core.
