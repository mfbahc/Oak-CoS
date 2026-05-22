# Granola Connector Spec

Status: optional integration.

## Use For

Manual transcript ingestion and meeting follow-up extraction.

## Permissions

May require transcript export or read access.

## Default Safety Mode

Manual import initially.

## Setup

Export or connect only after confirming the transcript source and sensitivity.

## Disable

Stop imports, revoke access, and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not ingest transcripts into durable memory or share summaries without explicit approval.
