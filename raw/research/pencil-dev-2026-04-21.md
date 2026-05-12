# Pencil.dev — Raw Research

**Fetched:** 2026-04-21
**Source:** https://www.pencil.dev

## Homepage (pencil.dev)

**Tagline:** "Pencil – Design on canvas. Land in code."

**Downloads section:**
- Pencil Desktop: macOS (Apple Silicon + Intel), Windows (x64 + ARM64, ARM coming soon), Linux (AppImage + Tarball)
- Pencil Extension: Cursor, VSCode, Google Antigravity, Windsurf, Open VSX
- Pencil CLI: `npm install -g @pencil.dev/cli`

## Pricing Page (pencil.dev/pricing)

"Pencil is currently free. In the future, we may introduce paid features or plans. If we do, we'll clearly describe the terms and pricing before you're charged."

## SKILL.md (from @pencil.dev/cli@0.2.5 npm package)

Skill name: `pencil-design`
Version: bundled with CLI 0.2.5

Core capability: Create high-quality visual designs — websites, app screens, dashboards, slides, marketing materials, social media graphics — using natural language prompts.

**Key commands:**
```bash
pencil --out design.pen --prompt "..." --export design.png --export-scale 2
pencil --in design.pen --out design-v2.pen --prompt "..." --export design-v2.png
pencil interactive -o output.pen  # headless MCP shell
pencil interactive -a desktop -i design.pen  # connect to desktop
```

**Models available:** claude-opus-4-6 (default), claude-sonnet-4-6, claude-haiku-4-5

**Timing expectations:**
- Simple designs: 1-2 minutes
- Medium designs: 2-3 minutes
- Complex designs: 3-5+ minutes

**Auth:** Requires Pencil account (`pencil login`) or `PENCIL_CLI_KEY` env var for CI

## README.md (from @pencil.dev/cli@0.2.5)

**CLI tools (MCP):**
- `batch_design` — insert, update, delete, move, copy, replace nodes
- `batch_get` — search/read nodes by pattern or ID
- `get_variables` / `set_variables` — design variables
- `get_editor_state` — document metadata/structure
- `snapshot_layout` — structure with computed bounds
- `find_empty_space_on_canvas` — find available space
- `search_all_unique_properties` / `replace_all_matching_properties` — recursive property operations
- `get_screenshot` — render node to PNG
- `export_nodes` — export to PNG/JPEG/WEBP/PDF
- `get_guidelines` — load guide/style templates

**Image generation:**
- `G(nodeId, "ai", prompt)` — AI-generated image
- `G(nodeId, "stock", keywords)` — Unsplash stock photo

**Interactive shell syntax:**
```
tool_name({ key: value })   Call an MCP tool
save()                      Save the document
exit()                      Exit shell
```

**Environment variables:**
- `PENCIL_CLI_KEY` — CLI API key for CI/CD
- `ANTHROPIC_API_KEY` — Anthropic API key
- `PENCIL_API_BASE` — Backend API base (default: https://api.pencil.dev)
- `DEBUG` — enable debug logging

**Session file:** `~/.pencil/session-cli.json` (separate from desktop app session)

**License:** Proprietary — High Agency, Inc.
