# Routines

Routines are templates for repeated work, not background jobs. They help Oak repeat useful workflows such as a morning brief or weekly review using the local workspace and any selected read-only connectors.

Onboarding asks whether the user has an always-on device or hosted runner. That answer determines whether scheduled routines should be treated as realistic or just documented for later.

## Day 1

Use routines manually:

- run onboarding
- open `workspace/routines/`
- ask Oak to run one routine using local data, selected read-only connector context, or synthetic data
- keep outputs in `workspace/artifacts/`

No routine sends messages, creates calendar events, shares files, or posts updates by default.

## Safe Local Examples

Morning daily brief:

```text
Run the daily brief routine using my project/domain context and selected read-only connector context such as Calendar or Google Drive. Write the brief under `workspace/artifacts/` and do not contact anyone.
```

Evening wrap:

```text
Run the evening wrap routine. Summarize open loops, completed work, and tomorrow's first useful action. Write a local note only.
```

Meeting prep:

```text
Prepare me for [MEETING] using local notes and selected read-only connector context such as Calendar, Google Drive, email, or transcripts. Return purpose, decisions, questions, risks, and follow-ups. Do not send an agenda.
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
| Daily brief | daily | brief in `workspace/artifacts/` from local and selected connector context |
| Evening wrap | daily | local wrap and open loops |
| Weekly review | weekly | local retro and next-week focus |
| Monthly audit | monthly | local review of stale context and tasks |
| QMD refresh | daily or weekly | refreshed local search index |
| Stale-task review | weekly | local list of old commitments |
| Connector health check | weekly | local connector status note |
| Domain tracker refresh | weekly | local update per selected domain |

## Cron Safety

Scheduled jobs are opt-in. They only run reliably when the chosen host is awake, online, and allowed to run background jobs.

Use manual/on-demand routines when:

- the workspace lives on a laptop that sleeps
- the computer is often shut down
- network access is unreliable
- connector sessions require an interactive login

Use scheduled routines only when the user has one of:

- an always-on Mac or desktop
- a home server or NAS
- a cloud runner or hosted scheduler
- another device that stays awake at the scheduled times

If a user adds automation later, the safe default is:

```text
Run the routine, write a local artifact, and do not contact anyone or update an external system.
```

External delivery requires explicit approval for the exact destination and action.

## Reliability Requirements

Scheduled wrappers should:

- run from the intended runtime root, not a stale backup path
- set a hard timeout
- write logs to a known local path
- report visible failure when a run fails or times out
- never wait for stdin or an interactive permission prompt
- avoid injecting text into a running terminal or TUI session
- verify connector and delivery capabilities before the first scheduled run

If these requirements are not met, keep the routine manual/on-demand.

## Delivery Reality

Before enabling delivery, verify what the runtime can actually do. Email may only support draft creation. Slack, Drive files, or local artifacts may be safer default destinations. Discord and personal messaging apps require runtime-specific checks and are manual relay by default in the public starter.

## Migration And Retirement

If the user already has another assistant or scheduled system, do not retire it immediately. Run Oak side-by-side until the new routine has produced verified useful output for the same job and duplicate delivery risk is understood.

## Local Customization

Onboarding copies selected routine instructions into:

```text
workspace/routines/
```

Edit those local files instead of changing public core files.
