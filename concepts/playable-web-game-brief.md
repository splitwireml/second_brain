---
title: Playable Web-Game Brief
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [workflow, web-development, ui-design, creative]
sources: [raw/articles/thread-zeuuss_01-2081837342726214087.md]
related_entity: [[zeuuss-01]]
---

# Playable Web-Game Brief

A constraint-dense game-design and build brief for an instantly playable browser game. The source asks to “Build a playable web game” titled **Sands of the Lost Carpet**, explicitly original with no existing IP. It is a fast, stylized third-person / 2.5D endless flying-runner: the player rides a magic carpet, dodges obstacles, collects gold coins and gems, and races to escape a collapsing cavern and soar out over a desert oasis. Score = distance + coins; one run ends on 3 hits or a crash. ^[raw/articles/thread-zeuuss_01-2081837342726214087.md]

## Controls and platform boundary

The controls are intended to stay simple on desktop + mobile:

- Left / Right (A-D or arrow keys, or tilt/drag on touch) — steer the carpet.
- Up / Down (W-S or swipe) — climb / dive.
- Space / tap — BOOST, a short speed burst limited by an energy meter.

The source does not specify the browser API, input library, framework, engine, renderer, or mobile-device test matrix. ^[raw/articles/thread-zeuuss_01-2081837342726214087.md]

## Gameplay loop

- Auto-forward flight at steady speed.
- Inside the cavern, weave around falling rocks, stone pillars, and molten bursts.
- Collect floating gold coins for score and rare blue gems for a bonus + boost refill.
- After ~30 seconds, burst through a giant beast-mouth cave into a bright oasis.
- In the oasis, obstacles change to palm trees, waterfalls, and city spires.
- Difficulty ramps through faster speed and denser obstacles over time.

The requested run boundary is 3 hits or a crash; the brief does not specify collision tolerances, spawn algorithms, level-seed behavior, pause handling, checkpointing, or a scoring-balance procedure. ^[raw/articles/thread-zeuuss_01-2081837342726214087.md]

## Visual and character direction

The visual style is vibrant stylized-cartoon (“Pixar-meets-Fortnite”), with a saturated gold-teal-magenta palette, warm sunset light, glowing bloom, and particle sparkles. The two environments are (1) a collapsing golden treasure cavern and (2) a lush oasis valley with a turquoise river, waterfalls, and a domed palace-city at sunset. ^[raw/articles/thread-zeuuss_01-2081837342726214087.md]

The character is fully original: a young acrobat hero with a teal hood and vest, red sash, and tan trousers, riding an ornate patterned carpet with a small original critter companion clinging on. The source explicitly says “No Disney designs.” It does not specify a modeling, illustration, animation, asset-generation, or copyright-review toolchain. ^[raw/articles/thread-zeuuss_01-2081837342726214087.md]

## HUD, UI, and feedback

The HUD must show score top-right, a coin counter, a BOOST energy bar, 3 hit-point hearts top-left, and a distance meter. The UI must include a simple start screen with the title + “Tap to Fly,” a game-over screen with score + “Retry” button, rising difficulty, a coin pickup sound, and a boost whoosh. ^[raw/articles/thread-zeuuss_01-2081837342726214087.md]

## Delivery constraints and evidence boundary

The requested outcome is “smooth, juicy, and instantly playable in the browser,” with original assets and characters only—no logos, no brand marks, and no real game titles. This is a source-provided design/build brief, not evidence that an implementation exists, runs, or passed QA. The source names no command, configuration, parameter beyond the gameplay/UI values above, file format, path, deployment host, audio pipeline, accessibility behavior, performance target, browser compatibility matrix, or testing/evaluation procedure; none is inferred here. ^[raw/articles/thread-zeuuss_01-2081837342726214087.md]

## Related

- [[zeuuss-01]] — source author and adjacent AI-assisted production workflows.
- [[ui-design]] — HUD, controls, interaction, and visual-direction context.
- [[website]] — broader browser/web presence concept.
- [[ai-website-production-loop]] — adjacent constraint-first web-production loop; this source does not specify that its tools or stages were used.
