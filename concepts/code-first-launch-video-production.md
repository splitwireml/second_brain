---
title: Code-First Launch Video Production
created: 2026-07-12
updated: 2026-09-29
type: concept
tags: [ai-video, video-generation, agent, workflow, coding, content, marketing, product, framework, x-article]
sources: [raw/articles/xarticle-how-we-made-our-yc-launch-video-in-15-days-with-fa-2075672770483269788.md, raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]
related_entity: [[trope]]
author: [[matt-chow]]
---

# Code-First Launch Video Production

A launch-video production pattern in which an AI coding agent works inside the real product codebase and a code-rendered video project, so product visuals remain editable, reusable, and faithful to the shipped interface. The pattern is source-described by Matt Chow's Trope launch-video case study rather than independently verified. ^[raw/articles/xarticle-how-we-made-our-yc-launch-video-in-15-days-with-fa-2075672770483269788.md]

## Core pattern

Instead of recording a finished product or asking an image model to invent a UI, give the agent the product code, design tokens, fixture data, fonts, storyboard, and motion references. The agent can then rebuild product scenes in React/[[remotion]], preserving real interface details and making later changes cheap. ^[raw/articles/xarticle-how-we-made-our-yc-launch-video-in-15-days-with-fa-2075672770483269788.md]

## Pipeline

1. **Prepare the brief:** draft and revise the script from customer calls; choose the talking-head plus product-showcase structure; storyboard key frames with GPT-Image-2; collect motion references in one PDF.
2. **Capture the human footage:** record the talking head in a controlled location, prioritizing lighting and usable microphone audio.
3. **Build in parallel:** run multiple [[claude-code]]/Fable 5 sessions against a Remotion project, roughly one per clip, and merge the resulting edits.
4. **Synchronize and inspect:** transcribe voiceover with [[whisper]] word-level timestamps; render frames; use annotated screenshots and single-frame inspection to correct visual problems.
5. **Finish the mix:** simplify sound effects and music, then use DaVinci Resolve for final audio levels and the social target of -14 LUFS.

## Operating rules

- Give the agent the actual product code so product shots use real UI primitives rather than generic mockups.
- Treat timecodes, screenshots, and physical timing language such as "0.5s longer" as concrete feedback.
- Use code for punch-ins, reframes, easing, and motion blur; upscale filmed footage when needed, but re-render generated UI at native resolution.
- Keep the final editor pass narrow: the hard visual work should already be represented in code.

## Source-reported economics

The source reports 1.5 days of build time and roughly $2.3k at market rates: about $2,250 in Claude usage, $78 for Topaz, and $19 for ElevenLabs. It compares that with agency quotes of $4–8k and 2–4 weeks; these figures remain author-reported claims. ^[raw/articles/xarticle-how-we-made-our-yc-launch-video-in-15-days-with-fa-2075672770483269788.md]


## Opus 5.5 HTML-motion course (2026-09-29)^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

[[twoclipping]]'s local X Article presents a source-described alternative branch: Claude Code with Opus 5.5 generates a self-contained HTML motion renderer instead of working in a real product codebase/Remotion project. The author claims “0 mcp”, “0 external tools”, no subscription, no After Effects/editor, and studio-quality $5,000–$15,000 motion designs; those cost, capability, and quality claims are unverified. The article also says its three examples are demos, not real product launches. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

### Reference and studio setup

- The reference-analysis prompt names `reference.mp4`, `ffmpeg`, “2 frames per second”, and contact sheets, then asks Claude Code to break the video into beats, scene transitions, camera moves, colors, and fonts before writing the same structure for `[your product + link]`. Without a reference, the source says to ask for three product ideas and choose one. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]
- The stated anti-default style prompt is: `Style: 2D only. Warm white background, black UI, one accent color, one clean font (Geist or Inter). No 3D, no dark mode, no glows, no particles. Think Apple keynote, not a video game trailer.` ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]
- The setup command says: `Set up a motion design studio in this folder. Install ffmpeg and Playwright with Chromium. Then render a 2 second test where a black circle grows into a pill on a spring, 60fps, and show me the first and last frame.` The described interface is one HTML file with `seek(t)` drawing any requested frame; Playwright screenshots frames and ffmpeg turns them into an MP4. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]
- For assets, the source names `mixkit.co/free-stock-music`, `mixkit.co/free-sound-effects`, `pexels.com`, `fonts.google.com`, screenshots, and a logo. Its audio prompt requests a royalty-free Mixkit track around 120 BPM with a clear drop, `numpy` beat-grid/drop analysis, one Mixkit sound effect per event, and measured SFX peaks; it says synthesized effects sounded cheap. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

### Food-ordering film prompt: exact operating parameters

The first template asks for a product plus one typed request, 6–8 result-card photos, a royalty-free Mixkit song around 130 BPM with a clear drop, and a brand mark; its defaults are the food-ordering story, Pexels fire noodles/birria tacos/hot chicken/buffalo wings/smash burger/spicy ramen, and Mixkit “Cat Walk”. It specifies a 15 second, 1920x1080, 60fps, 2D-only continuous take: no fades/blurs/cuts; shape-changing handoffs; one eased camera move per scene; no back-to-back zoom reversal; and banned crossfades, blur-ins, 3D, particles, reverse camera moves, holds over 1s, and template-like output. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

Its exact palette is warm white `#f5f5f2`, black UI `#0e0e10`, lime `#cdf24f`, orange `#ff6a2a`, blue send button `#2f6bff`, a rotating conic pink/orange/lime/cyan/violet Apple-Intelligence-style iridescent glow, Geist UI text, and a serif end-card product name. The beat map is 130 BPM, 32 beats (14.8s), with the song starting 12 beats before the drop: beats 0–6 type the fixed three-line food request; beat 6 turns send into a chat bubble/428x900 phone with 11px bezel and 9:41 status bar; beats 6–12 turn it into an orange wok; beat 12 floods lime in about 0.35s and introduces 330x440/radius-28 food cards; beats 16–21 resolve into chat and “✓ Ordered”; beats 21–32 end with the courier/pin/wordmark sequence. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

The implementation prompt requires one 1920x1080 HTML file with every style computed inside `seek(t)`—no CSS transitions, timers, or state between frames; one container camera transform keyed `[time, zoom, x, y]` with eased segments and log-space zoom interpolation; closed-form spring step responses; shared elements for layer handoffs; measured-peak Mixkit SFX for typing/send/toss/drop/cards/click/success/whoosh/sparkle; `loudnorm` to `-14 LUFS`; and Playwright rendering with 8 subframes per frame blended through `ffmpeg tmix` at 60fps, followed by fast-moment and whole-video single-frame-pop scans. Its caveats: four subframes ghost fast moves, so use eight and slow the move; a flood must clear the farthest corner in about 0.35s; set each layer's `z-index`; never chase wrapping cursor text; and declare variables before the first `seek()` run. The requested handoff is a beat map plus four stills—ask, drop, chat, outro—before full-film code. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

### Photo-to-print Apple-keynote template

The second template asks for a one-word verb-like brand, 9–12 high-res photos, a Mixkit commercial-use track around 120 BPM with drop plus quiet breakdown, and a Pexels plain-wall/plant-shadow clip. It specifies warm off-white, black UI, iOS 26 liquid glass, `Archivo (wdth 125, weight 800)` wordmark type, Geist UI type, direct cursor clicks/drags/long presses, and bans crossfades, blur-ins, brightness “developing”, 3D flips, particles, glows, holds over 1s, and template-like output. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

Its 120-BPM, 54-beat structure requires something on every beat: accordion wordmark/pill/iris/photo/grid/bento/drop; glass word to droplet/toolbar/slider/lens/orb/lock-screen/player; phone/Dynamic Island/Mac-window/Safari/landing-page/product-card transition; ordered→printing→on-the-way→delivered; and a real-wall-footage return whose last frame equals the first. The renderer is one square 1440x1440 HTML file with an `async seek(t)`, no CSS transitions/timers/state, closed-form springs summed per target change, and a glass implementation that clones the scene behind each element and filters an SVG `feImage` rounded-rect distance field through three `feDisplacementMaps` at differing scales, with rim light. Other named techniques are blur plus alpha threshold plus source compositing for goo; six iris blades around a hexagonal aperture; wordmark width-axis squeeze; and `ffmpeg -g 1` all-intra footage loaded as a blob URL with `await 'seeked'` before each draw. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

For this template, every Mixkit SFX is downloaded rather than synthesized and placed at its measured peak; the song begins on a downbeat, zoom hits the drop, wall sits in the breakdown, and audio is `loudnorm`ed to `-14 LUFS`. Playwright renders 4 subframes per frame through `ffmpeg tmix` at 60fps; review one frame per beat and scan for frame-difference spikes “3x their neighbours”. The source warns that Chromium `backdrop-filter: url()` misreads displacement maps, so clone the scene; floods must overscale past corners in about 0.3s; `visibility: visible` can leak through a hidden parent, so use `inherit`; swapping morph text needs its own mask; and `python http.server` cannot range-seek video, so use the blob URL. It requests beat map plus open/glass/stage/wall stills before code. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

### One-shape UI-loop template

The third template asks for 8–12 UI states (button, loader, player, slider, toggle, tabs, chart, command palette, toast), black/white or one accent, and a 120-BPM Mixkit-style song. It is a 1440x1440, 2D, single-shape 7-bar loop with something on every beat: button → loader → check → Dynamic Island → music player/play-pause → scrubber → overextended volume slider → toggle → liquid tabs → chart/tooltip → `⌘K` filter → toast → button. The source specifies direct-manipulation drags, different spring responses for leading/trailing tab or toggle edges, `numpy` beat-grid/downbeat analysis, measured-peak UI sounds, 4-subframe Playwright/`ffmpeg tmix` 60fps output, and one frame per beat before the full render. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

Its caveats are not to put `will-change` on camera-scaled elements because text blurs; text swapping inside a morphing container needs separate enter/exit timing; and the final frame must equal the first including cursor position and speed or the loop stutters. The requested handoff is the state list on the beat grid before code. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

### Review and evidence boundary

The source's craft rules are: change shape instead of fading, derive every scene from the prior scene, make something happen on every beat, give landings a small bounce, make one camera move at a time, use real sound for every click/whoosh, and have the renderer check its own work. The finishing instruction is `Render the final video in 60fps with motion blur. Put every sound effect exactly on the moment it belongs to, balance the audio, and check every frame for glitches before you show me.` The author says feedback should be director-style (“this part is too slow”, replace cheap fade with shape change, hit zoom on the drop) and usually takes 2 or 3 rounds. No source evidence establishes that Opus 5.5, Claude Code, Playwright, Chromium, ffmpeg, numpy, Mixkit, Pexels, or the described process will yield a particular price, quality, licensing outcome, or commercial result. ^[raw/articles/xarticle-how-i-make-10k-launch-videos-for-0-with-opus-55-fu-2104446706741825818.md]

## Related

- [[matt-chow]]
- [[trope]]
- [[remotion]]
- [[claude-code]]
- [[claude-fable-5-loop-design]]
- [[agentic-video-hyperframes]]
- [[viral-launch-system]]
- [[open-montage]]
