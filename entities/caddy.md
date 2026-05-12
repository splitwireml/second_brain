---
title: Caddy
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [infrastructure, self-hosted, platform]
sources: [raw/articles/homelab-private-cloud-ahmad-2026-05-01.md]
url: https://caddyserver.com/
---

# Caddy

Open-source web server (Go) with automatic HTTPS. Key features: automatic TLS certificate management (via ACME/DNS validation), reverse proxy, HTTP/3 support, and a Caddyfile configuration format.

## Role in Homelab Private Cloud

Caddy serves as the **internal service gateway** — the homelab's application edge. In the [[homelab-private-cloud]] architecture it runs on its own VM and handles:

- **TLS termination** with DNS-validated certificates (through an upstream DNS provider)
- **Public/private route split** — normalizing paths from CDN/proxy, LAN, and private-only traffic
- **Real client IP handling** — trusting the right forwarded headers only from the right sources, stripping spoofed headers

The key property: **the backend can move, the container can restart, the VM can be rebuilt — the client still speaks to the same front door.**

## Why Caddy Specifically

The article notes the gateway must:
1. Handle TLS termination
2. Validate DNS certificates via an upstream provider
3. Split traffic between public and private routes
4. Preserve real client IP through upstream proxies (for useful logs and rate limits)

Caddy's automatic HTTPS and DNS validation support make it suited to this role in the homelab context.

## Relationship to Other Concepts

- [[homelab-private-cloud]] — Caddy is the service gateway layer

## Sources

- `raw/articles/homelab-private-cloud-ahmad-2026-05-01.md`
