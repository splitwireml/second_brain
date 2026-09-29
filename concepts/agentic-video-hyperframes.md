---
title: Agentic Video via HTML
created: 2026-04-19
updated: 2026-09-29
type: concept
tags: [agent, vibe-coding, video-generation]
sources: [raw/articles/agentic-video-hyperframes-open-source-bin-liu-2044827628700684463.md, raw/articles/xarticle-how-to-run-an-ai-video-agency-full-guide-2104231799090217078.md]
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

## Chris's source-described code-video production loop (2026-09-27)

A local X Article by [[everestchris6]] describes a code-first commercial-video workflow. It says `claude opus 5.5` and `gpt-6 astra`, used through [[claude-code]] or [[codex]], can write titles, camera moves, 3D objects, transitions, and the renderable video code; it presents this as a source claim, not an independent capability benchmark. The source routes HTML/GSAP animation through [[hyperframes]] frame by frame into an `mp4`, reporting about one minute for a full `1080p` render, and uses `three.js` for code-built 3D. It names `elevenlabs` for music and HyperFrames' clean sound-effects library. ^[raw/articles/xarticle-how-to-run-an-ai-video-agency-full-guide-2104231799090217078.md]

### Asset-access and provenance gate

The source-specific access prompt puts the Replicate key in `REPLICATE_API_TOKEN`, uses `gpt image 2.5` for stills and `seedance 2.5` to turn an image into a short clip, requires one test image and one test clip, and saves every generation with its prompt so it can be redone. If either named model is unavailable on Replicate, the instruction is to report that rather than switch models. Generated support footage is restricted to storyboard-marked AI shots; real-work shots retain client footage, generated material is labelled as conceptual, and the prompt forbids fake finished jobs, customers, or results. The source reports 720p/24-frames-per-second clips that are upscaled to `1080p` and smoothed to `60 frames` and requires a physical-plausibility check before regeneration. ^[raw/articles/xarticle-how-to-run-an-ai-video-agency-full-guide-2104231799090217078.md]

### Storyboard, components, and visual constraints

The storyboard prompt asks for a 25-second video shot by shot: what is on screen, what moves, hold time, transition, and whether a shot uses client footage, code-built 3D, or generated imagery/clips. It requires useful customer information, no empty frames or static shots, and placeholders instead of invented testimonials, ratings, prices, savings, warranties, or results. The source says to study reference launch videos—28 videos / about 48 minutes in its example—and preserve transition-carrying foreground objects, one continuity object across shots, one main motion plus layered overlaps, variable speed, matched cuts, and business-specific explanatory shots.

For a `three.js` component, the source requires one explanation at a time, HyperFrames compatibility, smooth `60 frames a second`, purposeful speed changes, non-overlapping readable labels, an isolated short-clip render/check, and a report plus simpler suggestion if 3D cannot show the idea clearly. Its roofing example names a layered house/roof (shingles, underlayer, deck, rafters), inspection-photo placement on the roof, and maintain/repair/replace patches; each component is separately built, rendered, and checked before assembly. ^[raw/articles/xarticle-how-to-run-an-ai-video-agency-full-guide-2104231799090217078.md]

### Independent critic and audio loop

The article calls its review process the `gauntlet loop`, credits `matt shumer` / `somethingbig.ai/gauntlet-loop`, and separates builder from a fresh critic that has not seen the build. The critic receives render, brief, and references; ranks problems by severity; checks empty frames, holds, spacing, colliding/flying text, physical errors, and customer-fit music/sound; timecodes each problem; and must not change the video's subject. The source reports five fresh-critic passes plus a final check, stopping when the target bar is met or changes become small; it also tracks nearly frozen screen time.

Audio is source-described as customer-matched rather than tech-launch energy: `elevenlabs` music timed to storyboard sections, two music options, a small set of clean standard effects only at important moments, effects under music, and calm web volume with no effect louder than music. The article's `alder` made-up roofing sample is reported as 28.6 seconds after more than seven full versions, from 10 seconds to 40 and back; over a couple of agent-hours it used 10 AI images and 10 AI clips, with 5 clips in the final. These figures are not independently audited. ^[raw/articles/xarticle-how-to-run-an-ai-video-agency-full-guide-2104231799090217078.md]

## Related

- [[hyperframes]] — the specific framework
- [[bin-liu]] — primary author
- [[ai-cinematic-website-design]] — marketing website application
- [[seedance-2-0]] — alternative video generation
