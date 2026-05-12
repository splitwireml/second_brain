---
title: Proxmox
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [infrastructure, platform, self-hosted]
sources: [raw/articles/homelab-private-cloud-ahmad-2026-05-01.md]
url: https://www.proxmox.com/
---

# Proxmox

Open-source virtualization platform (Proxmox VE) that provides a complete infrastructure virtualization stack: KVM hypervisor for VMs, LXC containers, software-defined storage (LVM-thin, ZFS, Ceph), networking, and a web management interface.

## Role in Homelab Private Cloud

In the [[homelab-private-cloud]] architecture, Proxmox serves as the **physical substrate** — the layer that runs the workloads and provides rollback points via snapshots. It is explicitly *not* the cloud by itself; the cloud-like behavior comes from the layers above it (naming, routes, gateways, tokens, health checks, traces, backups).

### What Proxmox Provides in This Stack

- **Lightweight containers (LXC)** for narrow services
- **VMs** for heavier workloads or stronger isolation
- **Snapshots** before risky changes
- **Direct console access** when networking is broken
- **Storage attachment** for stateful services
- **Failure domain separation**

### Storage Stack in This Setup

- Guest root disks on **LVM-thin**
- Bulk data on a MergerFS pool of spinning-rust drives
- **SnapRAID parity** protecting the bulk pool
- **NFS exports** making bulk storage available to other LAN machines

## Relationship to Other Concepts

- [[homelab-private-cloud]] — the architecture concept Proxmox serves as substrate for

## Sources

- `raw/articles/homelab-private-cloud-ahmad-2026-05-01.md`
