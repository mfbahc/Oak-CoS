# Capability Matrix

This matrix keeps public claims honest. A capability is marked as implemented, scaffolded, connector-backed opt-in, or future/private extension.

| Capability | Status | Public support | Validation |
| --- | --- | --- | --- |
| Beginner onboarding | Implemented | `scripts/onboard`, `.oak/START_HERE.md`, `.oak/launch-prompts.md` | `scripts/eval-onboarding`, `scripts/release-check` |
| Codex App launch | Implemented | `AGENTS.md`, `docs/codex.md`, generated Codex App prompt | release-check runtime-doc and prompt checks |
| Codex CLI launch | Implemented | `AGENTS.md`, `docs/codex-cli.md`, generated Codex CLI prompt | release-check runtime-doc and prompt checks |
| Claude CLI launch | Implemented | `CLAUDE.md`, `docs/claude-cli.md`, generated Claude CLI prompt | release-check runtime-doc and prompt checks |
| Claude Desktop launch | Implemented | `CLAUDE.md`, `docs/claude-desktop.md`, generated Claude Desktop prompt | release-check runtime-doc and prompt checks |
| QMD/local search | Implemented | `scripts/qmd-setup`, `scripts/qmd-update`, `core/connectors/qmd.md` | QMD setup, update, local search, large-fixture performance gate |
| Clean public export | Implemented | `scripts/export-public` | export privacy scan and fresh-run checks in release-check |
| Generalized onboarding issue gate | Implemented | `docs/onboarding-issues-release-gate.md` | release-check coverage for safety-critical issue classes |
| First domain/project setup | Scaffolded | `core/skills/first-domain-project-setup/SKILL.md`, `core/templates/first-domain-project.md`, onboarding-generated local files | beginner onboarding eval and release-check generated-output checks |
| Daily brief | Scaffolded | `core/skills/daily-brief/SKILL.md`, `core/templates/daily-brief.md`, `core/routines/daily-brief.md` | demo output, template checks, first starter brief check |
| Meeting prep | Scaffolded | `core/skills/meeting-prep/SKILL.md`, `core/templates/meeting-prep.md` | demo output and template checks |
| Transcript ingest | Scaffolded | `core/skills/ingest/SKILL.md`, `core/templates/transcript-ingest.md` | template and safety checks |
| Inbox triage | Scaffolded | `core/skills/inbox-triage/SKILL.md`, `core/templates/inbox-triage.md` | template and safety checks |
| Initial inbox scan and writing style | Scaffolded | `core/skills/initial-inbox-scan/SKILL.md`, `core/templates/writing-style-profile.md` | release-check guardrail phrase checks |
| Weekly retro | Scaffolded | `core/skills/retro/SKILL.md`, `core/templates/weekly-retro.md`, `core/routines/weekly-review.md` | routine and template checks |
| Board/project briefing | Scaffolded | `core/skills/board-brief/SKILL.md`, `core/templates/board-project-brief.md` | template checks |
| Decision memo | Scaffolded | `core/templates/decision-memo.md` | template checks |
| Relationship note | Scaffolded | `core/templates/relationship-note.md` | template checks |
| Travel/logistics plan | Scaffolded | `core/templates/travel-logistics-plan.md` | template checks |
| Domain tracker refresh | Scaffolded | `core/templates/domain-tracker.md`, `core/routines/domain-tracker-refresh.md` | routine and template checks |
| Gmail inbox work | Connector-backed opt-in | `core/connectors/gmail.md`, inbox triage skills and templates | connector docs and no-send defaults |
| Google Calendar agenda work | Connector-backed opt-in | `core/connectors/google-calendar.md`, meeting prep skill | connector docs and no-write defaults |
| Google Drive document work | Connector-backed opt-in | `core/connectors/google-drive.md` | connector docs and no-share defaults |
| Granola transcript import | Connector-backed opt-in | `core/connectors/granola.md`, transcript ingest template | connector docs and no-share defaults |
| Slack summaries and drafts | Connector-backed opt-in | `core/connectors/slack.md` | connector docs and no-send defaults |
| Browser automation | Connector-backed opt-in | `core/connectors/browser.md` | connector docs and disabled-by-default checks |
| WhatsApp, Telegram, Discord bridges | Connector-backed opt-in | `core/connectors/whatsapp.md`, `core/connectors/telegram.md`, `core/connectors/discord.md` | connector docs and disabled/read-draft defaults |
| Telegram/WhatsApp live connector access | Future/private extension | manual-import/read-only public starter guidance only | release-check messaging safety checks |
| Scheduled external delivery | Connector-backed opt-in | routines docs require host, timeout, logs, visible failure, and capability verification | release-check routine safety checks |
| Email sending | Future/private extension | public starter treats email as read/manage/draft only with no-send defaults | release-check email identity and hard-deny checks |
| User-specific private workflows | Future/private extension | `workspace/extensions/` after local customization | ignored-state and privacy checks |

Public Oak should not imply that connector-backed capabilities are active just because they are documented or selected in config. They become active only after the user connects the provider in the runtime and grants access.
