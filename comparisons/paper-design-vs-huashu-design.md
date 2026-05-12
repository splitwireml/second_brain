---
title: "Paper.design vs huashu-design vs Pencil"
created: 2026-04-21
updated: 2026-04-21
type: comparison
tags: [comparison, design-tool, ai-design, html, mcp]
sources: [web/paper.design, web/pencil.dev, web/pencil.dev/download, web/pencil.dev/pricing]
participants:
  - [[paper-design]]
  - [[huashu-design]]
  - [[pencil]]
---

# Paper.design vs huashu-design vs Pencil

Three distinct approaches to AI-mediated design: a canvas-first tool, an agent skill, and a desktop-native design tool.

## Context

The emergence of AI coding agents has fractured the design tool landscape into three irreconcilable philosophies:

1. **Canvas stays, agents join** (Paper.design) — the canvas is irreplaceable for spatial reasoning; agents are execution tools
2. **Canvas is unnecessary** (huashu-design) — agents can design directly in code; the canvas adds no value
3. **Design tool with AI generation** (Pencil) — professional canvas with AI generation via Claude; MCP for programmatic access

All three involve "AI doing design work," but they solve different problems for different users.

## Comparison Matrix

| | **Paper.design** | **huashu-design** | **Pencil** |
|---|---|---|---|
| **Core model** | Visual canvas (Figma-like) + local MCP server | Agent *skill* — writes HTML/CSS/JS files from chat | Desktop canvas + Claude AI generation + MCP tools |
| **Human works in** | GUI (drag, select, arrange) | Terminal + conversation with agent | GUI canvas or CLI |
| **Agent works in** | MCP → reads/writes DOM in the canvas | Writes HTML/CSS/JS/MP4/PPTX files | MCP tools → batch_design, get_screenshot, etc. |
| **Design file format** | Real HTML/CSS DOM (Paper file) | HTML/CSS/JS files + media | `.pen` (JSON, proprietary) |
| **Bidirectional?** | Yes — agent reads design, writes code back | No — one-way artifact generation | Yes — MCP tools read and write `.pen` files |
| **Canvas/GUI** | Yes, full professional canvas | No | Yes, desktop WebGL canvas |
| **MCP / API** | Yes, local MCP server | No | Yes, CLI exposes MCP tools |
| **Design → Code** | Yes, `get_jsx` exports live to React/Tailwind | Yes, agent writes HTML directly | Export to PNG/JPEG/PDF; no code export |
| **Code → Design** | Yes, `write_html` injects into canvas | N/A | No |
| **Collaboration** | Real-time multiplayer, share URL | None (file-based, single user) | Desktop app only; no multiplayer |
| **Pricing** | Free (100 MCP calls/week), Pro $20/mo | Free (personal), commercial requires authorization | Free (currently) |
| **Open source** | No | Yes (GitHub, ~1,357 stars) | No |
| **Team / Funding** | $4.2M seed (Accel + Basecase) | Solo creator (huasheng) | High Agency, Inc. (VC-backed) |
| **Platform** | Desktop app (macOS/Windows) + web | Agent-agnostic (any LLM with skill support) | Desktop app (macOS/Windows/Linux) + CLI + IDE extensions |
| **Primary output** | Design file + optionally React/Tailwind code | HTML/CSS/JS + MP4 + GIF + PPTX files | `.pen` design file + PNG/PDF export |
| **Output ownership** | Paper file + exported code | You own the HTML/CSS files | `.pen` file you own; no code export |
| **Target user** | Professional designers collaborating with AI agents | Terminal-first developers, agent builders | Developers and designers who want AI-assisted design in their workflow |

## Paper.design — The Canvas + Agent Model

Paper.design keeps designers in a visual canvas and connects AI agents via MCP so agents can read and write the design. The agent operates bidirectionally: it can examine the Paper file's DOM (via `get_jsx`, `get_selection`, `get_node_info`) and it can write back (`write_html`, `update_styles`, `create_artboard`).

The key insight from Paper's founding blog post: spatial reasoning — comparing multiple alternatives side by side, exploring visual directions, holding the "road not taken" in view — cannot happen in a chat log. The canvas is where humans do the part agents are bad at. The agent becomes an extension of your hands, not your replacement.

Paper exports designs to real React/Tailwind code via `get_jsx`. The agent can then work in a code editor, and the designer reviews live in the browser. Changes flow back and forth without either side becoming a dead end.

**Who it's for:** Professional designers who want to stay in control of visual decisions while leveraging AI for execution and boilerplate. Teams who need real-time multiplayer collaboration.

## huashu-design — The Agent-Native Model

huashu-design removes the canvas entirely. The agent writes HTML/CSS/JS directly as the design artifact. No visual canvas, no GUI, no multiplayer. The entire workflow is conversation: you describe what you want, the agent embodies domain experts (slide designer, animator, prototyper) and writes finished HTML.

The Core Asset Protocol enforces downloading real brand assets (logos, UI screenshots) before any CSS is written — a discipline borrowed from Claude Design's system prompts. Anti-slop rules prohibit the purple-gradient-emoji-icon defaults that make all AI-generated pages look identical.

**Who it's for:** Terminal-first technical users who want an agent to produce a finished HTML artifact without opening any design tool. Developers building UIs programmatically. Anyone who prefers code review over canvas manipulation.

## Pencil — Desktop Design Tool with AI + MCP

Pencil is a desktop-native design tool built by High Agency, Inc. with AI generation powered by Claude and an MCP interface for programmatic design operations. Tagline: *"Design on canvas. Land in code."*

Unlike Paper.design (which runs as a local web app) or huashu-design (which has no canvas), Pencil is a full desktop application with:
- **Canvas**: WebGL-based professional canvas
- **AI generation**: Claude Opus/Sonnet/Haiku for creating designs from prompts
- **MCP tools**: `batch_design`, `batch_get`, `get_screenshot`, `get_editor_state`, and more — agents can read and write `.pen` files programmatically
- **IDE extensions**: Cursor, VSCode, Windsurf, Google Antigravity
- **CLI**: Headless design generation via `pencil --out design.pen --prompt "..."`

Pencil outputs `.pen` files (JSON format) and exports to PNG/JPEG/WEBP/PDF. There is no code export — the design artifact is the `.pen` file and its rendered images. Currently free.

**Who it's for:** Developers and designers who want AI-assisted visual design within their existing workflow (IDE, CLI), without needing a separate browser-based tool.

## Key Insights

### The canvas question

Paper's thesis is that spatial thinking requires a canvas. huashu-design's thesis is that the canvas is unnecessary overhead — if the agent writes good HTML, the output is the deliverable.

Both positions are defensible. Paper suits designers who think visually and want to stay in a creative tool. huashu-design suits technical users who think in code and prefer to stay in the terminal.

### Bidirectionality

Paper is the only tool where the agent can read *and* write to the design file. huashu-design is agent → output only. Pencil supports bidirectional MCP operations — agents can use `batch_get` to read and `batch_design` to write `.pen` files, but the output is a visual design file not code.

This makes Paper uniquely suited to iterative human-agent collaboration. huashu-design is optimized for agents producing finished artifacts, not for humans and agents jointly iterating on a shared design.

### Ownership

Paper and huashu-design both output code you own. Paper's exported code is React/Tailwind; huashu-design's output is inline HTML/CSS/JS. Pencil outputs a `.pen` design file you own but no code.

### Agent compatibility

huashu-design works with any coding agent that supports markdown skills. Paper requires its own desktop app + MCP server + a connected IDE (Cursor, Claude Code, etc.). Pencil has its own MCP tools exposed via CLI and IDE extensions, but uses a separate `.pen` format not compatible with Paper or huashu-design.

## Practical Verdict

| Use case | Tool |
|---|---|
| Designer wants visual exploration + AI execution help | **Paper.design** |
| Technical user wants finished HTML artifacts from terminal | **huashu-design** |
| Developer wants AI design in their IDE via MCP | **Pencil** |
| Designer wants to hand off to an agent and get code back | **Paper.design** |
| Developer wants low-ceremony design generation in a coding session | **huashu-design** |
| Team needs real-time multiplayer design collaboration | **Paper.design** |
| Solo technical user wants open-source, no account, no quota | **huashu-design** |

## Related Comparisons

- [[paper-design-vs-huashu-design]] — direct comparison of the two design paradigms
- [[claude-design-vs-huashu-design]] — Anthropic's design tool vs agent-native design skill
- [[html-native-design-skill]] — the pattern huashu-design embodies
