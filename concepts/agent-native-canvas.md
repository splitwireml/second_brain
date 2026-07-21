---
title: Agent-Native Canvas
created: 2026-07-19
updated: 2026-07-19
type: concept
tags: [ai-agent, agent-systems, agent-tool, tools, local-first, design-tool, ai-design, workflow, framework, desktop-app, software]
sources: [raw/articles/xarticle-introducing-tldraw-offline-2077784657869902121.md]
related_entity: [[tldraw-offline]]
author: [[tldraw]]
---

# Agent-Native Canvas

An **agent-native canvas** is a visual canvas whose persisted file is directly accessible to a local AI agent as an editable artifact, rather than only as a human-facing GUI session. The source’s tldraw offline launch is a concrete example: the app has no account or server, keeps files on the computer, and lets agents access, edit, and script those files. ^[raw/articles/xarticle-introducing-tldraw-offline-2077784657869902121.md]

## Core pattern

1. **File as substrate** — the canvas document lives locally and can be opened, saved, and manipulated like a normal project artifact.
2. **Agent-readable operations** — an agent can create shapes, import assets, observe changes, and modify the document through the product’s SDK or scripts.
3. **Persistent behavior** — scripts can load with the file, react to external data, or communicate with other software, turning an individual document into a small application.
4. **Human-plus-agent surface** — people can draw, diagram, annotate, and wireframe while agents handle repeatable construction or implementation work.

The tldraw article describes these capabilities as source-reported; it does not establish a security model, compatibility matrix, or independent benchmark. ^[raw/articles/xarticle-introducing-tldraw-offline-2077784657869902121.md]

## Distinction from adjacent patterns

This narrows [[agent-native-apps]] to a spatial, artifact-centered interface. It differs from a conventional browser canvas that an agent can only control through UI automation: the local file and SDK expose a more direct programmatic surface. [[paper-design]] is a related canvas-plus-agent model, while [[ai-design-workflow]] describes a broader plan-in-design-then-ship pipeline rather than this specific file-native substrate.

## Related

- [[tldraw-offline]] — source-described product example
- [[tldraw]] — source author identity
- [[agent-native-apps]] — broader agent-facing software category
- [[ai-design-workflow]] — adjacent AI design workflow
- [[paper-design]] — related canvas-plus-agent product
- [[claude-code]] — one of the local agents named by the source
