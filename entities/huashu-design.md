---
title: huashu-design
created: 2026-04-21
updated: 2026-04-24
type: entity
tags: [design-tool, agent-tool, html, open-source, skill]
sources:
  - https://github.com/alchaincyf/huashu-design
  - raw/articles/huashu-design-readme-en-2026-04-21.md
related_entity:
  - [[paper-design]]
  - [[claude-design]]
  - [[pencil]]
---

# huashu-design

Agent-native design skill that writes HTML/CSS/JS files directly from conversation. No canvas, no GUI — the agent embodies domain experts (slide designer, animator, prototyper) and produces finished HTML artifacts.

See [[paper-design-vs-huashu-design]] for comparison with Paper.design and Pencil.

## Installation

### Prerequisites

| Requirement | Details |
|---|---|
| **Runtime** | Node.js 18+ (for `npx`) |
| **Agent** | Claude Code, Cursor, Trae, Codex, OpenClaw, Hermes, or any markdown-skill-capable agent |
| **Browser** | Chromium (for Playwright-verified prototypes and video export) |
| **Internet** | Required for first-run asset download and npm install |

### Install

```bash
npx skills add alchaincyf/huashu-design
```

This clones the skill to `~/.claude/skills/alchaincyf/huashu-design/` (Claude Code) or the equivalent skills directory for other agents. No npm install step needed — all dependencies are bundled.

### Agent Compatibility

| Agent | Status | Notes |
|---|---|---|
| Claude Code | ✅ Full support | Primary target |
| Cursor | ✅ Full support | Chat or Composer |
| Trae | ✅ Full support | |
| Codex | ✅ Full support | Via `claude --code` or direct |
| OpenClaw | ✅ Full support | Markdown skill format |
| Hermes | ✅ Full support | Via skill loader |
| Other agents | ✅ Compatible | Any agent that reads `.md` skill files |

### First-Run Verification

After install, verify the skill is loaded by asking your agent:

```
"What capabilities does huashu-design have?"
```

A properly loaded skill responds with a summary of its capabilities — slide decks, prototypes, motion, infographics, design critique.

### What Gets Installed

```
~/.claude/skills/alchaincyf/huashu-design/
├── SKILL.md           # Main agent instruction doc (Chinese)
├── README.en.md       # English README
├── assets/
│   ├── animations.jsx    # Stage + Sprite + Easing + interpolate APIs
│   ├── ios_frame.jsx     # iPhone 15 Pro bezel
│   ├── macos_window.jsx
│   ├── browser_window.jsx
│   ├── deck_stage.js     # HTML deck engine
│   ├── showcases/       # 24 prebuilt samples (8 scenes × 3 styles)
│   └── bgm-*.mp3       # 6 scene-specific background tracks
├── references/          # Drill-down docs by task type
├── scripts/             # Export toolchain (MP4, PPTX, PDF)
└── demos/               # Capability demos with GIF/MP4/HTML
```

### Post-Install: Brand Asset Protocol

For brand-specific work, the skill enforces a **5-step asset gathering workflow** before writing any CSS. The agent will ask for:

1. Logo (SVG preferred → inline SVG → social avatar fallback)
2. Product shots (hero → press kit → video frames → AI-generated from reference)
3. UI screenshots (App Store → official video frames)
4. Color palette + fonts
5. Brand guidelines (if any)

If no assets are provided, the skill falls back to its built-in 20 design vocabularies — still avoids AI slop defaults but quality drops to 60–65/100. **Best results require real brand assets.**

### Uninstall

```bash
rm -rf ~/.claude/skills/alchaincyf/huashu-design
```

Or re-add a different version via `npx skills add alchaincyf/huashu-design` (overwrites existing).

## Quick Start

Once installed, talk to your agent:

```
"Make a keynote for AI psychology. Give me 3 style directions to pick from."
"Build an iOS prototype for a Pomodoro app — 4 screens, actually clickable."
"Turn this logic into a 60-second animation. Export MP4 and GIF."
"Run a 5-dimension expert review on this design."
```

## Capabilities

| Capability | Deliverable | Typical time |
|---|---|---|
| Interactive prototype (App / Web) | Single-file HTML · iPhone bezel · clickable · Playwright-verified | 10–15 min |
| Slide decks | HTML deck (browser) + editable PPTX (real text frames) | 15–25 min |
| Motion design | MP4 (25fps / 60fps interpolation) + GIF + BGM | 8–12 min |
| Design variations | 3+ side-by-side · live param tweaks | 10 min |
| Infographic / data viz | Print-quality typography · PDF/PNG/SVG export | 10 min |
| Design direction advisor | 5 schools × 20 philosophies · 3 directions with demos | 5 min |
| 5-dimension expert critique | Radar chart + Keep/Fix/Quick Wins punch list | 3 min |

## Core Mechanics

**Core Asset Protocol** — Mandatory for brand-specific tasks: ask → search official channels → download (3 fallback paths) → verify + extract → freeze to `brand-spec.md`. Never guess brand assets from memory.

**Junior Designer Workflow** — Send full question set in one batch; write assumptions + placeholders into the HTML early; show to user before filling in real content; iterate through variations.

**Anti AI-slop Rules** — Avoid common AI visual defaults (purple gradients, emoji icons, rounded corners, SVG silhouettes). Use `text-wrap: pretty`, CSS Grid, serif display faces, oklch colors.

## Output Formats

- **HTML** — single-file, self-contained; iPhone/Android/macOS/browser frames available
- **MP4 / GIF** — 25fps or 60fps interpolated; optional BGM scored to scene
- **PPTX** — editable PowerPoint with real text frames (not image-bed fakes)
- **PDF / PNG / SVG** — for print-grade infographics and data visualizations

## vs. Other Design Tools

- **vs Paper.design**: Paper keeps a canvas (human drives direction, agent reads/writes via MCP). huashu-design has no canvas at all — agent writes HTML files directly.
- **vs Claude Design**: Claude Design is a better graphics tool. huashu-design makes the graphics-tool layer disappear entirely. Two paths, different audiences.
- **vs Pencil**: Pencil retains the canvas. huashu-design is agent-only with no design file export — you own the generated code.

## Limitations

- No layer-editable Figma/Keynote round-trip; output is HTML (screenshot/recordable, not draggable)
- Framer Motion-tier complex animations (3D, physics, particles) are out of scope
- Brand-from-zero quality drops to 60–65 points — best results with provided brand assets

## Repository

```
huashu-design/
├── SKILL.md                  # Main doc (Chinese, read by agent)
├── README.en.md              # English README
├── assets/                   # Starter components
│   ├── animations.jsx       # Stage + Sprite + Easing + interpolate
│   ├── ios_frame.jsx        # iPhone 15 Pro bezel
│   ├── macos_window.jsx
│   ├── browser_window.jsx
│   ├── deck_stage.js         # HTML deck engine
│   ├── showcases/            # 24 prebuilt samples (8 scenes × 3 styles)
│   └── bgm-*.mp3            # 6 scene-specific background tracks
├── references/               # Drill-down docs by task
├── scripts/                   # Export toolchain (video, PPTX, PDF)
└── demos/                     # Capability demos with GIF/MP4/HTML
```

## License

Personal use is free and unrestricted. Enterprise or commercial use requires authorization from Huasheng.

## Author

[[huasheng]] (花叔) — AI-native independent developer and content creator. Also known for Nüwa.skill (12k+ GitHub stars), Cat Fill Light (App Store Paid #1), and *A Book on DeepSeek*.
