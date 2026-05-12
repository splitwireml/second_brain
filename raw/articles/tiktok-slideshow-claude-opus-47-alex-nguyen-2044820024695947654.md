---
updated: 2026-04-19
title: "How to Automate TikTok Slideshow Content Creation with Claude Opus 4.7 (Step-by-Step Guide)"
author: "Alex Nguyen"
username: "@alexcooldev"
created: "2026-04-16"
source: "https://x.com/alexcooldev/status/2044820024695947654"
type: "xarticle"
tags: []
---


# How to Automate TikTok Slideshow Content Creation with Claude Opus 4.7 (Step-by-Step Guide)

How to Automate TikTok Slideshow Content Creation with Claude Opus 4.7 (Step-by-Step Guide)

Currently, TikTok is heavily boosting views and engagement for slideshows, you can check out these channels.

And actually, all these images are taken from Pinterest (an endless source of images, no need to use AI generation at all Cost = $0 and easy viral than AI generate).

> Stack: TikTok · SnapTik · Claude Opus 4.7 · Pinterest · Node.js Canvas · Postiz Agent CLI, Cost: ~$0. (Almost Open Source option)

## Why This Workflow?

Most creators are still doing content manually: come up with an idea → design → post one by one. It's time-consuming and inconsistent. Here's why this workflow works:

- No expensive tools. Buffer, Later, and Hootsuite all have limited free tiers. Self-hosted Postiz is unlimited.

- Scalable. Once set up, you can batch 30 posts/week in 2 hours.

- Data-driven. Hooks come from actually viral videos, not guesswork.

## Overview: The 5-Step Workflow

```bash
[TikTok Scroll] → [SnapTik Download] → [Claude Opus 4.7 Extract Hook]
       ↓
[Pinterest Pick Images] → [Node.js Canvas Script → PNG Slides]
       ↓
[Postiz Agent CLI → Schedule Draft]
       ↓
[TikTok App → Drafts → Tap Post at peak time]
```

## Step 1: Find Hooks From TikTok

The hook is the first 3 seconds that determine whether someone stops scrolling or not. This is your best data source, pulled directly from videos that are already going viral in your niche.

How to scroll with purpose

Open TikTok and search keywords in your niche (e.g. "StudyTok", "GymTok", "BookTok"...). Filter by Most Liked or Most Recent to see what's currently trending.

While watching, pay attention to:

- The first text overlay, appearing within the first 2 seconds

- The opening line, usually a question or a shocking statement

- Recurring formats: "You're doing X wrong", "X things Y never tells you", "I did X and here's what happened"

Download videos to analyze

Use SnapTik or SSSTik to download videos without a watermark:

1. Copy the TikTok video link

2. Go to [snaptik.app](https://snaptik.app/) or [ssstik.io](https://ssstik.io/)

3. Paste the link → Download (select "Without Watermark")

Save locally, then upload to Claude in the next step.

## Step 2: Extract Hooks with Claude Opus 4.7 (From Slideshows)

This is the step most people skip.

Instead of guessing hooks, let Claude Opus 4.7 analyze viral slideshow patterns that are already working.

Prompt to Extract Hooks from a Slideshow

Upload the slideshow images (or PDF/carousel) to Claude Opus 4.7, then use this prompt:

Analyze this TikTok slideshow and:

1. Identify the main hook used in the first slide
   (focus on text overlay, headline, and visual framing)

2. Explain why this hook works
   (curiosity / pain point / surprise / relatability)

3. Break down the hook structure
   (e.g., number + outcome, negative framing, identity targeting)

4. Write 5 similar hook variations for the niche [YOUR NICHE HERE]
   - Each hook under 10 words
   - Format: a question OR a strong statement
   - Avoid generic openers like "Did you know"

Output as a numbered list, one hook per line.

Prompt if You Only Have the Slideshow Content (No Images)

If you extracted text manually from slides:

Here is the content of a viral TikTok slideshow in the niche [NICHE]:
[PASTE CONTENT HERE]

Task:
- Identify the core hook from the first slide
- Write 7 hook variations for a similar slideshow
- Each hook must trigger one of 3 emotions:
  curiosity / FOMO / empathy
- Max 8 words per hook
- Include a short explanation of why each hook works

Real Output Example

For the personal finance niche, Claude might return:

Save & Build Your Hook Library

Save all hooks into:

- Obsidian (Super powerful)

- Notion

- Google Sheets

Over time, you’ll build a hook database → faster content creation → higher hit rate

Bonus: Generate Pinterest Search Terms (for Step 3)

While you still have the slideshow in Claude Opus 4.7, run this:

Based on this slideshow, suggest 10 Pinterest search queries
that match the visual style and content theme.

Focus on:
- Aesthetic keywords
- Composition (minimal, bold text, dark mode, etc.)
- Niche-specific visuals

Output as a list of short search phrases.

This helps you go into Step 3 with precise visuals, instead of guessing.

## Bonus: Extract Visual Style + Pinterest Queries (for Slideshows)

While you still have the slideshow in Claude Opus 4.7, run this:

Now look at the visual style of this slideshow:

1. Describe the color palette, lighting, and overall aesthetic
   (dark/moody, bright/clean, luxury, minimal, etc.)

2. What kind of images would work as slideshow backgrounds
   for the hooks you just wrote?

3. Give me 5 specific Pinterest search queries to find those images
   - Format: short keyword phrases, 2–4 words each
   - Optimized for Pinterest search, not Google

Example Output (Personal Finance Slideshow)

👉 Copy these directly into Pinterest search for Step 3.

## Step 3: Pick Images From Pinterest

By now Claude has given you both the hooks and the Pinterest search terms. Go straight to searching, no need to figure out what to look for.

What makes a good TikTok image

- Ratio: Prioritize portrait / 9:16. Landscape works too; the script will crop it.

- Colors: Bold, high contrast. Avoid soft pastels since the TikTok feed is competitive.

- Content: Minimal text in the image (since you'll be overlaying your own text)

- Vibe: Should match the emotion of your hook. Money hook = lifestyle image, fitness hook = action shot

Use the search terms from Claude Opus 4.7

Paste the 5 queries Claude Opus 4.7 gave you directly into Pinterest search. Each query targets a specific visual vibe rather than a broad topic, so results are much more consistent and on-brand.

How to download Pinterest images

Option 1: PinDown Chrome Extension

1. Install [PinDown](https://chrome.google.com/webstore/detail/pindown) on Chrome

2. Open a Pinterest image → Click the PinDown icon → Download full resolution

Option 2: Direct right-click

1. Click the image to open full size

2. Right-click → "Open image in new tab"

3. Right-click the image → Save image as

Option 3: Bulk download with Python (for full automation)

```python
# pinterest_downloader.py
import requests
from pathlib import Path

def download_image(url: str, filename: str, folder: str = "pinterest_images"):
    Path(folder).mkdir(exist_ok=True)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(f"{folder}/{filename}.jpg", "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {filename}")

# Paste direct image URLs from Pinterest
urls = [
    "https://i.pinimg.com/originals/...",  # URL 1
    "https://i.pinimg.com/originals/...",  # URL 2
]

for i, url in enumerate(urls):
    download_image(url, f"image_{i+1:03d}")
```

Organize by niche:

```bash
pinterest_images/
  ├── finance/
  ├── fitness/
  └── lifestyle/
```

## Step 4: Generate Slides with Node.js Canvas (No Canva Needed)

Instead of designing manually in Canva, use a script to programmatically overlay hook text onto your Pinterest images and export them as 1080×1920 PNGs, fully automated.

Install dependencies

```bash
mkdir tiktok-slide-gen && cd tiktok-slide-gen
npm init -y
npm install canvas @napi-rs/canvas sharp
```

> @napi-rs/canvas is a fast, native Node.js canvas implementation. No browser required.

Slideshow structure

```bash
Slide 1: HOOK       (text overlay on the strongest image)
Slide 2: Problem / Setup
Slide 3: Point 1
Slide 4: Point 2
Slide 5: Point 3
Slide 6: CTA        (Follow, Save, Comment, Download app)
```

The script: generate-slides.js

```javascript
// generate-slides.js
import { createCanvas, loadImage, GlobalFonts } from '@napi-rs/canvas'
import { writeFileSync, mkdirSync } from 'fs'
import { join } from 'path'

// ─── CONFIG ───────────────────────────────────────────────
const OUTPUT_DIR = './output'
const CANVAS_W = 1080
const CANVAS_H = 1920
const OVERLAY_OPACITY = 0.52   // dark overlay on image, 0–1
const OVERLAY_COLOR = '0,0,0'  // RGB for overlay

// Optional: load a custom font (TTF/OTF)
// GlobalFonts.registerFromPath('./fonts/Inter-Bold.ttf', 'InterBold')

// ─── SLIDE DEFINITIONS ────────────────────────────────────
// Each slide: { imagePath, lines: [{ text, size, weight, y }] }
const slides = [
  {
    imagePath: './pinterest_images/finance/image_001.jpg',
    lines: [
      { text: 'I saved $5k in 6 months', size: 88, weight: 'bold', y: 860 },
      { text: 'doing this one thing', size: 72, weight: 'normal', y: 970 },
    ],
  },
  {
    imagePath: './pinterest_images/finance/image_002.jpg',
    lines: [
      { text: 'Most people spend', size: 64, weight: 'normal', y: 820 },
      { text: 'before they save.', size: 64, weight: 'bold', y: 910 },
      { text: "Here's why that's a trap.", size: 56, weight: 'normal', y: 990 },
    ],
  },
  {
    imagePath: './pinterest_images/finance/image_003.jpg',
    lines: [
      { text: '01. Pay yourself first', size: 72, weight: 'bold', y: 900 },
      { text: 'Move 20% to savings on payday.', size: 52, weight: 'normal', y: 990 },
      { text: 'Before any expense hits.', size: 52, weight: 'normal', y: 1060 },
    ],
  },
  {
    imagePath: './pinterest_images/finance/image_004.jpg',
    lines: [
      { text: '02. Kill subscriptions', size: 72, weight: 'bold', y: 900 },
      { text: 'Audit every recurring charge.', size: 52, weight: 'normal', y: 990 },
      { text: 'Cancel what you forgot existed.', size: 52, weight: 'normal', y: 1060 },
    ],
  },
  {
    imagePath: './pinterest_images/finance/image_005.jpg',
    lines: [
      { text: '03. Use cash envelopes', size: 72, weight: 'bold', y: 900 },
      { text: 'Allocate per category, in cash.', size: 52, weight: 'normal', y: 990 },
      { text: 'When it runs out, it runs out.', size: 52, weight: 'normal', y: 1060 },
    ],
  },
  {
    imagePath: './pinterest_images/finance/image_006.jpg',
    lines: [
      { text: 'Save this post 🔖', size: 80, weight: 'bold', y: 860 },
      { text: 'Follow for more money tips', size: 56, weight: 'normal', y: 970 },
      { text: 'every week →', size: 56, weight: 'normal', y: 1050 },
    ],
  },
]

// ─── HELPERS ──────────────────────────────────────────────
function wrapText(ctx, text, maxWidth) {
  const words = text.split(' ')
  const lines = []
  let current = ''
  for (const word of words) {
    const test = current ? `${current} ${word}` : word
    if (ctx.measureText(test).width > maxWidth && current) {
      lines.push(current)
      current = word
    } else {
      current = test
    }
  }
  if (current) lines.push(current)
  return lines
}

async function generateSlide(slide, index) {
  const canvas = createCanvas(CANVAS_W, CANVAS_H)
  const ctx = canvas.getContext('2d')

  // 1. Draw background image, cover-fit
  const img = await loadImage(slide.imagePath)
  const scale = Math.max(CANVAS_W / img.width, CANVAS_H / img.height)
  const drawW = img.width * scale
  const drawH = img.height * scale
  const offsetX = (CANVAS_W - drawW) / 2
  const offsetY = (CANVAS_H - drawH) / 2
  ctx.drawImage(img, offsetX, offsetY, drawW, drawH)

  // 2. Dark overlay
  ctx.fillStyle = `rgba(${OVERLAY_COLOR},${OVERLAY_OPACITY})`
  ctx.fillRect(0, 0, CANVAS_W, CANVAS_H)

  // 3. Draw each line of text
  const PADDING = 80
  const MAX_TEXT_W = CANVAS_W - PADDING * 2

  for (const line of slide.lines) {
    ctx.font = `${line.weight} ${line.size}px sans-serif`
    ctx.fillStyle = '#ffffff'
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'

    // Drop shadow
    ctx.shadowColor = 'rgba(0,0,0,0.75)'
    ctx.shadowBlur = 12
    ctx.shadowOffsetY = 4

    const wrapped = wrapText(ctx, line.text, MAX_TEXT_W)
    const lineHeight = line.size * 1.2
    wrapped.forEach((l, i) => {
      ctx.fillText(l, CANVAS_W / 2, line.y + i * lineHeight)
    })
  }

  // 4. Export PNG
  mkdirSync(OUTPUT_DIR, { recursive: true })
  const outPath = join(OUTPUT_DIR, `slide_${String(index + 1).padStart(2, '0')}.png`)
  const buffer = canvas.toBuffer('image/png')
  writeFileSync(outPath, buffer)
  console.log(`✓ ${outPath}`)
}

// ─── MAIN ─────────────────────────────────────────────────
async function main() {
  console.log(`Generating ${slides.length} slides...`)
  for (let i = 0; i < slides.length; i++) {
    await generateSlide(slides[i], i)
  }
  console.log(`\nDone → ${OUTPUT_DIR}/`)
}

main().catch(console.error)
```

Run it

Output:

```bash
node generate-slides.js

```

Generating 6 slides...

```bash
✓ output/slide_01.png
✓ output/slide_02.png
✓ output/slide_03.png
✓ output/slide_04.png
✓ output/slide_05.png
✓ output/slide_06.png

Done → output/
```

Using a custom font

Download any TTF/OTF font (e.g. Inter Bold, Montserrat Black) and register it:

```javascript
import { GlobalFonts } from '@napi-rs/canvas'

GlobalFonts.registerFromPath('./fonts/Montserrat-Black.ttf', 'MontserratBlack')

// Then use in ctx.font:
ctx.font = `bold 88px MontserratBlack`
Batch-generate from a JSON config
Instead of editing the script each time, drive it from a JSON file:
// slides-config.json
[
  {
    "imagePath": "./pinterest_images/finance/image_001.jpg",
    "lines": [
      { "text": "I saved $5k in 6 months", "size": 88, "weight": "bold", "y": 860 },
      { "text": "doing this one thing",    "size": 72, "weight": "normal","y": 970 }
    ]
  }
]
// At the top of generate-slides.js, replace the slides array with:
import { readFileSync } from 'fs'
const slides = JSON.parse(readFileSync('./slides-config.json', 'utf-8'))
```

Now your content team can edit slides-config.json without touching code. Pair this with the hook list from your Claude Opus 4.7 output and you have a fully automated content pipeline.

## Step 5: Install Postiz Agent CLI

With your videos produced and any post-production complete, it is time to schedule them for publication. Postiz serves as your distribution command center, handling the timing, cross-posting, and engagement automation.

Repo / docs: [postiz.com/agent](https://postiz.com/agent)

```bash
Install
npm install -g postiz
Authenticate
Go to postiz.com → sign up for free → Settings → API Keys → copy your key.
# Set the API key (add to ~/.zshrc or ~/.bashrc to persist)
export POSTIZ_API_KEY=your_api_key_here
```

Verify it's working:

```bash
postiz integrations:list

```

This returns all your connected social accounts as JSON. If you see an empty array [], you need to connect TikTok first.

Connect TikTok to Postiz

1. Go to [app.postiz.com](https://app.postiz.com/) → Integrations → Add Channel → TikTok

2. Authorize with your TikTok account

3. Run postiz integrations:list again and you'll see your TikTok integration ID:

Copy the id. You'll need it in every posts:create command.

```javascript
[
  {
    "id": "clx9abc123",
    "provider": "tiktok",
    "name": "My TikTok Account",
    "picture": "https://..."
  }
]

```

Core CLI commands for TikTok

```bash
# Upload slides (PNG files), get back CDN URLs
SLIDE1=$(postiz upload ./output/slide_01.png | jq -r '.path')
SLIDE2=$(postiz upload ./output/slide_02.png | jq -r '.path')
SLIDE3=$(postiz upload ./output/slide_03.png | jq -r '.path')

# Schedule a slideshow post — pass multiple -m flags for each slide
postiz posts:create \
  -c "I saved \$5k in 6 months doing this 💰 #personalfinance #moneytips" \
  -m "$SLIDE1" -m "$SLIDE2" -m "$SLIDE3" \
  -s "2025-04-21T09:00:00Z" \
  -i "clx9abc123"

# List all scheduled posts
postiz posts:list

# Check TikTok-specific settings available
postiz integrations:settings clx9abc123
Every command outputs structured JSON, easy to parse in scripts or pipe into other tools.
Batch schedule a full week from schedule.json
// batch-schedule.js
// Reads schedule.json, uploads each slide set, schedules via Postiz Agent CLI
import { execSync } from 'child_process'
import { readFileSync } from 'fs'

const INTEGRATION_ID = process.env.TIKTOK_INTEGRATION_ID
const schedule = JSON.parse(readFileSync('./schedule.json', 'utf-8'))

for (const post of schedule) {
  // 1. Upload each PNG slide, collect CDN URLs
  const slideFlags = post.slides.map(slide => {
    const result = JSON.parse(execSync(`postiz upload ${slide}`).toString())
    return `-m "${result.path}"`
  }).join(' ')

  // 2. Schedule slideshow post via Postiz Agent
  execSync(
    `postiz posts:create \
      -c "${post.caption}" \
      ${slideFlags} \
      -s "${post.scheduledAt}" \
      -i "${INTEGRATION_ID}"`,
    { stdio: 'inherit' }
  )

  console.log(`✓ Scheduled: ${post.slides.length} slides at ${post.scheduledAt}`)
}
// schedule.json
[
  {
    "slides": ["./output/mon_01.png", "./output/mon_02.png", "./output/mon_03.png", "./output/mon_04.png", "./output/mon_05.png", "./output/mon_06.png"],
    "caption": "I saved $5k in 6 months doing this 💰 #personalfinance",
    "scheduledAt": "2025-04-21T09:00:00Z"
  },
  {
    "slides": ["./output/tue_01.png", "./output/tue_02.png", "./output/tue_03.png", "./output/tue_04.png", "./output/tue_05.png", "./output/tue_06.png"],
    "caption": "Stop putting money in these 3 things 🚫 #moneytips",
    "scheduledAt": "2025-04-22T09:00:00Z"
  },
  {
    "slides": ["./output/wed_01.png", "./output/wed_02.png", "./output/wed_03.png", "./output/wed_04.png", "./output/wed_05.png", "./output/wed_06.png"],
    "caption": "The money trap nobody warns you about 😮 #finance",
    "scheduledAt": "2025-04-23T09:00:00Z"
  }
]
```

Run it:

```bash
TIKTOK_INTEGRATION_ID=clx9abc123 node batch-schedule.js
```

One command, entire week scheduled.

## Step 6: Post as TikTok Draft to Avoid Spam Detection

This is the most overlooked part of any TikTok automation setup. If you push posts directly via the API at scheduled times from a server IP, TikTok's system will eventually flag the pattern as bot behavior: reduced reach, shadow restrictions, or full account flags.

The safe approach: upload to Drafts, publish manually from the app.

Why Draft mode matters

When you auto-publish via API, TikTok sees:

- A server IP initiating the post

- Consistent robotic posting intervals

- No human interaction before the post goes live

When you post from Drafts:

- The slides land in your TikTok Drafts silently

- You open the app at peak time, review the draft, and hit Post

- From TikTok's perspective: a human published from a real device on a real network

- No server fingerprint on the actual publish action

This one change makes a significant difference for account health, especially on new accounts or when posting at high frequency.

The hybrid workflow

```bash
[generate-slides.js] → PNG slides (slide_01.png ... slide_06.png)
         ↓
[tiktok-draft-upload.js] → upload slides to TikTok Drafts via API
         ↓
[Postiz Notify mode] → sends push notification at peak time
         ↓
[You open TikTok app] → Drafts → review → tap Post
```

Postiz handles the scheduling calendar and reminder. The actual publish comes from your device, which reads as a clean signal to the algorithm.

## Upload PNG slides to TikTok Drafts

Option 1: Draft inside Postiz (kept in Postiz, not published)

Use the -t draft flag:

```bash
# Upload video first
RESULT=$(postiz upload video.mp4)
VIDEO_URL=$(echo "$RESULT" | jq -r '.path')

# Create post as draft
postiz posts:create \
  -c "Your caption #fyp" \
  -m "$VIDEO_URL" \
  -s "2026-04-20T10:00:00Z" \
  -t draft \
  -p tiktok \
  --settings '{
    "title": "Video title",
    "privacy_level": "PUBLIC_TO_EVERYONE",
    "duet": false,
    "stitch": false,
    "comment": true,
    "autoAddMusic": "no",
    "brand_content_toggle": false,
    "brand_organic_toggle": false,
    "video_made_with_ai": false,
    "content_posting_method": "DIRECT_POST"
  }' \
  -i "tiktok-integration-id"
```

Post will sit in Postiz as draft and won't publish until you change status. Use postiz posts:status <id> --status schedule to queue it for publishing, or posts:delete to discard.

Option 2: Push to TikTok Inbox (draft inside TikTok app)

If you want the post to appear in the TikTok app as a pending draft you finalize on your phone, set content_posting_method to "UPLOAD":

```bash
postiz posts:create \
  -c "Caption shown when you open TikTok app" \
  -m "$VIDEO_URL" \
  -s "2026-04-20T10:00:00Z" \
  -p tiktok \
  --settings '{
    "privacy_level": "SELF_ONLY",
    "content_posting_method": "UPLOAD"
  }' \
  -i "tiktok-integration-id"
```

When Postiz "publishes" this, TikTok delivers the video to the Inbox in the app. You open the app → tap the notification → finalize and post manually.

Configure Postiz in Notify mode

Set Postiz to Notify instead of Auto Publish. Postiz manages your editorial calendar and sends a push notification at the scheduled time reminding you to publish the draft from the app:

1. Postiz Dashboard → New Post

2. Select TikTok → add your caption and schedule the time

3. Under Publish mode, select Notify (not Direct Post)

4. Save

At the scheduled time, Postiz sends a mobile push notification: "Time to post your TikTok!" Open the app, find the draft waiting, and tap Post.

## Troubleshooting Common Issues

POSTIZ_API_KEY environment variable is required

You haven't exported the key in the current shell session. Add it permanently:

```bash
echo 'export POSTIZ_API_KEY=your_key_here' >> ~/.zshrc
source ~/.zshrc
```

postiz integrations:list returns empty array []

Your TikTok account isn't connected to Postiz yet. Go to [app.postiz.com](https://app.postiz.com/) → Integrations → Add Channel → TikTok and authorize.

postiz upload fails

Check your POSTIZ_API_KEY is still valid. For large PNG files (unlikely with typical slides), try compressing first with pngquant:

```bash
pngquant --quality=80-90 output/slide_*.png --ext .png --force

```

Scheduled post didn't go out

Check postiz posts:list and look at the status field. If it's failed, Postiz will show an error reason (usually expired TikTok OAuth token or rate limit). Re-authenticate on [app.postiz.com](https://app.postiz.com/) or local (if you self host) and reschedule.

Noted: Make sure your account has been posting for a while and is genuinely healthy.

Good luck guys 🫡
