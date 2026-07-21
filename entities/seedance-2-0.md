---
title: Seedance 2.0
created: 2026-04-13
updated: 2026-07-21
type: entity
tags: [product, tools, genai, marketing, video-generation]
sources: [raw/articles/stijn-feijen-claude-seedance-makeugc-system-2026-04-13.md, raw/articles/frederikfeldt-seedance-pricing-2026-04-16.md, raw/articles/viktoroddy-gemini-seedance-websites-2026-04-17.md, raw/articles/vadoo-seedance-2-0-commercial-playbook-2045849016664248762.md, raw/articles/seedance-2-0-new-default-video-model-2045221480120885529.md, raw/articles/gpt-image-2-seedance-2-character-consistency-workflow-2075327959586537848.md, raw/articles/14-second-ai-vlog-method.md]
---

# Seedance 2.0

## Overview

Seedance 2.0 is the video-generation layer in the [[ai-ugc-ad-scaling-system]] documented by [[stijn-feijen]]. In the source thread, it is used through [[makeugc]] to generate AI creators, voiceovers, product demonstrations, and full ad scenes for short-form performance marketing.

## Function in the workflow

The source positions [[seedance-2-0]] between scripting and distribution:

- Claude produces hooks and scripts
- [[seedance-2-0]] turns those scripts into video assets
- [[makeugc]] handles publication, testing, and scale

The output formats named in the source are:

- 9:16 for TikTok and Instagram Reels
- 16:9 for Meta ads

## Pricing context (per Frederik Feldt, 2026-04-16)

[[frederikfeldt-seedance-pricing]] claims ByteDance's raw API cost is ~$0.10/second of video. This contrasts with markup pricing on hosted platforms:

| Provider | Price/second | Monthly (daily use) |
|---------|-------------|---------------------|
| Higgsfield | $0.25 | $450+ |
| YouArt | $0.37 | $660+ |
| Fal AI | $0.25 | $450+ |
| Raw ByteDance API | $0.10 (via Danish entity) | ~$170 |

**US access restrictions:** [[frederikfeldt-seedance-pricing]] claims BytePlus pulled Seedance 2.0 API access for US-based users earlier in 2026 after the Hollywood copyright backlash. The official Jimeng platform requires a Chinese phone number and Chinese payment methods. Danish entities reportedly still have access.

> ⚠️ These pricing figures are from a single unverified source. The claims about ByteDance API restrictions and raw costs have not been independently confirmed.

## Evidence level

Confirmed from the ingested materials:

- the thread names Seedance 2.0 as the video-creation layer
- the linked MakeUGC homepage says "Seedance 2.0 is LIVE"

Not yet confirmed from independent product documentation in this ingest:

- underlying model architecture
- provider/company behind Seedance 2.0
- pricing or direct API access outside MakeUGC

## Seedance 2.0 as Director (per SIP article, 2026-04-17)

The Startup Ideas Podcast article frames Seedance 2.0 as fundamentally different from previous video models: "You are not generating a clip anymore. You are directing one." Key capabilities documented:

- **Multi-input generation:** Up to 2 images + 2 videos + 1 audio file, all in one prompt
- **Reference discipline:** Everything starts with a strong source image; good references in → good video out
- **Prompt style:** Longer and more specific prompts (opposite of Kling); Sirio uses Claude Opus to optimize prompts before running
- **Three key use cases:** Virtual try-on (clothing swap), AI influencer product review (character + product), green screen replacement for games/landing pages
- **Model comparison:** Seedance V2 = default daily driver; Kling 3 = cinematic/emotion control; Enhancer V4 = talking heads only; Google VO3 = ~$3/clip pricing reference

- [[makeugc]] — platform where Seedance 2.0 is surfaced in this workflow
- [[ai-ugc-ad-scaling-system]] — the broader operating system using it
- [[stijn-feijen]] — source author
- [[frederikfeldt-seedance-pricing]] — pricing analysis and API access context
- [[prompt-engineering-patterns]] — upstream scripting layer that feeds the generation step
- [[startupideaspod]] — podcast that featured Sirio's Seedance 2.0 deep dive; covered virtual try-on, AI influencer, and green screen workflows

## Character-consistency workflow (Primee32 source claim)

Primee32's X Article positions Seedance 2.0 as the motion layer after GPT Image 2 has locked identity. The proposed sequence is:

1. Generate a paired rider/dragon reference sheet with turnarounds, expressions, action poses, and fixed color values.
2. Generate a 4x4 grid of 16 numbered storyboard frames from that sheet.
3. Animate one grid frame at a time with a structured JSON prompt and the matching reference image.
4. Review each clip against its frame, regenerate only drifting shots, then stitch and grade the sequence.

The workflow, JSON fields, five-second example duration, and platform export settings are source claims from one X Article; they are not independent product-documentation findings. See [[character-consistent-ai-video-workflow]] and [[primee32]]. ^[raw/articles/gpt-image-2-seedance-2-character-consistency-workflow-2075327959586537848.md]

## Source-described 14-second AI vlog workflow

The supplied source names Seedance 2.0 as the model behind an eComrads MCP workflow for a three-scene, 14-second AI vlog. The proposed sequence keeps a character block identical across wake-up, shower, and breakfast scenes, generates each shot separately, and uses a manual QC gate before assembly. These are source claims about a particular workflow, not independent findings about model reliability or the eComrads service. ^[raw/articles/14-second-ai-vlog-method.md]

The source specifically recommends close inspection of hands, eyes, teeth, liquid/foam motion, object continuity, and product labels. It claims 4K output and platform-specific 9:16/16:9 exports, but neither the render nor the endpoint was independently validated in this ingest. ^[raw/articles/14-second-ai-vlog-method.md]

Related pages: [[ecomrads-mcp]], [[14-second-ai-vlog-method]], [[character-consistent-ai-video-workflow]].

## References

- Original tweet: https://x.com/spwfeijen/status/2043692176689795202
- Homepage mention: https://www.makeugc.ai/
