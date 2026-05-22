---
name: first-domain-project-setup
description: Help a new Oak user create their first domain or project and first daily brief, using the local workspace plus selected read-only connector context when available.
---

# First Domain Or Project Setup

Use this when the user is new to Oak or asks for the first useful setup after onboarding.

Ask only the minimum:

1. What project or domain should Oak help with first?
2. What outcome would make the next week easier?
3. What should Oak definitely not do or assume?

Then create local drafts:

- `workspace/projects/{{slug}}/README.md`
- `workspace/domains/{{slug}}.md`
- `workspace/artifacts/daily-briefs/{{slug}}-first-brief.md`

Use `core/templates/first-domain-project.md` and `core/templates/daily-brief.md` as public scaffolds. Keep private details inside `workspace/`.

The first brief should be useful even with sparse context:

- today or next-session focus
- decisions needed
- waiting items
- risks or unknowns
- one next action

Use the local workspace plus any selected read-only connector context that is already available, especially Calendar, email, Google Drive, transcripts, and Slack. Selected connectors should improve the first useful brief, not replace the local workspace. If a connector is not available yet, continue from local context and note what would improve after connection. Do not send email, post messages, create calendar events, share files, submit forms, archive, label, delete, or change external systems unless the user explicitly approves that exact action.

Before writing, check for similar existing project/domain slugs and avoid duplicate directories. Run a lightweight reconciliation: if local wiki/source context or verified connector context suggests active projects without matching `workspace/projects/` files, flag the gap and ask which project/domain files to create.
