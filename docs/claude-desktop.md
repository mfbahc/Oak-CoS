# Claude Desktop

## Who should use this path?

Use Claude Desktop if you prefer a desktop app and do not want to live in Terminal. This path is first-class, but a small amount of setup still needs to happen in Terminal unless another helper runs the scripts for you.

## Before you start

- Download or clone the Oak folder.
- Know where the folder is on your computer.
- Give Claude Desktop access only to the Oak folder and any private folder you intentionally choose.
- You do not need Gmail, Calendar, Drive, Slack, or any other connector on day one.

## Step by step

1. Open Terminal.
2. Drag the Oak folder into Terminal after typing `cd `, then press Return. This moves Terminal into the Oak folder.
3. Run:

```bash
./scripts/onboard
./scripts/qmd-setup
```

4. Open Claude Desktop.
5. Add the Oak folder as a project or accessible folder.
6. Add `CLAUDE.md` as project instructions, or paste its contents into the project instructions area.
7. Open `.oak/START_HERE.md`.
8. Paste the Claude Desktop launch prompt from `.oak/launch-prompts.md`.

## What to paste

After onboarding, copy the prompt from `.oak/launch-prompts.md` under `## Claude Desktop`.

Fallback prompt:

```text
You are Oak in Claude Desktop. The Oak root is the project folder I added. Read CLAUDE.md or the project instructions first, then use docs/claude-desktop.md only as needed. Use QMD/local search before broad scans. Treat manifests as maps. Keep private state local. Do not send, share, post, invite, or publish externally unless I explicitly ask for that exact action. Start with a concise status and any file-access limits you see.
```

## How to know it worked

- Claude can see `CLAUDE.md`.
- Claude can see `.oak/START_HERE.md`.
- Claude can explain that private notes belong in `workspace/`.
- Claude can prepare a synthetic daily brief without connecting outside accounts.
- Claude asks before any send, share, post, invite, connector write, or calendar change.

## Common problems

- Claude cannot see `.oak/START_HERE.md`: check project folder access.
- Terminal says `permission denied`: run `chmod +x scripts/*` from the Oak folder.
- You do not want Terminal: ask a Codex or Claude helper that can run local scripts to run `./scripts/onboard` and `./scripts/qmd-setup`.
- A connector appears in config: that is only a local preference. It is not active until connected in Claude Desktop or another runtime.
