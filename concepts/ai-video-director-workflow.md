---
title: AI Video Director Workflow
created: 2026-08-04
updated: 2026-08-08
type: concept
tags: [ai-video, video-generation, image-generation, prompting, workflow, audio, optimization]
sources: [raw/articles/xarticle-ai-video-workflow-2026-cinematic-masterpiece-2078133327714738454.md, raw/articles/xarticle-how-to-master-seedance-25-full-course-2084666171446726767.md, raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md, raw/articles/xarticle-how-to-make-a-short-film-with-grok-imagine-start-t-2085365652509040768.md]
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

## Seedance 2.5 format-specific direction and reference pipeline (2026-08-04)

Machina's source adds five format recipes to the shot-first director pattern:

- **K-pop music video:** cut tightly on snares/drops with hard cuts, use symmetrical center-weighted framing and recurring archways/circular portals for eye-level backward dollies, keep one saturated block-color palette with neutral-to-warm skin, use medium close-ups with crisp diction/open vowels/staccato phrasing for lip sync, and pair one dance move with each cut.
- **Vlog:** specify handheld micro-jitter, arm's-length selfie framing, and natural body sway; use existing golden-hour backlight or cool overhead fluorescent light rather than a studio setup; cut on turns, steps, or reaching hands, insert quick b-roll, grade warm/soft outdoors and cooler/flatter indoors, and retain giveaway details such as a mic cable, windblown hair, and a friend-like look into the lens.
- **Product shot with 3D elements:** describe physical material properties (glossy polycarbonate with internal light scatter or matte PBT-style plastic with high diffuse roughness), keep a 360-degree texture orbit separate from a straight pull-back exploded-parts reveal, use large diffused softboxes, a translucent-edge rim, a gradient specular sweep, an infinite pastel backdrop with ambient occlusion, no visible edges or competing real-world environment, and pastel lifted blacks without clipped highlights.
- **Realistic lighting:** specify light direction and color temperature separately; contrast a warm key with cool sky fill, use hard directional light and crisp shadows near camera, atmospheric haze at distance, rim-lit hair, a tilt-triggered lens flare, smooth highlight rolloff, bounced local shadow color, and reduced background contrast/saturation with distance.
- **Animation:** commit to one era/style (cel-shaded, painterly-over-3D, or classic 2D), animate characters on twos while vehicles/cameras remain smooth, mix extreme close-ups, tracking shots, and low angles, use painterly brushstrokes and hand-painted highlights over 3D geometry, and keep one palette family across scenes.

The same source's production loop is: build the linked Obsidian reference bible; review it after every session with a short Claude note; write six details for each shot; place those details inside four timestamped 30-second beats; define each reference's allowed and forbidden role; build images first; lock recurring references; and adjust motion prompts rather than replacing locked images. The source's 30-second claims, format advice, and tool capabilities are source-described rather than independently verified. ^[raw/articles/xarticle-how-to-master-seedance-25-full-course-2084666171446726767.md]

## Aggregated Seedance 2.5 montage workflow (2026-08-06)

A source-described Seedance 2.5 variant treats the model as a coverage generator rather than a one-shot director: take `2–5 seconds` of script, expand it with ChatGPT into a `15–30 second` fast-cut montage, state that the edit will be done in Premiere, generate about `10`, and cut the strongest moments together. The source reports roughly `$15–$35` for ten 15-second montages at its cited API rates; cost, quality, and the claim that this avoids expensive broken-prompt retries remain unverified. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

Its narrative prompt grammar is `SHOT` → `REFERENCES` → `CHARACTER @image` → `SETTING @image` → `CAMERA` → timed `SEQUENCE` → reusable `STYLE PROMPT`, under `3,500` characters. A prompt repeats no music, inline diegetic sound, `face stable throughout, no deformation`, role-labeled references, and only observed negative failures. The source specifies emotion as body movement, physics as trajectory/distance/impact/reaction, and contrast-driven rhythm; narrative work stays at `3–4 beats per 15 seconds`, while montage prompts deliberately exceed that ceiling. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

For continuity, reuse the same references, environment, and lighting through one narrative block, bridge adjacent prompts with the same audio cue, and repeat framing and eye placement when an action crosses a cut. This complements the existing shot-first handoff rather than replacing it: the operator still selects, edits, and reviews the generated coverage. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

## Grok Imagine source-specific branch (2026-08-08)

Tetsuo's local X Article applies the director pattern to Grok Imagine: write a `CHARACTERS`/`LOCATIONS`/`PROPS`/`SCRIPT` bible, create references before video, map each beat to one shot, and seal every prompt with active state. Its runtime rule is 6–10 beats/minute (45 seconds → 5 beats; 2 minutes → 15–20), with a current three-reference `@`-tag ceiling, a 47°/63°/29°/18°/12° FOV ladder, explicit transition mechanics, roughly four generations per beat, optional `extend`, CapCut post-processing, and a web-beta Agent Mode. The detailed Grok-specific stack, API parameter, skill commands, camera/lighting values, and evidence boundaries are preserved in [[grok-imagine-short-film-pipeline]]. ^[raw/articles/xarticle-how-to-make-a-short-film-with-grok-imagine-start-t-2085365652509040768.md]

This is a product-specific branch rather than a new umbrella concept: [[grok-imagine]] records the product/interface claims and [[tetsuoai]] records the source attribution. Availability, `grok-imagine-video-1.5`, `reference_image_urls`, rollout, native 1080p, skill behavior, and quality claims remain source-described and unverified. ^[raw/articles/xarticle-how-to-make-a-short-film-with-grok-imagine-start-t-2085365652509040768.md]

## Related

- [[voyzlab]] — source author
- [[beechinour]] — source author of the Seedance 2.5 coverage variant
- [[ai-video]] — broader application area
- [[video-generation]] — model and generation context
- [[character-consistent-ai-video-workflow]] — identity-locking sub-workflow
- [[ai-animation-factory]] — modular AI media-production stack
- [[higgsfield]] — aggregator/generation layer named by the source
- [[seedance-2-0]] — multi-shot generation route
- [[kling]] — character-video route
- [[minimax]] — variation-testing route
- [[elevenlabs]] — voice and sound layer
