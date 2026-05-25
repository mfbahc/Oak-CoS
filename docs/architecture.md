# Architecture

Oak separates public system files from private user state, while allowing selected connectors such as Google Drive to supply working context.

## Public Core

Tracked files:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `docs/`
- `core/`
- `scripts/`
- `config/`
- `examples/synthetic-user/`
- `workspace.template/`
- `migrations/`

These files are safe to share publicly and contain only generic guidance, placeholders, and synthetic examples.

## Private Workspace

Ignored files:

- `workspace/`
- `local/`
- `.oak/`

These hold personal notes, tasks, connector settings, QMD indexes, backups, local launch prompts, and generated artifacts. Connected source documents can remain in their provider, such as Google Drive, while Oak stores only local notes, summaries, or artifacts the user chooses to keep.

Assistant identity is private local state, not public configuration. Onboarding renders a selected template from `core/personality-templates/` into `workspace/context/assistant-identity.md`; startup prompts tell the runtime to read that file after `AGENTS.md` or `CLAUDE.md`.

Each installation should have a dedicated Oak root folder. Existing Claude, Codex, OpenClaw, or other assistant memories, skills, tools, and project instructions are external context unless the user explicitly approves migration or consultation.

## Shared Core, Thin Adapters

The shared core owns:

- context architecture
- privacy rules
- QMD/local search discipline
- roles
- skills
- templates
- onboarding logic
- update workflow

Runtime adapters add environment-specific startup files and docs:

- Codex App uses `AGENTS.md` and `docs/codex.md`.
- Codex CLI uses `AGENTS.md` and `docs/codex-cli.md`.
- Claude CLI uses `CLAUDE.md` and `docs/claude-cli.md`.
- Claude Desktop uses `CLAUDE.md` or project instructions and `docs/claude-desktop.md`.

## Runtime Surfaces

Separate these concepts when planning a workflow:

- Agent model: the model that reasons.
- Runtime: Codex App, Codex CLI, Claude CLI, Claude Desktop, cloud routine, local scheduled job, or hosted runner.
- Connector: Calendar, email, Drive, Slack, QMD/local search, or another tool surface.
- Channel: where output appears, such as local artifact, Drive file, Slack, email draft, or manual relay.
- Permission model: read-only, draft-only, auto approval, explicit approval, deny/no-send, or scheduler bypass.
- Scheduler: manual/on-demand, local cron/launchd, cloud routine, or hosted runner.

Do not imply that changing the model automatically preserves the runtime, channel, connector, permission, or scheduler behavior.

## Backup And Runtime Roots

Cloud-synced storage can be a good backup source. Unattended scheduled jobs need a reliable local or hosted runtime root that is awake, online, and not blocked by an interactive file-provider prompt.

If a separate runtime mirror is used, QMD/local search indexes must follow the runtime root. Run QMD setup/update from the same root the runtime uses, and treat stale-index warnings as a reason to refresh before making same-day claims.

## Long-Running Sessions

Long-running interactive sessions can carry stale context after local files, connector state, runtime settings, or search indexes change. Use a refresh/restart protocol after such changes, and avoid saying an event has happened unless current wall-clock and context support it.

## Forbidden Automation Pattern

Do not solve parked or delayed channel messages by blindly pressing Enter in a running terminal or TUI. Any channel bridge must preserve source metadata and user intent, or fail visibly and ask for a restart/reload.

## Extension Points

Users can add private extensions under ignored paths:

```text
workspace/extensions/skills/
workspace/extensions/roles/
workspace/extensions/templates/
workspace/extensions/connectors/
```

Public extensions intended for sharing should be scrubbed, reviewed, and moved into `core/` through a normal change.
