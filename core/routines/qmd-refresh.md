# QMD Refresh Routine

Cadence: daily or weekly.

Default output: refreshed local search index.

Run `./scripts/qmd-update` or the runtime equivalent. It refreshes Oak's fallback
local index, verifies the configured QMD collection points at this Oak root when
the `qmd` binary is installed, runs QMD update/embed, and logs the result under
`.oak/qmd/`.

Do not ingest new private folders without approval.
