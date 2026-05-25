# Context Management

Oak is built around tight context, local search, and explicit boundaries.

## Rules

- Context manifests are manifests, not file-expansion instructions.
- Open only files needed for the immediate task.
- Use QMD/local search before broad scans.
- Keep active context small.
- Record durable facts in the right local file.
- Do not ingest private user data into public examples.
- Do not send external messages without explicit user direction.
- Resolve current-state conflicts using [operating-state source precedence](operating-state.md).

## Local State Map

| Path | Use |
| --- | --- |
| `workspace/tasks.md` | active tasks and commitments |
| `workspace/observations/` | dated observations and recurring patterns |
| `workspace/wiki/` | stable personal knowledge |
| `workspace/domains/` | domain-specific context |
| `workspace/projects/` | project plans and status |
| `workspace/artifacts/` | generated local outputs |
| `workspace/briefing-docs/` | optional active reading queue and briefing review surface |
| `.oak/qmd/` | local search manifests and indexes |

## Search-First Workflow

1. State the task.
2. Query QMD/local search.
3. Open the smallest set of relevant files.
4. Do the work.
5. Summarize sources used.
6. Ask before writing durable state if the update is sensitive or broad.

## QMD Fallback

`./scripts/qmd-setup` always creates `.oak/qmd/index.json`. If the `qmd` binary is installed, Oak can also register a named collection and run a QMD smoke search. If it is not installed, the JSON index remains the safe local fallback.

Run QMD setup/update from the runtime root Oak will actually use. If scheduled jobs or an always-on host use a local mirror, the search index must point at that mirror, not a backup source. After large imports or runtime-root changes, run `./scripts/qmd-update` and perform a smoke search before relying on search results.

Long-running sessions should refresh or restart after local state or search indexes change.

## Manifest Rule

A manifest tells Oak what exists. It is not permission to read every item. When a manifest lists many files, select only what the task requires.
