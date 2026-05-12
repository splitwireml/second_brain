---
title: "GPT Image 2 Is 24 Hours Old. /last30days Became an Expert and Wrote Me Perfect Prompts"
source: "https://x.com/unknown/status/2047016569923064055"
tweet_id: "2047016569923064055"
author: "{'username': 'mvanhorn', 'name': 'Matt Van Horn'}"
author_handle: "@unknown"
date: "Wed Apr 22 18:15:56 +0000 2026"
like_count: 352
retweet_count: 22
type: x-article
---

# GPT Image 2 Is 24 Hours Old. /last30days Became an Expert and Wrote Me Perfect Prompts

GPT Image 2 Is 24 Hours Old. /last30days Became an Expert and Wrote Me Perfect Prompts

OpenAI dropped GPT Image 2 yesterday. It jumped 250+ ELO on LMArena, the biggest single-release gap ever recorded in image generation. I ran /last30days on "Prompting GPT Image 2" to see what the community had already figured out. 86 seconds later it had pulled 29 Reddit threads, 19 X posts, 10 YouTube videos, 24 TikToks, 14 Instagram reels, 2 GitHub prompt libraries, and 1 Hacker News story. Then I told it to stop summarizing and start writing prompts. These are the five it gave me, and the images GPT Image 2 returned.

## What /last30days Learned Before Writing Anything

1. The LLM you pick changes the output.

> "This wasn't the case with previous image generators, but the LLM you select has a huge effect on GPT-imagegen-2 output. GPT-5.4 Thinking and GPT-5.4 Pro will produce much better images, especially for complex things. This is, of course, not intuitive or explained anywhere."- @emollick on X

Switch to a thinking model before you rephrase. Highest-leverage move in the whole workflow and nobody documented it.

2. Put literal text in double quotes. Single most-cited prompting move in the 30-day window, confirmed by the OpenAI cookbook and stress-tested across r/StableDiffusion's menu, poster, and multi-panel threads. Quoting exact text engages the high-accuracy text rendering engine. Typography goes near-perfect.

3. It's the first image model that thinks.

> "Every other image model is diffusion plus prompt equals picture. This one plans, searches the web for references, critiques its own output, and iterates before rendering."- @bywaviboy on Instagram (49K views, 1,415 likes)

Your prompts can carry way more context than they used to. The model reasons through them instead of embedding-matching.

4. The aspect-ratio hack nobody tells you. The API has no dedicated ratio control. Passing "2:1" alone fails 90% of the time. r/ChatGPT reverse-engineered the fix: append exact pixel dimensions in the prompt itself, like "Output in exactly 1774px x 887px (2:1 ratio) resolution landscape format." Top-rated practical hack of the 30-day window.

5. Prompt order is Scene, Subject, Details, Constraints. Plus the intended use (ad, UI mock, infographic, editorial photo) so the model picks the right polish level. Straight from the OpenAI cookbook. Sequential-weighting matters too: the first words carry the highest visual weight. Lead with style, not subject.

6. Text-to-image is magic. Reference-image editing is still broken.

> "It done really well in text to image, but if i give it a reference image, it will always overbake and produce a 1.5 result and have a yellow tint plus no prompt adherence at all."- r/OpenAI, "GPT image 2 weird weakness"

For design-final work, generate fresh. Image-to-image still yellow-tints and loses instruction following.

## The Five Prompts It Wrote, And The Images GPT Image 2 Returned

## 1. Research-Result Mobile UI Mockup

Dark-mode iOS screen showing /last30days' actual "All agents reported back" output as if it were a research reader app. Editorial typography, per-source accent colors, sparklines, cream on deep ink.

## 2. Editorial Magazine Cover

Typography stress test. Every cover line quoted. Didone display serif on cream paper, newsstand trim at 300dpi. Designed to demo the "near-perfect text rendering" claim at scale.

## 3. Brand Identity Reveal Board For A Fictional Coffee Bar

Noon and Co., six-panel grid: primary wordmark, reverse, monogram, tagline lockup, favicon system, real-world applications (cup, storefront awning, app icon). Vector-feeling marks on cream. The test was mark consistency across six panels in a single generation.

## 4. Photoreal Editorial Photograph, Hands Cutting A Blood Orange

50mm prime, morning kitchen light, Kodak Portra 400 rendering, weathered butcher block. Prompt includes a full believable-imperfection list: one stray seed, a juice bead on the thumbnail, a paper-cut, a single breadcrumb. Describing the photograph, not the fantasy.

## 5. Eight-Up Character Consistency Sheet

The miracle demo. One prompt, one sheet, eight full-body shots of the same person across a week of real moments (commute, yoga, coffee meeting, late work, gallery, market, rainy walk home, brunch). Hand-labeled arrows, cream background, no grid. Previous image models needed seeds, LoRAs, or ControlNet for this. Here: one prompt.

## All Agents Reported Back

## Bonus: The Five Prompts, Ready To Paste Into GPT Image 2

Quick reminder before you paste any of these: switch ChatGPT to GPT-5.4 Thinking or GPT-5.4 Pro, and turn Thinking mode on in the composer. It matters more than any prompt change you will make.

## Prompt 1: Research-Result Mobile UI Mockup

High-fidelity iOS UI screenshot, isolated on a warm off-white #F5F1EA paper backdrop with a soft long shadow beneath the phone. Straight-on device shot, pixel-perfect render at 1x, no reflections, no lens distortion. The aesthetic is editorial-meets-terminal: a beautifully designed research reader, in the spirit of Linear, Granola, Arc Browser, Superhuman, and Readwise Reader. Not generic iOS.

Device: an iPhone 16 Pro in natural titanium, portrait orientation. Dynamic Island preserved, home indicator pill at the bottom. No case, no hand.

App inside the phone is DARK MODE. Palette, used strictly: Deep ink background #0B0C10, Card surface 1 #15171D, Card surface 2 #1C1F27, Hairline divider #232630, Primary text warm cream #F4EDE0 (NOT pure white), Secondary text #8E8B84. Accent per source: Reddit #FF4500, X #4A90E2, YouTube #FF2D46, TikTok #FE2C55 with teal #25F4EE, Instagram #E1306C, Hacker News #FF6600, GitHub violet #A78BFA. Global warm accent for the "success" moment: muted saffron #D9A441.

Typography, two families only. Display: modern editorial serif (GT Sectra Display, Canela, or Ogg feeling). UI: precise geometric sans (Inter, Söhne, or Neue Haas Grotesk).

Status bar: "9:41" cream Semibold 15px left, signal/5G/wifi/93% right.

Navigation header (56px, bottom hairline divider): left 16px back chevron, center eyebrow sans 11px all caps letter-spaced +260 muted cream rendered exactly as "RESEARCH RESULT - APRIL 22, 2026", right 16px share glyph plus 16px bookmark glyph.

HERO BLOCK (24px padding): saffron eyebrow sans 11px all caps letter-spaced +260 exactly "LAST 30 DAYS". Hero title in display serif cream two lines Bold 40px. Line 1: "Prompting". Line 2: "GPT Image 2". Then a 40px-wide 1px cream-at-20-percent hairline under the title. Success row: 14px saffron circular check plus cream sans Medium 14px rendered exactly "All agents reported back". Beside it, a small chip sans Regular 12px rendered exactly "86.4s - 99 items - 7 sources".

SOURCE-CLUSTER CARDS (stacked, 16px gaps, 20px side margins). Each card on Card Surface 1, 14px radius, 1px #232630 stroke, 20px padding, 3px left-edge accent bar in that source's color, monochrome source glyph top-left.

Card 1 REDDIT (#FF4500, Snoo silhouette): label "Reddit", 10px chevron right. Three serif numerals 28px with thin vertical rules between, labels below in sans 10px all-caps. Exactly: "29" "5,469" "1,292" / THREADS UPVOTES COMMENTS. 4px sparkline in Reddit accent at bottom.

Card 2 X (#4A90E2, X mark): "19" "2,384" "160" / POSTS LIKES REPOSTS.

Card 3 YOUTUBE (#FF2D46, play glyph): "10" "380,535" "7" / VIDEOS VIEWS TRANSCRIPTS.

Card 4 TIKTOK (#FE2C55 plus teal offset): "24" "105,462" "5,218" / VIDEOS VIEWS LIKES.

Card 5 INSTAGRAM (#E1306C, aperture glyph): "14" "1,247,706" "16,364" / REELS VIEWS LIKES. Plus saffron "#1 REACH" micro-badge top-right.

Card 6 (two-up row). 6a HACKER NEWS (#FF6600, Y glyph): "1" "5" / STORY POINTS. 6b GITHUB (#A78BFA, octocat): "2" "3,161" / ITEMS REACTIONS.

TOP VOICES section (24px gap above): sans 11px all-caps eyebrow muted rendered exactly "TOP VOICES". Soft pill chips on Card Surface 2, 10px radius, 1px hairline, 14px sans Medium cream. First three are X handles (tiny cream x prefix), last three are subreddits (tiny Snoo prefix). Rendered exactly: "@emollick" "@OpenAIDevs" "@HsanC_" "r/ChatGPT" "r/singularity" "r/OpenAI".

RAW FILE SAVED banner (above tab bar, full width, Card Surface 2, 10px radius, 12px padding, paperclip glyph left, chevron right). Top line sans 11px muted all-caps letter-spaced +220 rendered exactly "RAW RESULTS SAVED". Bottom line sans Medium 13px cream rendered exactly "~/Documents/Last30Days/prompting-gpt-image-2-raw-v3-imagegen.md".

TAB BAR (83px, top hairline #232630, four custom single-weight line glyphs, not SF Symbols pastiche, not emoji): Tab 1 active, search glyph saffron plus "Research" saffron plus 4px saffron dot. Tab 2: 4-point spark plus "Trending" muted. Tab 3: clock-with-arrow plus "History" muted. Tab 4: person-in-circle plus "You" muted.

Polish details: faint 1px top-to-bottom gradient behind hero from #0F1116 to #0B0C10. Paper-grain noise overlay at about 3% opacity across content. Source-card numerals get a 1px outer glow in their accent color at 15%.

Constraints: every quoted string renders letter-perfect including commas, slashes, hyphens, and the tilde at the file path start. Real editorial serif plus real modern sans. No default SF, no Arial, no Times. Source glyphs are monochrome in accent color, NOT Apple emoji. No neon iOS #0A84FF, no pure white text, no pure black background. Sparklines ambient and restrained, never dominant. No gloss, no bokeh, no 3D device render, no fake screen glare. No additional cards or sections beyond what is listed.

Output in exactly 1000px x 2000px (portrait phone composition with margin).

## Prompt 2: Editorial Magazine Cover

Premium editorial magazine cover, newsstand-grade print quality, shot on medium-format film then lightly screen-printed. Clean studio lighting, matte paper texture, subtle spine shadow on the left, no glare, no lens distortion. Composed dead-on as a flat cover scan.

Style: cross between The New Yorker, Wired, and Monocle. Restrained palette: off-white paper #F5F1E8, deep navy ink #0A1F3D, warm accent red #C4362A, one tertiary mustard #D9A441. Generous negative space. Editorial, not corporate.

MASTHEAD (top centered): wordmark in high-contrast Didone serif (Bodoni or Didot), all lowercase, letter-spacing -20, exactly "last30days". Beneath, thin all-caps gothic 14px letter-spaced +200 exactly "THE MONTHLY REPORT ON WHAT PEOPLE ARE ACTUALLY SAYING". Thin 1px navy horizontal rule spans the masthead width.

TOP-RIGHT CORNER (small caps serif 10px navy): "VOL. 03 - ISSUE 04 - APRIL 2026" and "US $12.00 - CAN $15.00".

HERO COVER LINE (center, 45% of height, giant Didone Bold three stacked lines, centered, ragged-bottom, tight leading). Line 1: "The first". Line 2: "image model". Line 3: "that thinks.". Line 3 in accent red; lines 1 and 2 in navy.

DEK (sans 22px navy centered, two lines), exactly: "How GPT Image 2 went from launch to leaderboard #1 in seventy-two hours - and what prompters figured out first."

STACKED COVER LINES (left edge, vertical stack of six, small dot bullet each, sans 14px navy, left-aligned, 18px vertical gap). Exactly: "PROMPTING - Why the LLM you pick changes the image". "TYPOGRAPHY - Put every word in quotes, here's why". "FORMAT - The pixel trick for ratios the API forgets". "COMMUNITY - 725 prompts before the model was even out". "DEBATE - Closed models, open editing, and Flux Klein". "ECONOMICS - $0.165 an image, and what that kills".

LOWER-RIGHT CORNER (accent red italic Didone 16px): "Plus: the aspect-ratio hack every API user is copying."

BARCODE AREA (bottom-left, classic UPC, 1.2in wide, printed not pixelated, small "04>" issue marker at right).

Constraints: every quoted string renders letter-perfect. Two type families only: real Didone for display, real modern geometric sans for secondary. No Times New Roman, no Arial. Proper editorial 12-column grid, 0.5in margins. No photograph of a person, no AI face. Typography cover, not photo cover. No QR codes, no URLs, no social handles, no hashtags. No gloss, no foil. Matte paper finish only. No torn-edge or paper-curl effects.

Output in exactly 2550px x 3300px (8.5 x 11 at 300dpi) portrait, full bleed.

## Prompt 3: Brand Identity Reveal Board For Noon And Co.

Premium brand identity presentation board, Behance case-study aesthetic, overhead flat layout on warm cream paper #F7F0E8. Matte finish, subtle paper grain, soft diffuse studio lighting, no glare, no lens distortion. Single landscape reveal board with a six-panel grid and quiet typographic labels.

Brand: fictional independent coffee bar "Noon & Co." Aesthetic is calm midday light: warm minimalism, vintage-but-now, the feeling of a sunlit marble counter at 12:15pm. Vector-clean marks, NOT photographic or painterly.

Palette (use only these): cream paper base #F7F0E8, deep espresso brown (primary ink) #3C2414, warm noon gold (accent) #D9A441, soft sage (secondary, sparing) #8A9A7B.

Typography (two families only). Display: warm high-contrast serif with humanist curves (Canela, GT Sectra, or Ogg feeling) for wordmark and headlines. UI: geometric neo-grotesque sans (Inter, Neue Haas Grotesk, or Söhne) for tiny labels and captions.

Board header (top 10%): left all-caps sans 11px letter-spaced +280 espresso "NOON & CO. - BRAND IDENTITY SYSTEM". Right same style "2026 - CASE STUDY 01". Thin 1px espresso rule below.

SIX-PANEL GRID (3 cols x 2 rows, 48px gutter, 64px outer margin).

Panel 1 PRIMARY WORDMARK (top-left): label "01 - PRIMARY WORDMARK". Wordmark exactly "Noon & Co." in display serif espresso on cream, centered, large. Ampersand is old-style italic ligature, slightly larger. Tight kerning. Caption: "Primary lockup. Use on cream or white."

Panel 2 REVERSE (top-center): label "02 - REVERSE". Same wordmark exactly "Noon & Co." in cream on solid espresso tile. Caption cream 10px: "Reverse lockup. Use on dark or photo."

Panel 3 MONOGRAM (top-right): label "03 - MONOGRAM". Geometric monogram: uppercase "N" with a small circle (noon sun) tucked into the letter's negative space. Espresso on cream, vector-crisp single-weight, no gradients, no shadows. Caption: "Stamp mark. Favicons, buttons, embroidery."

Panel 4 LOCKUP WITH TAGLINE (bottom-left): label "04 - LOCKUP WITH TAGLINE". Wordmark "Noon & Co." centered, thin 1px rule beneath, then tagline in all-caps sans 11px letter-spaced +280 exactly "COFFEE FOR THE MIDDLE OF THE DAY". Caption: "Tagline lockup. Use on menus, packaging."

Panel 5 FAVICON GRID (bottom-center): label "05 - FAVICON / APP TILE". Three 96px squares, 16px gap: (a) espresso tile plus cream monogram, (b) gold tile plus espresso monogram, (c) cream tile plus espresso monogram plus 1px espresso border. Caption: "Favicon / app tile variations. 16px to 512px."

Panel 6 APPLICATIONS (bottom-right): label "06 - APPLICATIONS". Three stacked application vignettes. (a) Cream single-wall takeaway cup, straight-on, wordmark "Noon & Co." wrapping the front with "COFFEE FOR THE MIDDLE OF THE DAY" curving beneath. (b) Minimal storefront: cream plaster, narrow dark-oak door, espresso awning with cream-reverse "Noon & Co." wordmark. Eye-level, no people. (c) iOS app icon on 180px rounded square, espresso tile plus cream monogram, subtle 2px inner shadow. No phone bezel.

Footer (bottom 6%): left sans 10px "Designed by Studio Noon - Spring 2026", center sans 10px "www.noonandco.studio", right sans 10px "Page 01 of 24".

Constraints: all quoted text renders letter-perfect including the ampersand and period. Marks are vector-crisp single-color fills. No gradients, no drop shadows, no bevels, no photo textures on the marks themselves. No generic coffee-shop clip art (steaming cups, beans, swirls). Identity is typographic plus one small geometric monogram. No people, no hands, no baristas. No lens flare, bokeh, tilt-shift. Do not invent additional text beyond what is quoted. Panel 6 vignettes can be lightly photographic but stay matte and clean.

Output in exactly 3840px x 2400px (16:10 landscape presentation board).

## Prompt 4: Photoreal Editorial Photograph, Blood Orange On Weathered Wood

Photoreal editorial food photograph, shot on a Leica Q3 full-frame, 50mm f/1.4 Summilux prime, 1/200s at f/2.2, ISO 400. Kodak Portra 400 color rendering, warm skin-tone-leaning palette, natural grain visible at 100%, mild halation on brightest highlights, slight lens vignetting at the corners. Editorial magazine aesthetic, New York Times Food or Kinfolk spread, not stock photo.

Scene: morning kitchen, late-spring sunlight from a single east-facing window just out of frame on the upper-left. Low-angle raking unmodified light, dust motes visible in the beam. Warm temperature about 4800K, slight blue spill in the shadows for contrast.

Subject: a pair of adult hands captured mid-action, slicing a blood orange in half on a wooden cutting surface. One hand steadies the orange in a claw grip, knuckles forward. The other hand holds a well-used chef knife, blade partway through, a thin ribbon of juice trailing down the flat of the blade. The orange is freshly bisected: deep crimson flesh against cream-pink pith, three visible seeds inside, one half slightly tipped so juice pools on the wood.

Surface: thick weathered end-grain butcher block, years of use visible. Fine knife-scar hatching, darker oiled patina where hands rest, one shallow scorch mark at the right edge, a permanent orange-juice stain ring in the lower corner, a few tiny woodgrain fissures. Wood catches morning light and throws warm reflected bounce onto the fingers.

Framing: tight overhead three-quarter angle, camera about 35 degrees off vertical. Hands and orange occupy the lower two-thirds, slightly right of center (rule-of-thirds anchor). Shallow DOF: blade edge and cut face critically sharp; far knuckles and far half of board in soft falloff. Background heavily blurred into clean bokeh circles.

Background detail (all softly out of focus, ordinary, unstyled): cream linen tea towel crumpled at upper-right, draped over the counter lip. Small chipped ceramic espresso cup, empty except for a dried coffee ring. Cast-iron pan with one visible handle catching a specular highlight. Half-used wedge of butter on crumpled parchment. Worn hardcover cookbook, spine cracked, closed, fabric bookmark.

Believable imperfections (all subtle): one tiny seed rolled free onto the wood a few inches from the orange. A single bead of juice on the subject's thumbnail. Thumbnail has a short, uneven natural cut, not a manicure. Knife blade shows faint patina and a fingerprint smudge near the heel. One breadcrumb and a single grain of coarse salt on the far corner. Hairline scratch on countertop edge at bottom-left. Juice on the board does not form a perfect circle; it bleeds unevenly into the woodgrain on one side.

Skin detail: realistic pore structure, fine hair catching rim light, faint healing paper-cut on the index finger. Warm skin tone, no waxy smoothing, visible capillaries near nail beds. One knuckle slightly reddened.

Constraints: single decisive moment. No second pair of hands, no face, no plating. No text, stickers, brand labels, or logos anywhere. No symmetrical composition; orange halves are not mirrored perfectly. No gloss or lip-gloss specular on the orange flesh. Matte-juicy, not lacquered. Five fingers per hand, correct knuckle spacing, nails in place, no fused or impossible anatomy. No tilt-shift miniature. No HDR halos. No over-sharpened edges. No food-stylist props (no rosemary sprigs, no oil drizzle, no flaky salt performance). This is breakfast, not a shoot. Morning light warm but not orange; correct white balance, not a filter.

Output in exactly 6000px x 4000px (3:2 landscape, 35mm full-frame resolution).

## Prompt 5: Eight-Up Character Consistency Sheet

Freeform editorial character consistency sheet on a single clean cream studio background #EDE6D6, one continuous sheet with eight full-body shots of the same person scattered organically across the page. Not a grid. Not boxed panels. Not a contact sheet. Arranged loosely, overlapping at the edges, like a fashion studio wall where polaroids and proofs are pinned during editing.

Style: natural daylight studio photography, Fujifilm GFX 100 with 80mm f/1.7, Kodak Portra 400 palette, soft grain, slight film halation on highlights. Everyday documentary feel, not glamour.

Subject: THE SAME PERSON in all eight shots, rendered as a woman in her late twenties, shoulder-length wavy dark brown hair, warm olive skin, a small beauty mark above the upper-right lip, medium build, approximately five feet eight inches tall (convey through proportion only, never mention height in any label). Face, build, posture, and hair length MUST remain consistent across all eight shots.

Each shot is a distinct moment from a real week. Full body visible in every shot, feet included. Natural candid body language, not runway poses. Slightly different hair styling per shot (down, up, half-up, damp from rain) but same length and color.

Shot 1 MON 8:14 AM commute. Crosswalk, cross-body bag, paper coffee cup, looking left for traffic. Navy overcoat, white tee, straight jeans, white sneakers. Three-quarters toward camera.

Shot 2 TUE 7:02 AM yoga. Kneeling mid-adjustment, reaching to tighten a ponytail. Black cropped tank, sage leggings, bare feet. Side view.

Shot 3 WED 11:38 AM coffee meeting. Sitting on a stool, laptop closed on lap, leaning elbows-on-knees, laughing mid-sentence. Oatmeal sweater, dark slacks, loafers. Frontal.

Shot 4 THU 10:47 PM late work. Standing, one arm overhead, small yawn, eyes closed. Oversized gray sweatshirt over same white tee, athletic shorts, wool socks, no shoes. Three-quarters from behind.

Shot 5 FRI 7:19 PM gallery opening. Walking toward camera, hand behind one ear, wine glass in the other. Black slip dress, kitten heels, small clutch.

Shot 6 SAT 9:55 AM farmers market. Crouching beside a crate of produce, inspecting a tomato. Denim jacket, vintage tee, relaxed jeans, canvas tote, worn Vans. Profile.

Shot 7 SAT 11:30 PM walking home in rain. Hood up, hands in pockets, damp hair, small smile, looking slightly down. Black rain shell, dark jeans, boots, umbrella closed at her side. Three-quarters back.

Shot 8 SUN 10:22 AM brunch. Seated on a cafe chair turned sideways, one ankle crossed over opposite knee, reading a book. Linen shirt, wide-leg trousers, loafers, wire-frame reading glasses. Side view.

Arrangement: no borders, no rectangles, no grid lines, no boxed panels. Eight shots at different sizes, some overlapping, some with negative space, as if laid out freehand. Top-left denser, bottom-right breathier, natural editorial reading rhythm.

Handwritten labels (NOT for the clothing, for the moment). Next to each shot, a thin hand-drawn black arrow points to the figure, and beside it a short handwritten note in natural ballpoint-pen script. Each note rendered exactly: Shot 1 "MON / 8:14 AM / commute". Shot 2 "TUE / 7:02 AM / yoga". Shot 3 "WED / 11:38 AM / coffee meeting". Shot 4 "THU / 10:47 PM / late work". Shot 5 "FRI / 7:19 PM / gallery". Shot 6 "SAT / 9:55 AM / market". Shot 7 "SAT / 11:30 PM / rain home". Shot 8 "SUN / 10:22 AM / brunch". Handwriting is a real human script: slight inconsistent slant, occasional looped 'g', varying letter heights, not uniform hand-lettering font.

Top of sheet, small all-caps ballpoint header same hand, exactly "ONE WEEK - 8 MOMENTS - SAME PERSON". Beneath, smaller: "character consistency study - april 2026". Bottom-right corner, tiny pen scribble, exactly "proofs 01-08 - do not distribute".

Constraints: all eight figures MUST be the same person: same face, body proportion, hair length and color. No face drift, age drift, or build drift. Five fingers per hand, correct knuckles, no fused fingers, no impossible poses. Each pose distinct; no two shots are mirrored copies. Every quoted label renders letter-perfect with exact slashes, lowercase, punctuation. No grid, no borders, no drop shadows behind figures, no torn-photo edges, no polaroid frames, no tape, no pushpins. Figures sit directly on cream paper. Cream background flat and unified across the whole sheet, not eight stitched backdrops. No text except the quoted handwritten labels and header/footer. No brand logos on garments, no legible printed text on clothing. Labels describe the moment, not the clothes.

Output in exactly 2400px x 1800px (4:3 landscape, single continuous sheet).