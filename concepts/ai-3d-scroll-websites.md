---
title: "AI 3D Scroll-Effect Websites"
created: 2026-05-04
updated: 2026-07-26
type: concept
tags: [3d-animation, ai, claude-code, kling, no-code, scroll-effect, website-design]
sources: [raw/articles/2026-05-04-explorax-ai-3d-scroll-websites-2051261067339157657.md, raw/articles/explorax_-2051261067339157657.md, raw/articles/xarticle-35k-motion-website-playbook-higgsfield-claude-code-2067204840342630789.md, raw/articles/thread-0xKenny1st-2080369523765436623.md, raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]
---

# AI 3D Scroll-Effect Websites

Building high-end, animated, 3D scroll-effect marketing websites with a stack of AI image-generation, image-to-video, video-editing, frame-extraction, design-generation, and AI coding tools. The defining implementation pattern is to create a visual sequence first, convert it into a frame sequence, render that sequence as scroll-linked motion, and then integrate ordinary website sections around the cinematic hero.

## Core claim and evidence boundary

The sources claim that agency-style animated websites that previously cost approximately $5k–$10k can be produced in minutes at roughly $2–3 in model/video costs, or positioned as $10k websites. These are source-reported production and pricing claims, not independently verified benchmarks. The durable concept is the workflow: visual direction and asset generation are separated from code assembly, then connected through a scroll-controlled frame sequence. ^[raw/articles/2026-05-04-explorax-ai-3d-scroll-websites-2051261067339157657.md] ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

## Toolchain map

| Tool | Technical role in the source-described workflow |
|---|---|
| **Pinterest** | Find visual references for the hero, banners, and additional website sections. |
| **ChatGPT** | Recreate or modify reference images, write image-to-video camera prompts, and generate website copy. |
| **Google AI Studio** | Design individual website sections from reference images; refine layout, typography, spacing, cards, and glassmorphism; export the generated code as a ZIP. |
| **Flow AI** | Generate video transitions between specified start and end images. |
| **Clipchamp** | Merge multiple generated clips, adjust playback speed, add a transition, and export the combined video. |
| **EZGIF** | Convert the exported video into a JPG frame sequence at a selected duration and frame rate. |
| **Antigravity IDE** | Assemble the frame-based scroll animation, integrate the exported Google AI Studio sections, preview locally, and apply final interaction polish through its AI chat. |
| **Cloudinary** | Host replacement images and provide direct URLs for Antigravity when local-file references are less reliable. |
| **Claude Code / taste skill / Higgsfield / Kling** | Related variants in the surrounding concept cluster: AI coding and design guidance, Kling motion assets through Higgsfield, and skill-assisted website assembly. |

The exact X Article at `2077042196155363401` uses ChatGPT, Google AI Studio, Flow AI, Clipchamp, EZGIF, Antigravity IDE, Cloudinary, and Pinterest. It does not use Claude Code, Higgsfield, or Kling in its own step-by-step workflow; those belong to adjacent sources in this concept. ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

## Detailed asset-first workflow: Kenny1st's free-tool variant

The July 14, 2026 X Article uses a Paris travel website as the worked example. Its production path is not one vague prompt: the hero animation, website sections, frame extraction, code integration, and final interaction pass are separate handoffs. ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

### 1. Create the hero keyframes in ChatGPT

1. Search **Pinterest** for a reference image, such as a view through a plane window.
2. Upload the reference to **ChatGPT** and ask it to:
   - recreate the image in a **16:9** aspect ratio;
   - remove all text;
   - slightly widen the window frame.
3. Iterate in ChatGPT with targeted corrections such as `make the frame wider` until the composition is acceptable.
4. Generate a second keyframe showing the Eiffel Tower with the same color palette and soft clouds for visual consistency.
5. Generate a middle keyframe consisting entirely of clouds, with the camera positioned as if it is inside the clouds. This intermediate state splits the journey into two transition clips.

The output is three images: **plane window → clouds → Eiffel Tower**. ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

### 2. Generate start-frame/end-frame transitions in Flow AI

1. Open **Flow AI** and upload all three keyframes.
2. Select the video-generation mode that accepts a starting frame and an ending frame.
3. Generate **Video 1** with the plane-window image as the start frame and the cloud image as the end frame.
4. Generate **Video 2** with the cloud image as the start frame and the Eiffel Tower image as the end frame.
5. Use **ChatGPT** to write short camera-movement prompts for each transition, then paste those prompts into Flow AI.

Using the cloud keyframe as the endpoint of the first clip and the start point of the second creates a continuous camera path rather than asking one generation to travel across an unbounded scene. ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

### 3. Merge and time the clips in Clipchamp

1. Open **Clipchamp** and choose **Create a new video**.
2. Import both Flow AI clips through **My media → Import media**.
3. Place the clips on the timeline sequentially: plane window → clouds, then clouds → Eiffel Tower.
4. Slightly increase the playback speed of both clips for a faster, smoother feel.
5. Add a transition effect between the clips so the cloud handoff is seamless.
6. Export the merged video to the computer.

^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

### 4. Convert the video into scroll frames with EZGIF

1. Open **EZGIF** and select **Video to JPG**.
2. Upload the merged Clipchamp video.
3. Set the duration to approximately **10 seconds** and the frame rate to **30 fps**.
4. Select **Convert to JPG**.
5. Download the resulting ZIP archive and extract it.

The extracted JPG sequence is the frame-by-frame visual state that the website will reveal as the visitor scrolls. At approximately 10 seconds and 30 fps, the source-described output represents roughly 300 frames before any implementation-specific optimization. The frame count is implied by the stated settings, while the source does not describe compression, lazy loading, canvas rendering, or memory management. ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

### 5. Build the base scroll animation in Antigravity IDE

1. Download **Antigravity IDE** from its official website and choose the version for the operating system.
2. Open the IDE and select **Open Folder**.
3. Create and open a project folder such as `travel-site`.
4. Drag the extracted JPG-frame folder into the project window.
5. Drag the same frame folder into the **Antigravity AI chat panel** so the agent has access to the assets.
6. Request the implementation with:

```text
Create a smooth scroll animation using the provided image sequence. Don't add any extra components, text or UI elements. Keep the animation smooth and generate a local host preview link.
```

7. Approve any permission prompts while Antigravity generates the project.
8. Open the generated local-host link to inspect the base frame animation.

This stage deliberately creates only the scroll animation. The article then adds the ordinary website sections separately, rather than asking the IDE to invent the entire site and hero in one step. ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

### 6. Design the website sections in Google AI Studio

For the surrounding sections, the source uses **Pinterest** as the reference layer and **Google AI Studio** as the section-design surface.

1. Search Pinterest for banner and section references.
2. Upload a chosen reference to Google AI Studio with a prompt such as:

```text
Use this as a reference and recreate the banner. Keep the same layout and text structure, remove the background, use a solid black background instead. Apply the VM sense font, use pure white text, and maintain the overall composition.
```

3. Refine the section through follow-up prompts that specify implementation values, including:
   - banner height of **900 pixels**;
   - headline size of **54 pixels**;
   - medium font weight;
   - exact spacing and card-size adjustments;
   - transparent glassmorphism cards with a blurred background;
   - headline, subheading, card, icon, and layout corrections.
4. In parallel, ask **ChatGPT** to write copy for approximately four or five sections: headlines, subheadings, and card descriptions.
5. Paste the generated copy into Google AI Studio while designing each section.
6. Repeat the reference → recreate → refine → add copy cycle for the remaining sections, keeping the visual language consistent.
7. For a final section, the source suggests placing a centered Eiffel Tower visual with two information cards on each side and the main visual occupying the center.

The relevant technical principle is to design sections independently from the frame animation, preserve a consistent design system through reference reuse, and specify concrete values instead of relying only on adjectives such as `premium` or `beautiful`. ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

### 7. Export and integrate the sections with the scroll animation

1. In **Google AI Studio**, select **Code → Export → Download as ZIP**.
2. Extract the downloaded archive.
3. Locate the archive's `src` folder.
4. Drag the `src` folder into the **Antigravity IDE** AI chat panel.
5. Ask Antigravity to merge the section components and content into the previously created scroll animation:

```text
The uploaded files contain the components and content for our website. Integrate this layout into the scroll animation that we created earlier. As the user scrolls, each section should appear smoothly one after another, synced with the animation.
```

The handoff is therefore **Google AI Studio code export → Antigravity IDE integration**, not a direct publish from AI Studio. The article does not specify the generated framework, build command, runtime, or deployment host. ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

### 8. Apply final visual and interaction changes

The article's final Antigravity prompts are targeted adjustments rather than a full regeneration. Examples include:

- center the hero headline, subheading, and CTA button;
- add a gradient background to cards that look flat;
- generate a replacement image in ChatGPT;
- upload the replacement to Cloudinary;
- copy the Cloudinary direct URL into Antigravity, because the source says the AI handles URLs better than local files;
- request `smooth hover effects, entrance animations, and small interactions across the website`.

The intended output is a page with smooth hover states, entrance animations, and small interaction details layered on top of the scroll-linked cinematic hero. ^[raw/articles/xarticle-10k-website-free-ai-tools-2077042196155363401.md]

## Earlier Claude Code + taste-skill variant

A separate source describes a shorter Claude Code path: write the desired site as bullet points, load a design-oriented **taste skill**, and use that skill to constrain spacing, luxury aesthetics, and design schematics before generating the site. ^[raw/articles/2026-05-04-explorax-ai-3d-scroll-websites-2051261067339157657.md]

It then uses **Kling 3.0** through **Higgsfield** to generate exploded-view animations, rotating elements, and parallax sequences, with the source reporting 1080p output and approximately three minutes per animation. The reported cost breakdown is roughly $0.50–$1 for Claude Code prompts, $1–$2 for Kling through Higgsfield, and approximately $0.50 for image generation such as Nano Banana. These figures remain source claims. ^[raw/articles/2026-05-04-explorax-ai-3d-scroll-websites-2051261067339157657.md]

Technical effects named in this branch include locomotive-scroll sequences, dual-video backgrounds, GSAP ScrollTrigger, and a `nano-animate`-style 3D library. One cited GSAP example uses `rotateX: 8`, `scale: 0.92`, and `y: -60` for a tilt-back effect. ^[raw/articles/2026-05-04-explorax-ai-3d-scroll-websites-2051261067339157657.md]

## Motion-website and skill-pack extensions

The surrounding cluster adds two related implementations:

- **Kenny1st skill-pack variant:** select two or three motion or color references from Pinterest or Dribbble, recreate them as AI images, turn them into video, then give the video to a skill pack in Cursor or another IDE with a request for a 3D-scroll hero. The skill is source-described as carrying smooth-scroll logic and implementation practices. ^[raw/articles/thread-0xKenny1st-2080369523765436623.md]
- **ZEUS motion-website variant:** connect Higgsfield MCP to Claude or Claude Code, load a Motion Website Generator skill, generate motion clips, extract frames, assemble HTML/CSS and scroll behavior, then reskin the result for niche-specific client demos. ^[raw/articles/xarticle-35k-motion-website-playbook-higgsfield-claude-code-2067204840342630789.md]

These are not interchangeable toolchains. They share the same architecture—reference-led visual direction, generated motion assets, frame or video integration, AI-assisted implementation, and reusable deployment—but their named tools and handoff steps must remain distinct.

## Technical architecture

The recurring architecture is:

```text
visual references
→ generated keyframes or visual assets
→ image-to-video transition generation
→ clip merge and timing
→ video-to-JPG frame extraction
→ scroll-linked frame renderer
→ independently designed page sections
→ code export and IDE integration
→ targeted interaction polish
→ local preview and deployment
```

The high-leverage boundary is the asset/code handoff. The video-generation tools produce a finite visual sequence; the IDE turns that sequence into a scroll-controlled experience; the section-design tool supplies ordinary page structure and copy; and the final IDE pass joins the two. The sources do not establish one mandatory renderer or frontend framework, so implementation details such as canvas versus `<img>`, preloading, frame compression, responsive fallbacks, reduced-motion behavior, and deployment must be decided and verified separately.

## Cost, quality, and verification boundaries

**Confirmed as source content:** the named tools, keyframe sequence, Flow AI start/end-frame workflow, Clipchamp merge steps, EZGIF 10-second/30-fps extraction settings, Antigravity prompts and local preview, Google AI Studio section-export flow, Cloudinary URL handoff, and the adjacent Claude Code/Kling/Higgsfield variants.

**Likely useful:** the strongest quality control is reference selection plus explicit parameters—aspect ratio, frame dimensions, typography, spacing, card treatment, frame rate, and transition boundaries—rather than a single vague request for a premium website.

**Unverified:** the “no code,” “no design skills,” “under 10 minutes,” `$2–3` cost, `$5k–$10k` or `$10k` value framing, agency-equivalent output, generated-code quality, smoothness across devices, browser performance, accessibility, reduced-motion support, and whether the named tools still expose the same interfaces.

The source does not specify production safeguards such as frame compression, lazy loading, canvas virtualization, mobile poster fallbacks, keyboard behavior, contrast over video, reduced-motion handling, or performance budgets. Those are implementation requirements, not claims supplied by the article.

## Related concepts

- [[0xkenny1st]] — source author and skill-pack workflow.
- [[ai-website-production-loop]] — reusable reference-to-assets-to-agent implementation loop.
- [[ai-cinematic-website-design]] — broader premium visual-design framework.
- [[motion-website-service-playbook]] — productized motion-website service layer.
- [[scroll-stopping-effect]] — attention mechanism used by cinematic hero motion.
- [[claude-code]] — coding-agent branch of the cluster.
- [[kling]] — video-generation model in the Higgsfield branch.
- [[higgsfield]] — platform used by the adjacent Kling workflow.

## Sources

- [exploraX_ tweet 2051261067339157657](https://x.com/exploraX_/status/2051261067339157657) — original AI 3D-scroll demo.
- [Kenny1st X Article 2077042196155363401](https://x.com/0xKenny1st/status/2077042196155363401) — detailed free-tool Paris travel-site workflow.
- [Kenny1st thread 2080369523765436623](https://x.com/0xKenny1st/status/2080369523765436623) — skill-pack 3D-scroll variant.
- [ZEUS X Article 2067204840342630789](https://x.com/zeuuss_01/status/2067204840342630789) — Higgsfield MCP and Claude Code motion-website variant.
