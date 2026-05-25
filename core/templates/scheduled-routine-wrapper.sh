#!/usr/bin/env bash
# Template: safe local Oak scheduled routine wrapper.
#
# Copy this file into an ignored local path before use, for example:
#   local/bin/run-daily-brief.sh
#
# Do not edit or run this public template directly.
# Scheduled wrappers should run with a hard timeout, write logs, produce a
# visible failure, never wait for stdin, avoid interactive permission prompts,
# and avoid injecting text into an already-open user session.

set -o pipefail

export PATH="${PATH:-/usr/local/bin:/usr/bin:/bin}"
OAK_ROOT="${OAK_ROOT:-$HOME/Documents/oak-cos}"
ROUTINE_NAME="${ROUTINE_NAME:-daily-brief}"
LOG_DIR="${OAK_ROOT}/.oak/logs"
ARTIFACT_DIR="${OAK_ROOT}/workspace/artifacts/scheduled"
TIMEOUT_SECONDS="${TIMEOUT_SECONDS:-900}"

mkdir -p "$LOG_DIR" "$ARTIFACT_DIR"
LOG="${LOG_DIR}/${ROUTINE_NAME}.log"

echo "$(date): ${ROUTINE_NAME} starting" >> "$LOG"

if [ ! -f "$OAK_ROOT/AGENTS.md" ] && [ ! -f "$OAK_ROOT/CLAUDE.md" ]; then
  echo "$(date): ${ROUTINE_NAME} failed: OAK_ROOT does not look like Oak: $OAK_ROOT" >> "$LOG"
  exit 2
fi

cd "$OAK_ROOT" || exit 2

PROMPT="Run the ${ROUTINE_NAME} routine from workspace/routines/${ROUTINE_NAME}.md using local workspace context and selected read-only connector context only. Write the result as a local artifact under workspace/artifacts/. Do not send, post, share, invite, delete, archive, label, or change any external system. If a connector is unavailable or stale, say so in the artifact and continue from local context."

if command -v timeout >/dev/null 2>&1; then
  timeout "$TIMEOUT_SECONDS" "${AI_COMMAND:-codex}" <<< "$PROMPT" >> "$LOG" 2>&1
  EXIT_CODE=$?
else
  "${AI_COMMAND:-codex}" <<< "$PROMPT" >> "$LOG" 2>&1 &
  PID=$!
  (
    sleep "$TIMEOUT_SECONDS"
    if kill -0 "$PID" 2>/dev/null; then
      kill -TERM "$PID" 2>/dev/null
      sleep 5
      kill -KILL "$PID" 2>/dev/null
      echo "$(date): ${ROUTINE_NAME} timeout after ${TIMEOUT_SECONDS}s" >> "$LOG"
    fi
  ) &
  WATCHER=$!
  wait "$PID"
  EXIT_CODE=$?
  kill "$WATCHER" 2>/dev/null
fi

if [ "$EXIT_CODE" -ne 0 ]; then
  echo "$(date): ${ROUTINE_NAME} failed with exit ${EXIT_CODE}" >> "$LOG"
  exit "$EXIT_CODE"
fi

if [ -x "$OAK_ROOT/scripts/qmd-update" ]; then
  "$OAK_ROOT/scripts/qmd-update" >> "$LOG" 2>&1 || \
    echo "$(date): ${ROUTINE_NAME} qmd refresh failed" >> "$LOG"
fi

echo "$(date): ${ROUTINE_NAME} complete" >> "$LOG"
