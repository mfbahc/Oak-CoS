# Onboarding

Run:

```bash
./scripts/onboard
```

The first question is always:

```text
Where do you plan to run Oak?
```

This comes before file generation so Oak can create the right runtime guidance.

If you are not sure what a question means, use the recommended answer. Onboarding can be rerun later, and changed local files are backed up before replacement.

## Plain-English Terms

- Runtime: the AI tool you plan to use with Oak, such as Codex App or Claude Desktop.
- Configured files: private local setup files Oak writes for you.
- Docs-only guidance: setup notes without a full local workspace.
- Connectors: recommended but skippable outside accounts or tools. They are not active until configured in the runtime.
- QMD/local search: a local search helper so Oak can find notes without reading every file.
- Routines: templates for repeated work, not background jobs.
- Automation host: the awake machine or hosted runner that would run scheduled routines. If the device sleeps or turns off, scheduled work will not run reliably.
- Templates: starter files copied into your private workspace for editing.

## Flow

Onboarding asks for:

- runtime target
- whether to generate configured files, docs-only guidance, or both
- assistant name
- personality or work style, using a soul-style template or `Custom / build my own`
- what the CoS should call the user
- relationship and role
- actions Oak must never take without asking
- domains to support
- first project or domain
- operating cadence
- whether you have an always-on device or hosted runner for scheduled routines
- backup/storage model and whether scheduled jobs need a separate runtime path
- preferred delivery channel, with a reminder to verify actual runtime capability
- email account identities and no-send boundaries
- whether Oak should infer domains/projects from verified read-only connector context
- recommended connector setup, with opt-out choices
- QMD/local search setup
- executive-coaching lens

## Generated Local State

When file generation is enabled, onboarding writes only to ignored paths:

```text
workspace/
local/
.oak/
```

Existing files are backed up before replacement.

Onboarding writes a checkpoint before file generation. If you stop at the review step, rerun:

```bash
./scripts/onboard --resume
```

The generated first-project path creates:

- `workspace/projects/<first-project>/README.md`
- `workspace/domains/<first-project>.md`
- `workspace/artifacts/daily-briefs/<first-project>-first-brief.md`

It also separates identity from user context:

- `workspace/context/assistant-identity.md` for assistant name, role, working style, relationship, and boundaries
- `workspace/context/user-profile.md` for user facts, domains, cadence, and account boundaries
- `workspace/context/onboarding-safety.md` for connector verification, delivery checks, storage/runtime limits, and scheduling safety
- `.oak/onboarding-resume.md` for the next-session prompt

Personality templates are seeds, not fixed personas. They use the six-section SOUL.md pattern described in the [OpenClaw SOUL.md guide](https://clawdocs.org/guides/soul-md/): opening, core truths, boundaries, vibe, continuity, and closing. Oak stores the generated identity in `workspace/context/assistant-identity.md`, not in public files.

A user can choose `Custom / build my own` during onboarding, or edit `workspace/context/assistant-identity.md` later to tune tone, directness, challenge posture, caution areas, and behaviors that feel wrong. Onboarding also copies all public personality templates into `workspace/templates/personality/` so users can compare styles and build their own.

## Value-First Order

The first session should produce useful work, not just infrastructure. Create a first project/domain and starter brief before adding scheduled routines or advanced delivery.

If verified read-only connectors are available, Oak can use them to infer candidate domains/projects and then let the user correct the list. If connectors are unavailable, skipped, or not verified in the current runtime, continue from local context and user answers.

## Pause And Resume

Onboarding writes `.oak/onboarding.checkpoint.json` and `.oak/onboarding-resume.md`. Pause before risky steps such as connector auth, runtime restart, delivery setup, or scheduled jobs. Resume by pasting the prompt from `.oak/onboarding-resume.md`.

After web OAuth or connector authorization, restart or refresh the runtime before assuming the connector is available.

## Demo Mode

For a safe non-interactive run:

```bash
./scripts/onboard --demo
```

Demo mode uses synthetic names, synthetic domains, and synthetic connector choices. It is safe for validation and public examples.

## After Onboarding

1. Open `.oak/START_HERE.md`.
2. Read `.oak/launch-prompts.md`.
3. Run `./scripts/qmd-setup`.
4. Run `./scripts/doctor`.
5. Start Oak in your chosen runtime with the matching launch prompt.
6. Connect the selected runtime connectors, or confirm which ones you skipped.
7. Decide whether routines stay manual/on-demand or run on an always-on host.
8. Add private context gradually instead of importing large folders.

## Reset

To reset local Oak state, move ignored folders aside:

```bash
mv workspace workspace.backup
mv local local.backup
mv .oak .oak.backup
./scripts/onboard
```

Use your system trash if you decide to delete old local state.
