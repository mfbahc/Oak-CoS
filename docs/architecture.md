# Architecture

Oak separates public system files from private user state.

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

These hold personal notes, tasks, connector settings, QMD indexes, backups, local launch prompts, and generated artifacts.

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

## Extension Points

Users can add private extensions under ignored paths:

```text
workspace/extensions/skills/
workspace/extensions/roles/
workspace/extensions/templates/
workspace/extensions/connectors/
```

Public extensions intended for sharing should be scrubbed, reviewed, and moved into `core/` through a normal change.
