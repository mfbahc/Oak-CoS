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
- Connectors: optional outside accounts or tools. They are not active until configured in the runtime.
- QMD/local search: a local search helper so Oak can find notes without reading every file.
- Routines: templates for repeated work, not background jobs.
- Templates: starter files copied into your private workspace for editing.

## Flow

Onboarding asks for:

- runtime target
- whether to generate configured files, docs-only guidance, or both
- assistant name
- what the assistant should call the user
- relationship and role
- personality or work style
- actions Oak must never take without asking
- domains to support
- first project or domain
- operating cadence
- optional connectors
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
6. Add private context gradually instead of importing large folders.

## Reset

To reset local Oak state, move ignored folders aside:

```bash
mv workspace workspace.backup
mv local local.backup
mv .oak .oak.backup
./scripts/onboard
```

Use your system trash if you decide to delete old local state.
