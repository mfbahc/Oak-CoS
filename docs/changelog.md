# Changelog

## 0.1.0-public

- Initial public Oak core.
- Added Codex App, Codex CLI, Claude CLI, and Claude Desktop runtime guidance.
- Added guided onboarding, local workspace generation, QMD/local search setup, privacy audit, demo, upgrade helper, and release gate.
- Added public roles, skills, connector specs, routines, templates, and synthetic fixtures.
- Fixed `./scripts/doctor` so it validates demo onboarding in a temporary copy
  instead of rewriting a user's live `.oak/`, `local/`, or `workspace/` setup.
- Clarified dedicated-folder setup and existing-assistant-context handling so
  Claude, Codex, OpenClaw, or other memories/tools do not silently steer a new
  Oak onboarding unless the user explicitly migrates them.
- Added a runtime-neutral `./scripts/update` flow and `oak-update` skill so
  Codex and Claude users can ask Oak to check for updates and then apply safe
  fast-forward public-core updates without touching private workspace state.
- Added generalized public skills for meeting transcript ingestion, reading
  queue maintenance, and board briefing refreshes.
- Added a top-level browsable skills library, README skill list, operating-state
  precedence guidance, and a lightweight reading-queue launcher/template.
- Added skill-authoring context budgets plus release-gated skill validation so
  public skills stay terse and operational.
- Added a provider-neutral transcript adapter contract, local adapter template,
  scheduled routine wrapper template, and QMD refresh hardening so repeated local
  workflows can be packaged without adding private provider logic to the public
  core.
- Added a compact `current-actions` layer plus session launch / closeout skills
  so fresh sessions can recover live sign / check / flag / wait posture without
  reading long briefs or old chats.
- Added radar-summary guidance for recurring tracker routines so silent refreshes
  surface material deltas and stale active copies.

Future changes should preserve ignored local user state under `workspace/`, `local/`, and `.oak/`.
