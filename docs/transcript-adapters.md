# Transcript Adapters

Transcript adapters are optional local extensions that let Oak ingest meeting
records from a user's own transcript source without putting provider-specific
credential logic in the public core.

The public repo does not ship live provider decryption, API tokens, browser
sessions, or personal account logic. Put those pieces in ignored local paths such
as `local/extensions/` or `workspace/extensions/`.

## Adapter Contract

A transcript adapter should expose three read-only operations:

| Operation | Required behavior |
| --- | --- |
| `check` | confirm the source is reachable without printing secrets |
| `list` | return meeting IDs, dates, titles if available, segment counts, and source caveats |
| `export` | write one raw transcript to a private local artifact path |

Adapters must:

- never print secrets, access tokens, decrypted caches, cookies, or session data
- write outputs under ignored private folders
- preserve raw transcript text before summarizing
- include source metadata and attribution caveats
- treat AI summaries as secondary to raw transcript text
- refresh local search/QMD after authorized durable writes
- fail closed when auth, source freshness, or export integrity is uncertain

## Suggested CLI Shape

Use any language, but keep the interface simple:

```bash
local/extensions/transcript-adapter --check
local/extensions/transcript-adapter --list --date YYYY-MM-DD
local/extensions/transcript-adapter --export MEETING_ID --output workspace/artifacts/transcripts/raw.md
```

The `list` output should be structured data where possible:

```json
{
  "ok": true,
  "transcripts": [
    {
      "id": "provider-id",
      "title": "Meeting title if available",
      "date": "2026-01-01",
      "start_time": "2026-01-01T14:00:00Z",
      "segments": 250,
      "source_caveat": "speaker labels are unverified"
    }
  ]
}
```

## Ingestion Flow

1. Run the adapter `list` command for the relevant date or meeting.
2. Export the raw transcript to `workspace/artifacts/`.
3. Run the meeting transcript ingest skill on the raw artifact.
4. Review proposed durable updates before writing, unless the user already
   authorized routine ingestion for that source.
5. Refresh local search with `./scripts/qmd-update`.

## Provider Notes

Granola, Fireflies, Zoom, Google Meet, Teams, and local transcript files can all
fit this adapter shape. Keep provider details in local ignored files because
account storage and export mechanics change frequently.

Do not claim a provider is connected until the adapter has passed `check` and
exported a small non-sensitive test transcript in the runtime that will use it.
