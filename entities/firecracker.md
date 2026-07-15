---
title: Firecracker
created: 2026-05-19
updated: 2026-05-19
type: entity
tags: [agent, aws, cloud, microvm, open-source, sandbox]
sources: [raw/articles/xarticle-why-agent-sandboxes-are-converging-on-libkrun-not--2055329887431393309.md]
---

# Firecracker

## Overview
Firecracker is an open-source Virtual Machine Monitor (VMM) originally developed by AWS for [Lambda](https://aws.amazon.com/lambda/) and released in 2018. It implements the "microVM" concept: minimal device model (no BIOS, PCI, VGA), fast boot times (sub-second), low overhead (few MBs).

## Key Facts
- **Type**: VMM (process-based, not a library)
- **Platform**: Linux only (x86_64 or aarch64 with KVM)
- **Rootfs**: virtio-block device backed by ext4 image on host
- **Created by**: AWS (for Lambda serverless sandboxes)
- **Released**: 2018

## Limitations
Firecracker **cannot run on macOS**. It requires `/dev/kvm` which is a Linux kernel module. Apple Silicon occupies that architectural slot with Hypervisor.framework. Running Firecracker on a Mac requires nested virtualization (VM inside VM), which has real performance costs and defeats the purpose of fast local sandboxes.

## Relationship to libkrun
The article positions Firecracker as the right answer for **cloud-side** agent sandboxes (where agents run in a data center), while libkrun is the right answer for **local-first** agents (CLI tools, IDE plugins running on developer machines).

## Related Entities
- [[libkrun]] — the alternative VMM that works on macOS
- [[iii-sandbox]] — built on libkrun (not Firecracker)

## Source
> "People shouting Firecrackers as the future sandbox everyone needs assumes the agent and the sandbox both live in someone else's data center." — Rohit Ghumare