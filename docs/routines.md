# Routines

Routines are templates for repeated work, not background jobs. They help Oak do the same kind of local review again later, such as a morning brief or weekly review.

## Day 1

Use routines manually:

- run onboarding
- open `workspace/routines/`
- ask Oak to run one routine using local or synthetic data
- keep outputs in `workspace/artifacts/`

No routine sends messages, creates calendar events, shares files, or posts updates by default.

## Safe Local Examples

Morning daily brief:

```text
Run the daily brief routine using my local project/domain context only. Write a local brief and do not contact anyone.
```

Evening wrap:

```text
Run the evening wrap routine. Summarize open loops, completed work, and tomorrow's first useful action. Write a local note only.
```

Meeting prep:

```text
Prepare me for [MEETING] using local notes only. Return purpose, decisions, questions, risks, and follow-ups. Do not send an agenda.
```

Transcript ingest:

```text
Ingest this transcript as private local context. Extract decisions, commitments, questions, and proposed updates. Do not write durable memory until I approve.
```

Weekly review:

```text
Run the weekly review routine. Use local tasks and observations. Return wins, misses, stale commitments, and one improvement for next week.
```

## Suggested Routines

| Routine | Cadence | Output |
| --- | --- | --- |
| Daily brief | daily | local brief in `workspace/artifacts/` |
| Evening wrap | daily | local wrap and open loops |
| Weekly review | weekly | local retro and next-week focus |
| Monthly audit | monthly | local review of stale context and tasks |
| QMD refresh | daily or weekly | refreshed local search index |
| Stale-task review | weekly | local list of old commitments |
| Connector health check | weekly | local connector status note |
| Domain tracker refresh | weekly | local update per selected domain |

## Cron Safety

Scheduled jobs are opt-in. If a user adds automation later, the safe default is:

```text
Run the routine, write a local artifact, and do not contact anyone or update an external system.
```

External delivery requires explicit approval for the exact destination and action.

## Local Customization

Onboarding copies selected routine instructions into:

```text
workspace/routines/
```

Edit those local files instead of changing public core files.
