---
title: Code-First Launch Video Production
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [ai-video, video-generation, agent, workflow, coding, content, marketing, product, framework, x-article]
sources: [raw/articles/xarticle-how-we-made-our-yc-launch-video-in-15-days-with-fa-2075672770483269788.md]
related_entity: [[trope]]
author: [[matt-chow]]
---

# Code-First Launch Video Production

A launch-video production pattern in which an AI coding agent works inside the real product codebase and a code-rendered video project, so product visuals remain editable, reusable, and faithful to the shipped interface. The pattern is source-described by Matt Chow's Trope launch-video case study rather than independently verified. ^[raw/articles/xarticle-how-we-made-our-yc-launch-video-in-15-days-with-fa-2075672770483269788.md]

## Core pattern

Instead of recording a finished product or asking an image model to invent a UI, give the agent the product code, design tokens, fixture data, fonts, storyboard, and motion references. The agent can then rebuild product scenes in React/[[remotion]], preserving real interface details and making later changes cheap. ^[raw/articles/xarticle-how-we-made-our-yc-launch-video-in-15-days-with-fa-2075672770483269788.md]

## Pipeline

1. **Prepare the brief:** draft and revise the script from customer calls; choose the talking-head plus product-showcase structure; storyboard key frames with GPT-Image-2; collect motion references in one PDF.
2. **Capture the human footage:** record the talking head in a controlled location, prioritizing lighting and usable microphone audio.
3. **Build in parallel:** run multiple [[claude-code]]/Fable 5 sessions against a Remotion project, roughly one per clip, and merge the resulting edits.
4. **Synchronize and inspect:** transcribe voiceover with [[whisper]] word-level timestamps; render frames; use annotated screenshots and single-frame inspection to correct visual problems.
5. **Finish the mix:** simplify sound effects and music, then use DaVinci Resolve for final audio levels and the social target of -14 LUFS.

## Operating rules

- Give the agent the actual product code so product shots use real UI primitives rather than generic mockups.
- Treat timecodes, screenshots, and physical timing language such as "0.5s longer" as concrete feedback.
- Use code for punch-ins, reframes, easing, and motion blur; upscale filmed footage when needed, but re-render generated UI at native resolution.
- Keep the final editor pass narrow: the hard visual work should already be represented in code.

## Source-reported economics

The source reports 1.5 days of build time and roughly $2.3k at market rates: about $2,250 in Claude usage, $78 for Topaz, and $19 for ElevenLabs. It compares that with agency quotes of $4–8k and 2–4 weeks; these figures remain author-reported claims. ^[raw/articles/xarticle-how-we-made-our-yc-launch-video-in-15-days-with-fa-2075672770483269788.md]

## Related

- [[matt-chow]]
- [[trope]]
- [[remotion]]
- [[claude-code]]
- [[claude-fable-5-loop-design]]
- [[agentic-video-hyperframes]]
- [[viral-launch-system]]
- [[open-montage]]
