---
name: reading-queue
description: Maintain a private reading queue, current tracker copies, read/superseded state, and one-click review folder.
---

# Reading Queue

Use this for private document queues that support meetings, decisions, reviews, or recurring briefs.

## Queue Rules

- Add documents the user explicitly asks to review.
- Add obvious read candidates for upcoming meetings or decisions.
- Do not add every artifact; keep the queue focused on items the user actually needs to read.
- When the user says an item is read, move or mark it as read.
- When a newer version replaces an unread item, move the old item to superseded rather than deleting the source.
- Never delete source artifacts.

## Source-Backed Current Copies

For living trackers or source-backed briefings, prefer stable "current" filenames in the review folder. Keep an index that records the source path and last refresh time. When a newer source arrives, update the current copy and move stale dated copies out of the active review folder.

## What To Read View

When the user asks what to read, return a practical queue:

- today: items needed for imminent meetings, votes, decisions, or deadlines;
- this week or can wait: useful context that is not blocking;
- stale or superseded: items to move out of the active folder;
- blocked: items that need missing source access or user input.

If the user has a one-click review folder, `scripts/open-reading-queue` can open or print the active `_to-read` folder. Treat that folder as a review surface, not the source of truth.

## Standard Procedure

1. Read the queue index and only the relevant domain/project folder.
2. Make the narrow queue change:
   - add requested or obvious documents;
   - mark read items read;
   - move stale versions to superseded;
   - refresh stable current tracker copies from source artifacts.
3. Update the queue index with active unread, read, and superseded state.
4. Sync or render the one-click review folder if the workspace has one.
5. Verify the active review folder contains only intended current items.
6. Log meaningful queue changes when they affect active work.

## Safety

- Keep private materials in ignored local workspace paths unless the user explicitly chooses a shared destination.
- Do not upload or share queue documents externally unless the user explicitly asks.
- If a cloud-drive mirror fails, keep the local canonical queue correct and report the mirror failure.
