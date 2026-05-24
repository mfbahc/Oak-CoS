# Changelog

## 0.1.0-public

- Initial public Oak core.
- Added Codex App, Codex CLI, Claude CLI, and Claude Desktop runtime guidance.
- Added guided onboarding, local workspace generation, QMD/local search setup, privacy audit, demo, upgrade helper, and release gate.
- Added public roles, skills, connector specs, routines, templates, and synthetic fixtures.
- Fixed `./scripts/doctor` so it validates demo onboarding in a temporary copy
  instead of rewriting a user's live `.oak/`, `local/`, or `workspace/` setup.

Future changes should preserve ignored local user state under `workspace/`, `local/`, and `.oak/`.
