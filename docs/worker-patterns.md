# Worker Patterns

Oak works best with one main instance and focused workers.

## Main Oak

The main instance:

- keeps the operating picture
- decides which context is needed
- launches workers for narrow jobs
- receives handoffs
- asks before updating durable local state

## Workers

Workers are useful for:

- inbox review
- calendar review
- meeting prep
- transcript ingestion
- research
- board or advisory prep
- engineering/code support
- personal admin
- coaching reflection

## Worker Prompt Shape

Use the worker prompt in `docs/prompt-bible.md`. A worker should not run full startup. It should read only the core instructions needed for identity, privacy, context discipline, and worker rules.

## Handoff Format

```text
Task:
Sources read:
Findings:
Recommended updates:
Blockers:
Next step:
```

## Context Boundaries

Do not move private data between domains unless the user asks. If inbox context is needed for a board prep worker, ask before sharing it.
