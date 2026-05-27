---
name: session-launch
description: Start a fresh Oak session from durable local state without importing prior chat context.
---

# Session Launch

Use when the user starts a new day, new thread, or asks Oak to resume cleanly.

## Procedure

1. Read the runtime instruction file: `AGENTS.md` for Codex, `CLAUDE.md` for Claude.
2. Read `workspace/context/assistant-identity.md` if present.
3. Read `workspace/context/current-actions.md` if present.
4. Read only the task rows, observations, project notes, or launch prompt needed for the immediate question.
5. Reconcile contradictions before answering:
   - current user instruction wins;
   - `current-actions.md` controls live sign / check / flag / wait posture;
   - latest tasks and observations beat older briefs or stale manifests;
   - user-confirmed sends/actions beat missing connector evidence.
6. Return:
   - short status;
   - current action items only if decision-relevant;
   - today's high-stakes meetings or constraints;
   - top actions;
   - decisions needed;
   - first recommended action.

## Guardrails

- Do not import old chat history unless the user provides it in this session.
- Do not expand manifests. Treat them as maps.
- Do not mention launch mechanics unless they affect the recommendation.
- Do not send, post, share, invite, or edit external systems without explicit approval for that exact action.

Stop when the user has a clean operating picture and one obvious next action.
