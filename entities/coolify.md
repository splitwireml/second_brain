---
title: Coolify
created: 2026-04-15
updated: 2026-04-15
type: entity
tags: [platform, open-source, self-hosted]
sources: [raw/articles/coollabsio-coolify-2026-04-15.md]
---

# Coolify

An open-source, self-hostable PaaS (Platform as a Service) alternative to Vercel, Heroku, and Netlify. Lets you deploy static sites, databases, full-stack applications, and 280+ one-click services on your own servers via SSH — VPS, bare metal, Raspberry PIs, or any hardware.

## Overview

Coolify positions itself as "the ease of a cloud with your own servers." You install it on one server (the management node) and then register additional servers through SSH to deploy resources onto them. All configurations are saved directly to the managed servers, meaning resources remain running and manageable even if Coolify itself is removed.

**Installation:** Single command: `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash`

**Paid cloud option:** app.coolify.io for users who want the management server hosted by the team — same pricing as a ~$4-5/month VPS but with high availability, free email notifications, and better support.

## Key Facts

| Fact | Detail |
|------|--------|
| Stars | 53,044 (GitHub) |
| Forks | 4,064 |
| Language | PHP |
| License | Apache-2.0 |
| Created | 2021-01-25 |
| Latest release | v4.0.0-beta.473 (2026-04-13) |
| Core maintainers | Andras Bacsai, Peak Labs |
| One-click services | 280+ |

## How It Works

1. Install Coolify on a management server (SSH required)
2. Register additional servers (VPS, bare metal, etc.) via SSH
3. Deploy applications, databases, and services from the Coolify dashboard
4. Resources are configured directly on your servers — no agent on local machine needed

## Relationship to Other Tools

Coolify overlaps with infrastructure-as-code and deployment tooling. It is complementary to:

- [[hermes-agent]] — both are open-source, self-hosted tools; Hermes manages AI coding agents while Coolify manages deployment infrastructure
- [[reclip-video-downloader]] — both are self-hosted, open-source tools deployable via a single install script; ReClip is a specific use-case app while Coolify is a general-purpose platform
- [[searxng]] — both are self-hosted open-source projects; SearXNG handles search aggregation while Coolify handles application deployment
- [[agent-web-stack]] — the three-stage agent web stack (SearXNG → Firecrawl → Camofox) can be self-hosted on Coolify for full local AI tool deployment
- [[vllm]] / [[sglang]] — both Coolify and these inference engines can serve LLM deployment; Coolify could orchestrate vLLM/SGLang instances as managed resources

## Commercial Model

Coolify is fully open-source with no feature paywalls. Revenue comes from:
- Paid cloud hosted version (app.coolify.io)
- Sponsorships (huge list including Hetzner, Hostinger, SerpAPI, RunPod, and 50+ others)

The project has strong enterprise sponsorship presence, with recognitions from Hacker News and Product Hunt.

## Sponsors

**Huge Sponsors:** MVPS, SerpAPI, ScreenshotOne  
**Big Sponsors:** Hetzner, Hostinger, RunPod, American Cloud, Arcjet, Convex, ByteBase, CodeRabbit, Formbricks, Greptile, Logto, Supabase, Tigris, Ubicloud, and 40+ more  
**Small Sponsors:** 50+ listed in README

---

Sources: raw/articles/coollabsio-coolify-2026-04-15.md
