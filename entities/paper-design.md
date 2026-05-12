---
title: Paper.design
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [design-tool, ai-design, html, mcp, design]
sources: [web/paper.design]
related_entity:
  - [[huashu-design]]
  - [[claude-design]]
---

# Paper.design

> *"The canvas must evolve to embrace the new paradigm. It should connect design to code and back, and just work."*
> — Agu S. (Paper.design team)

A professional canvas-based design tool with a Figma-like UI, built on **real HTML/CSS internals** — the design file *is* the DOM. Funded $4.2M seed round (Accel + Basecase). Desktop app (macOS/Windows) + web app. Targets professional designers who collaborate with AI coding agents.

## Overview

Paper.design is a vector GUI design tool where every design element maps directly to HTML/CSS. Unlike Figma (which uses a proprietary format), Paper's canvas is a live DOM — agents can read and write it via MCP without any translation layer. The founding thesis: *"the canvas never learned to speak the same language" as code, and this gap has historically broken the design-to-production handoff. Paper closes that gap natively.*

Key differentiator: the design canvas and the web platform share the same substrate. An agent reading a Paper design reads real CSS properties. When it exports, it produces real React/Tailwind — not a screenshot, not a translation of a custom format.

**The agent workflow (from Paper's docs):**
1. Designer creates frames in the Paper canvas (flex layouts, containers)
2. AI agent connects via MCP from Cursor / Claude Code / Codex / Copilot / OpenCode
3. Agent reads the selected frame via `get_jsx` → examines DOM structure
4. Agent writes code to a local folder (React + Tailwind)
5. Designer reviews in browser, requests changes via chat
6. Agent iterates via `write_html` (injects into canvas) or rewrites code
7. When satisfied, agent commits to git and optionally deploys

Paper's Feb 2026 blog post ("A real space to design in the age of agents") articulates the philosophy: spatial thinking — holding multiple futures visible at once, comparing paths, deciding what matters — cannot happen in a chat log. The canvas is irreplaceable for this. Agents are infinite interns who handle execution and boilerplate; humans provide direction.

## Key Facts

| | |
|---|---|
| **URL** | paper.design |
| **Platform** | Desktop app (macOS, Windows) + web app |
| **Format** | Real HTML/CSS/DOM — no translation layer |
| **MCP** | Local MCP server at `http://127.0.0.1:29979/mcp` |
| **AI integration** | MCP: Cursor, Claude Code, Codex, Copilot, OpenCode |
| **Pricing** | Free (100/week MCP tool calls), Pro $20/mo (1M/week) |
| **Funding** | $4.2M seed (Accel + Basecase, Feb 2025) |
| **Team** | Stephen Haney (founder), Vlad Moroz, Ksenia Kondrashova |
| **License** | Proprietary SaaS |

## MCP Tools (key capabilities)

Paper exposes these tools to connected AI agents:

| Tool | Function |
|---|---|
| `get_jsx` | Export selection as React/Tailwind or inline-styles JSX |
| `write_html` | Inject/replace HTML nodes in the canvas directly |
| `get_selection` | Read currently selected nodes (IDs, names, types, size, artboard) |
| `get_node_info` | Full DOM subtree for a node by ID |
| `get_tree_summary` | Compact text hierarchy of a node's subtree |
| `get_screenshot` | Base64 screenshot of a node (1x or 2x scale) |
| `get_computed_styles` | Computed CSS styles for one or more nodes |
| `create_artboard` | Create new artboard with optional styles |
| `update_styles` | Update CSS styles on existing nodes |
| `delete_nodes` | Delete nodes and all descendants |
| `set_text_content` | Batch text updates on Text nodes |
| `duplicate_nodes` | Deep-clone nodes, returns new ID map |
| `start_working_on_nodes` | Show "being worked on" indicator on artboards |

The MCP server runs locally on the desktop app. Agents connect over HTTP to `localhost:29979/mcp`. Paper also has a **Script and Prompt Engine** (planned) — open a scripter pane and write Paper code or prompt new tools in real time.

## Design Philosophy (from blog)

Core thesis from the Feb 2026 blog post "A real space to design in the age of agents":

1. **Spatial thinking is irreplaceable** — chat cannot hold multiple alternatives side by side for comparison; the canvas can
2. **The bottleneck moved up** — execution is cheap; the scarce resource is *care* and *context coherence*
3. **Canvas + agents > canvas-only or agent-only** — agents as infinite interns; humans as directors of intent
4. **Design-to-code must be bi-directional** — pull reality onto canvas, push decisions back into code, without either side becoming a dead end
5. **20 years of design tooling should compound, not reset** — typography, color science, vectors, filters, all the way to multiplayer

Notable quote on the "slot machine" trap: *"Prompt, wait, output, repeat. It's fast. It's magical. You can have an army of agents now. But the bottleneck had to go somewhere."*

## Design System & Export

Paper supports P3 wide gamut color, OkLCh/OkLab perceptual color science, gradient interpolation, palette extraction. Typography includes system fonts, web fonts, variable settings, OpenType features. Visual effects include shaders, image filters, CSS filters, backdrop filters, shadows.

Export pipeline: `get_jsx` → React/Tailwind. Native Tailwind CSS integration is in progress (partnered with Tailwind team).

Paper Snapshot (planned) — browser extension to copy sections of a live site and paste into Paper for iteration.

## Roadmap Highlights

- **In progress**: CSS Grid layouts, Native Tailwind CSS integration, Fetch live data (MCP agents from APIs/Google Sheets), Host assets from Paper as CDN
- **Planned**: Components with slots (props + slots, aligned with code), Themes and tokens (calc, color-mix, blend modes), Full sharing permissions, Pen tool + vector editing, Icon packs + shadcn integration, LLM smart search + nested folders
- **Canvas-aware agent assistant**: reduce boilerplate by asking agents to do repetitive work
- **Right click → Remix**: fast variations, font pairings, color scales
- **Generate videos**: paste or generate videos in designs
- **Particle system**: advanced visual effects
- **Three.js islands**: embed Three.js inside design files

## Relationship to huashu-design

Paper.design and [[huashu-design]] solve overlapping problems — AI-mediated design — from opposite interaction models:

- **Paper**: designer in visual canvas, agent reads/writes via MCP. Bidirectional.
- **huashu-design**: no canvas at all; agent writes HTML files directly from conversation. Unidirectional artifact generation.

Paper's canvas is the space for spatial reasoning. huashu-design eliminates the canvas entirely — the agent *is* the design tool. See [[paper-design-vs-huashu-design]] for full comparison.

## Relationship to Claude Design

Paper.design and [[claude-design]] (Anthropic) share the "canvas + AI agent" model but differ in implementation:

- **Paper**: real HTML/CSS DOM, local MCP server, desktop app
- **Claude Design**: browser-based GUI, proprietary canvas, Claude.ai-only integration

Paper's MCP makes it agent-agnostic (works with Cursor, Claude Code, Codex, Copilot, OpenCode). Claude Design is tied to Claude.ai. Paper also supports real-time multiplayer collaboration ("share a URL with your team").

## Relationship to Pencil.software

Pencil.software (pencil.software) is a chat-based no-code web app builder — fundamentally different category:

- **Paper**: visual canvas + MCP, designer stays in control
- **Pencil**: you describe what you want → it generates a hosted web app, no canvas, no design file export
- **huashu-design**: agent writes HTML files directly, no canvas, no hosted output

See [[paper-design-vs-huashu-design]] for the three-way comparison.

## Sources

- paper.design (homepage, docs, blog, compare/pencil, pricing, roadmap)
- Blog: "A real space to design in the age of agents" (Feb 27, 2026)
- Blog: "Announcing Paper's $4.2M seed round" (Feb 25, 2025)
- MCP documentation (paper.design/docs/mcp)
