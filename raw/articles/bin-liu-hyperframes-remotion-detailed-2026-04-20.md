---
title: "bin"
source: "x-bookmarks"
tweet_id: "2046337462604279828"
tweet_url: "https://x.com/liu8in/status/2046337462604279828"
author_name: "Bin Liu"
author_handle: "@liu8in"
tweet_date: "2026-04-23"
bookmark_date: "2026-04-20"
content_type: "x_article"
character_count: 10708
retweet_count: 0
like_count: 0
---

external_urls:
  - "http://paper.design/)"
---

# HyperFrames vs Remotion - a detailed rundown

HyperFrames vs Remotion - a detailed rundown

## someone commented "remotion wrapper?"

## No - HyperFrames was designed for native agent usage, built from scratch.

First and foremost - Remotion is an awesome project - we used Remotion for many months in our production pipelines.

Remotion promoted the idea of using code to orchestrate and animate video production, they proved that headless Chrome could be a reliable, deterministic video renderer.

However, Remotion is React based.

As we scaled our code-to-video pipelines, we kept running into the same kinds of limits inside a React-first authoring model.

We debated internally, on continuing with Remotion, or build our own from scratch.

## Two factors drove our decision:

#1 - the agent-native workflow

In our evals, LLMs writing Remotion compositions produced less creative visual outputs, needed a lot more guardrails and prompting to improve, when compared with the same LLMs writing HTML compositions and GSAP animations directly. Two related issues compounded it:

Animation libraries with their own internal clocks (GSAP, Anime.js, Motion One) don't compose cleanly with React's per-frame render.

And arbitrary HTML or CSS that wasn't written as React doesn't have a clean path into a React composition; you must rewrite it.

#2 - the human editing workflow

We want the same code to be the render layer AND data layer - because we need to build a UI for human atop the agentic experience.

HTML is both the render layer and the editable source of truth. The same DOM is what you see and what you edit. This makes building a real visual editor (selection, drag & drop, property panels, timeline, etc.) much more natural and robust — exactly like how @paper & @pencildev  does it.

With Remotion (React), the source of truth of the Remotion Editor is json, converted to code + build tooling. Round-tripping through a visual editor becomes painful and fragile. Although the Remotion team has shown some progress here, it’s much more difficult to build a real time editor on top of React than HTML.

We architected HyperFrames so it’s the most native to agents while easy to build a human interface on top.

Now let’s dive into all the detailed differences between Remotion & HyperFrames:

# Difference at the core: React vs HTML

Remotion and HyperFrames both drive headless Chrome. Both are deterministic. Both ship agent skills. They differ on one decision: what the primary author (either Agent or Human) writes.

Remotion's bet is React. Video compositions are React components. You get typed JSX, the React ecosystem, component reuse, and the whole of React tooling. Remotion's strengths come from committing to that surface: five years of production use, Lambda at hyperscale, a large community, careful type-safe APIs.

HyperFrames' bet is HTML. Video compositions are HTML pages. You can paste in a landing page, a design-system component, a CodePen demo, and animate it. We think this is the right surface for two specific use cases: AI agents writing video, and visual editors built directly on the DOM the renderer consumes.

Different bets, different strengths.

# What the difference means in practice

## Agents express visuals better in HTML than in React

When an LLM writes HyperFrames, it's writing the medium it was trained on most heavily. The web as browsers see it (HTML, CSS, JavaScript, GSAP idioms from CodePen, 25+ years of accumulated web animation content) is the deepest well in the model's training data. React-specific sources inevitably would be a much much smaller slice.

From running both systems in production: an agent asked to write a Remotion composition spends tokens learning framework rules (which hooks are allowed, which APIs are forbidden, how to scaffold a project), before it can be creative. Output tends to converge on a narrow visual vocabulary: centered titles, stock transitions, conventional typography. The same agent, writing HTML with GSAP, reaches for a wider creative range because that's what its training data looks like.

## Animation libraries with their own clocks

Asking an agent to port a GSAP animation or an existing web page into Remotion loses details on the first try: timing nuances, audio level relationships, text sizing. The HTML-first path avoids the translation step entirely.

We gave both tools the same 4-second GSAP timeline: 11 letters of "HYPERFRAMES" enter staggered with a back-out ease, hold for 1.5 seconds, then each letter rotates and falls out of frame. Identical animation code, identical easings, identical stagger. The only thing we changed was the renderer.

HyperFrames output (what the animation is meant to look like):

In this render, all four seconds are used. Letters fly in one by one, the full word holds in the center for about a second and a half, then the letters spin and drop away.

Remotion output (same timeline, same code):

In this render, GSAP plays through its entire 4-second animation in roughly the first second of render wall-clock time. By the time Remotion starts capturing later frames of the video, GSAP has already finished and every letter has exited. Most of the output is black frames of an empty stage.

Why: GSAP drives its own timeline via performance.now(), which ticks at real-time speed during render. HyperFrames pauses GSAP and seeks it to frame / fps before capturing each frame, so the library runs in lockstep with the output. Remotion has no equivalent primitive, so GSAP's internal ticker races through the timeline at wall-clock speed while Remotion captures a handful of frames during the entrance and mostly-empty frames after.

Everything GSAP supports (SplitText, ScrollTrigger, MotionPath, physics, 15 years of snippets on CodePen) works the same way in HyperFrames. The pattern generalizes to Anime.js and Motion One and any other library with its own clock, and any JS library without it’s own clock just works. Wrapping a library clock in a Remotion component is possible but awkward; you give up most of what the library is good at.

## Arbitrary HTML, CSS, JavaScript

Every web page is a potential HyperFrames composition. Landing pages. Claude Design artifacts. Design-system docs. CodePen embeds. You paste in the HTML, render.

Remotion asks you to translate first: rewrite HTML as JSX, convert CSS for React, wrap imperative code (Canvas, WebGL, GSAP) in React components with refs and effects. Every translation step is a chance for an agent or a human to lose fidelity or introduce bugs. The translation is round-tripping work anyway; both frameworks ultimately serve HTML to the browser to render.

## Auto-fallback for edge primitives

HyperFrames has two capture modes.

BeginFrame mode (Linux + chrome-headless-shell) drives Chrome's compositor atomically via HeadlessExperimental.beginFrame, producing byte-for-byte reproducible frames across machines.

Screenshot mode (macOS, Windows, and as an automatic fallback) runs Chrome in real time and takes ordinary screenshots, the same approach Remotion uses.

The renderer inspects each composition at compile time and falls back to screenshot mode when it spots primitives BeginFrame can't handle: inline <iframe>s, raw `requestAnimationFrame` loops outside a Frame Adapter. It injects a virtual-time shim so rAF and iframe content stay frame-driven instead of wall-clock-driven. You get a diagnostic explaining the fallback, and the render produces visibly-correct output. When the composition can run in BeginFrame mode, you get determinism for free.

In practice: GSAP timelines, CSS @keyframes (via the Web Animations API adapter), Lottie, Three.js, and the Web Animations API all render deterministically in BeginFrame mode. Raw canvas loops and live-web embeds get screenshot mode automatically.

## React UI components reuse (Remotion's home turf)

If your team already has a design system in React components, Remotion lets you compose videos from the same primitives you ship in your app. Type safety, IDE completion, cross-file refactoring, everything React brings to developer ergonomics. For teams with existing React investment, this is a real advantage that HyperFrames doesn't try to match.

## Distributed rendering (Remotion's clean lead)

Remotion Lambda splits long videos across hundreds of AWS Lambda functions. Mature, production-tested, well-documented. It's a thing you can pick up today and use at hyperscale.

HyperFrames’ renderer logic runs on a single machine today. For long-form at large scale, HyperFrames' architecture doesn't block distributed rendering (compositions are stateless HTML, the renderer is stateless), just that we haven't gotten there yet. Closing this gap is on our roadmap.

## Visual editing over the render source (HyperFrames' natural bet)

The DOM you render is the DOM you edit. HyperFrames Studio previews compositions in a live iframe and lets you pick and edit elements directly: click an element, drag to reposition, edit properties in a panel. The editor and the renderer share one source of truth.

Building the same editor on top of React is harder because the source of truth is code plus a build step. Round-tripping a visual edit back to JSX means re-compiling. That's why tools like [Paper.Design](http://paper.design/) chose HTML as the editable source in the first place.

Stay tuned - this will soon materialize and continue to be open sourced.

## HDR output

Both tools currently render through headless Chrome, which outputs sRGB. Remotion documents this as unsupported. HyperFrames is working on an HDR output path.

## Open Source vs Licensing

HyperFrames: Apache 2.0

Remotion: Commercial (free for teams of 3 or fewer, then $0.01/render, $100/mo minimum)

## Recap:

the single difference between Remotion and HyperFrames is the choice of React v.s. HTML (+CSS+Javascript)

but this decision leads to many differences down the line.

for our needs:

> #1 - most native to agents so they perform the best.

> #2 - architected to enable UI layer for humans.

HTML + CSS + Javascript is the obvious bet:

1. Agents already “think” in HTML - LLMs have seen massive amounts of web code

2. True “one file in, video out”. No package.json, no installs, no bundler config, no composition setup. Fewer moving parts = way fewer random failures in automated/agentic workflows.

3. Highest creative ceiling: anything the browser can render, HTML can represent.

4. HTML is both the render layer and the editable source of truth. The same DOM is what you see and what you edit.

We at HeyGen are all-in with HyperFrames - but we cannot do this alone, that’s why we open sourced it under Apache 2.0 - so together we build the foundation for agentic video creation.
