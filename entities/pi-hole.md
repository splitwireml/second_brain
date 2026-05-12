---
title: Pi-hole
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [infrastructure, self-hosted, platform]
sources: [raw/articles/homelab-private-cloud-ahmad-2026-05-01.md]
url: https://pi-hole.net/
---

# Pi-hole

Open-source DNS sinkhole (advertisingBlocker + DNS server) that runs on bare metal or as a container/VM. Blocks ads and trackers at the network level by resolving DNS queries against blocklists. Also provides DHCP server capabilities, making it a centralized network management tool for homelabs.

## Role in Homelab Private Cloud

Pi-hole serves as the **private DNS/DHCP control point** in the [[homelab-private-cloud]] architecture. Ad blocking is a bonus feature; the primary value is having one authoritative place for internal service naming.

### What It Provides

- **Private DNS**: internal services get stable role-based names that survive backend moves and service rebuilds
- **DHCP**: centralizes IP address management on the LAN
- **VPN integration**: remote devices on the WireGuard tunnel can resolve the same private names as LAN clients — making remote access feel "native" rather than bolted on

### Naming Pattern

Clients depend on role names, not machine trivia. If a backend moves from one container to another, the name stays stable. Health checks target the role, not a specific IP.

## Relationship to Other Concepts

- [[homelab-private-cloud]] — Pi-hole is the naming layer
- [[wireguard]] — Pi-hole ties VPN clients into the same DNS namespace as LAN

## Sources

- `raw/articles/homelab-private-cloud-ahmad-2026-05-01.md`
