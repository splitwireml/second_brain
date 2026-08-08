---
title: beech
created: 2026-08-08
updated: 2026-08-08
type: entity
tags: [person, content-creator, x-article, ai-video, video-generation, prompt-engineering, creator]
sources: [raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md, raw/articles/xarticle-httpstcobqzsujkorj-2085016215261712848.md]
---

# beech

## Overview

beech (`@beechinour`) is the author of a source-described Seedance 2.5 prompting and production guide. The substantive local X Article is dated 2026-08-06 and covers prompt grammar, reference discipline, montage aggregation, continuity, sound, UGC, and a painted-animation pipeline. The model behavior, pricing, quality, ROI, and style claims below are attributed to that source and are not independent product findings. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

A prior exact-handle local export (`2085016215261712848`) is preserved as metadata-only raw provenance. It contains an export failure and shortened URL but no recoverable article body, so it supplies no topic or author fact. ^[raw/articles/xarticle-httpstcobqzsujkorj-2085016215261712848.md]

## Source-described Seedance 2.5 operating model

The guide says Seedance 2.5 is expensive but listens well when the prompt is right, produces unusually realistic footage, and remains weak at text in frame. It reports API pricing of roughly `$0.50–$1.20` for a 5-second clip depending on resolution, and 2,000+ credits for a full 30-second 4K generation on credit platforms. It also reports 50 reference slots that remember structure. These are source-described figures and capabilities, not independently verified. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

The core operating shift is to aggregate coverage rather than one-shot a whole video, transitions, or audio: prompt more than needed, select the best moments, and let the model propose shots the operator did not explicitly plan. A batch of ten 15-second montages is reported at roughly `$15–$35` at the cited API rates; the source frames that spend as paying for usable coverage rather than repeatedly rerunning a broken prompt. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

## Production loop

1. Take `2–5 seconds` of the actual script.
2. Turn it into one `15–30 second` fast-cut montage prompt; the source says to use ChatGPT for the breakout.
3. Tell Seedance the operator is cutting in Premiere and wants extra shots and options.
4. Generate about `10` montages.
5. Cut the best moments into one edit.

The guide calls `15–30 seconds` the montage sweet spot, with 30 seconds carrying more cost and risk. The intended handoff is model output → selected coverage → operator edit; most extra shots are discarded, but occasional unplanned shots are retained. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

## Prompt grammar

The source's narrative prompts use this macro-to-micro structure, with a hard limit of under `3,500 characters`; montage prompts intentionally run longer and looser:

```text
SHOT: name it, plus one line on whats happening
REFERENCES: who each @image is. lock this before anything else
CHARACTER @image1: the same exact person description every time, plus what theyre doing and feeling in this shot. clothing locked
SETTING @image2: the place, matched to your environment sheet. light and materials
CAMERA: lens, distance, movement, framing, light
SEQUENCE: the timed beats. this is where the video lives
STYLE PROMPT: your look, pasted identical in every shot. ratio, duration, 24fps
```

Every prompt carries four additional rules: no music (diegetic sound is described per beat and music is added in the edit); `face stable throughout, no deformation`; a named role for each `@image` in the order it appears, with no reference cited unless the model receives it; and a short negative list containing only failures already observed in generations. A style paragraph already used in Midjourney or GPT image models can be pasted identically into every Seedance prompt. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

## Sequence, continuity, and reference rules

The `SEQUENCE` block makes each timed beat a shot type + action + camera + sound. The guide's rules are: express emotion as body movement rather than an adjective; specify physics as trajectory, distance, impact, and reaction; put diegetic sound inline in each beat; and create rhythm through contrast between extreme-wide and macro, fast and still, impact frames, speed changes, and held freezes. Narrative shots use a ceiling of `3–4 beats per 15 seconds`; montage prompts deliberately break that ceiling.

For a longer narrative, prompts in one continuity block reuse the same references, environment descriptor, and light. Bridge prompt A to B with the same audio cue, and repeat the same framing and eye placement when shot B continues shot A. A character sheet uses three face angles; an environment sheet uses two or three environment angles. The guide says it normally uploads `4–10` reference images per prompt, while montages work better with fewer references so the model can invent coverage without losing the rough environment and style. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

## Fighter-jet montage prompt

The article's 15-second example intentionally uses `13` beats and one `@image1` reference for the pilot, primary fighter, sky environment, and style. It asks for a large variety of aggressive angles across `18mm` rigid cockpit mounts, `24mm` air-to-air chase, `35mm` underside/wingline tracking, `50mm` pilot close-ups, `85mm` explosive near-pass angles, and `135mm` long-lens silhouette flybys. The opposing jets stay simple and distant while the reference aircraft remains locked, readable, undamaged, and consistent. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

```text
CINEMATOGRAPHY: ultra-dynamic cinematic aerial-combat coverage using 18mm rigid cockpit mounts, 24mm air-to-air chase cameras, 35mm underside and wingline tracking shots, 50mm pilot close-ups, 85mm explosive near-pass angles, and 135mm long-lens silhouette flybys. Prioritize a large variety of aggressive angles: nose-on closing passes, belly-up overhead flybys, wingtip-mounted bank shots, rear chase, top-down dive coverage, close crossing passes through smoke, and distant long-lens explosions. Camera motion must obey believable aircraft inertia, air resistance, G-force, speed, and combat geometry.

SEQUENCE: use timed beats from 0–1.2s through 13.2–15s, including cockpit close-up, nose-on near miss, top-down dive, wingtip bank, underside flyby, control-stick pull, rear chase missile/projectile burst, distant explosion, belly-up pass, cockpit brace, side-profile chase, defensive flares, and a rear three-quarter climb into sunlight. Each beat specifies camera behavior plus diegetic sound such as breathing, radio crackle, turbine roar, wind blast, warning tones, explosions, debris, flares, and fading radio static.

STYLE: [your style prompt goes here, identical in every shot]
negative: no face morph, no identity drift, no helmet redesign, no oxygen-mask deformation, no aircraft redesign, no changing wing geometry, no changing tail shape, no changing markings, no duplicated primary jet, no aircraft merging, no bent wings, no floating aircraft parts, no impossible instant direction changes, no weightless movement, no random extra jets beyond brief enemy silhouettes, no close-detailed enemy cockpit shots, no primary aircraft damage, no pilot ejecting, no graphic injury, no gore, no cockpit explosion, no oversized unrealistic mushroom clouds, no sci-fi lasers, no neon engine glow, no photoreal rendering, no smooth commercial CGI, no motion blur
```

The full source prompt, including the locked pilot/aircraft descriptions and all 13 timed beats, remains verbatim in the raw capture; the block above preserves its operational camera, timing, sound, style, and negative-prompt grammar. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

## Sound, UGC, and style pipeline

The guide keeps native sound effects for cars, planes, and mechanical subjects, treats lip-sync as somewhat usable for UGC talking heads, mostly skips native dialogue, and always adds music during editing. It calls phone-camera honesty—slight shake, casual autofocus hunting, no gimbal smoothing—and real speech pauses, filler words, trailing off, and quiet action-only stretches useful for UGC realism; objects should enter frame through visible hand action. These UGC observations are attributed to the guide's discussion of Maximalist's separate prompt, not presented as independent benchmarks. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

The author's preferred lane is painted animation: Midjourney creates base images; GPT image models convert them to a specific style, upscale them, and style-lock them; `4–10` resulting images become Seedance references per prompt. One style prompt is reused in Midjourney, GPT image, and Seedance at every shot. The guide says Gemini can extract style details from imagery or cartoons the operator loves and turn them into keywords; the resulting paragraph becomes the reusable style prompt. The source says this style is being pursued at an Into the Spider-Verse-like tier, which is an unverified personal target rather than an established result. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

The guide says Seedance 2.5 is already useful for B-roll, organic vlog content, animation/motion, and fake VHS or broadcast styles, while embedded examples and the claim that a VHS clip fooled a French news channel remain source-described evidence boundaries. It says text in frame should be left to captions and overlays in the edit. The article closes by pointing readers to the author's free Telegram at `t.me/beechhq`; no channel or embedded tweet was fetched in this local-only ingest. ^[raw/articles/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md]

## Related

- [[seedance-2-0]] — video-generation entity and source-specific model context
- [[ai-video-director-workflow]] — shot planning, timed beats, and model-directed production
- [[ai-ugc]] — synthetic-UGC formats and production constraints
- [[character-consistent-ai-video-workflow]] — reference-led identity locking
