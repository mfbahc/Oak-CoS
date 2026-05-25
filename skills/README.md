# Skills Library

This is the user-facing index for Oak's included skills. The canonical skill source files live under `core/skills/<skill-name>/SKILL.md`; this folder exists so users can browse what Oak includes without digging through implementation paths.

Private or user-specific skills should live under `workspace/extensions/skills/`, which is ignored by git.

## Included Skills

| Skill | Use it for |
| --- | --- |
| [Board Brief](../core/skills/board-brief/SKILL.md) | Build a decision-oriented board, investor, lender, or project briefing. |
| [Board Briefing Refresh](../core/skills/board-briefing-refresh/SKILL.md) | Refresh a board or governance briefing from new materials, emails, trackers, and transcripts. |
| [Coaching](../core/skills/coaching/SKILL.md) | Run optional executive-coaching style check-ins on priorities, energy, decisions, and commitments. |
| [Daily Brief](../core/skills/daily-brief/SKILL.md) | Prepare a concise day plan from tasks, observations, calendar, inbox, Drive, transcripts, and project notes. |
| [First Domain/Project Setup](../core/skills/first-domain-project-setup/SKILL.md) | Create a user's first local Oak domain or project workspace. |
| [Inbox Triage](../core/skills/inbox-triage/SKILL.md) | Review inbox context into priorities, drafts, and next actions without sending by default. |
| [Ingest](../core/skills/ingest/SKILL.md) | Turn provided notes or artifacts into structured local memory and follow-ups. |
| [Initial Inbox Scan](../core/skills/initial-inbox-scan/SKILL.md) | Infer domains, projects, and optional writing-style patterns from read-only email context. |
| [Meeting Prep](../core/skills/meeting-prep/SKILL.md) | Prepare objectives, context, questions, risks, and follow-ups for an upcoming meeting. |
| [Meeting Transcript Ingest](../core/skills/meeting-transcript-ingest/SKILL.md) | Preserve a raw meeting transcript and extract decisions, commitments, questions, and durable updates. |
| [Oak Update](../core/skills/oak-update/SKILL.md) | Check for and apply safe public-core updates while preserving private workspace state. |
| [Onboard](../core/skills/onboard/SKILL.md) | Guide a new user through runtime, personality, connector, project, and routine setup. |
| [Reading Queue](../core/skills/reading-queue/SKILL.md) | Keep review folders current, mark items read, and move superseded versions out of the active queue. |
| [Research Memo](../core/skills/research-memo/SKILL.md) | Produce a source-grounded research memo with citations and open questions. |
| [Retro](../core/skills/retro/SKILL.md) | Run a weekly or periodic review of commitments, decisions, patterns, and improvements. |
| [Task Tracking](../core/skills/task-tracking/SKILL.md) | Maintain tasks, stale commitments, waiting items, and follow-up status. |

## Adding Skills

For reusable public skills, add a new folder under `core/skills/` with a short `SKILL.md`, then add one row to this index and update `README.md`.

For personal workflows, keep the skill under `workspace/extensions/skills/` and do not commit it unless it has been fully generalized and scrubbed.

Follow [docs/skill-authoring.md](../docs/skill-authoring.md): keep descriptions short, keep bodies operational, and run `./scripts/validate-skills`.
