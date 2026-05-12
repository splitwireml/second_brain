---
title: Homelab Private Cloud
created: 2026-05-01
updated: 2026-05-03
type: concept
tags: [self-hosted, platform, local-first, infrastructure]
sources: [raw/articles/homelab-private-cloud-ahmad-2026-05-01.md]
related_entity: [[proxmox]]
author: [[theahmadosman]]
---

# Homelab Private Cloud

The architecture pattern of building a cloud-like operating model on local homelab hardware — treating local servers, workstations, and dedicated appliances as a private platform with control planes for access, routing, naming, compute, and state.

## Core Idea

A homelab running local hardware (servers, workstations, appliances) is organized as a private platform rather than a collection of one-off services. The same physical machines serve as the substrate; the cloud-like behavior comes from the layers above: private DNS, VPN access, service gateways, model routing, searchable state, and compute fabric.

The key distinction: **"I run some services at home"** vs **"I have a private control plane for my own infrastructure."**

## Architecture Layers

### Physical Substrate
Local hardware — workstation-class nodes, containers, VMs, storage — managed via [[proxmox]] as the virtualization layer. SnapRAID provides parity protection. Bulk data on MergerFS pools; guest root disks on LVM-thin.

### Access Path
[[wireguard]] VPN with split-tunnel and full-tunnel modes. SNAT preserves device identity across VPN/LAN boundaries. [[pi-hole]] provides private DNS/DHCP for stable role-based naming.

### Service Gateway
[[caddy]] running as the internal service gateway — TLS termination, DNS-validated certificates, public/private route split. Stable front doors so backends can move without clients needing to know.

### Agent Plane
Model routing layer with generated client profiles — a read-only registry publishes model catalogs and route metadata; an authenticated router validates machine tokens before forwarding requests. Each LAN machine has its own router token for independent revocation.

The agent plane handles: chat completions, embeddings, reranking, RAG queries, and Anthropic-format message translation through a single authenticated front door.

### Web Evidence Lane
[[searxng]] + [[firecrawl]] + headless browser + evidence gateway. A lane in the homelab for search, scraping, crawling, and browser automation with a saved evidence cache so agent decisions can be audited.

### Searchable State Plane
[[clickhouse]] backing operational metadata: logs, traces, agent events, tool calls, conversation metadata, job artifacts, web evidence, backup metadata, health check results. MCP endpoint for programmatic agent queries.

### Compute Fabric
GPU VM (e.g., RTX 3070) for local llama.cpp inference, dedicated LAN model appliances exposing OpenAI-compatible APIs, cloud provider routes for heavy lifting. Work placement directed by the model router.

### Operations
- Snapshots before risky changes
- Health checks (health-only + real-client smoke tests)
- Parity checks between central store and source hosts
- Restore drills for the state plane and conversation surfaces

## Key Design Principles

1. **Boring foundation first** — virtualization, DNS, VPN, gateway, backups before GPUs and AI tools
2. **Role names, not machine trivia** — clients depend on stable role names; backends can move without rewiring
3. **Stable front doors** — the gateway is the one constant; backends are disposable
4. **Explicit boundaries** — LAN membership doesn't imply public API access
5. **Clients of the platform** — UIs are clients with allowlisted routes, not trusted everything-boxes
6. **Platform handles routing** — clients don't need to know the topology; they use stable entry points

## What Makes It "Cloud" vs Just "Homelab"

A reverse proxy is only one layer. The full system has multiple control planes:

- Network access control (VPN + firewall policy)
- Naming and discovery (private DNS)
- Application routing (service gateway)
- Model and provider routing (agent plane)
- Evidence routing (web tools lane)
- Operational memory (state plane)
- Work placement (compute fabric)
- Safety (backups, snapshots, health checks)

The operating model — not the hardware — is what makes it feel like cloud.

## Quote

> No, I did not duplicate my homelab to the cloud. My homelab became the cloud I use.
> — [[theahmadosman]]

## Related Concepts

- [[hermes-memory-architecture]] — principles for machine-scale agent memory (related to the state plane pattern)
- [[agent-web-stack]] — three-stage agent web access pipeline (related to the web evidence lane)

## Related Entities

- [[proxmox]] — the virtualization substrate
- [[wireguard]] — VPN edge
- [[caddy]] — internal service gateway
- [[clickhouse]] — searchable state plane backend
- [[searxng]] — candidate source discovery in web evidence lane
- [[firecrawl]] — known-URL scraping in web evidence lane
- [[obscura]] — Rust headless browser for hard-to-render pages
- [[theahmadosman]] — X creator who authored this pattern
