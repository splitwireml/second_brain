---
title: "Pretext Text Measurement Engine"
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [tools, performance]
sources: [raw/articles/x-bookmarks-2026.md, raw/articles/x-bookmarks-weekly.md]
---

# Pretext — Zero-Dependency Text Measurement Engine

## Overview

Cheng Lou's (`@chenglou`, creator of ReasonML/React Season) open-source library for **virtualization and occlusion of hundreds of thousands of text boxes** — each with differing height — without any DOM measurement.

Single linear cache-less traversal of heights. 120fps scrolling and resizing.

## Key Technical Properties

- **Zero dependencies** — pure JS, ~15KB
- **No DOM measurement required** — simplifies visibility check to a single linear traversal
- **120fps** scrolling and resizing even with hundreds of thousands of items
- Handles text boxes with **differing heights** natively (no预先-measured heights needed)

## Performance Numbers

| Approach | Hot path latency |
|----------|-----------------|
| DOM interleaved reads | 43ms |
| Pretext (no DOM access) | 0.09ms |

~477x faster on the hot path.

## Use Cases

- Virtualized lists with varying row heights (e.g. chat interfaces, feeds)
- Canvas-based UIs that need text measurement without DOM round-trips
- Any scenario where DOM reads are a bottleneck

## Installation

```bash
npm install @chenglou/pretext
# or
bun install @chenglou/pretext
```

## Relationship to [[prompt-engineering-patterns]]

Pretext enables AI interfaces to handle long, variable-length outputs (like AI-generated content) with smooth rendering performance. Relevant to prompt output display and streaming text interfaces.

## See Also

- [[prompt-engineering-patterns]] — where this tool could optimize AI-generated content display
- [[html-in-canvas-wicg-proposal]] — canvas rendering context where pretext-style text measurement applies
- [[vibe-kanban-agent-spawning]] — UI rendering in kanban boards could benefit from virtualized text
