---
title: ClickHouse
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [infrastructure, database, self-hosted]
sources: [raw/articles/homelab-private-cloud-ahmad-2026-05-01.md]
url: https://clickhouse.com/
---

# ClickHouse

Open-source column-oriented OLAP database (Yandex origin) optimized for analytical workloads. Handles massive data volumes with columnar storage, compression, and vectorized query execution. Supports SQL, HTTP interface, and integrations with BI tools and data pipelines.

## Role in Homelab Private Cloud

ClickHouse serves as the **searchable state plane** — the memory of the system — in the [[homelab-private-cloud]] architecture. It runs in its own container and backs operational metadata:

- Logs, traces, agent events, tool calls
- Conversation metadata
- Job artifacts
- Saved web evidence
- Backup metadata
- Health check results
- Restore drill evidence

### State Plane Properties

The state plane is **deliberately separate from the model router** — generation shouldn't depend synchronously on the trace store being perfect. If the state plane is unavailable, clients degrade by spooling or retrying later, rather than turning every model call into an outage.

### MCP Endpoint

ClickHouse exposes an MCP endpoint so agent clients can query the state programmatically.

### Sync Architecture

- Workstations and runtime hosts run near-live file watchers mirroring session archives to the central corpus over SSH
- Proxmox-side timers handle heavier work: backing up conversation surfaces, syncing router proxy traces, running parity checks
- Parity checks confirm the central store agrees with every source host; a specific exit code indicates host-unavailable gap vs confirmed drift

## Related Concepts

- [[homelab-private-cloud]] — ClickHouse is the state plane backend
- [[agent-memory-architecture]] — the state plane concept is related to agent memory principles (selective injection, structured retrieval, scoring, conflict resolution, decay)

## Sources

- `raw/articles/homelab-private-cloud-ahmad-2026-05-01.md`
