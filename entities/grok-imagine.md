---
title: Grok Imagine
created: 2026-08-08
updated: 2026-08-08
type: entity
tags: [product, tools, ai-tools, ai-video, video-generation, generation, platform]
sources: [raw/articles/xarticle-how-to-make-a-short-film-with-grok-imagine-start-t-2085365652509040768.md]
---

# Grok Imagine

Grok Imagine is the xAI image/video-generation surface described in Tetsuo's local X Article. The source presents it as a web, iOS, Android, and API workflow for building short films from a written bible, locked reference assets, and sealed per-shot prompts. Availability, capability, model, and performance statements on this page remain source-described and unverified.

## Availability and API details

- **Imagine Video 1.5:** the source says it shipped the previous month with improved motion, physics, and audio; on July 31, xAI added image and voice references, text-to-video, and native 1080p.
- **Image and voice references:** described as launched in the US for SuperGrok Heavy and SuperGrok Plus on `grok.com/imagine` and iOS, with rollout to all tiers over the following days.
- **Text-to-video and 1080p:** described as generally available on web, iOS, and Android.
- **API:** the source names `grok-imagine-video-1.5` and the `reference_image_urls` parameter. It says billing is per second, with duration and resolution driving cost. No endpoint, authentication method, request schema, response schema, codec, or file handoff is specified.

## Skill surface

The article's pipeline uses four Grok skills, installed before generation:

1. **Script writer** — converts a one-line premise into characters, locations, props, and numbered beats, with each beat mapped to one shot; the result is the story bible and beat structure.
2. **Char sheet** — creates a locked three-view character reference; the source says one face view is safer than multiple face views, a light-grey background is preferred, and green screens cause green bleed into references.
3. **Location/prop reference** — creates empty, correctly lit location references and product-style prop references.
4. **Prompt-creator** — converts each script beat into one detailed Grok Imagine video prompt.

The source preserves four `grok.com/skill-link/` URLs for these skills in the raw capture; their current availability and exact implementation are not independently verified here.

## Reference-tag interface

The manual interface takes reference images in the prompt bar and calls each one with an `@` element tag. The source says up to three references can currently be used per generation, with each reference locking one element such as a face, location, or prop. After a prompt is returned, the operator clicks each `@` tag and selects the correct element. The author explicitly says the script does not assume the three-reference ceiling because the interface may be extended.

## Agent Mode and finishing

Grok Imagine Agent Mode is described as a web beta for paid accounts. It replaces a prompt-and-response loop with an infinite canvas where an agent plans, generates, edits, and stitches clips; each operation is a node that can be opened and reprompted. The source gives two modes: submit the one-line brief for speed and less shot-level control, or feed the operator's own beats one at a time for control and organization.

The source recommends gluing beats and adding music in any video editor, naming CapCut as a good choice. It does not specify a renderer, editor project format, codec, export preset, storage path, music source, or API handoff.

## Evidence boundary

The workflow, interface terms, skill roles, model name, parameter name, availability notes, and Agent Mode description are preserved as claims from one local X Article. They are not independent product documentation or a test of Grok Imagine. Pricing, rollout, reference limits, model quality, motion/physics/audio behavior, and the claim that the workflow makes actual filmmaking possible remain source-described and unverified.

## Related

- [[tetsuoai]] — source author
- [[grok-imagine-short-film-pipeline]] — detailed source-specific workflow appendix
- [[ai-video-director-workflow]] — mature shot-first production concept
- [[character-consistent-ai-video-workflow]] — identity-locking sub-workflow
- [[video-generation]] — broader model and generation context
