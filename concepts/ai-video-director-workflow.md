---
title: AI Video Director Workflow
created: 2026-08-04
updated: 2026-08-04
type: concept
tags: [ai-video, video-generation, image-generation, prompting, workflow, audio, optimization]
sources: [raw/articles/xarticle-ai-video-workflow-2026-cinematic-masterpiece-2078133327714738454.md]
related_entity: [[voyzlab]]
author: [[voyzlab]]
---

# AI Video Director Workflow

A source-described end-to-end method for turning one idea into a cinematic AI-video sequence. Its defining move is to act as a film director before acting as a prompt writer: plan the emotional arc, shot list, camera language, references, sound, and finishing pass before generating clips.

This is broader than [[character-consistent-ai-video-workflow]]. Identity locking is one phase here; the new framework also covers story structure, storyboard validation, model-per-shot routing, audio-first decisions, editing, and color continuity. It is also an upstream production method for [[ai-video]] and [[ai-animation-factory]], not a short-form virality taxonomy.

## Core distinction: prompt monkey vs. director

The source contrasts two operating modes:

- **Prompt monkey:** describes a scene in one sentence and hopes the model infers the film.
- **AI film director:** decides shot count, emotional function, framing, camera movement, lighting, and what happens immediately before and after every cut before opening a generation tool.

The source's quality rule is simple: the best pixels do not rescue an undefined shot. The operator's scarce input is taste and judgment; models are used for structural grind, still generation, motion, voice, sound effects, and assembly.

## Phase 1 — idea and script

1. Write the emotional core in one sentence, not the plot. Example: “A man realizes the house he grew up in doesn't recognize him anymore.”
2. Ask Claude or ChatGPT for three different beat structures; select the surprising one rather than the safest one.
3. Convert the selected structure into a shot list, not a prose screenplay.

For a 30–90 second piece, the source recommends a hook in the first three seconds, three to five tension-building shots, a turn, and a payoff: usually five to eight shots total.

### Source prompt template

```text
Here's the emotional core: [one sentence]. Give me a shot list of 6 shots for a 40-second piece. For each one: what happens, framing, camera movement, one sensory detail. No dialogue unless a shot specifically needs it.
```

The source's reason for avoiding “screenplay” as the request is that generators respond better to camera language than literary prose.

## Phase 2 — storyboard and shot planning

Generate stills before motion so a weak idea costs one image instead of a ten-second render. The source uses Google Flow as a default storyboard-to-video space and describes it as combining Whisk, ImageFX, and Flow around Veo 3.1, Nano Banana, and Gemini. A tool-free alternative is a Claude-generated `framing / lighting / mood` table reviewed on paper.

Two vocabularies are mandatory:

- **Framing and movement:** wide, medium, close-up, over-the-shoulder, dutch angle, dolly-in, handheld tracking, static shot.
- **Lighting:** golden hour, hard noir shadow, soft overcast, practical lamp light, cold fluorescent.

If the platform supports first/last-frame locking, use it where the shot arc matters. The source treats the last frame as a destination that constrains motion more effectively than a textual direction alone.

Example shot sheet:

| # | Scene | Lens | Motion | Notes |
|---|---|---|---|---|
| 1 | Corridor | 35mm | Static | Empty hallway |
| 2 | Door | 50mm | Push in | Slow reveal |
| 3 | Face | 85mm | Handheld | Hold 3 sec |
| 4 | Garden | 24mm | Orbit | Main reveal |
| 5 | Leaf | 85mm | Slow motion | End transition |

## Phase 3 — consistent characters and assets

Character drift comes from treating every generation as independent randomness. The source's rule is to create one strong front-facing portrait as the master reference and use that exact image for every following shot; never re-describe the character in text twice.

Named tool roles in the source:

- Midjourney Omni Reference: `--oref` with `--ow` weight for reference-driven still composition.
- Nano Banana Pro: faster face stability across scenes with less manual tuning.
- Leonardo AI: fine editable control for team workflows.
- Higgsfield Soul ID: persistent identity reusable across generations and video models.
- Kling 3.0 Voice Binding: source-described voice continuity across up to six cuts and five languages.

Build the still-image library first, then use approved stills as video keyframes. The source says reversing that order produces noticeably worse continuity.

## Phase 4 — model-per-shot generation

The source offers two stack shapes: an aggregator with many models under one subscription, or a direct line into one ecosystem. It presents Higgsfield as a simpler starting aggregator with 15+ models, Cinema Studio virtual lenses (`35mm`, `50mm`, `85mm`), and a connector for generation inside a Claude chat. These platform counts and capability descriptions are source claims.

Generation order:

1. Hero stills for characters and locations, using the locked references.
2. First and last stills for each shot; inspect the arc before paying for motion.
3. Dialogue- and sound-critical shots first, on a model with native audio so picture and sound can emerge together.
4. B-roll and transitions last because they tolerate randomness and are cheaper to retry.

The source's role map is:

| Model/tool | Source-described fit |
|---|---|
| Seedance 2.0 | Multi-shot commercial work, native picture/audio, up to 12 references |
| Veo 3.1 | Realism, motion physics, and environmental light |
| Kling 3.0 | Character-driven stories and native 4K |
| WAN 2.6 | Video-to-video restyling of footage already shot |
| Runway Gen-4.5 | Motion fidelity and cinematic 21:9 output |
| MiniMax | Fast variation testing |

The general decision rule is not “find the best model.” Match the model to the job of each shot.

## Phase 5 — sound, edit, and finish

The source treats picture as roughly 60% of perceived realism and puts sound earlier than beginner workflows do. [[elevenlabs]] is named for cloned or synthetic dialogue, text-described SFX, video-to-sound suggestions, and dubbing. The article gives no independent test of these capabilities or a fixed API/handoff specification.

The source's edit stack is:

- CapCut for social cuts and integration with the Dreamina/Seedance path.
- Runway for frame-level fixes that propagate a corrected frame through the clip.
- Descript for dialogue-heavy edits through transcript manipulation.

Finish by color-grading the entire sequence. Clips from different models vary in color, contrast, and grain; one unifying grade is presented as the difference between an “AI reel” and footage that reads as one camera. Watch once without sound and once with sound; boredom in either pass is a stop condition.

## Full handoff sequence

```text
emotional core
→ three beat structures
→ 5–8 shot list with framing, movement, and sensory detail
→ mood board / shot table
→ reference portrait per character
→ first and last frame for every shot
→ dialogue and sound-critical shots
→ b-roll and transitions
→ model matched to each shot
→ SFX, voice, music
→ edit
→ one color grade
→ silent and sound-on review
```

## Failure modes and correction rules

- Caption-like prompts without camera or lighting language → specify the shot.
- One prompt for the whole story → break it into a shot list.
- Re-describing a character → use the locked reference image.
- One model for every shot → route by shot requirement.
- Sound left until the end → generate sound-critical shots first.
- Mixed color and grain → apply one final grade.
- Thirty retries on a weak prompt → fix the reference or camera language once.
- Motion before checking the arc → inspect first/last stills before rendering.
- Common artifacts → use negative prompts for morphing, extra fingers, stray text, and watermark ghosts.

## Evidence layers

- **Confirmed:** the full source text, prompt template, phase sequence, shot table, named tool roles, and failure rules are preserved in the cited raw X Article.
- **Likely:** shot-first planning, reference-first identity locking, and still-frame arc checks are reusable production disciplines because they create explicit review gates before expensive motion generation.
- **Source-claimed / unverified:** model rankings, “best/strongest/cheapest” comparisons, native feature support, personal quality improvements, and any implied render-time or cost advantage.

## Related

- [[voyzlab]] — source author
- [[ai-video]] — broader application area
- [[video-generation]] — model and generation context
- [[character-consistent-ai-video-workflow]] — identity-locking sub-workflow
- [[ai-animation-factory]] — modular AI media-production stack
- [[higgsfield]] — aggregator/generation layer named by the source
- [[seedance-2-0]] — multi-shot generation route
- [[kling]] — character-video route
- [[minimax]] — variation-testing route
- [[elevenlabs]] — voice and sound layer
