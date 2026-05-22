---
name: first-domain-project-setup
description: Help a new Oak user create their first local domain or project and first local daily brief without connectors.
---

# First Domain Or Project Setup

Use this when the user is new to Oak or asks for the first useful setup after onboarding.

Ask only the minimum:

1. What project or domain should Oak help with first?
2. What outcome would make the next week easier?
3. What should Oak definitely not do or assume?

Then create local-only drafts:

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

Do not connect outside accounts. Do not send email, post messages, create calendar events, share files, submit forms, archive, label, delete, or change external systems. If the user asks for connector-backed context, stop and explain the local-only default first.

