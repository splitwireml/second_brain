---
title: LabelMe
created: 2026-04-18
updated: 2026-04-18
type: entity
tags: [tools, computer-vision]
sources: [raw/articles/labelme-v6.1-release-2026-04-16.md]
---

# LabelMe

Offline-first image annotation tool with built-in AI segmentation. Available for Windows, macOS, and Linux. Maintained by [wkentaro](https://github.com/wkentaro) on GitHub.

## Overview

LabelMe is a graphical image annotation tool used for creating computer vision datasets. It supports polygon, rectangle, circle, line, and point annotations. v6.0+ added AI-powered annotation modes using the Segment Anything Model (SAM).

## Key Features

- **AI-Box mode** (v6.1): Drag a single bounding box → SAM3 segments all objects inside separately. Useful for crowds, shelves, and cluttered scenes.
- **AI-Points mode**: Click points to guide SAM3 segmentation.
- **Unified AI toolbar** (v6.1): Consolidated from 4 AI tools to 2 (AI Points → Shape, AI Box → Shape) with polygon/mask toggle.
- **Async canvas repaints** (v6.1): Heavy redraws no longer block the UI.
- **AI model download progress** (v6.1): Progress bar with cancel button during model download (previously froze with no feedback).
- **Folder loading** (v6.1): Opening one image loads the rest of its folder into the file list.
- **Multi-language** (v6.1): Greek, Ukrainian, and Russian translations added.

## v6.1 Migration Notes

- `labelme.utils.lblsave` deprecated → use `imgviz.io.lblsave` instead (old import emits `DeprecationWarning`, will be removed).
- "Open Recent" submenu removed from File menu → use the file list dock or OS file dialog instead.

## Related

- [[sam3-ai-box]] — the SAM3 AI-Box segmentation technique introduced in v6.1
- [[segmentation]] — annotation and segmentation as a task type
- [[computer-vision]] — the broader domain LabelMe operates in
