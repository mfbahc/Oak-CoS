# GitHub Connector Spec

Status: optional integration.

## Use For

Repository, issue, PR, and CI review.

## Permissions

May require repo read access and optional write.

## Default Safety Mode

Read-only initially.

## Setup

Connect GitHub and choose repositories.

## Disable

Revoke token or app access and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not push, merge, comment, close issues, or change repo settings without explicit approval.
