---
title: virtio-fs
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [filesystem, microvm, virtio, virtualization]
sources: [raw/articles/xarticle-why-agent-sandboxes-are-converging-on-libkrun-not--2055329887431393309.md]
---

# virtio-fs

## Definition
virtio-fs is a virtio device that provides file system access from a guest to a directory on the host, using a shared memory queue for communication. Unlike virtio-block which exposes a disk image, virtio-fs exposes a directory directly.

## Why It Matters
libkrun uses virtio-fs instead of virtio-block. This means:
- **No image creation**: You point libkrun at a directory and the guest sees that directory
- **No image rebuilds**: Changing a file on the host immediately changes it for the guest
- **No re-pack on cache bust**: OCI images can be unpacked once and reused

For sandboxes that boot arbitrary rootfses from OCI registries, this is dramatically better than Firecracker's block device model.

## Known Issue
libkrun's virtio-fs has a **readdir bug**: calling `ls /` enumerates entries in a pattern that OOM-kills the caller on guests with <1GB RAM. iii-sandbox works around this by pivoting `/` onto a tmpfs and using bind mounts for everything underneath, so no process ever reads the virtio-fs root directly.

## Related Entities
- [[libkrun]] — uses virtio-fs for rootfs
- [[Firecracker]] — uses virtio-block (block device, not directory)
- [[iii-sandbox]] — has work-around for readdir bug