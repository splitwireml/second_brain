---
title: Seedance 2.0
created: 2026-04-13
updated: 2026-10-07
type: entity
tags: [product, tools, genai, marketing, video-generation]
sources: [raw/articles/stijn-feijen-claude-seedance-makeugc-system-2026-04-13.md, raw/articles/frederikfeldt-seedance-pricing-2026-04-16.md, raw/articles/viktoroddy-gemini-seedance-websites-2026-04-17.md, raw/articles/vadoo-seedance-2-0-commercial-playbook-2045849016664248762.md, raw/articles/seedance-2-0-new-default-video-model-2045221480120885529.md, raw/articles/gpt-image-2-seedance-2-character-consistency-workflow-2075327959586537848.md, raw/articles/14-second-ai-vlog-method.md, raw/articles/makeugc-ad-remake-viral-ad-workflow.md, raw/articles/xarticle-how-to-master-seedance-25-full-course-2084666171446726767.md, raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md, raw/articles/xarticle-how-to-get-rich-in-the-attention-economy-ai-influe-2107476083851534377.md]
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
- [[beechinour]] — source author of the Seedance 2.5 prompting and coverage guide

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

## MakeUGC Ad Remake model choice

The MakeUGC Ad Remake paste lists Seedance 2.0, Veo 3.1, and Kling 3 Pro as model choices for recreating a reference-led product ad. It recommends Seedance 2.0 as the author's default while explicitly leaving comparative testing to the operator. This is a source-described interface/workflow claim, not independent confirmation of availability or model quality. ^[raw/articles/makeugc-ad-remake-viral-ad-workflow.md]

## Seedance 2.5 source-described upgrade and control pattern (2026-08-04)

Machina's article describes Seedance 2.5 as a forthcoming successor: one prompt can cover a 30-second story rather than 15 seconds, and audio/video are generated together in one pass rather than stitched afterward. It reports up to 30 image references, 10 video clips, and 10 audio clips, but says the stable range from the cited guide is 1–8 images and 1–5 video/audio clips. The source warns that stretching an old 15-second prompt to 30 seconds without structure can produce incoherent actions, disappearing props, and character drift; it attributes the stable 1–8 image and 1–5 video/audio guidance to ByteDance's own guide. These model behavior, release, and guide-attribution claims remain source-described and unverified. ^[raw/articles/xarticle-how-to-master-seedance-25-full-course-2084666171446726767.md]

The source's default control grammar is to specify, for each shot or timed beat, what is present, what it does, where it is, how the camera moves, the visual style, and rules to follow. A 30-second prompt is divided into 0–6 seconds (set the scene), 6–14 (build it out), 14–24 (the turn/big moment), and 24–30 (the ending). Reference tags include `@image`, `@video 1`, `@audio 1`, grouped ranges such as `@images 6 to 10`, and `@clay render 1`; each reference must state what it controls and what it must not transfer. The source gives the example `@video 1 defines motion, camera movement, and pacing` followed by a prohibition on transferring identity, clothing, or scene. ^[raw/articles/xarticle-how-to-master-seedance-25-full-course-2084666171446726767.md]

A source-described edit pattern is: `edit @video 1, keep the characters and visual style unchanged, adjust only the camera movement over 6 to 12 seconds`. The article defines `@clay render 1` as an untextured 3D shape used for camera movement and blocking while a separate image controls look, materials, and lighting. These are preserved workflow examples, not verified product requirements. ^[raw/articles/xarticle-how-to-master-seedance-25-full-course-2084666171446726767.md]

## Seedance 2.5 prompt-and-coverage workflow (beech, 2026-08-06)

beech's local X Article describes Seedance 2.5 as a costly but instruction-sensitive video model: API pricing is reported at roughly `$0.50–$1.20` per 5-second clip by resolution, while a 30-second 4K generation on credit platforms is reported at `2,000+` credits. The guide says the model has 50 reference slots that remember structure, but these pricing, capacity, realism, text-rendering, and ROI claims are source-described and unverified. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

The production rule is to aggregate coverage rather than one-shot a whole video. Convert `2–5 seconds` of script into a `15–30 second` fast-cut montage prompt, tell the model the operator will cut in Premiere, generate about `10` variants, and assemble the best moments. The source reports roughly `$15–$35` for ten 15-second montages at the cited API rates and treats that spend as coverage rather than hope-driven retries. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

The narrative prompt grammar is `SHOT`, `REFERENCES`, `CHARACTER @image`, `SETTING @image`, `CAMERA`, `SEQUENCE`, and `STYLE PROMPT`, with a hard narrative limit under `3,500` characters. Every prompt repeats `no music`, describes diegetic sound inline, includes `face stable throughout, no deformation`, names each received `@image` by role and order, and keeps negatives limited to observed failures. `ratio`, `duration`, and `24fps` belong in the reusable style paragraph. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

The `SEQUENCE` block encodes emotion as body movement, physics as trajectory/distance/impact/reaction, sound per beat, and rhythm through contrast. Narrative prompts stay at `3–4 beats per 15 seconds`; montage prompts intentionally break that ceiling. For continuity, reuse references, environment, and light across a narrative block, bridge cuts with the same audio cue, and repeat framing/eye placement when the next shot continues the action. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

The source's fighter-jet montage uses one `@image1` for pilot, primary aircraft, sky, and style; it requests 13 beats in 15 seconds and lens coverage at `18mm`, `24mm`, `35mm`, `50mm`, `85mm`, and `135mm`. Opposing aircraft stay distant and simple while the primary aircraft remains locked. The full timed prompt and its negative list are preserved in [[beechinour]] and the immutable raw source. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

Reference sheets use three face angles for a character and two or three environment angles. The guide reports `4–10` references per prompt for narrative work, but fewer references for montages to leave room for invention. It keeps native SFX for mechanical subjects, mostly omits native dialogue, adds music in Premiere, and says text in frame should be handled with captions and overlays in the edit. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

The source-specific style branch runs Midjourney → GPT image models for conversion, upscaling, and style-locking → `4–10` Seedance references. Gemini is described as a style-detail extractor that turns loved imagery or cartoons into reusable keywords; the same style paragraph is pasted into Midjourney, GPT image, and Seedance. These tool roles and the claimed Into-the-Spider-Verse-like target are source-described, not independently evaluated. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

## Seedance 2.5 original-ad branch (Machina, 2026-10-06)

Machina's Higgsfield-sponsored article names **Seedance 2.5** for original formats after reference-led trend copying. It claims **up to 30 seconds**, aspect ratios **9:16 to 21:9**, **audio generated in the same pass**, and **up to 50 references**. Its handoff is image-first: **a turnaround character sheet on white → tag those images into the video prompt**. Unlike the earlier modality-specific 30-image/10-video/10-audio description, this source does not break down the 50 references by modality or give exact tag syntax; retain the source-specific descriptions rather than infer 50 images or a new API. ^[raw/articles/xarticle-how-to-get-rich-in-the-attention-economy-ai-influe-2107476083851534377.md]

The production rules are **3.5 words per second** of spoken line, **one beat per generation** in short clips **stitched after**, **hook first** by rendering the opening line before anything else, and **1080p** for client delivery. The article attributes to an unnamed independent review a warning that a showcase does not prove repeatable **character or product consistency**, and **limits change by provider and plan**; **test the character across a batch of renders before promising a brand anything**. These remain attributed, unverified capabilities/constraints and instructions, not a reported batch-test result. See [[ai-influencer-path]] and [[character-consistent-ai-video-workflow]]. ^[raw/articles/xarticle-how-to-get-rich-in-the-attention-economy-ai-influe-2107476083851534377.md]

## References
## References

- Original tweet: https://x.com/spwfeijen/status/2043692176689795202
- Homepage mention: https://www.makeugc.ai/
