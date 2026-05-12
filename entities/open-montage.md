---
title: OpenMontage
created: 2026-04-12
updated: 2026-04-12
type: entity
tags: [tools, genai, oss-ai, product]
sources: [raw/articles/open-montage-github-repo-2026-04-12.md]
---

# OpenMontage

> The first open-source, agentic video production system. Turn your AI coding assistant into a full video production studio.

**GitHub:** [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)
**Stars:** 1,425 | **Forks:** 261 | **License:** AGPL-3.0
**Created:** 2026-03-29 | **Last push:** 2026-04-12
**Author:** Calesthio AI Labs

## Overview

OpenMontage is an agentic video production system that turns any AI coding assistant (Claude Code, Cursor, Copilot, Windsurf, Codex) into a full video production studio. The agent handles the complete pipeline — research, scripting, asset generation, editing, and final composition — from a plain-language prompt.

The core architectural distinction: **there is no code orchestrator**. The AI coding assistant IS the orchestrator. OpenMontage provides Python tools, YAML pipeline manifests, and Markdown stage director skills — the agent reads these and executes the workflow.

OpenMontage can produce both **image-based animated videos** (via Remotion animating FLUX/SD-generated stills) and **real documentary footage** (via CLIP-indexed stock footage retrieval from Archive.org, NASA, Wikimedia Commons, Pexels, Pixabay).

## Capabilities at a Glance

| Category | Count | Examples |
|----------|-------|----------|
| Production pipelines | 12 | Animated Explainer, Documentary Montage, Talking Head, Cinematic, Clip Factory, Localization & Dub |
| Video providers | 14 | Kling, Runway Gen-4, Veo 3, Grok, Higgsfield, [[minimax-m27]], HeyGen, + local WAN/Hunyuan/CogVideo |
| Image providers | 10 | FLUX, Imagen, Grok, DALL-E 3, Recraft, Stable Diffusion, stock images |
| TTS providers | 4 | ElevenLabs, Google TTS (700+ voices), OpenAI TTS, Piper (local/free) |
| Python tools | 48 | Video gen, image gen, TTS, music, mixing, subtitles, upscaling, face restore |
| Agent skills | 124+ | Pipeline directors, creative techniques, quality checklists, tool skills |

## Free Tier (Zero API Keys)

Out of the box with zero API keys:
- **Narration:** Piper TTS (offline, free)
- **Real footage:** Archive.org + NASA + Wikimedia Commons + Pexels + Unsplash + Pixabay
- **Composition:** Remotion (spring physics, Ken Burns, particle overlays, kinetic typography)
- **Post-production:** FFmpeg (encoding, subtitle burn-in, audio mixing)
- **Subtitles:** Built-in word-level captions

This enables fully-produced documentary montages at **$0** in API costs.

## Architecture

```
tools/              # 48 Python tools (the agent's "hands")
pipeline_defs/      # 11 YAML pipeline manifests (playbook: stages, tools, gates)
skills/             # 124 Markdown skills (HOW to execute each stage)
schemas/            # 15 JSON Schemas (contract validation)
styles/             # Visual style playbooks
remotion-composer/  # React/Remotion video composition engine
lib/                # Core infrastructure
tests/              # Contract tests, QA integration
```

Every pipeline follows: `research → proposal → script → scene_plan → assets → edit → compose`

Each stage has a dedicated director skill. The agent reads the skill, uses tools, self-reviews, checkpoints state, and requests human approval at creative decision points.

**Provider selection:** Scored across 7 dimensions (task fit, output quality, control, reliability, cost efficiency, latency, continuity) with an auditable decision log.

## Example Productions (from README)

| Video | Style | Tools | Cost |
|-------|-------|-------|------|
| "SIGNAL FROM TOMORROW" | Sci-fi trailer | Veo motion clips, soundtrack | ~$1.50 |
| "THE LAST BANANA" | Pixar animation | 6x Kling v3 clips, Chirp3-HD narration | $1.33 |
| "VOID — Neural Interface" | Product ad | GPT-image-1, OpenAI TTS | $0.69 |
| "Afternoon in Candyland" | Ghibli anime | 12x FLUX images, Remotion animation | $0.15 |
| Documentary montage | Real footage | Archive.org, Wikimedia, Pexels | $0 |

## Reference Video Analysis

Can analyze a YouTube Short/Reel/TikTok/local clip and produce:
- What to keep: pacing, hook style, structure, tone
- What to change: topic, visual treatment, angle, narration
- Cost estimate before execution
- 2-3 differentiated concept variants

## Relationship to Other Tools

- **vs. [[open-higgsfield-ai]]:** OpenMontage is a pipeline/orchestration layer on top of providers including Higgsfield. OpenHiggsfield provides the unified multi-model UI (200+ models in 4 studios); OpenMontage provides the end-to-end agentic production workflow. OpenMontage can use OpenHiggsfield's providers.
- **[[reclip-video-downloader]]:** ReClip can supply reference videos for OpenMontage's reference-driven creation flow.
- **[[vibevoice]]:** VibeVoice ASR could supplement OpenMontage's WhisperX transcription pipeline for long-form audio.

## Related Concepts

- [[openmontage-vs-open-higgsfield-ai]] — comparison vs OpenHiggsfield AI; pipeline/orchestration vs unified multi-model UI; OpenMontage uses OpenHiggsfield as a provider within its workflow

## See Also

- [[open-higgsfield-ai]] — Unified multi-model creative suite (200+ models); OpenMontage can use its providers
- [[reclip-video-downloader]] — Video downloader for reference content ingestion into OpenMontage workflows
- [[vibevoice]] — ASR/TTS pipeline; potential supplement to OpenMontage's audio pipeline
- [[gsd-2-ai-vibe-coding-framework]] — Vibe coding framework; OpenMontage is itself a vibe-coding-native application
