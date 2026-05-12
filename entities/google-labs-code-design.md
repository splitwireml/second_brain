---
title: design.md
created: 2026-04-24
updated: 2026-04-24
type: entity
tags: [design, ai-design, ai-agents, productivity]
sources:
  - raw/articles/github-google-labs-code-design.md-2026-04-24.md
  - raw/transcripts/2026-04-24-Stitch-by-Google.md
url: https://github.com/google-labs-code/design.md
related_entity: []
---

# design.md

A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a design system by combining machine-readable design tokens (YAML front matter) with human-readable design rationale (markdown prose).

## Setup

Install via npm:

```bash
npm install @google/design.md
```

Or run directly with npx:

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md diff DESIGN.md DESIGN-v2.md
npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.json
npx @google/design.md spec
```

## Key Features

- **Dual-layer format**: YAML front matter for machine-readable tokens + markdown prose for human-readable rationale
- **Token types**: Colors (hex), Dimensions (px/em/rem), Typography objects, Token references (`{path.to.token}`)
- **CLI tools**: `lint` (validate + WCAG contrast checks), `diff` (compare two versions), `export` (Tailwind/DTCG formats), `spec` (output format spec)
- **Linter with 7 rules**: broken-ref (error), missing-primary (warning), contrast-ratio (warning), orphaned-tokens (warning), token-summary (info), missing-sections (info), missing-typography (warning), section-order (warning)
- **Programmatic API**: Import `{ lint } from '@google/design.md/linter'` for Node.js usage
- **Design token interoperability**: Exports to Tailwind theme config and W3C DTCG tokens.json format
- **Structured JSON output**: All CLI commands output machine-parseable JSON for agent consumption

## Architecture / Technical Notes

- **Format status**: `alpha` — under active development, expect changes
- **Token schema**: version, name, description, colors, typography, rounded, spacing, components
- **File structure**: YAML front matter (delimited by `---`) + markdown body with `##` sections in canonical order (Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts)
- **Consumer behavior**: Unknown section headings preserved, unknown color/typography tokens accepted if valid, duplicate section headings rejected
- **Inspired by**: W3C Design Token Format
- **Disclaimer**: Not eligible for Google OSS Vulnerability Rewards Program
