---
title: Grok Imagine Short-Film Pipeline
created: 2026-08-08
updated: 2026-08-08
type: concept
tags: [ai-video, video-generation, image-generation, prompting, workflow, ai-tools, x-article]
sources: [raw/articles/xarticle-how-to-make-a-short-film-with-grok-imagine-start-t-2085365652509040768.md]
related_entity: [[grok-imagine]]
author: [[tetsuoai]]
confidence: medium
contested: true
---

# Grok Imagine Short-Film Pipeline

A source-specific technical appendix to [[ai-video-director-workflow]] and [[character-consistent-ai-video-workflow]], not a competing umbrella concept. Tetsuo's local X Article describes a Grok Imagine pipeline that turns one idea into a finished short by separating story structure, reference assets, shot prompts, generation, and editing. The source's product and quality claims are not independently verified.

## Product and skill stack

The source says Imagine Video 1.5 improved motion, physics, and audio; xAI then added image and voice references, text-to-video, and native 1080p. Image/voice references are described for US SuperGrok Heavy and SuperGrok Plus on `grok.com/imagine` and iOS, while text-to-video and native 1080p are described as generally available on web, iOS, and Android. The API model is `grok-imagine-video-1.5`, with `reference_image_urls`; billing is described as per second with duration and resolution affecting cost. The source supplies no endpoint, auth, request/response schema, codec, renderer, or storage handoff.

Four Grok skills are treated as the pipeline rather than optional add-ons:

1. **Script writer** — one-line premise → characters, locations, props, numbered beats, and one-shot-per-beat structure.
2. **Char sheet** — locked three-view character references. The source warns that more than one face view can increase facial drift, says to use one face shot, frames a head crop as composition rather than a missing head, prefers light grey over green screen, and keeps hidden twist features out of reference images.
3. **Location/prop reference** — empty, correctly lit location references plus product-style object references.
4. **Prompt-creator** — one fully detailed Grok Imagine video prompt for each script beat.

The raw source preserves the four `grok.com/skill-link/` URLs and the named community resources Codex 3.0, Cinematique, and grokfilm.app. Those resources, the embedded-post context, and all capability statements are source-described rather than independently checked.

## Consistency architecture

The article's governing rule is that video models have no memory between generations. References carry identity; text carries action and critical details. Every clip therefore restates the current facts it needs, while the written bible and `STATE` notes carry continuity between otherwise independent generations. The author describes the workflow as front-loading consistency into references and a sealed prompt, not as relying on model memory.

The interface takes references in the prompt bar and calls them with `@` element tags. The source says the current ceiling is three references per generation, with one reference locking one element such as a face, location, or prop. After the prompt-creator returns a prompt, the operator must click each `@` tag and select the correct element. The article says its script does not assume that ceiling because the interface may change.

## Step 1 — beat script and bible

The source starts from a one-line premise and makes four decisions before writing beats:

- **Runtime:** generated shots run 5 to 1 seconds; budget 6–10 beats per minute. The example budgets 45 seconds as 5 beats and a 2-minute film as 15–20 beats.
- **Settings:** choose the number of locations deliberately because every location becomes a reference image to generate and manage. The example uses an alley and rooftop as the initial two-location decision.
- **Dialogue:** silent or minimal beats are safer because long speeches fail in AI lip-sync. If characters speak, the source says voice references can travel with the face and recommends one or two sentences per line.
- **Ending:** choose happy, tragic, loop, or cliffhanger first and build every beat toward it; the example uses a cliffhanger.

The script is ordered exactly as `CHARACTERS`, `LOCATIONS`, `PROPS`, `SCRIPT`. The first three are the bible and the source of truth copied into prompts. Each character has a name, an element tag such as `@vera`, role, age/build/hair/clothing, and a distinctive identity lock; each location has a tag plus time, palette, weather, and landmarks; props are a bullet list with a tag and short visual description when reused.

The screenplay uses a slugline, an `ASSETS` line listing only visible tags, and numbered beats. One beat equals one shot and one camera setup with one visual change; if a beat has two camera setups, split it. End a beat that changes a continuing fact with a `STATE:` line, for example ``STATE: the chip is inside her fist from here on.`` Later prompts must restate that fact. Do not attach a reference for an object excluded from the frame: the model may force it into the shot.

The structural recipe is discovery → threat → close call → catastrophe → transition. End cuts on a reveal, impact, or incoming threat; carry one prop or motif through every scene; plant a visual twist at least two beats before the reveal.

## Canonical example: THE WALK

The article's complete example uses Vera (`@vera`), the skeptic with a sharp dark bob and permanent crimson scarf, and Otis (`@otis`), the believer with a gray-streaked short beard and permanent round brass glasses. The scarf and glasses survive wardrobe changes and function as identity locks.

Locations are Roman Forum (`@roman_forum`: white marble, dusty ochre ground, cloudless blue sky), Medieval Market (`@medieval_market`: timber stalls, mud, snow, stone gatehouse), 1920s Street (`@jazz_street`: wet asphalt, tungsten storefronts, Model T cars, theater marquee), Neon Alley (`@neon_alley`: rain, pink/cyan holographic signs, steam, dark chrome), and Bedroom (`@bedroom`: dim phone-screen light, shallow depth of field). Props are the Red Scarf (`@red_scarf`) and Phone (`@phone`) with a generation-app UI and `REGENERATE` button.

The script's nine beats are: Roman walk and dialogue; statue eyes track/blink and a white-bloom transition; medieval walk and dialogue; merchant fingers multiply five→six→seven, snow→confetti, and wardrobe transition; 1920s dialogue and marquee-glyph distortion; neon walk with scarf dye spreading into a puddle; Otis removes glasses while the alley dissolves into pixels; “We wouldn't”; and a phone-screen smash cut where a thumb taps `REGENERATE`, the UI glitches white, and the image cuts black.

## Step 2 — reference assets

Characters come first. The source's three-panel sheet is: (1) full-body front with the top of frame cropping at the base of the neck and both hands visible; (2) full-body back with the head in frame; (3) head-and-shoulders portrait square to the lens. It calls for a clean light-grey studio backdrop, not green, and says the face should appear only in the portrait panel. The source's exact operational command is `/imagine-character-sheet-prompt` followed by the character tag and bible description.

The Vera and Otis examples specify 47° neutral full-body optics, 18° portrait compression, a locked-off tripod, chest height 4 m back for full-body cuts, eye height 2 m back for close-up, a fixed operator axis, one slow breath, and a 1 cm shoulder settle. The lighting example uses a soft white front-left key at 5600K and 45° off axis, a cool back-right rim, and even fill. The style block says photoreal, 8K, clean studio, fine film grain, real-time speed. Identity locks repeat scarf/hair/eye/face or glasses/beard details in every cut.

For locations and props, the source calls `/imagine-location-prop-prompt`, one empty establishing image per location, the same lighting as the screenplay, and one product-style image per prop. It names location temperature examples of 5600K Roman midday, approximately 6500K overcast medieval light, approximately 7000K dusk sky mixed with 2700K tungsten, approximately 9000K neon-alley fill, and approximately 6500K phone-screen light. It specifies no people in location references and, for the bedroom, no phone/device in the location reference so the phone remains a separate prop.

## Step 3 — load references

Drop the reference images into the Grok prompt bar and call them with their `@` tags. Keep the role of each reference narrow: identity, location, or prop. The source explicitly notes that the current three-reference limit may change, so a future-expanded interface should not be treated as a reason to redesign the bible.

## Step 4 — sealed prompt per beat

Each beat becomes one standalone prompt. It must contain no “continuing from before,” no off-frame characters or props, and every active `STATE` fact. The fixed order is:

1. `SCENE CONTEXT` — who is where and what the shot is.
2. `ACTIVE REFERENCES` — each `@` tag plus a short anchor and “100% matches the reference.”
3. `LOCATION MAP` — foreground, midground, background, and light source.
4. `FIRST FRAME / BLOCKING` — positions before movement.
5. `FORMAT MODE` — one continuous shot or explicit cuts/transitions.
6. `OPTICS` and `CAMERA` — camera language in the middle of the prompt.
7. `ACTION`, `PERFORMANCE`, and `PHYSICS` — visible, measurable movement.
8. `LIGHTING`, `WARDROBE`, `AUDIO`, and `STYLE`.
9. `POSITIVE LOCKS` — continuity facts restated once.

Write measurable quantities: km/h for speed, percent for fog, and field of view on the source's fixed ladder: 84° establishing wide, 63° observational wide, 47° neutral, 29° dialogue bust, 18° identity close-up, 12° tele detail. Left/right mean camera-left/camera-right. Use positive phrasing (“stays upright, feet planted”), physical muscle actions instead of emotion labels, and concrete environment interaction such as rain on hair or water off boots. Keep reference anchors short because the image controls appearance while text controls action; put logos and on-screen text in words because references often drop them.

The source says to save the screenplay to a text or Markdown file on the computer, pass that file back to Grok with the required scene images, use `/imagine-prompt-creator`, then click each returned `@` tag in the UI. Generate about four videos per beat, ask Grok to edit its prompt when a change is needed, and use `extend` when continuing a usable clip is better than generating a new one. The generated script is a guideline; the operator uses intuition and may revise it.

## Handoffs, transitions, and finish

The example uses explicit visual transition mechanics: a pure-white bloom through a stone arch, snow becoming paper confetti, wardrobe changing only beyond the transition, a merchant's hands alone multiplying fingers, a scarf's dye spreading in water, an alley end dissolving into discrete pixels, and a phone UI glitching to white then black. The source recommends giving each larger world/scene change its own beat so residual drift is hidden by an explicit cut mechanic.

Post-processing is intentionally open-ended: glue beats and add music in any video editor, with CapCut named as a suitable choice. Grok Agent Mode is a web beta for paid accounts with an infinite canvas of plan/generate/edit/stitch nodes. Either submit the one-line brief for a fast, less-controllable film or feed the authored beats one at a time for shot-level control and organization.

## Evidence layers

- **Confirmed from the local source:** the full text, named skills and commands, API model/parameter names, reference/tag interface, beat/bible ordering, camera/lighting values, prompt structure, asset/beat handoffs, transition mechanics, and post-processing/Agent Mode descriptions.
- **Source-described / unverified:** xAI rollout and tier availability, native 1080p, voice/image reference behavior, the three-reference ceiling, `grok-imagine-video-1.5` billing, skill availability, model quality, physics/audio improvements, and the claim that the pipeline enables actual filmmaking.
- **Unspecified:** API endpoint/auth/request-response schemas, renderer, codec, bitrate, export dimensions beyond native 1080p, project/file handoff format, storage path, audio/music source, and independent evaluation protocol.

## Related

- [[grok-imagine]] — product and interface entity
- [[tetsuoai]] — source author
- [[ai-video-director-workflow]] — mature umbrella workflow
- [[character-consistent-ai-video-workflow]] — reference-first identity locking
- [[video-generation]] — broader model context
- [[ai-video]] — broader application area
