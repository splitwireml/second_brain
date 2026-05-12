---
title: Defileo thread export failure
created: 2026-05-04
updated: 2026-05-04
type: concept
tags: [thread, export-failure, bird-read-failure]
sources: [raw/articles/thread-defileo-2050656413006053793.md]
related_entity: [[defileo]]
author: [[defileo]]
---

# Defileo thread export failure

A [[defileo]] thread from May 2, 2026 (tweet ID 2050656413006053793) that initially failed to export via `bird read --json-full`. **RECOVERED on re-ingest**: full 8,728-character X Article successfully captured via `bird read --json`.

## Metadata

||-
||
|| **Tweet ID** | 2050656413006053793 |
|| **Likes** | 210 |
|| **Retweets** | 18 |
|| **Characters** | 8,728 |
|| **Subject** | [[kimi-k2.6]] agent swarm |
|| **External URL** | https://kimi.com |
|| **Export Status** | ✅ Recovered (2026-05-04) |

## History

- Initial ingest (2026-05-04): `bird read --json-full` failed; only metadata captured
- Re-ingest (2026-05-04, same tweet ID): `bird read --json` succeeded; full article recovered

## Pattern

This entry documents a recurring pattern in the wiki for high-engagement tweets where `bird read --json-full` fails (likely due to rate-limiting on the `--json-full` flag) but standard `bird read --json` succeeds. The `--json-full` flag appears to trigger different rate-limit behavior than the standard JSON output.

See also: [[teddy-riker]], [[raytar]], [[ig-claims]] — other threads with the same initial export failure pattern.

## Related

- [[defileo]] — Author
- [[kimi-k2.6]] — Primary subject of the thread
- [[karpathy-claude-md]] — Defileo's prior thread on Claude Code behavioral config (successfully exported)
