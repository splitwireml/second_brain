---
title: Dokploy
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [platform, open-source, self-hosted]
sources: [raw/articles/dokploy-dokploy-2026-04-16.md]
---

# Dokploy

An open-source, self-hostable Platform as a Service (PaaS) alternative to Vercel, Netlify, and Heroku. Built on Docker-native architecture — every resource runs as a container managed by the Dokploy agent/service on target servers.

## Overview

Dokploy positions itself as a free, self-hostable PaaS that handles the full deployment lifecycle: applications, databases, backups, monitoring, and scaling via Docker Swarm. Unlike [[coolify]] (which uses SSH-based server management), Dokploy is entirely container-centric — you deploy Docker images and Docker Compose stacks through the Dokploy dashboard or CLI.

**Installation:** `curl -sSL https://dokploy.com/install.sh | sh`

**Managed cloud:** [app.dokploy.com](https://app.dokploy.com) for hosted management without self-hosting.

**Documentation:** [docs.dokploy.com](https://docs.dokploy.com)

## Key Facts

| Fact | Detail |
|------|--------|
| Stars | 33,044 (GitHub) |
| Forks | 2,349 |
| Language | TypeScript (monorepo: `apps/` + `packages/`) |
| License | Custom (source-available, not Apache-2.0) |
| Created | 2024-04-19 |
| Default branch | `canary` |
| Homepage | dokploy.com |
| Open issues | 462 |
| Discord | discord.gg/2tBnJ3jDJc |

## Architecture

Dokploy is Docker-native — every deployment target must have Docker installed. The Dokploy agent/service runs as a container on target servers and orchestrates deployments. This is architecturally distinct from [[coolify]]'s SSH approach:

- **Agent-based:** Dokploy runs an agent on each target server; Coolify connects via SSH with no agent
- **Container-first:** All resources are Docker containers; Coolify configs are written directly to servers
- **Docker Swarm:** Multi-node clusters use Docker Swarm for container orchestration
- **Traefik:** Integrated as the reverse proxy and load balancer, auto-provisioning SSL certs

## Features

### Application Deployment
- Deploy any runtime as a Docker container: Node.js, PHP, Python, Go, Ruby, any language with a Dockerfile
- Native Docker Compose support for multi-container applications
- Built-in build process with automatic SSL via Traefik Let's Encrypt
- One-click templates: Plausible, Pocketbase, Calcom, and more via the templates marketplace

### Databases
- Managed MySQL, PostgreSQL, MongoDB, MariaDB, Redis
- Automated database backups to external storage destinations (S3, Backblaze, etc.)
- Persistent storage management

### Multi-Node and Scaling
- Docker Swarm-based cluster management across multiple nodes
- Docker overlay networking for cross-node communication
- Traefik load balancing with automatic service discovery
- Horizontal pod autoscaling (Docker Swarm replicated services)

### Monitoring and Operations
- Real-time monitoring: CPU, memory, storage, network per resource
- Deployment notifications via Slack, Discord, Telegram, Email
- Full REST API and CLI (see github.com/Dokploy/cli)
- Web dashboard for visual management

### Templates Marketplace
Dokploy hosts a curated [templates repo](https://github.com/Dokploy/templates) (184 stars) alongside an [examples repo](https://github.com/Dokploy/examples) (92 stars). These provide one-click deployment configs for popular open-source apps.

## Repository Structure

```
Dokploy/dokploy     — Main application (33K stars)
Dokploy/cli         — Dokploy CLI tool
Dokploy/templates  — One-click deployment templates
Dokploy/examples    — Example deployment configs
```

## Relationship to Other Tools

- [[coolify]] — direct competitor; SSH-based vs Docker-native; Apache-2.0 vs custom license; 280+ one-click vs templates marketplace
- [[hermes-agent]] — both open-source, self-hosted tools; Dokploy manages deployment infrastructure, Hermes manages AI coding agents
- [[vllm]] / [[sglang]] — Dokploy can orchestrate LLM inference servers as managed Docker containers alongside other workloads
- [[agent-web-stack]] — the SearXNG → Firecrawl → Camofox pipeline can be self-hosted on Dokploy for full local AI tool deployment

## Commercial Model

Dokploy is source-available with no feature paywalls in the self-hosted version. Revenue comes from:
- Paid managed cloud at app.dokploy.com
- GitHub Sponsors for the maintainer (Siumauricio)

## Comparison with [[coolify]]

See [[dokploy-vs-coolify]] for detailed side-by-side analysis covering architecture, licensing, ecosystem, multi-node strategy, and when to choose which.

---

Sources: raw/articles/dokploy-dokploy-2026-04-16.md
