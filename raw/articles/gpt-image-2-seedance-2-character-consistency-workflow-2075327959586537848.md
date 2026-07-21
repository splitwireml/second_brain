---
source_url: https://x.com/primee32/status/2075327959586537848
ingested: 2026-07-20
sha256: e9da5b4ddfbac9c1cc7ad875f173904cf537ed93806c987464129e32c21f5b5b
---
GPT IMAGE 2.0 + SEEDANCE 2.0: THE ONLY WORKFLOW WHERE YOUR CHARACTER NEVER DRIFTS

GPT Image 2.0 builds the character. Seedance 2.0 brings it to life.

Most creators treat these as two separate steps — generate an image, then hope the video model keeps it together. That's where drift happens: a dragon losing its horns mid-flight, a rider's jacket changing color between cuts, a face that looks different in every new shot.

This guide is the complete system for using both tools together so that never happens — from building a single character reference sheet, through a full storyboard grid, to a finished cinematic sequence with zero drift.

Everything below is built around one real example: a rider and her black dragon, flying through a misty canyon, a waterfall drop, and a forest landing — the same two characters, locked, from first frame to last.

---

Seedance 2.0 vs Kling 3.0 vs Runway Gen-4 vs WAN 2.7

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
|  Feature | Seedance 2.0  | Kling 3.0 | Runway Gen-4  | WAN 2.7  |
| Character consistency  | Excellent  | Good  | Fair  | Excellent  |
| JSON prompting  | Yes  | No  | No  | Partial  |
| Multi-shot in one prompt  | Limited  | No | No  | Yes  |
| Cinematic camera control  | Yes  | Yes  | Limited  | Yes (FLF2V)  |
| Clip duration  | up to 10 sec  | up to 10 sec  | up to 16 sec  | up to 15 sec  |

---

Both tools run on paid tiers, but you don't need the most expensive plan to run this workflow. Here's exactly what each tier unlocks, so you're not paying for capacity you won't use.

|  Plan | Price  | Image 2.0 Access  | Best For  |
| --- | --- | --- | --- |
| Free  | $0/mo  | No  | Exploring ChatGPT  |
| Plus  | $20/mo  | Yes  | Individual creators  |
| Pro  | $200/mo  | Yes  | Active producers  |
| Team  | $30/user/mo  | Yes  | Teams & agencies  |

Seedance 2.0 pricing works differently — instead of a flat monthly cap, you're spending credits per generation. A single 5-second clip costs roughly 50-80 credits depending on resolution, so your monthly credit pool determines how many finished shots you can actually produce, not just how many times you can log in.

| Plan  | Price  | Credits/mo  | Video Quality  |
| --- | --- | --- | --- |
| Free  | $0  | ~80 credits  | 720p  |
| Standard  | $13/mo  | 500 credits  | 1080p  |
| Pro  | $35/mo  | 2,000 credits  | 1080p + 4K  |
| Business  | $99/mo  | 8,000 credits  | 4K  |

💡 Recommended starter: ChatGPT Plus ($20/mo) + Dreamina Standard ($13/mo). Together $33/month — enough to run the full workflow in this guide, including multiple character sheets and a full storyboard grid per month.

If you're just testing whether this workflow fits your style, both free tiers are enough to build one character sheet and generate a handful of test clips before committing to a paid plan.

---

A prompt is the instruction you give the AI. The quality of your prompt directly determines the quality of the result — this is true whether you're generating a single reference image or a full cinematic shot.

Most weak prompts fail for the same reason: they describe the subject and stop there, leaving lighting, camera, and mood entirely up to the model's guess. The fix is to think in blocks instead of sentences — six categories that together leave nothing to chance.

|Block   |What It Describes   |Example   |
| --- | --- | --- |
|Subject   | Who or what is in the frame  |A rider on a black dragon   |
| Action  | What the subject is doing  | Banking through a waterfall drop  |
| Environment  | Where the action takes place  | Misty canyon at golden hour  |
| Lighting  |Type and color of light   |Warm rim light, deep blue shadows   |
|Style   | Artistic reference  |Cinematic, photorealistic, 8K   |
|Camera   | Shot type and angle  | Wide shot, static, low angle  |
|Mood   |Emotional atmosphere   | Epic, primal, weightless  |

Here's what happens when you apply that structure to the same idea — once with just the subject, once with all six blocks filled in.

❌ Weak prompt: A dragon flying with a rider on its back.

✅ Strong prompt: A massive black dragon with amber eyes and hooked wing tips, banking hard through a waterfall drop at golden hour, mist and spray catching the light. A rider in leather flight gear leans low against the wind. Wide tracking shot, camera panning right to follow the motion. Cinematic photorealistic style, 8K, epic and weightless mood.

```
{
  "subject": "A massive black dragon with amber eyes and hooked wing tips",
  "action": "banking hard through a waterfall drop",
  "environment": "misty canyon, golden hour, spray catching the light",
  "lighting": "warm rim light, deep blue shadow falloff",
  "camera": {
    "type": "tracking shot",
    "angle": "wide, slightly low",
    "movement": "smooth pan right matching dragon's bank"
  },
  "style": "cinematic photorealistic, 8K",
  "mood": "epic, weightless, primal"
}
```

---

Before you build a single frame of your storyboard, you need to lock your characters. This is the step most creators skip — they generate one hero shot, move on, and then spend the rest of the project fighting drift.

The fix is a single character sheet that captures everything Seedance 2.0 needs to hold both the rider and the dragon consistent: turnarounds, expressions, action poses, and exact color values — all in one image, generated once in GPT Image 2.0.

Create a paired character reference sheet for a visual storytelling project.

Characters:

1. Rider — an adult woman, athletic build, dark hair in a tight braid, angular leather flight gear with metal buckles, amber eyes, confident stance

2. Dragon — a large black-scaled dragon, ridged spine running down the back, broad membranous wings with hooked wingtips, elongated narrow snout, glowing amber eyes

Generate on a neutral dark background:

1. Rider turnaround — front view, side profile (90 degrees), back view

2. Dragon turnaround — front view, side profile, back view

3. Rider expression set — focused takeoff, windswept dive, calm glide, triumphant landing

4. Dragon action poses — full wingspan glide, tucked dive, banking turn, landing crouch

Style: cinematic, dramatic lighting, photorealistic, 8K

Maintain identical appearance for both characters across every view and pose.

Lock exact color values: dragon scale tone, leather grain color, hair tone — no variation between panels.

| Parameter  | Description  | Example  |
| --- | --- | --- |
| Rider name  |Unique identifier   | Kira  |
| Rider build  |Body type, height   | Athletic, 5'8"  |
| Rider gear  | Signature outfit  | Dark leather flight gear, metal buckles  |
| Dragon build  |Size, scale color   |Large, black scales   |
|Dragon features   |Wings, spine, snout   | Hooked wingtips, ridged spine  |
|Hex values   | Locked color codes  | Scale #1A1A1A, leather #4A3728  |

---

With the character sheet locked, you're ready for the part that actually keeps consistency through motion — building the entire sequence as one storyboard grid before Seedance 2.0 ever sees a single frame.

Instead of generating shot by shot and hoping the rider and dragon hold together, you design all 16 frames together in GPT Image 2.0, using the character sheet as the reference. The grid becomes both your shot list and your consistency anchor.

Using the attached character reference sheet, generate a 4x4 storyboard grid — 16 numbered frames — for a flight sequence.

Sequence: rider and dragon take off through a misty canyon, bank through a waterfall drop, and glide into a forest clearing for landing.

Frames:

1. Wide shot, takeoff from canyon floor, wings extending

2. Medium shot, ascending past canyon walls

3. Wide shot, leveling out into open sky, mist below

4. Close-up, rider's posture as she leans into the climb

5. Wide shot, approaching the waterfall, spray visible ahead

6. Medium shot, banking hard right toward the drop

7. Close-up, dragon's wing tucking mid-turn

8. Wide shot, diving through the waterfall spray

9. Medium shot, emerging from the mist, sunlight breaking through

10. Wide shot, gliding low over the tree line

11. Close-up, rider scanning the forest below

12. Medium shot, dragon's wings adjusting for descent

13. Wide shot, forest clearing coming into view

14. Medium shot, final approach, wings flaring

15. Close-up, landing crouch, dust and leaves scattering

16. Wide shot, final resting position, wings folding down

Style: cinematic, dramatic lighting, photorealistic, 8K, consistent with the character reference sheet

Numbered corners, thin black borders between frames, one-line caption baked into each frame

Maintain identical rider and dragon appearance across all 16 frames — same colors, same proportions, no variation.

Once the grid is generated, pull each frame out individually — these become your direct references for Seedance 2.0 in the next section. You're no longer feeding the model a vague idea of the sequence; you're feeding it 16 pre-approved, already-consistent shots.

---

With 16 consistent frames in hand, the last piece is telling Seedance 2.0 exactly how to animate each one. Plain-text prompts work, but they leave too much room for the model to guess at camera behavior — and guessing is where drift creeps back in even after all the prep work.

JSON prompting removes the guesswork. Instead of one long sentence, you're handing Seedance 2.0 a structured object — every parameter explicit, nothing left to interpretation.

```
{
  "subject": "The rider and dragon from the character reference sheet",
  "action": "banking hard through a waterfall drop, wings tucking mid-turn",
  "environment": "misty canyon, waterfall spray, golden hour light",
  "lighting": "warm rim light on wings, deep blue shadow falloff in the mist",
  "camera": {
    "type": "tracking shot",
    "angle": "wide, slightly low",
    "movement": "smooth pan right matching the dragon's bank",
    "duration_sec": 5
  },
  "reference_image": "frame_06_grid.jpg",
  "style": "cinematic photorealistic, 8K",
  "motion_intensity": "high",
  "transition_out": "hold on final frame, no fade"
}
```

Run one JSON object per frame from your grid, feeding in the matching reference image each time. It's more setup than a single prompt, but it's the difference between Seedance 2.0 interpreting your shot and Seedance 2.0 executing it exactly as planned.

---

Here's the full process from grid to finished clip, start to finish. Nothing here is complicated on its own — the value is in doing every step in order, without skipping ahead.

|Step   | Action  | Note  |
| --- | --- | --- |
|1   | Open Seedance 2.0 in Dreamina  | Select Image to Video mode  |
| 2  | Upload the matching grid frame  | One frame = one shot  |
| 3  | Activate JSON mode  | Toggle in the prompt panel  |
| 4  | Paste the JSON prompt  |Validate syntax before generating   |
|  5 |Set duration   | 5 sec for standard shots, 8-10 sec for transitions  |
| 6  |Click Generate   | First run is a test — review before finalizing  |
|7   | Repeat for each of the 16 frames  |Keep filenames matching frame numbers   |
| 8  |Stitch clips in sequence order   | Move to editing software next  |

The first generation almost never needs zero adjustment — treat it as a draft, check it against your reference frame, and regenerate only the shot that's drifting instead of restarting the whole sequence.

---

Even with a locked character sheet and a clean JSON prompt, raw output from Seedance 2.0 usually needs a pass before it's publish-ready. Two things typically need fixing: resolution for the platform you're posting to, and small inconsistencies that slip through between shots.

|Method   |Tool   |Result   | Difficulty  |
| --- | --- | --- | --- |
|Built-in Dreamina upscale   |Upscale button   | 720p → 1080p or 1080p → 4K  | Easy  |
|  Topaz Video AI | Standalone app  | Up to 8K, artifact cleanup  |Medium   |
| DaVinci Resolve  | Free editor  | Super Scale up to 4x  |Medium   |
|Runway Upscale   | Online  |  Good quality | Easy  |

Upscaling fixes resolution. It doesn't fix drift. If something still looks off after upscaling, it's almost always one of these four causes.

| Problem  | Cause  | Solution  |
| --- | --- | --- |
| Flickering  | Incorrect transition_out  |Specify smooth hold or dissolve   |
|Blurry motion   | motion_intensity too high  | Reduce to medium  |
| Inconsistent lighting  | Different lighting parameters between shots  | Unify color temperature across all JSON prompts  |
| Character looks different  |Missing or wrong reference image   | Re-check the frame number matches the shot  |

---

The clips are generated, upscaled, and clean. What's left is assembling them into one finished sequence and exporting it in the right format for wherever you're posting — get this step wrong and even a perfect sequence looks amateur.

| Software  | Price  | Level  |Best For   |
| --- | --- | --- | --- |
| DaVinci Resolve  | Free  | Beginner+  | Full editing, color grading  |
| CapCut Desktop  | Free  | Beginner  | Quick edits for social media  |
|Adobe Premiere   | $55/mo  | Advanced  |Commercial projects   |
|Final Cut Pro   | $300 (one-time)  |Mac   |Fastest render on Apple Silicon   |

Whichever software you pick, the process is the same: import, arrange, trim, and grade. Here's the exact sequence.

1. Import all 16 clips. Organize by frame number.

2. Review every clip and confirm it matches its reference frame — regenerate anything that drifted.

3. Arrange clips on the timeline in sequence order.

4. Trim each clip — remove the first and last 0.3-0.5 seconds where generation artifacts are most common.

5. Add transitions: hard cut for energy, cross dissolve only where the scene genuinely shifts (canyon → waterfall → forest).

6. Add music. Sync major beats — the banking turn, the dive, the landing — to the track.

7. Color grade: warm gold tones for the canyon and waterfall, cooler green-blue for the forest landing.

| Platform  | Resolution  | Format  | FPS  | Bitrate  |
| --- | --- | --- | --- | --- |
| X (Twitter)  |  1080x1920 |  MP4 H.264 |30   |15-20 Mbps   |
|  YouTube Shorts |1080x1920   |MP4 H.264/H.265   |  30-60 | 20-25 Mbps  |
|Instagram Reels   | 1080x1920  | MP4 H.264  | 30  |15-20 Mbps   |
| TikTok  | 1080x1920  |MP4 H.264   |30-60   |  15 Mbps |
| YouTube 4K  | 3840x2160  | MP4 H.265  | 24-60  |35-45 Mbps   |

---

Here's the part most guides leave out: everything above isn't just a workflow. It's a set of skills people are already paying for — and once you can produce a sequence like the one in this guide, there are five direct ways to turn it into income.

💰 PROMPT PACKS

Package your character sheet prompts, grid prompts, and JSON templates as a digital product. Creators pay for tested workflows, not raw ideas.

Price: $15-$100 per pack

💰 SPONSORED CONTENT

Once your sequences get consistent views, AI tool companies pay for exposure — ElevenLabs, Runway, Dreamina, and similar platforms sponsor creators who already use their tools naturally.

Price: $500-$5,000 per post

💰 DONE-FOR-YOU VIDEOS

Brands and creators who don't want to learn the workflow will pay you to run it for them — character sheet, grid, generation, edit, delivered.

Price: $300-$1,500 per video

💰 PAID NEWSLETTER

Weekly breakdowns of new prompts, tool comparisons, and workflow updates. Your audience already wants this — they're commenting on it under every post.

Price: $10-$30/month per subscriber

💰 MINI COURSE

Turn this entire guide into a structured course — character sheets, grid method, JSON prompting, editing — the exact system, taught start to finish.

Price: $97-$297 per course

Every tool in this guide is available to anyone. What isn't available to everyone is a system that turns "I made a cool AI video" into "I built something people pay for."

The window for this is still wide open — most creators are still generating one clip at a time and hoping it holds together. Follow and bookmark this guide before that changes.

---

This is the exact system behind every consistent sequence I've posted here. More breakdowns like this are coming — grid variations, new character setups, and a few tricks I haven't shared yet.

🔖 Bookmark and follow @Primee32