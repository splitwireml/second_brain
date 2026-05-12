---
title: WireGuard
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [infrastructure, self-hosted, security]
sources: [raw/articles/homelab-private-cloud-ahmad-2026-05-01.md]
url: https://www.wireguard.com/
---

# WireGuard

Fast, modern VPN protocol and software (Linux kernel module + userspace tools). Designed to be simpler and more efficient than older VPN protocols like OpenVPN and IPSec. Multi-platform: Linux, macOS, Windows, iOS, Android, and router firmware.

## Role in Homelab Private Cloud

WireGuard serves as the **network entry point** — the first real control point for remote access. In the [[homelab-private-cloud]] architecture:

- Laptop, phone, and tablet connect to a WireGuard endpoint that lands on a VPN concentrator inside the homelab
- The concentrator owns: peer identity, VPN address assignment, split-tunnel and full-tunnel profiles, routes between VPN clients and LAN, and NAT behavior for boundary crossing
- Runs inside an **LXC container** with a small dashboard for peer management (not a heavyweight VPN appliance)

### Tunnel Properties

- **Dual-stack internally**: each peer gets both an IPv4 address and an IPv6 ULA address
- **IPv4-only public endpoint** by design (mobile carriers may block WireGuard UDP over IPv6)
- Client tooling pins the A record if DNS drifts

## Key Concepts from This Setup

### Split Tunnel vs Full Tunnel

Two client modes provisioned per device, activated depending on location:
- **Split tunnel**: only routes necessary traffic through VPN
- **Full tunnel**: all traffic through VPN (useful on untrusted networks)

### SNAT (Source Network Address Translation)

WireGuard VPN peers get addresses from the VPN network, but LAN services expect traffic from the LAN subnet. SNAT at the VPN edge translates source addresses so the LAN sees VPN traffic as coming from stable LAN-side identities (one per peer), preserving device identity through the tunnel without teaching every LAN host a route back to the VPN subnet.

SNAT is NOT a security model — WireGuard handles encryption, peer keys handle tunnel identity, firewall/ACLs handle policy, DNS handles names.

## Relationship to Other Concepts

- [[homelab-private-cloud]] — WireGuard is the access path layer

## Sources

- `raw/articles/homelab-private-cloud-ahmad-2026-05-01.md`
