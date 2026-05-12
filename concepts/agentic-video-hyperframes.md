---
title: Agentic Video via HTML
created: 2026-04-19
updated: 2026-04-19
type: concept
tags: [agent, video-generation, vibe-coding]
sources: [raw/articles/agentic-video-hyperframes-open-source-bin-liu-2044827628700684463.md]
author: [[bin-liu]]
---

# Agentic Video via HTML

Using HTML/CSS as the agent-native video editing format — the HyperFrames paradigm.

## Definition

HyperFrames (by HeyGen) enables AI coding agents to generate MP4/MOV/WebM videos by writing HTML annotated with `data-` attributes, then rendering through a local toolchain.

Core thesis (Bin Liu): "What the symphony was to Beethoven, play was to Shakespeare — HTML is to agents."

## How It Works

HTML elements get `data-composition-id`, `data-` attributes defining timeline properties. Standard Web syntax + a handful of HyperFrames attributes = video timeline.

```html
<div id="root" data-composition-id="hyperframes-intro">
  <div id="hero" data-start="0" data-duration="3">Text here</div>
</div>
```

Agent writes HTML → HyperFrames renders → MP4 output. No GUI, no manual keyframing, no API calls to external video services.

## Setup

```bash
npx skills add heygen-com/hyperframes
```

## Comparison to Other Approaches

| Approach | Mechanism | Agent-native? | Cost |
|---|---|---|---|
| HyperFrames | HTML/CSS + local render | Yes | Free (local) |
| [[seedance-2-0]] | API calls to ByteDance | Indirect | ~$0.10/sec |
| [[open-montage]] | 12-pipeline agentic system | Yes | $0 free tier (Piper) |
| Kling/Runway | GUI/API | No | Per-second pricing |

## Use Cases

- AI-generated launch videos ([[heygen]] use case)
- Animated marketing websites ([[ai-cinematic-website-design]])
- Loop animations for landing pages

## Related

- [[hyperframes]] — the specific framework
- [[bin-liu]] — primary author
- [[ai-cinematic-website-design]] — marketing website application
- [[seedance-2-0]] — alternative video generation
