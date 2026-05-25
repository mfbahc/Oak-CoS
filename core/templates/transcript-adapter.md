# Transcript Adapter Template

Use this template when creating a local transcript adapter under
`local/extensions/` or `workspace/extensions/`.

## Purpose

Provider: {{provider_name}}
Runtime: {{runtime_name}}
Owner: {{owner_or_team}}
Default artifact folder: {{default_artifact_folder}}

## Operations

- `check`: confirms source availability without printing secrets.
- `list --date YYYY-MM-DD`: lists candidate transcripts with IDs, titles if
  available, timestamps, segment counts, and caveats.
- `export MEETING_ID --output PATH`: writes the raw transcript to a private local
  artifact path.

## Safety Rules

- Do not print secrets, tokens, cookies, decrypted caches, or full account data.
- Do not write outside ignored private folders.
- Do not upload transcript text to shared folders or external systems by default.
- Preserve raw transcript text before summarizing.
- Treat speaker labels and AI summaries as unverified unless independently
  confirmed.
- Fail closed if the source freshness or auth state is unclear.

## Validation

Record the latest local smoke test:

- Date:
- Command: {{check_command}}
- Result: {{check_result}}
- Caveats: {{source_caveats}}

## Ingest Prompt

```text
Ingest this exported raw transcript as private local context. Preserve source
metadata and attribution caveats, extract decisions/commitments/questions, and
propose durable updates before writing them. Do not create external-ready notes
or contact anyone unless I explicitly ask.
```
