---
title: "I Built a $5,000 Landing Page With AI. Here's Exactly How."
source: "x-bookmarks"
tweet_id: "2048742030466339120"
tweet_url: "https://x.com/PrajwalTomar_/status/2048742030466339120"
author_name: "Prajwal Tomar"
author_handle: "@PrajwalTomar_"
tweet_date: "Mon Apr 27 12:32:18 +0000 2026"
bookmark_date: "2026-04-27"
content_type: "x_article"
character_count: 12033
retweet_count: 0
like_count: 21
---

# I Built a $5,000 Landing Page With AI. Here's Exactly How.

I Built a $5,000 Landing Page With AI. Here's Exactly How.

"AI generated websites look generic and boring."

I see this take every single day on X. And every single time I think the same thing. You're not using AI wrong. You're prompting wrong.

I just built a cinematic, scroll driven landing page with 3D effects, shader distortions, and buttery smooth animations. Entirely with AI. Zero manual code. The kind of landing page that agencies charge $5,000 or more to build. And the entire difference between "this looks like AI slop" and "wait, AI built THIS?" came down to how I wrote my prompts.

Here's the exact workflow I used. No fluff. Just the system.

## The Stack That Makes This Possible

Before we get into the workflow, the stack matters. Not as much as the prompts, but it sets the ceiling for what's possible.

I used Lovable as the builder. The project runs on React with Tailwind CSS and TypeScript. For scroll driven animations, GSAP with ScrollTrigger. For 3D models, Spline. For the WebGL shader effects, Three.js.

If you're opening Lovable and typing "make me a landing page," you've already lost. That's like walking into a recording studio and saying "make me a hit song." The tool has the capability. You just need to know how to direct it.

The stack gives you the range. The prompts give you the result.

## Start With the Hero Section and Get Specific

This is where 90% of people mess up. They write a vague prompt, get a vague output, and then blame the tool. The problem was never the tool.

Here's what most people prompt: "Build me a hero section for a landing page."

Here's what I actually prompted:

"Build a full screen hero section with a pure black background and a subtle grain noise SVG overlay at roughly 3% opacity. The section should be sticky with top 0 and full viewport height. Apply CSS perspective at 1200px and use GSAP ScrollTrigger to animate with rotateX 8, scale 0.92, and y negative 60 as the user scrolls, creating a 3D tilt back effect."

See the difference? I'm giving it layout structure, visual treatment, animation parameters, and responsive behavior all in one prompt. The AI doesn't need creativity from you. It needs SPECIFICITY. Exact values. Exact behavior. Exact structure.

That one prompt produced a hero section that looks like it came from a high end agency portfolio. Not because the AI is magic, but because I told it exactly what I wanted.

Topped With a Minimal Pill Style Nav

Same principle for the header. I prompted for a minimal pill style navigation, "Menu" pill on the left with a hamburger icon, "NEXUS" logo centered with wide letter spacing, and three pills on the right for Solutions, Platform, and Get Started. On mobile it collapses to a single Start pill with a dropdown menu using backdrop blur.

Tiny detail. Huge impact. A generic top nav is one of the fastest ways to make a page feel like a template. A custom pill nav signals intent from the first second someone lands on the page.

## Add a Text Scramble Animation

I wanted that cyberpunk tech feel for the heading text. So I asked for a character by character scramble reveal animation. Characters start as random glyphs and progressively resolve to the final text over about three seconds.

It looks like something out of a sci fi movie. And it took one prompt to get it working.

This is the kind of detail that separates a $500 landing page from a $5,000 one. Not more sections. Not more content. Just one thoughtful animation that makes the whole page feel intentional.

## Integrate a 3D Model With Spline

This is where people's jaws drop.

I embedded a Spline 3D scene directly into the hero section. Positioned it absolute on the right side for desktop only. Added mouse tracking parallax with a subtle 0.05 multiplier so the model responds to cursor movement. Set it to fade in only after the text scramble animation completes so the reveal feels sequenced and cinematic.

The key here is to give the AI the exact Spline embed code so it knows the URL and the viewer tag. Don't make it guess. Don't describe the 3D model in words. Paste the actual embed code. It will integrate it perfectly.

This is a principle that applies across the entire workflow. When you have the code, paste the code. Stop trying to describe complex things in natural language when you can just hand over the implementation.

## Use Real Background Images

This one is SO underrated and almost nobody talks about it.

Stop relying on AI generated placeholder images. Upload a real, dark, atmospheric background image and tell the AI to use it. Specify background cover, background center, background no repeat.

This single change takes your page from "clearly AI generated" to "designed by someone who knows what they're doing." Instantly. The difference is night and day and it costs you nothing except the 30 seconds it takes to find a good image.

Real assets make AI output feel real. Placeholders make everything feel like a prototype.

## Build Scroll Driven Section Stacking

Here's the architecture that makes the whole page feel cinematic rather than just a series of sections stacked on top of each other.

The hero section is sticky with z index 0. It tilts back as you scroll. The projects section is relative with z index 10 and scrolls over the hero. The features section is relative with z index 20 and scrolls over projects. The contact section is relative with z index 30 and scrolls over features.

Each section has a black background so the transitions are seamless. No white gaps. No jarring cuts. Just smooth, layered scrolling where each section reveals itself by covering the one before it.

You need to tell the AI EXACTLY how sections relate to each other in 3D space. Sticky versus relative positioning. Z index values. Perspective origins. This is not something the AI can guess. If you don't specify the layering architecture, you'll get a flat page with sections that just sit on top of each other like a normal website. The magic is in the spatial relationships and you have to define those explicitly.

## Projects Section With Hover Slideshows

For the projects section, I asked for a two column grid of project cards with image slideshows that activate on hover. Three images per project cycling every 1.5 seconds with smooth opacity crossfade transitions. Tags, year, and description overlay on each card. An arrow icon that appears on hover to signal interactivity.

One prompt. Worked on the first try.

This is what specificity gets you. When you describe the exact interaction model, the exact timing, and the exact visual treatment, the AI delivers it cleanly. When you say "make a projects section," you get something generic. The gap between those two outcomes is entirely in your prompt.

## Scroll Driven Features Section

I built a four slide scroll driven section at 400vh height with a sticky inner container. Content crossfades based on scroll position rather than click events. Step indicators with spinning loaders show progress. Dots on the right side indicate which slide you're on.

This is the section that makes people scroll slowly because they don't want to miss anything. And it's all driven by scroll position, which means the user controls the pacing with their own scrolling. That level of interactivity makes the page feel alive in a way that click based navigation never does.

## Add WebGL Shader Effects

This is where it gets wild.

I gave the AI an entire GridDistortion component built with Three.js. A mouse reactive ripple distortion effect that runs on the features section background. The grid responds to cursor movement with a wave like distortion that feels organic and fluid.

Here's the key insight that changed everything for me. You can paste ENTIRE component implementations into the prompt. The AI will integrate them correctly into your project. Stop trying to describe complex visual effects in words. If you have the code for a shader, a particle system, or a custom animation, just paste it. The AI adapts it and wires it into your existing architecture.

This principle alone will 10x the quality of what you can build with AI. Most people are trying to explain things the AI could just read directly from source code.

## Contact Section With Clean Execution

For the contact section, I went with a split layout. Left side has a contact form with styled inputs. Right side has contact details, social links, and office hours. Bottom has a minimal footer with copyright and legal links.

Nothing fancy here. Just clean execution. And that's an important point. Not every section needs to be a showstopper. Sometimes "clean and works" is exactly the right move. The cinematic sections earlier in the page earn you the right to have a simple, functional contact section at the end. If everything is trying to be impressive, nothing feels impressive.

## Polish and Iterate

The first pass is never perfect. Here's what I fixed after the initial build.

The last row of projects wasn't fully visible so I adjusted the minimum height. The background image was loading after the animation started so I added image preloading. There was a gap between sections caused by z index and sticky positioning conflicts so I fixed the layering.

This is normal. Don't expect perfection on the first try. Expect 80% right and then iterate on the remaining 20%. That's how AI works best. You get the heavy lifting done in one pass and then you refine the details with targeted follow up prompts. Be specific about what's wrong and where it's happening. "Fix the gap between the hero and projects section" is a good prompt. "Make it look better" is not.

## The Prompting Principles That Make All of This Work

After building multiple pages like this, I've distilled the approach down to six principles that consistently produce high quality output.

Be specific about visual details. Don't say "make it look cool." Say "font light, letter spacing 0.2em, font size clamp 10px 1.2vw 13px, color #BFBFBF." The more precise you are, the less the AI has to guess.

Describe animations with exact values. Don't say "add a scroll animation." Say "GSAP ScrollTrigger, scrub true, rotateX 8, scale 0.92, y negative 60, ease power2 out." Parameters matter. Timing matters. Easing matters.

Specify the layering architecture. Tell the AI exactly how sections relate to each other in 3D space. Sticky versus relative. Z index values. Perspective origins. It cannot guess this and it will not get it right without explicit instructions.

Upload real assets. Stop using placeholders. Real images, real backgrounds, real 3D models. This is the fastest way to make AI output stop looking like AI output.

Paste code when needed. For complex effects like shaders, custom animations, and 3D integrations, paste the entire component. The AI adapts and integrates. This is faster and more accurate than trying to describe the effect in natural language.

Iterate on details. Fix layout problems, timing issues, and responsive bugs one at a time. Be specific about what's wrong and where. Each fix prompt should address one thing clearly.

## The Final Result

A cinematic, scroll driven landing page with 3D scroll tilt effects using GSAP and CSS perspective, an embedded Spline 3D model with mouse tracking, character scramble text animations, WebGL shader distortion effects built with Three.js, scroll driven content transitions, hover image slideshows, seamless section stacking with no gaps, full responsiveness from mobile to desktop, and image preloading for a smooth load experience.

All built with AI. Zero manual code.

The secret is not the tool. It never was. It's knowing what to ask for and how to ask for it.

Most people prompt AI like they're talking to a junior designer. "Make it look nice." That's why their output looks generic. Start prompting like you're writing a technical spec. Give it exact values. Exact structure. Exact behavior.

The gap between "AI can't design" and "AI designed THIS?" is literally just your prompts.
