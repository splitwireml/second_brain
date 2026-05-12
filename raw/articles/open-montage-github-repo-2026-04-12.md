---
updated: 2026-04-12
type: raw
title: OpenMontage — Agentic Video Production System
source_type: github-repo
url: https://github.com/calesthio/OpenMontage
author: calesthio (Calesthio AI Labs)
date: 2026-03-29 (created), last push 2026-04-12
retrieved: 2026-04-12
stars: 1425
forks: 261
language: Python
license: AGPL-3.0
---

# OpenMontage — The First Open-Source Agentic Video Production System

**GitHub:** github.com/calesthio/OpenMontage
**Stars:** 1,425 | **Forks:** 261 | **License:** AGPL-3.0
**Created:** 2026-03-29 | **Last push:** 2026-04-12

Turn your AI coding assistant into a full video production studio. Describe what you want in plain language — the agent handles research, scripting, asset generation, editing, and final composition.

## Core Distinction

OpenMontage can make image-based videos (animated stills via Remotion), but also makes **real video** via free/open-source workflows: the agent builds a corpus from free stock footage and open archives, retrieves actual motion clips, edits them into a timeline, and renders a finished piece.

## Key Stats

- **12 production pipelines** — Animated Explainer, Animation, Avatar, Cinematic, Clip Factory, Documentary Montage, Hybrid, Localization & Dub, Podcast Repurpose, Screen Demo, Talking Head
- **48 Python tools** — video gen, image gen, TTS, music, audio mixing, subtitles, enhancement, analysis
- **124 Markdown skill files** — production skills, pipeline directors, creative techniques, quality checklists
- **14 video providers** — Kling, Runway Gen-4, Google Veo 3, Grok, Higgsfield, MiniMax, HeyGen, plus local (WAN 2.1, Hunyuan, CogVideo, LTX-Video)
- **10 image providers** — FLUX, Google Imagen, Grok, DALL-E 3, Recraft, Local Diffusion, stock images
- **4 TTS providers** — ElevenLabs, Google TTS, OpenAI TTS, Piper (local/free)
- **400+ agent skills** including pipeline directors, creative techniques, quality checklists

## Architecture: Agent-First

There is no code orchestrator. The AI coding assistant IS the orchestrator:

```
User prompt → Agent reads pipeline manifest (YAML) → Stage director skill (Markdown)
→ Python tools (scored provider selection, 7 dimensions) → Self-review (reviewer skill)
→ Checkpoint state (JSON, resumable) → Human approval at creative decisions
→ Pre-compose validation gate → Render (Remotion or FFmpeg) → Post-render self-review
→ Final video output
```

- **Pipeline manifests** (`pipeline_defs/`): YAML definitions of stages, tools, review criteria, success gates
- **Stage director skills** (`skills/pipelines/`): Markdown instruction files teaching the agent HOW to execute each stage
- **Tool registry** (`tools/tool_registry.py`): Scored provider selection across 7 dimensions (task fit, output quality, control, reliability, cost efficiency, latency, continuity)
- **Decision log**: Every provider choice, creative decision, and fallback logged with alternatives considered + confidence scores

## Two Free Paths (Zero API Keys)

| Capability | Tool | What It Does |
|-----------|------|-------------|
| Narration | Piper TTS | Free offline text-to-speech |
| Stock footage | Archive.org + NASA + Wikimedia Commons | Free/open archival footage |
| Extra stock | Pexels + Unsplash + Pixabay | Free (developer keys) |
| Composition | Remotion | Animated video from stills with spring physics, transitions, typography |
| Post-production | FFmpeg | Encoding, subtitle burn-in, audio mixing |
| Subtitles | Built-in | Auto-generated captions with word-level timing |

**Image-based path:** Piper narrates, images provide visuals, Remotion animates.
**Real-footage path:** Documentary pipeline builds a CLIP-indexed corpus from free sources, cuts together actual motion footage.

## Local Video Generation (Free, GPU Required)

```bash
make install-gpu
# Then in .env:
VIDEO_GEN_LOCAL_ENABLED=true
VIDEO_GEN_LOCAL_MODEL=wan2.1-1.3b  # or wan2.1-14b, hunyuan-1.5, ltx2-local, cogvideo-5b
```

## Supported Providers

**Video:** Kling, Runway Gen-4, Google Veo 3, Grok, Higgsfield, MiniMax, HeyGen, WAN 2.1 (local), Hunyuan (local), CogVideo (local), LTX-Video (local), Pexels, Pixabay, Wikimedia Commons

**Images:** FLUX, Google Imagen, Grok, DALL-E 3, Recraft, Local Diffusion (SD), Pexels, Pixabay, Unsplash, ManomCE

**TTS:** ElevenLabs, Google TTS (700+ voices, 50+ languages), OpenAI TTS, Piper (local)

**Music:** Suno AI, ElevenLabs Music, ElevenLabs SFX

**Post:** FFmpeg (always free), Video Stitch, Video Trimmer, Audio Mixer, Audio Enhance, Color Grade, Subtitle Gen

**Enhancement:** Upscale (Real-ESRGAN), Background Remove (rembg), Face Enhance, Face Restore (CodeFormer/GFPGAN)

**Analysis:** WhisperX (transcription), Scene Detect, Frame Sampler, Video Understand (CLIP/BLIP-2)

**Avatar/Lip Sync:** SadTalker/MuseTalk (talking head), Wav2Lip (lip sync)

## Example Costs (from README)

- "The Last Banana" (60s Pixar animation, 6 Kling v3 clips): **$1.33**
- "VOID — Neural Interface" (product ad, OpenAI only): **$0.69**
- "Afternoon in Candyland" (Ghibli animation, FLUX only): **$0.15**
- Zero-key setup: **$0** (Piper + stock + Remotion)

## Agent Compatibility

Works with Claude Code, Cursor, Copilot, Windsurf, Codex — any AI coding assistant that reads files and runs code. OpenClaw-style agents get a dedicated AGENT_GUIDE.md.

## Topics

open-source, video-production, agentic-ai, ai-video, text-to-video, image-to-video, animated-explainer, documentary, stock-footage, remotion, fal-ai, coding-agent, claude-code, cursor, workflow-automation, content-creation