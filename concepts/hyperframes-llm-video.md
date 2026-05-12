---
title: HyperFrames LLM Video
created: 2026-05-07
updated: 2026-05-07
type: concept
tags: [ai-video, video-generation, llm, html, cost-optimization]
sources: [raw/articles/rames-jusso-hyperframes-2026-05-07.md]
related_entity: [[hyperframes]]
author: [[rames-jusso]]
---

# HyperFrames LLM Video

LLM-driven visual story generation built on top of [[hyperframes]] — HeyGen's open-source HTML-for-video framework. The approach replaces traditional photoreal video generation models (Veo, Sora, Seedance) with LLMs writing HTML compositions, reducing per-story cost to ~$0.02 on cheap cloud models.

## Core Thesis

For many visual products — animated explainers, dashboards-as-video, narrated stories — you don't need photoreal video generation. You can just write code. An LLM generates HyperFrames HTML, which is previewed as live HTML in the browser (no render latency until export), with TTS handling narration and the [[vercel]] AI SDK tying it all together.

## Cost Breakdown

| Model | Cost/Story |
|-------|-----------|
| Gemini 3 Flash (cheap cloud) | ~$0.02 |
| Local model on own GPU | ~zero (electricity only) |
| Claude Sonnet 4.6 + GPT-5.4-mini (frontier) | ~$0.20 |

Previous image-gen approach cost **$0.04+ per image** with hallucination problems (misspelled words, garbled brand names), and every fix required another paid regeneration.

## The Editability Advantage

Once the LLM produces valid HTML, most tweaks are cheap. A misspelled word? Edit the string. Wrong color across 12 chapters? Find-and-replace once. With image generation, each fix was 4 cents and a re-roll with no guarantee of correctness.

## Technical Stack

- **Frontend**: `<hyperframes-player>` web component — zero-dependency, drop into Next.js, vanilla HTML, or any framework; live browser preview of generated compositions without rendering
- **Backend**: Full-stack Next.js on Vercel, Vercel AI SDK for LLM orchestration
- **LLM**: Outlines story + generates HyperFrames HTML
- TTS: Via [[vercel]] AI SDK for narration
- **Optional render**: Vercel Sandbox (Firecracker microVM running Chromium + ffmpeg) + Vercel Blob for MP4 output

## What You Can Build

- Animated changelog reels for SaaS releases
- Dashboards-as-video, weekly metrics auto-generated and shared online
- Language-learning shorts with synced narration and word highlighting
- AI-narrated docs walkthroughs (LLM picks code samples, generates animated explanation)

## Resources

- App: [https://llm-stories-hyperframes.vercel.app/](https://llm-stories-hyperframes.vercel.app/)
- Template: [https://github.com/heygen-com/hyperframes-vercel-template](https://github.com/heygen-com/hyperframes-vercel-template)

## Related Concepts

- [[hyperframes]] — the HTML-for-video rendering layer
- [[agentic-video-hyperframes]] — the broader agentic video pipeline concept
- [[claude-code]] — the coding agent that writes HyperFrames compositions
- [[vercel]] — the platform hosting the Next.js app and AI SDK
- [[heygen]] — the company behind HyperFrames