---
title: libkrun
created: 2026-05-19
updated: 2026-05-19
type: entity
tags: [agent, apple-silicon, macos, microvm, open-source, sandbox]
sources: [raw/articles/xarticle-why-agent-sandboxes-are-converging-on-libkrun-not--2055329887431393309.md]
---

# libkrun

## Overview
libkrun is an open-source Virtual Machine Monitor (VMM) written as a C library. It originated as a Red Hat project to power [podman machine](https://podman.io/docs/installation#macos) on macOS. Unlike Firecracker, libkrun works natively on macOS Apple Silicon via [Hypervisor.framework](https://developer.apple.com/documentation/hypervisor).

## Key Facts
- **Type**: C library / VMM
- **Platforms**: Linux (KVM), macOS Apple Silicon (Hypervisor.framework)
- **Note**: Intel Macs not supported (Apple Intel hardware is end-of-life)
- **Rootfs**: Uses [virtio-fs](https://virtio-fs.gitlab.io/) instead of block devices — no image creation needed
- **Network**: Uses [smoltcp](https://github.com/smoltcp-rs/smoltcp) userspace TCP/IP stack

## Why It Matters for Agent Sandboxes
The article argues libkrun is the **only** open-source VMM that provides Firecracker-class isolation on macOS, which is critical because coding agents like Claude Code, Codex, OpenCode, and Cursor run natively on developer MacBooks. Firecracker cannot run on macOS (requires KVM which only exists on Linux).

## Related Entities
- [[Firecracker]] — competing VMM, cloud-focused, cannot run on macOS
- [[iii-sandbox]] — built on libkrun
- [[smoltcp]] — network stack used by libkrun
- [[virtio-fs]] — filesystem mechanism used by libkrun

## Source
> "There is exactly one open-source VMM that meets that bar right now. It's libkrun." — Rohit Ghumare