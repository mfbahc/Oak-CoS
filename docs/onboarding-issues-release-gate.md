# Onboarding Issues Release Gate

This document converts local onboarding defects into public, scrubbed release requirements. It must not contain private names, accounts, project facts, paths, emails, or customer examples.

## Status Labels

- Implemented and validated: public docs, scripts, templates, or checks exist.
- Generalized into safe public guidance: the public starter documents the safe pattern without claiming a live integration.
- Intentionally out of public starter scope: useful later, but unsafe or too runtime-specific for the starter repo.
- Blocked by external runtime/provider limitations: Oak can explain and verify, but cannot fix the provider surface locally.

## Release Gate Matrix

| Issue class | Public status | Public requirement |
| --- | --- | --- |
| Connector auth reality | Implemented and validated | After web OAuth, tell users to restart or refresh the runtime and verify actual connector availability before claiming connection. |
| Runtime-specific connector state | Implemented and validated | Track connector state per runtime: Codex App, Codex CLI, Claude CLI, Claude Desktop, cloud routine, local scheduled job, or hosted runner. |
| Value-first onboarding | Implemented and validated | First session creates a real first project/domain and starter brief before optional automation. |
| Assistant identity and working style | Implemented and validated | Ask for assistant name, role, relationship, working style, and boundaries early; reflect them in generated prompts. |
| File placement for identity vs user context | Implemented and validated | Keep assistant identity in `workspace/context/assistant-identity.md` and user facts in `workspace/context/user-profile.md`. |
| Pause/resume | Implemented and validated | Write checkpoint and `.oak/onboarding-resume.md` with a pasteable next-session prompt. |
| Connector prepopulation | Generalized into safe public guidance | When verified read-only connectors exist, infer domains/projects and let the user correct them; otherwise use local/contextual intake. |
| Email attachment limitations | Generalized into safe public guidance | Explain that email connectors may expose message bodies without attachments; save important attachments to Drive or another readable source. |
| Backup storage vs runtime path | Generalized into safe public guidance | Cloud-synced storage can be backup, but unattended jobs should run from a reliable local or hosted runtime path. |
| Always-on host | Implemented and validated | Ask whether the user has an awake, online host; keep routines manual/on-demand when no reliable host exists. |
| Scheduled job reliability | Generalized into safe public guidance | Scheduled wrappers need timeout, logs, visible failure, no interactive prompts, and explicit local artifact outputs. |
| Scheduled job safety | Implemented and validated | No sends, posts, calendar writes, file shares, pushes, or external updates by default. |
| Delivery-channel reality | Generalized into safe public guidance | Verify the actual runtime capability before promising delivery; email may only support drafts, while Slack or Drive may be better supported. |
| Messaging connectors | Intentionally out of public starter scope | Telegram and WhatsApp are manual-import/read-only only; no browser/app automation or send-capable token path. |
| Email identity separation | Implemented and validated | Record account identities, allowed read/manage actions, prohibited outbound actions, and technical no-send guardrails where possible. |
| Hard deny rules | Generalized into safe public guidance | Behavioral instructions are not enough; use runtime/tool-level deny or no-send controls where supported. |
| Domain/project reconciliation | Generalized into safe public guidance | If connected or local context suggests active work, create or flag corresponding project/domain files. |
| Local search freshness | Implemented and validated | QMD/local search setup runs from the active runtime root, writes a manifest, and includes smoke checks/stale-index guidance. |
| Context refresh | Generalized into safe public guidance | Long-running sessions must refresh/restart after local state, connector, or search-index changes. |
| Existing user settings | Generalized into safe public guidance | Preserve complete runtime settings files; never write a partial replacement that drops existing permission rules. |
| Runtime/model portability | Implemented and validated | Distinguish model, runtime, connector, channel, permission model, and scheduler in architecture and capability docs. |
| Migration from an existing assistant | Generalized into safe public guidance | Retire old systems only after Oak has produced verified useful output and duplicate automation risk is gone. |
| Relationship imports from professional networks | Intentionally out of public starter scope | Manual CSV import guidance may be added later; live scraping/browser automation is not part of the public starter. |
| Chat/channel plugin automation | Intentionally out of public starter scope | Do not auto-submit text into an interactive TUI. Channel plugins require explicit runtime-specific verification and access policy review. |
| Cloud routine network/provider limits | Blocked by external runtime/provider limitations | Public docs require capability verification and fallback to local artifacts, Drive, Slack, or manual delivery when a provider blocks a path. |

## Release-Check Expectations

`./scripts/release-check` should fail if safety-critical public coverage disappears:

- restart-after-auth guidance
- per-runtime connector verification
- always-on host language
- scheduled wrapper timeout/log/visible failure guidance
- no-send/no-post/no-share defaults
- messaging manual-import/read-only constraints
- email identity and technical no-send guidance
- QMD runtime-root and stale-index guidance
- pause/resume checkpoint output
- assistant identity separated from user profile
- migration/retirement checklist guidance

Warnings are allowed only for concrete external runtime/provider limitations that cannot be solved locally.
