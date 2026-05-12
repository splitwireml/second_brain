---
title: Pencil
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [design-tool, ai-design, mcp, desktop-app, ide-extension, cli]
sources: [https://www.pencil.dev, https://www.pencil.dev/download, https://www.pencil.dev/pricing, https://registry.npmjs.org/@pencil.dev/cli/0.2.5]
related_entity:
  - [[paper-design]]
  - [[huashu-design]]
---

# Pencil

**Pencil** is a desktop-native design tool with AI generation and MCP agent integration. Tagline: *"Design on canvas. Land in code."* Creates `.pen` files (structured JSON design format) that export to PNG/JPEG/WEBP/PDF, with an MCP server for programmatic design operations.

## Overview

Pencil is distinct from the no-code builder at pencil.software (which was incorrectly documented in the original entry). Pencil is a local-first design application with:

- **Desktop apps**: macOS (Apple Silicon + Intel), Windows (x64 + ARM64), Linux (AppImage + Tarball)
- **IDE extensions**: Cursor, VSCode, Google Antigravity, Windsurf, Open VSX
- **CLI**: `npm install -g @pencil.dev/cli` — headless design generation + interactive MCP shell
- **File format**: `.pen` (JSON-based design document)
- **AI models**: Claude Opus 4.6 (default), Claude Sonnet 4.6, Claude Haiku 4.5
- **Current pricing**: Free (no paid plans currently; "may introduce paid features in the future")

## MCP / Agent Integration

Pencil ships a local MCP server (bundled in the CLI) that agents can invoke for design operations. The CLI's interactive mode exposes MCP tools directly:

### Design Operations
| Tool | Description |
|------|-------------|
| `batch_design` | Insert, update, delete, move, copy, replace nodes |
| `batch_get` | Search and read nodes by pattern or ID |
| `get_variables` / `set_variables` | Read/update design variables |
| `get_editor_state` | Document metadata and structure (with optional schema) |
| `snapshot_layout` | Document structure with computed bounds |
| `find_empty_space_on_canvas` | Find available space for new elements |
| `search_all_unique_properties` | Recursively search node tree properties |
| `replace_all_matching_properties` | Recursively replace properties |

### Visual Operations (headless rendering)
| Tool | Description |
|------|-------------|
| `get_screenshot` | Render a node to PNG |
| `export_nodes` | Export nodes to PNG/JPEG/WEBP/PDF |

### Image Generation
| Operation | Description |
|-----------|-------------|
| `G(nodeId, "ai", prompt)` | AI-generated image |
| `G(nodeId, "stock", keywords)` | Stock photo from Unsplash |

## Workflow

1. **Desktop app**: Drag-and-drop canvas with design tools, AI generation via chat panel, real-time collaboration
2. **IDE extension**: Design inside Cursor/VSCode — no context switching
3. **CLI**: `pencil --out design.pen --prompt "..." --export design.png` — headless AI design generation
4. **Interactive shell**: `pencil interactive -o output.pen` — direct MCP tool access for scripting

## Relationship to Other Tools

### vs Paper.design
Both are canvas-based design tools with MCP integration. Pencil is desktop-native (WebGL/CanvasKit rendering), while Paper runs as a local web app with a React/Figma-like UI. Pencil's design format (`.pen`) is proprietary JSON; Paper exports to HTML/CSS. Pencil positions as "design in your IDE"; Paper positions as "design canvas with agent access."

### vs huashu-design
Both support AI-driven design via agents. Pencil retains the canvas (human designer drives direction), while huashu-design is agent-only (no canvas, outputs HTML artifacts directly). Pencil gives you a visual design file you own; huashu-design gives you generated code you own.

## Key Facts

| | |
|---|---|
| **URL** | pencil.dev |
| **Platform** | Desktop app (macOS/Windows/Linux) + IDE extensions + CLI |
| **File format** | `.pen` (JSON, proprietary) |
| **Output** | PNG/JPEG/WEBP/PDF images, `.pen` design files |
| **AI models** | Claude Opus 4.6, Sonnet 4.6, Haiku 4.5 |
| **Pricing** | Currently free |
| **Open source** | No (proprietary) |
| **Company** | High Agency, Inc. |
| **CLI package** | `@pencil.dev/cli` v0.2.5 (npm) |

## CLI Reference

```bash
# Install
npm install -g @pencil.dev/cli

# Create design from prompt
pencil --out design.pen --prompt "Create a login page" --export design.png --export-scale 2

# Iterate on existing design
pencil --in design.pen --out design-v2.pen --prompt "Make the header blue"

# Interactive MCP shell (headless)
pencil interactive -o output.pen

# Interactive shell (connect to running desktop app)
pencil interactive -a desktop -i design.pen

# Check auth status
pencil status

# List available models
pencil --list-models
```

## Skill File

AI agents can use Pencil via the bundled `SKILL.md` (published with the npm package):

```
https://unpkg.com/@pencil.dev/cli@latest/SKILL.md
https://cdn.jsdelivr.net/npm/@pencil.dev/cli@latest/SKILL.md
```

The skill is auto-versioned with the CLI — update CLI to get the latest skill instructions.

See [[paper-design-vs-huashu-design]] for the three-way comparison.
