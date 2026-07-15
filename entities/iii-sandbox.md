---
title: iii-sandbox
created: 2026-05-19
updated: 2026-05-19
type: entity
tags: [agent, microvm, open-source, rust, sandbox]
sources: [raw/articles/xarticle-why-agent-sandboxes-are-converging-on-libkrun-not--2055329887431393309.md]
---

# iii-sandbox

## Overview
iii-sandbox is the hardware-isolated execution layer for [iii](https://iii.dev/), an open-source engine where every primitive (HTTP routes, queues, agents, sandboxes) is a worker connecting to the engine over WebSocket. Built on [libkrun](https://github.com/containers/libkrun).

## Key Facts
- **Type**: Sandbox daemon / worker
- **Built with**: Rust
- **Hypervisor**: libkrun (via Hypervisor.framework on macOS, KVM on Linux)
- **Architecture**: Fork+exec model for crash isolation between parent daemon and VM
- **Init binary**: [iii-init](https://github.com/iii-hq/iii/tree/main/crates/iii-init) — custom PID 1 in Rust

## Architecture Highlights

### Boot Sequence
1. Caller fires `sandbox::create`
2. Daemon forks `__vm-boot` subprocess with boot params as CLI flags
3. `__vm-boot` links libkrun, configures VM (CPUs, RAM, kernel, filesystem, network)
4. Guest boots, runs iii-init as PID 1
5. Shell Unix socket ready for `sandbox::exec` calls

### Init Binary (iii-init)
Custom Rust PID 1 that handles:
1. `pivot_to_tmpfs_root` — work around virtio-fs readdir bug
2. `mount_filesystems` — bind mounts
3. `mount_virtiofs_shares` — virtio-fs shares
4. `override_proc_meminfo` — fake MemTotal for bun allocator
5. `raise_nofile` — raise RLIMIT_NOFILE to 1M
6. `configure_network` — set up eth0 and DNS if network enabled
7. `exec_worker` — supervisor loop for user commands

### No systemd
Uses a custom 6.4k lines of Rust PID 1 instead of systemd (which is 1.5M and designed for laptops). The init binary knows specific bugs and edge cases of every runtime hosted.

## Related Entities
- [[libkrun]] — underlying VMM
- [[Firecracker]] — alternative VMM (not chosen, would require same init work)
- [[iii]] — parent engine/project
- [[virtio-console]] — host-guest RPC mechanism used
- [[smoltcp]] — network stack used

## Code References
- Sandbox daemon: `crates/iii-worker/src/sandbox_daemon/`
- Init binary: `crates/iii-init/src/`
- VM boot: `crates/iii-worker/src/cli/vm_boot.rs`

## Source
> "The piece of iii-sandbox that took the longest and matters the most isn't in libkrun. It's in iii-init, the PID 1 binary we ship into every guest." — Rohit Ghumare