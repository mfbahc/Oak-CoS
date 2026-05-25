---
name: oak-update
description: Check for and apply safe Oak public-core updates without touching private workspace state.
---

# Oak Update

Use the same flow in Codex App, Codex CLI, Claude CLI, and Claude Desktop.

## User Phrases

- "check for updates"
- "update Oak"
- "pull the latest Oak"
- "upgrade this instance"

## Safety Model

- Public core updates come from git.
- Private local state lives in ignored paths: `workspace/`, `local/`, and `.oak/`.
- Checking for updates does not change private workspace content.
- Applying updates may change public core files such as `README.md`, `docs/`, `core/`, `scripts/`, `config/`, and `examples/`.
- Existing customized files in ignored local paths must not be overwritten.
- A running AI session may keep old instructions in context. After applying an update, ask the user to restart or refresh the Codex/Claude session.

## Procedure

1. For "check for updates", run:

```bash
./scripts/update --check-only
```

2. Summarize the report in plain English:

- up to date
- updates available
- no upstream configured
- local public-core changes need review
- apply failed and why

3. For "update Oak", run:

```bash
./scripts/update --apply
```

4. If the apply step fails because public-core files are dirty, stop and explain that the user has local edits in the shared core. Do not force or discard changes unless the user explicitly approves that exact action.

5. After a successful update, tell the user to restart or refresh the current Codex/Claude session so updated instructions and skills are loaded.

## Do Not

- Do not edit private workspace files as part of a public-core update.
- Do not commit, push, reset, clean, or discard local changes unless the user explicitly asks.
- Do not use a zip download as the normal update path when the folder is already a git clone.
- Do not claim connector changes are active until the target runtime verifies them.
