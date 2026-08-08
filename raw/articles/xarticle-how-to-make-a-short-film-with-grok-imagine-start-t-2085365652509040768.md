---
source_url: "https://x.com/tetsuoai/status/2085365652509040768"
ingested: 2026-08-08
sha256: 096a7f4c2d7a67643d4a841761cb72b9124afd9d99d818d3f8b9e7adff2eb4ee
tweet_id: "2085365652509040768"
tweet_url: "https://x.com/tetsuoai/status/2085365652509040768"
source_file: "/Users/mali/Development/x-bookmarks/data/run-2026-08-06/2026-08-06/xarticle-how-to-make-a-short-film-with-grok-imagine-start-t-2085365652509040768.md"
run: run-2026-08-06
---
---
title: "How to make a short film with Grok Imagine, start to finish"
source: "x-bookmarks"
tweet_id: "2085365652509040768"
tweet_url: "https://x.com/tetsuoai/status/2085365652509040768"
author_name: "tetsuo"
author_handle: "@tetsuoai"
tweet_date: "Thu Aug 06 14:01:30 +0000 2026"
bookmark_date: "2026-08-06"
content_type: "x_article"
character_count: 58470
retweet_count: 226
like_count: 1341
external_urls:
  - "https://vvsvs.pro/codex/3)"
  - "https://vvsvs.pro/cinematique)"
  - "https://grokfilm.app/)"
  - "https://grok.com/skill-link/4ea4d5d0f3db64a305201b8ecdd58c19"
  - "https://grok.com/skill-link/2fc5926c10669d41d5b59d012b3bf11b"
  - "https://grok.com/skill-link/9ea62d13b889ef13d561f2bdf58fb05f"
  - "https://grok.com/skill-link/0792131c8a1e985998c0973522a41255"
---

# How to make a short film with Grok Imagine, start to finish

How to make a short film with Grok Imagine, start to finish

Grok Imagine crossed a line this week. Imagine Video 1.5 shipped last month with better motion, physics, and audio. On July 31 xAI added the piece that makes actual filmmaking possible: image and voice references, text-to-video, and native 1080p. You can now attach named reference images to a single generation, and each one locks one thing in place. A face, a location, a prop. Keep the character and swap the scene. Keep the scene and swap the character. Hold both and change only the action.

Availability first so nobody wastes an evening looking for the button. Image and voice references launched in the US for SuperGrok Heavy and SuperGrok Plus on grok.com/imagine and iOS, rolling out to all tiers over the following days. Text-to-video and native 1080p are generally available on web, iOS, and Android. On the API side the model is grok-imagine-video-1.5 with a reference_image_urls parameter, billed per second with duration and resolution driving cost.

This post is the full pipeline. One idea in, a finished cut out. I'll show every prompt, every beat, and every generation along the way.

I will also give you access to all of the skills I use in Grok to create marketing content and short films.

## Community Resources

Before we start here are some resources for Grok Imagine.

- [Codex 3.0](https://vvsvs.pro/codex/3): A free downloadable "world building codex" from [@_VVSVS](https://x.com/@_VVSVS), Ivan Flugelman's AI art project: a 120-page PDF of visual frameworks, lore theory, and Midjourney prompt sheets covering 10 aesthetic archetypes, used as a lead magnet for his newsletter and paid academy.

- [Cinematique](https://vvsvs.pro/cinematique): is his free open-source cinematic prompt library: 150+ film techniques across camera work, lighting, composition, editing, and genres, each with a copy-ready prompt for AI image and video generators.

- [grokfilm.app](https://grokfilm.app/): is @signerless open-source index of camera, lighting and editing techniques, catalogued, annotated and written as prompt language for generative film work, with example reels rendered in Grok Imagine.

- @heavypulp is one of the best content creators on X. They have multiple posts with instructions on how to create film with Grok Imagine.

[Embedded Tweet: https://x.com/i/status/2079629058287997221]

## The four skills you need before you start

Everything in this walkthrough runs through four Grok skills. Install all three before you touch step 1, they are not optional add-ons, they are the pipeline.

1. Script writer. Turns a one-line premise into a full short-film script: characters, locations, props, and numbered beats, each beat mapped to one shot. This builds the bible and the beat structure everything else reads from. https://grok.com/skill-link/4ea4d5d0f3db64a305201b8ecdd58c19

2. Char sheet. Generates a locked three-view reference image for each character, front, back, portrait, so they stay consistent across every shot instead of drifting scene to scene.  Something most people don't realize when building character sheets: video models drift on faces when a reference has more than one face view in it. You want ONE face shot only, the skill handles this for you. If it hands back a prompt that produces a character with the head cropped out of frame, that's correct, don't second guess it, you don't need a side profile of the face unless you're 3D modeling. Green screens don't work with AI references either, the green bleeds into the generated scene. Use a light grey background every time instead. https://grok.com/skill-link/2fc5926c10669d41d5b59d012b3bf11b

3. Location/prop reference. Generates a clean reference image for every location and prop, empty scenes, correct lighting, product-style objects, so places and objects stay as consistent across shots as your characters do. https://grok.com/skill-link/9ea62d13b889ef13d561f2bdf58fb05f

4. Prompt-creator. Turns each script beat into a single, fully detailed Grok Imagine video prompt, ready to generate. https://grok.com/skill-link/0792131c8a1e985998c0973522a41255

[Embedded Tweet: https://x.com/i/status/2083878550885830769]

## The one rule everything follows

Video models have zero memory between generations. Every clip starts from scratch. Your character will not look the same in shot 4 as in shot 1 unless you force it with reference images and repeated text. The entire workflow exists to fight that. Front-load consistency into a written bible, generate reference images before any video, and make every shot prompt a sealed document that restates everything the model needs to know.

References carry identity. Text carries action and locks the critical details. You need both.

# Step 1: turn the idea into a beat script

My idea was one line: A short film about two people walking through different times in history talking about Grok Imagine video and AI.

Before writing a single beat, answer four questions. These decisions cascade into everything downstream.

Runtime. Each generated shot runs 5 to 1 seconds, so budget 6 to 10 beats per minute of screen time. I wanted a 45 second short, so 5 beats. A 2 minute film is 15 to 20 beats. Decide this now because it caps your story.

Settings. How many distinct locations. Every location is a reference image you have to generate and manage, so fewer is cheaper and tighter. I picked two: an alley and a rooftop.

Dialogue. Silent or minimal beats talky every time. Long speeches die in AI lip-sync. Deadline is fully silent. If your character does speak, Grok Imagine now takes a voice reference alongside the face and holds both across scenes, so a talking short is viable. Keep lines to one or two sentences.

Ending. Happy, tragic, loop, cliffhanger. Pick one and build every beat toward it. I went cliffhanger: she delivers, then gets found.

Then write the script with four sections in this exact order: CHARACTERS, LOCATIONS, PROPS, SCRIPT. The first three sections are your bible. The bible is not flavor text. It is the source of truth every prompt will copy from.

Characters. 2 to 5 for a short. Each gets a name, a tag like @mara, a one-line role, and a visual description an image model could hold consistent: age, build, hair, clothing, plus at least one distinctive identifier. A scar, goggles, a torn sleeve. The identifier is what keeps them recognizable across shots. Write the description once and reuse the exact same phrasing every time it appears. Never paraphrase yourself later. The wording is a consistency tool.

Locations. Every setting gets a tag and a visual paragraph: time of day, palette, weather, key landmarks. Write it filmable, not literary. "Rust-orange desert at golden hour, heat shimmer, a single crashed satellite dish on the horizon" beats "a desolate wasteland."

Props. A bullet list of every object the plot needs. Any prop appearing in more than one shot gets a short visual description and a tag.

Script. Scene by scene, screenplay style. Slugline, then an ASSETS line listing which tags are visible in that scene, then numbered beats. One beat equals one shot equals one camera setup with one visual change. If a beat contains two camera setups, split it.

Two bookkeeping habits pay off hard at generation time:

Per-beat asset lists. If a beat is a close-up that excludes a prop, give that beat its own ASSETS line with only what is in frame. Attach a reference in a shot where the object should not appear and the model will force it into frame anyway.

STATE notes. Whenever a beat changes something that carries forward, end it with a line like `STATE: the chip is inside her fist from here on.` The model will not remember this. You will, and every later prompt must restate it as current fact.

Structural tips that separate a film from a slideshow: escalate each scene through discovery, threat, close call, catastrophe, transition. End every beat on a reveal, an impact, or an incoming threat. That hook at each cut point is what makes the edit feel alive. Carry one prop or motif across every scene so the film reads as one story. If you want a twist, plant it visually at least two beats before the reveal.

Here is THE WALK in full, built from that one line.

```markdown
# THE WALK

Logline: two friends stroll through four eras of history debating whether AI video can ever feel real, unaware they are the video.

## CHARACTERS

**VERA** `@vera`
The skeptic. Woman, mid 30s, sharp dark bob, upright walk. Wears a RED SCARF in every era regardless of costume. The scarf is her lock: same crimson wool, loose knot at the throat, one frayed end.

**OTIS** `@otis`
The believer. Man, late 40s, gray-streaked short beard, ROUND BRASS GLASSES in every era. Warm, animated hands when he talks. The glasses are his lock: thin brass rims, small circular lenses.

Wardrobe changes per era; scarf and glasses never do.

## LOCATIONS

**ROMAN FORUM** `@roman_forum`
Midday sun, white marble columns and statues, dusty ochre ground, blue cloudless sky, citizens in togas milling in soft focus behind the leads.

**MEDIEVAL MARKET** `@medieval_market`
Overcast gray light, timber stalls, mud street, hanging game and root vegetables, light snow falling, a stone gatehouse at the far end.

**1920S STREET** `@jazz_street`
Dusk, wet asphalt reflecting warm tungsten storefronts, Model T cars parked at the curb, a lit theater marquee, pedestrians in cloche hats and overcoats.

**NEON ALLEY** `@neon_alley`
Night, dense cyberpunk alley, rain, stacked holographic signage in pink and cyan, steam from vents, dark chrome walls.

**BEDROOM** `@bedroom`
Dim modern bedroom lit only by a phone screen, shallow depth of field, everything soft except the phone.

## PROPS

- **THE RED SCARF** `@red_scarf`: crimson wool, loose knot, one frayed end. Travels on Vera; locks via text in every prompt. The motif that stitches all four eras together.
- **THE PHONE** `@phone`: modern smartphone held in an unseen viewer's hand, playing a video in a generation app UI with a regenerate button. Appears only in the final scene.

## SCRIPT

EXT. ROMAN FORUM - DAY
ASSETS: characters @vera @otis — location @roman_forum — props @red_scarf

**BEAT 1.**
WIDE TRACKING SHOT. VERA and OTIS walk side by side through the forum in Roman dress, her red scarf bright against white marble. Citizens drift behind them.

                    OTIS
          People type one sentence now and get
          a whole world. Moving. Breathing.

                    VERA
          A trick. A very fast painting.

**BEAT 2.**
They pass a marble STATUE of an emperor. As they clear frame, the statue's eyes TRACK them — and BLINK. Neither notices. They step through a stone arch and the light BLOOMS WHITE.
STATE: wardrobe changes to medieval dress on the far side of the arch; scarf and glasses unchanged.

EXT. MEDIEVAL MARKET - DAY
ASSETS: characters @vera @otis — location @medieval_market — props @red_scarf

**BEAT 3.**
They emerge from the gatehouse into falling snow, now in wool cloaks, mid-stride, mid-conversation. Stalls and mud street around them.

                    VERA
          Real takes time. Film took a century
          to learn to lie this well.

                    OTIS
          And Grok Imagine learned it in a year.

**BEAT 4.**
ASSETS: @vera @otis — @medieval_market
They pass a MERCHANT counting coins. SNAP ZOOM IN: his hands BLUR, fingers multiplying, SIX then SEVEN. Back to the leads, oblivious, exiting under the far gate as the snow turns to drifting CONFETTI.
STATE: wardrobe changes to 1920s evening wear beyond the gate; scarf and glasses unchanged.

EXT. 1920S STREET - DUSK
ASSETS: characters @vera @otis — location @jazz_street — props @red_scarf

**BEAT 5.**
They stroll the wet sidewalk in 1920s coats, tungsten light glowing on the pavement, muffled jazz from a doorway.

                    OTIS
          Every frame you've ever loved was
          chemicals and luck. Now it's math.

                    VERA
          Math doesn't get goosebumps.

**BEAT 6.**
They pass the theater MARQUEE. The letters on it CRAWL and REARRANGE into gibberish glyphs behind their heads. Vera half-turns, almost catching it — the doors of the theater swing open onto pouring NEON RAIN.
STATE: wardrobe changes to dark techwear beyond the doors; scarf and glasses unchanged.

EXT. NEON ALLEY - NIGHT
ASSETS: characters @vera @otis — location @neon_alley — props @red_scarf

**BEAT 7.**
Rain. Pink and cyan light slides across their faces as they walk the alley. Vera stops. The frayed end of her scarf drips crimson dye into a puddle, the color SPREADING like ink.

                    VERA
          Otis. If the fakes get this good...
          how would we know?

**BEAT 8.**
Otis stops. Takes off his brass glasses. Looks PAST her, straight down the lens. Behind him the alley's far end DISSOLVES into drifting pixels.

                    OTIS
          We wouldn't.

INT. BEDROOM - NIGHT
ASSETS: location @bedroom — props @phone

**BEAT 9.**
SMASH CUT. The entire alley is a video playing on THE PHONE in a dark bedroom, framed inside a generation app, progress bar full. A THUMB taps REGENERATE. The screen GLITCHES WHITE. CUT TO BLACK.
```

# Step 2: generate the reference assets

Everything in the bible now becomes an image. Characters first, they drift the hardest.

The character sheet

For each character, generate one image containing three panels of the same figure on a flat light grey studio backdrop:

1. Full body front, cropped at the base of the neck so the head is out of frame. Wardrobe and hands carry this panel, both hands visible.

2. Full body back, same stance, head in frame so the hair reads from behind.

3. Head and shoulders portrait, face square to the lens. This panel is the identity anchor.

Prompt for grok.com to get the grok imagine prompt you will need for Vera.

```
/imagine-character-sheet-prompt 

**VERA** `@vera`
The skeptic. Woman, mid 30s, sharp dark bob, upright walk. Wears a RED SCARF in every era regardless of costume. The scarf is her lock: same crimson wool, loose knot at the throat, one frayed end.
```

The failure modes here are predictable, and the prompt below defends against every one of them. Frame the neck crop as composition, "top of frame crops at the base of the neck," never as a missing head, or you get decapitated bodies. For the portrait, write "face square to the lens, both eyes into the lens, both ears equidistant from camera, both sides of the hair visible." That combination makes a profile geometrically impossible, and portraits love drifting into profile. Asymmetric features get the side named from the character's own left and right, stated twice, with the back panel restating how the asymmetry reads from behind. Dark hair or clothing needs a rim light line or the silhouette merges into the grey. And if your twist depends on a hidden feature, leave it off the sheet entirely. Reference images leak. Lock hidden details per-shot in text instead.

Here is the full sheet prompt for vera.

```markdown
SCENE CONTEXT
Character reference sheet of one woman, three studio panels of the same figure against a clean light grey backdrop, no other people.

SUBJECT
Mid-30s woman, sharp chin-length black bob with blunt ends and a clean center part, deep brown eyes, defined dark arched brows, fair skin with cool undertones, natural full lips, slender athletic build, upright posture with shoulders level and spine straight. Crimson wool scarf is the permanent identity lock: same heavy crimson wool, loose knot at the throat, one visibly frayed end hanging to the character’s left side. 100% consistent identity across every cut.

LOCATION MAP
Seamless light grey studio floor curving into a flat light grey backdrop, evenly lit, soft contact shadow under the figure, key light from front-left of camera.

FIRST FRAME / BLOCKING
Figure stands upright, feet parallel and slightly apart, weight evenly distributed, arms relaxed at sides with both hands fully visible and relaxed, chin level, gaze forward. Same stance held through the first two cuts.

FORMAT MODE
Sequence of cuts, no timecodes. Cuts only at the specified points, the camera does not cut on its own.
CUT 1 — full body front view, headless framing: the body from the neck down, the top of frame crops at the base of the neck, the head above frame. Both hands visible at the sides. The crimson wool scarf sits in a loose knot at the throat with its frayed end hanging clearly to the character’s left side.
CUT 2 — full body back view, same upright stance, head in frame: the back of the head and the sharp black bob read fully from behind, the scarf knot visible at the nape with the frayed end still hanging to the character’s left.
CUT 3 — close-up front portrait, head and shoulders, face square to the lens: nose pointed straight at camera, both eyes into the lens, both ears equidistant from camera, both sides of the black bob visible, the crimson scarf knot and frayed left end fully readable at the throat.

OPTICS
47° neutral for full-body cuts, 18° natural portrait compression for the close-up, identity-preserving, no drift mid-segment.

CAMERA
Locked-off tripod, chest height 4 m back for full body cuts, eye height 2 m back for the close-up. Shadow side, fixed operator axis.

ACTION
Near-still. One slow breath cycle, a 1 cm settle of the shoulders.

PERFORMANCE
Pore-level skin realism, catch-light in each eye, neutral closed-mouth expression, calm direct gaze in the portrait.

LIGHTING
Soft white key front-left at 5600K, 45° off axis. Cool rim from back-right separating the dark bob and the crimson scarf from the backdrop, holding the outline in the back view. Even fill keeping the backdrop uniform.

WARDROBE
Simple fitted dark charcoal long-sleeve top with a clean crew neck that sits just below the scarf knot, slim dark trousers, no additional accessories. The crimson wool scarf remains the dominant visible identity element in every cut.

STYLE
Photoreal character turnaround sheet, 8K, clean studio look, fine film grain, real-time speed throughout.

POSITIVE LOCKS
Identity marks identical across all cuts: sharp black bob, deep brown eyes, crimson wool scarf with loose throat knot and frayed end always on the character’s left side. CUT 1 is framed from the neck down, the face appears only in CUT 3. Backdrop stays flat light grey with contact shadow only. Camera holds each framing until its cut.
```

Important: When you get the character back. The first image should NOT have a head. Video models will drift and there are subtle differences between each character pose.

That image is now Vara's canonical reference. Every video prompt in this film points at it.

OTIS:

```
/imagine-character-sheet-prompt 

**OTIS** `@otis`
The believer. Man, late 40s, gray-streaked short beard, ROUND BRASS GLASSES in every era. Warm, animated hands when he talks. The glasses are his lock: thin brass rims, small circular lenses.
```

```markdown
SCENE CONTEXT
Character reference sheet of one man, three studio panels of the same figure against a clean light grey backdrop, no other people.

SUBJECT
Late-40s man, short salt-and-pepper hair with gray concentrated at the temples, gray-streaked short beard kept close to the jaw, warm brown eyes behind the lenses, soft crow’s feet, medium skin with natural texture and light age lines at the forehead and mouth. Solid, approachable mid-height build, upright but relaxed posture. Round brass glasses are the permanent identity lock: thin brass rims, small perfectly circular lenses, always seated on the bridge of the nose. 100% consistent identity across every cut.

LOCATION MAP
Seamless light grey studio floor curving into a flat light grey backdrop, evenly lit, soft contact shadow under the figure, key light from front-left of camera.

FIRST FRAME / BLOCKING
Figure stands upright with a slight natural ease in the shoulders, feet parallel and slightly apart, weight evenly distributed, both hands visible and relaxed at the sides with fingers gently open, chin level, gaze forward. Same stance held through the first two cuts.

FORMAT MODE
Sequence of cuts, no timecodes. Cuts only at the specified points, the camera does not cut on its own.
CUT 1 — full body front view, headless framing: the body from the neck down, the top of frame crops at the base of the neck, the head above frame. Both hands fully visible and relaxed at the sides. The thin brass rims of the glasses catch a soft highlight where they rest against the neck line of the shirt.
CUT 2 — full body back view, same stance, head in frame: the back of the head and the short salt-and-pepper hair read fully from behind, the thin brass temples of the glasses visible along the sides of the head.
CUT 3 — close-up front portrait, head and shoulders, face square to the lens: nose pointed straight at camera, both eyes into the lens through the small circular brass lenses, both ears equidistant from camera, both sides of the short gray-streaked beard and hair visible, the thin brass rims and circular lenses fully readable and centered on the face.

OPTICS
47° neutral for full-body cuts, 18° natural portrait compression for the close-up, identity-preserving, no drift mid-segment.

CAMERA
Locked-off tripod, chest height 4 m back for full body cuts, eye height 2 m back for the close-up. Shadow side, fixed operator axis.

ACTION
Near-still. One slow breath cycle, a 1 cm settle of the shoulders and hands.

PERFORMANCE
Pore-level skin realism, catch-light visible in each eye through the circular lenses, neutral closed-mouth expression with a quiet warmth in the eyes, calm direct gaze in the portrait.

LIGHTING
Soft white key front-left at 5600K, 45° off axis. Cool rim from back-right separating the dark hair, beard, and brass frames from the backdrop, holding the outline in the back view. Even fill keeping the backdrop uniform. Soft specular highlights on the thin brass rims of the glasses.

WARDROBE
Simple charcoal merino crew-neck sweater over a soft open-collar shirt, dark trousers, no additional accessories. The round brass glasses remain the dominant visible identity element in every cut.

STYLE
Photoreal character turnaround sheet, 8K, clean studio look, fine film grain, real-time speed throughout.

POSITIVE LOCKS
Identity marks identical across all cuts: short salt-and-pepper hair, gray-streaked short beard, round brass glasses with thin rims and small circular lenses. CUT 1 is framed from the neck down, the face appears only in CUT 3. Backdrop stays flat light grey with contact shadow only. Camera holds each framing until its cut.
```

## Adding element tags to your characters

You'll want to create element tags for each Character, Location, and Prop.

## Locations and props

These are simpler. One clean establishing image per location, one product-style image per prop. Two rules. Generate locations empty, no people, so the reference locks the place and nothing else. And generate the location in the same lighting it has in the script. A noon reference fights every night prompt you write against it

The locations from the movie script Grok generated for us. For each location we will use the /imagine-location-prop-prompt skill on grok.com

## Locations

```markdown
## LOCATIONS

**ROMAN FORUM** `@roman_forum`
Midday sun, white marble columns and statues, dusty ochre ground, blue cloudless sky, citizens in togas milling in soft focus behind the leads.

**MEDIEVAL MARKET** `@medieval_market`
Overcast gray light, timber stalls, mud street, hanging game and root vegetables, light snow falling, a stone gatehouse at the far end.

**1920S STREET** `@jazz_street`
Dusk, wet asphalt reflecting warm tungsten storefronts, Model T cars parked at the curb, a lit theater marquee, pedestrians in cloche hats and overcoats.

**NEON ALLEY** `@neon_alley`
Night, dense cyberpunk alley, rain, stacked holographic signage in pink and cyan, steam from vents, dark chrome walls.

**BEDROOM** `@bedroom`
Dim modern bedroom lit only by a phone screen, shallow depth of field, everything soft except the phone.

```

ROMAN FORUM:

```markdown
SCENE CONTEXT
Empty Roman Forum at midday under a clear sky, no people.

LOCATION MAP
Foreground: dusty ochre packed-earth ground with fine dry grit and scattered small stones. Midground: tall white marble columns rising in pairs and rows, their fluted shafts and Corinthian capitals catching hard light, white marble statues of emperors and gods standing on low plinths between the columns. Background: more columns receding in orderly perspective under a cloudless deep blue sky.

LIGHTING
Hard midday sun high overhead and slightly front-left at 5600K, casting short sharp shadows from the columns and statues onto the ochre ground. Bright specular highlights on the polished white marble surfaces. Clear dry atmosphere with no haze.

STYLE
Photoreal, cinematic, fine film grain.

POSITIVE LOCKS
White marble columns and statues remain clean and intact in every generation. Ground stays dusty ochre. Sky stays cloudless deep blue. No figures of any kind appear in the frame.
```

MEDIEVAL MARKET:

```markdown
SCENE CONTEXT
Empty medieval market street under overcast gray light with light snow falling, no people.

LOCATION MAP
Foreground: wide muddy street of packed dark earth mixed with wet straw and shallow ruts. Midground: timber market stalls with rough wooden posts and thatched or plank roofs, strings of hanging game (hares, birds) and clusters of root vegetables (turnips, carrots, onions) suspended from the beams. Background: a heavy stone gatehouse with arched passageway and weathered battlements closing the far end of the street.

LIGHTING
Soft overcast gray daylight at approximately 6500K, fully diffuse with no hard shadows. Light snow falls steadily through the entire frame, collecting in thin white layers on the stall roofs, the hanging produce, and the mud. Cool ambient fill keeps the timber and stone evenly readable.

STYLE
Photoreal, cinematic, fine film grain.

POSITIVE LOCKS
The stone gatehouse remains at the far end of the street. Timber stalls stay occupied only by hanging game and root vegetables. Light snow continues to fall through the frame. No figures of any kind appear.
```

1920S STREET:

```markdown
SCENE CONTEXT
Empty 1920s city street at dusk, wet asphalt, no people.

LOCATION MAP
Foreground: wet black asphalt street reflecting warm storefront light in long broken streaks. Midground: Model T cars parked along the curb, dark bodies and thin spoked wheels. Background: continuous row of low storefronts with warm tungsten windows, a lit theater marquee centered above an entrance, its lettering glowing against the darkening sky.

LIGHTING
Dusk ambient sky at approximately 7000K mixing with warm tungsten storefront practicals at 2700K. Soft directional fill from the shop windows and marquee. Wet asphalt throws elongated golden reflections of the lights. No hard sunlight remains.

STYLE
Photoreal, cinematic, fine film grain.

POSITIVE LOCKS
The theater marquee stays lit and centered in the background. Model T cars remain parked along the curb. Wet asphalt continues to reflect the warm tungsten light. No figures of any kind appear in the frame.
```

NEON ALLEY:

```markdown
SCENE CONTEXT
Empty dense cyberpunk alley at night in the rain, no people.

LOCATION MAP
Foreground: wet dark pavement reflecting neon color, shallow standing water and rain streaks. Midground: narrow alley walls of dark chrome and black metal, vertical steam vents releasing slow white plumes, stacked holographic signage projecting layered pink and cyan glyphs and logos that float and flicker against the walls. Background: the alley continues into deeper stacked signage and denser steam under a black night sky.

LIGHTING
Primary illumination from the stacked holographic signage themselves: saturated pink and cyan practical light at high intensity, casting colored reflections across the wet chrome walls and pavement. Cool ambient night fill at approximately 9000K. Rain streaks catch the neon color. Steam is back-lit by the holograms, glowing soft pink and cyan at the edges.

STYLE
Photoreal, cinematic, fine film grain.

POSITIVE LOCKS
Stacked holographic signage remains pink and cyan only. Walls stay dark chrome. Steam continues to rise from the vents. Rain falls through the entire frame. No figures of any kind appear.
```

BEDROOM:

```markdown
SCENE CONTEXT
Empty dim modern bedroom at night, lit only by a single small cool light source, no people.

LOCATION MAP
Foreground: soft out-of-focus edge of a bed or nightstand surface. Midground: modern low bed with rumpled dark bedding, a simple nightstand, the far wall with a closed door or window. Background: the rest of the small room falls rapidly into soft darkness, walls and any furniture reduced to muted shapes.

LIGHTING
Sole illumination is a small, cool, directional source at approximately 6500K positioned near camera height and slightly off-center, matching the quality of a phone screen held close. The light falls in a tight pool across the bedding and nightstand, leaving the rest of the room in deep soft shadow. No other practicals or ambient light.

STYLE
Photoreal, cinematic, fine film grain, shallow depth of field with only the lit midground plane holding sharp detail.

POSITIVE LOCKS
The room remains empty of people and of any phone or device. Lighting stays limited to one small cool source. Depth of field stays shallow so that only the central lit plane is sharp.
```

## Props

```markdown
**THE RED SCARF** @red_scarf: crimson wool, loose knot, one frayed end. Travels on Vera; locks via text in every prompt. The motif that stitches all four eras together.

**THE PHONE** @phone: modern smartphone held in an unseen viewer's hand, playing a video in a generation app UI with a regenerate button. Appears only in the final scene.
```

THE RED SCARF:

```markdown
SCENE CONTEXT
Product photo of a single wool scarf, centered on a clean light grey studio background, no people, no hands.

SUBJECT
Crimson wool scarf of medium weight, loosely knotted once near the center, one end left deliberately frayed with irregular threads. The fabric shows natural wool texture and slight thickness. Scale reads as a full adult scarf when fully extended, here presented in a compact knotted form that displays the knot and the frayed end clearly.

LIGHTING
Soft even top light at 5600K with gentle fill, minimal shadow, highlighting the wool texture and the frayed threads without harsh specular highlights.

STYLE
Photoreal, macro detail, clean studio background.

POSITIVE LOCKS
The scarf remains pure crimson wool. The knot stays loose. One end stays visibly frayed. No additional objects or hands appear in the frame.
```

THE PHONE:

```
SCENE CONTEXT
Product photo of a modern smartphone held by an unseen viewer’s hand, centered on a dark neutral background, fingers and partial palm only, no face, no other people.

SUBJECT
Sleek modern smartphone with thin black bezels, screen illuminated and filling most of the frame. The screen displays a clean generation-app interface: a video player area, a full progress bar, and a clearly visible “REGENERATE” button. The phone is held at a natural viewing angle.

LIGHTING
Primary light is the phone screen itself at approximately 6500K, casting a cool soft glow onto the fingers and the edges of the device. Minimal additional fill so the screen remains the brightest element.

STYLE
Photoreal, macro detail, clean dark background.

POSITIVE LOCKS
The screen always shows a generation-app UI with a visible regenerate button. The phone remains a modern black smartphone. Only fingers and partial palm of one hand are visible; no face or other body appears.
```

# Step 3: loading references into Grok Imagine

The mechanics. Drop your reference images into the prompt bar and call each one in the prompt with an @ tag. Up to 3 per generation, each locking one element. This is the element tag system.

Currently you can only use up to 3 references at a time. Our script does not make this assumption so what is generated will be modified. I'm assuming references in Grok Imagine will be extended in the future.

# Step 4: one sealed prompt per beat

Every beat becomes one standalone prompt. The rules, compressed:

Seal the context. No scene numbers, no "continuing from before," no characters or props that are not in this shot. The prompt carries everything: the references in frame, the action, and every STATE note still active restated as current fact.

Write the visible. The model reacts to what can be seen and measured, not mood words. Write "she freezes, slowly clenches her fist, light only from the side, half her face in shadow" instead of "tense scene."

Structure in a fixed order. Scene context with who is positioned where. References, each tag with a minimal anchor. Location in layers, foreground, midground, background, plus where the light comes from. First frame blocking before anything moves. Then camera, then action. Camera sits in the middle of the prompt. At the front it fights identity, at the end it gets ignored. Lighting near the end, then a short block of positive locks restating critical continuity once.

Keep reference anchors short. The image sets appearance, text sets what happens. Long appearance paragraphs fight the image and degrade it. Age, build, current state, unique features, "100% matches the reference." Critical small details like logos or on-screen text still go in words. Models drop them from references constantly.

Make everything measurable. Speeds in km/h. Fog in percent. Field of view in degrees on a fixed ladder: 84 for establishing wides, 63 for observational wides, 47 for neutral, 29 for dialogue busts, 18 for identity-preserving close-ups, 12 for tele detail. Left and right always mean the camera's left and right.

Positive phrasing only. Never "does not fall backward," always "stays upright, feet planted." Negations plant the image of the thing you are negating.

Emotion through muscle, not labels. "Jaw tightens, eyes narrow, breath held" instead of "angry." State environment interaction physically. Rain runs down hair, wind moves fabric, water sprays off boots.

Now the beats. Watch how the STATE notes and asset lists from the script drive each one.

## Beats

For each beat we are going to use the /imagine-prompt-creator. We need to write our script to a text or markdown file and save it on our computer and then give it back to grok with the images required for the scene. It will help the model with context when writing the video prompt.

NOTE: Once you get the prompt back when you paste it into Grok Imagine you have to click on each @ element tag and select the correct element for the beat.

You will also have to change the scripts and ask for edits depending on what you get back. Use your intuition here. The generated script is only a guideline.

Generating 4 videos per beat is usually enough. If any changes need to be made give Grok back the prompt it created and describe the changes you want.

You should also take advantage of 'extend' where it makes sense. You wont always want to be generating new videos.

Beat 1.

Both Vera and Oatis are in this beat, so there tags get added to the location.

```markdown
SCENE CONTEXT
Midday in the Roman Forum. Vera and Otis walk side by side through white marble columns and statues on dusty ochre ground under a cloudless blue sky. Citizens in togas drift in soft focus behind them.

ACTIVE REFERENCES
@vera: mid-30s woman, sharp dark bob, upright posture, crimson wool scarf with loose knot and one frayed end. 100% matches the reference.
@otis: late-40s man, gray-streaked short beard, thin brass rims with small circular lenses. 100% matches the reference.
@roman_forum: white marble columns and statues, dusty ochre ground, blue cloudless sky. 100% matches the reference.

LOCATION MAP
Foreground: dusty ochre ground with fine grit underfoot. Midground: Vera and Otis walking toward camera-right on a clear path between columns. Background: tall white marble columns and statues receding under hard midday light, soft-focus citizens in togas moving slowly among the pillars.

FIRST FRAME / BLOCKING
Wide shot, both figures fully visible and already in motion. Vera on frame-left, Otis on frame-right, walking side by side at an easy pace, bodies angled slightly toward camera-right. Vera’s crimson scarf hangs bright against the white marble. Both face forward along their path.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
Wide tracking shot, 63° FOV, rectilinear, gentle motion blur on background elements only.

CAMERA
Eye-level tracking shot, camera moving parallel to the pair at the same walking speed, maintaining a steady medium-wide framing that keeps both full figures in frame with columns and sky readable behind them. Operator axis stays on the shadow side of the subjects.

ACTION
Vera and Otis walk forward at a calm conversational pace. The camera tracks alongside them, keeping pace. Soft-focus citizens drift in the background among the columns. The red scarf moves lightly with Vera’s steps.

PERFORMANCE
Otis speaks with warm, animated hand gestures, small circular lenses catching the light. Vera answers with a dry, upright calm, eyes forward, the frayed end of her scarf visible. Pore-level skin realism, living eyes, catch-lights under hard sun.

PHYSICS
Dust rises faintly from the ochre ground under their sandals. Fabric of Roman dress and the wool scarf shifts with natural weight and step. Marble surfaces hold hard specular highlights.

LIGHTING
Hard midday sun high and slightly front-left at 5600K, short sharp shadows from columns and figures on the ochre ground. Bright speculars on white marble. Clear dry air, no haze.

WARDROBE
Both wear simple Roman-era dress: Vera in a light stola with the crimson wool scarf knotted loosely at the throat, frayed end hanging to her left; Otis in a plain tunic and short cloak, round brass glasses unchanged. Sandals on both.

AUDIO
Otis: “People type one sentence now and get a whole world. Moving. Breathing.”
Vera: “A trick. A very fast painting.”

STYLE
Photoreal, cinematic, fine film grain, real-time speed.

POSITIVE LOCKS
Vera’s crimson scarf with loose knot and frayed end remains identical and bright against the marble. Otis’s thin brass circular glasses stay on his face. White marble columns and dusty ochre ground match the location reference. Citizens stay soft-focus and secondary. Camera tracks continuously without cutting.
```

Beat 2.

For beat 2 we will cut the scene short during post processing.

```
SCENE CONTEXT
Vera and Otis walk past a marble statue of an emperor in the Roman Forum, then step through a stone arch as the light blooms pure white. On the far side of the bloom they emerge into a snowy medieval market, now in wool cloaks, still mid-stride.

ACTIVE REFERENCES
@vera: mid-30s woman, sharp dark bob, upright posture, crimson wool scarf with loose knot and one frayed end. 100% matches the reference.
@otis: late-40s man, gray-streaked short beard, thin brass rims with small circular lenses. 100% matches the reference.
@medieval_market: overcast sky, timber stalls with hanging game and root vegetables, mud street, light snow, stone gatehouse at the far end. 100% matches the reference.

LOCATION MAP
First half — dusty ochre ground, white marble columns, a large marble emperor statue standing on a plinth in the midground. Second half — muddy rutted street between timber stalls, light snow falling, stone gatehouse visible in the distance.

FIRST FRAME / BLOCKING
Vera and Otis walk side by side past the marble statue, Vera on frame-left, Otis on frame-right. The statue occupies the right midground. Both face forward, neither looking at the statue.

FORMAT MODE
One continuous shot that contains a white light bloom transition, the camera does not cut on its own.

OPTICS
63° FOV tracking, rectilinear. During the bloom the frame fills with pure white light; as the light clears the same FOV continues into the new location.

CAMERA
Eye-level tracking shot moving with the pair at walking speed. Camera stays on the shadow side, holding both figures in a steady medium-wide frame through the arch and into the market.

ACTION
Vera and Otis pass the marble statue. As they clear the frame the statue’s eyes turn to follow them and then blink once. Neither character notices. They step through a stone arch; the light blooms pure white, filling the frame. On the far side of the bloom the pair continues mid-stride, now wearing wool cloaks, walking forward into the snowy medieval market street. Light snow falls around them.

PERFORMANCE
Both characters remain in calm mid-conversation posture, eyes forward, unaware of the statue. Pore-level skin realism, living eyes, natural breath visible in the cold air after the transition.

PHYSICS
Marble statue eyes move and blink with stone weight. White light bloom expands and clears as a continuous optical event. Snow falls in soft vertical flakes. Wool cloaks shift with natural weight and step. Mud gives slightly under their feet.

LIGHTING
First half: hard midday sun at 5600K with sharp marble shadows. Transition: pure white bloom that overexposes the entire frame. Second half: soft overcast gray light at approximately 6500K, diffuse, light snow catching the ambient light.

WARDROBE
Before the arch: simple Roman-era dress, Vera’s crimson scarf knotted at the throat with frayed end visible, Otis’s round brass glasses unchanged. After the bloom: heavy wool cloaks over the same bodies, scarf and glasses identical and continuous.

STYLE
Photoreal, cinematic, fine film grain, real-time speed.

POSITIVE LOCKS
Vera’s crimson scarf with loose knot and frayed end remains identical before and after the transition. Otis’s thin brass circular glasses stay on his face throughout. The statue’s eyes track and blink only after the pair has cleared the frame. Wardrobe changes only on the far side of the white bloom. Snow falls only in the medieval market half.
```

Something to notice here. The clothing isn't consistent. If you want to be detail orientated you should create different character sheets for each outfit so that there is consistency.

Beat 3.

```markdown
SCENE CONTEXT

Overcast medieval market. Vera and Otis emerge from the stone gatehouse into falling snow, already mid-stride and mid-conversation, wool cloaks on, walking the muddy street between timber stalls.

ACTIVE REFERENCES

@41335f66-f13d-4e83-a2d2-d4246ea1b96d : mid-30s woman, sharp dark bob, upright posture, crimson wool scarf with loose knot and one frayed end. 100% matches the reference.

@963eb91f-df96-43d9-96a5-58d08982350a : late-40s man, gray-streaked short beard, thin brass rims with small circular lenses. 100% matches the reference.

@6ef2b8ff-7cfa-4db6-b377-5b5b35076acd : timber stalls, mud street, hanging game and root vegetables, stone gatehouse, light snow. 100% matches the reference.

LOCATION MAP

Foreground: wet mud street with shallow ruts and scattered straw. Midground: Vera and Otis walking forward from the gatehouse, timber stalls lining both sides with hanging game and root vegetables. Background: the heavy stone gatehouse they have just exited, its arch still framing the path behind them under gray overcast sky.

FIRST FRAME / BLOCKING

Medium-wide shot. Vera and Otis are already clear of the gatehouse arch and walking toward camera, mid-stride. Vera on frame-left, Otis on frame-right, bodies angled slightly toward camera-right. Both wear heavy wool cloaks. The crimson scarf remains bright at Vera’s throat. Light snow falls around them.

FORMAT MODE

One continuous shot, the camera does not cut on its own.

OPTICS

63° FOV, rectilinear, gentle atmospheric softening from falling snow.

CAMERA

Eye-level tracking shot moving slowly backward as the pair advances, maintaining a steady medium-wide framing that keeps both full figures and the surrounding stalls readable. Operator stays on the shadow side.

ACTION

Vera and Otis walk forward at conversational pace through the falling snow. The camera tracks backward with them. Snow collects lightly on their cloaks and the mud. Stalls with hanging game and root vegetables pass on both sides.

PERFORMANCE

Vera speaks first with dry precision, upright posture, eyes forward. Otis answers with warm energy, small circular lenses catching the gray light, one hand gesturing lightly. Pore-level skin realism, visible breath in the cold air, living eyes.

PHYSICS

Light snow falls continuously and settles on cloaks, hair, and the muddy ground. Wool fabric shifts with natural weight. Mud gives slightly under their steps. Soft contact shadows underfoot.

LIGHTING

Soft overcast gray daylight at approximately 6500K, fully diffuse, no hard shadows. Cool ambient fill. Snowflakes catch the flat light as they fall.

WARDROBE

Both wear heavy medieval wool cloaks over period under-layers. Vera’s crimson wool scarf stays knotted loosely at the throat with the frayed end visible. Otis’s round brass glasses remain on. Practical boots for the mud.

AUDIO

Vera: “Real takes time. Film took a century to learn to lie this well.”

Otis: “And Grok Imagine learned it in a year.”

STYLE

Photoreal, cinematic, fine film grain, real-time speed.

POSITIVE LOCKS

Vera’s crimson scarf with loose knot and frayed end remains identical. Otis’s thin brass circular glasses stay on his face. Snow continues to fall throughout the shot. Timber stalls, mud street, and stone gatehouse match the location reference. Camera tracks continuously without cutting.
```

Beat 4-5. (Combined)

```markdown
SCENE CONTEXT

Medieval market under light snow transitions into a 1920s city street at dusk. Vera and Otis pass a merchant, remain oblivious to a brief distortion at his hands, exit the far gate as snow becomes confetti, and continue walking the wet sidewalk in 1920s coats under tungsten light.

ACTIVE REFERENCES

@41335f66-f13d-4e83-a2d2-d4246ea1b96d : mid-30s woman, sharp dark bob, upright posture, crimson wool scarf with loose knot and one frayed end. 100% matches the reference.

@963eb91f-df96-43d9-96a5-58d08982350a : late-40s man, gray-streaked short beard, thin brass rims with small circular lenses. 100% matches the reference.

@medieval_market: timber stalls, mud street, hanging game and root vegetables, stone gatehouse, light snow. 100% matches the reference.

@2ea727c5-67bf-494a-a08a-018dd428a468 : wet asphalt reflecting warm tungsten storefronts, Model T cars, lit theater marquee. 100% matches the reference.

LOCATION MAP

First half: muddy medieval street with timber stalls and the stone gatehouse at the far end.

Second half: wet 1920s asphalt street at dusk, warm storefront light reflecting on the pavement, theater marquee glowing in the background.

FIRST FRAME / BLOCKING

Medium-wide. Vera and Otis walk side by side toward the far medieval gate, a merchant counting coins at a stall on the right. Light snow falls.

FORMAT MODE

Sequence of cuts, no timecodes. Cuts only at the specified points, the camera does not cut on its own.

CUT 1 — Tracking with Vera and Otis as they pass the merchant.

CUT 2 — Snap zoom into the merchant’s hands.

CUT 3 — Return to Vera and Otis exiting the gate; snow becomes confetti; wardrobe and location shift.

CUT 4 — They stroll the wet 1920s sidewalk in evening coats and deliver the dialogue.

OPTICS

CUT 1: 63° FOV.

CUT 2: rapid snap to 18° FOV on the hands.

CUT 3–4: return to 63° FOV, no drift mid-segment.

CAMERA

CUT 1: eye-level tracking from behind at walking pace.

CUT 2: hard snap zoom, locked on the hands.

CUT 3: resume tracking as they pass under the arch; the camera continues forward with them into the new street.

CUT 4: smooth tracking alongside them on the wet sidewalk, keeping both full figures and the glowing storefronts readable.

ACTION

CUT 1: Vera and Otis walk past the merchant, who counts coins. They do not look at him.

CUT 2: The merchant’s hands blur; fingers multiply from five to six, then seven.

CUT 3: Back on the pair as they exit under the stone gate. Falling snow softens into drifting paper confetti. As they clear the arch the environment resolves into a wet 1920s street at dusk; their cloaks become 1920s evening coats while the crimson scarf and brass glasses remain.

CUT 4: They continue strolling the reflective wet sidewalk under warm tungsten light. Muffled jazz drifts from a doorway.

PERFORMANCE

Vera and Otis stay mid-conversation, upright and forward-facing, completely unaware of the merchant. In the 1920s street Otis speaks with warm, animated hands; Vera answers with dry precision. Pore-level skin realism, living eyes, visible breath in the cold air that fades as the location warms.

PHYSICS

Snow falls and transitions into lightweight drifting confetti. Mud gives way to wet asphalt. Reflections of tungsten light stretch across the pavement. Fabric shifts with natural weight through the wardrobe change.

LIGHTING

First half: soft overcast gray daylight at 6500K.

Second half: dusk ambient sky mixed with warm tungsten storefront practicals at 2700K. Wet asphalt throws long golden reflections. The theater marquee glows steadily.

WARDROBE

Medieval section: heavy beige wool cloaks over white under-layers.

Beyond the gate: 1920s evening coats and period street clothes.

Throughout: Vera’s crimson wool scarf stays knotted at the throat with the frayed end visible; Otis’s round brass glasses remain on.

AUDIO

Otis: “Every frame you've ever loved was chemicals and luck. Now it's math.”

Vera: “Math doesn't get goosebumps.”

STYLE

Photoreal, cinematic, fine film grain, real-time speed.

POSITIVE LOCKS

Vera’s crimson scarf with loose knot and frayed end remains identical across both eras. Otis’s thin brass circular glasses stay on his face. The merchant’s hands alone distort. Snow becomes confetti only at the gate. Wardrobe shifts cleanly to 1920s coats beyond the arch while scarf and glasses are unchanged. Wet asphalt and warm tungsten reflections match the 1920s location reference.
```

Beat 6-7-8. (Combined)

```markdown
SCENE CONTEXT
Dense cyberpunk alley at night in the rain. Vera and Otis walk through pink and cyan holographic light. Vera stops as dye drips from her scarf into a puddle. Otis stops, removes his glasses, and looks past her down the lens as the far end of the alley dissolves into pixels.

ACTIVE REFERENCES
@vera: mid-30s woman, sharp dark bob, upright posture, crimson wool scarf with loose knot and one frayed end. 100% matches the reference.
@otis: late-40s man, gray-streaked short beard, thin brass rims with small circular lenses. 100% matches the reference.
@neon_alley: dense cyberpunk alley, rain, stacked holographic signage in pink and cyan, steam from vents, dark chrome walls. 100% matches the reference.

LOCATION MAP
Foreground: wet dark pavement with shallow puddles reflecting neon color. Midground: Vera and Otis in the narrow alley, dark chrome walls on both sides. Background: stacked holographic signage and steam vents; the far end of the alley later dissolves into drifting pixels.

FIRST FRAME / BLOCKING
Medium shot. Vera and Otis walk side by side toward camera through the rain. Pink and cyan light slides across their faces. Vera is slightly ahead on frame-left.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
47° FOV, rectilinear, soft diffusion from rain and steam.

CAMERA
Eye-level tracking shot moving slowly backward as the pair advances, then settling into a gentle hold as they stop. Operator stays on the shadow side of the neon sources. Final framing holds Otis looking past camera.

ACTION
Vera and Otis walk forward through the rain. Pink and cyan light moves across their faces. Vera slows and stops. The frayed end of her crimson scarf hangs over a puddle; crimson dye drips from the threads and spreads across the water like ink. Otis stops a step later. He reaches up, removes his round brass glasses with one hand, and looks past Vera, straight down the lens. Behind him the far end of the alley begins to dissolve into drifting pixels that float and scatter like digital ash.

PERFORMANCE
Vera speaks with quiet intensity, upright, eyes searching. Otis listens, then removes his glasses and meets the lens directly with a calm, final certainty. Pore-level skin realism, living eyes, rain beading on faces and hair, visible breath in the cool air. Catch-lights from the neon shift as he turns his gaze to camera.

PHYSICS
Rain falls steadily and streaks the chrome walls. Steam rises from the vents. Crimson dye blooms outward across the puddle. The far end of the alley breaks apart into discrete drifting pixels that lose cohesion and scatter while the midground and characters remain solid.

LIGHTING
Primary light from stacked holographic signage in saturated pink and cyan, casting colored reflections across wet chrome and pavement. Cool ambient night fill. Rain streaks and steam catch the neon color. Soft specular highlights on the dark techwear and, while still worn, the brass glasses.

WARDROBE
Both wear dark techwear—matte black and charcoal layers, practical and close-fitting. Vera’s crimson wool scarf remains knotted loosely at the throat with the frayed end clearly visible and dripping. Otis begins with his round brass glasses on, then removes them and holds them at his side.

AUDIO
Vera: “Otis. If the fakes get this good... how would we know?”
Otis: “We wouldn't.”

STYLE
Photoreal, cinematic, fine film grain, real-time speed.

POSITIVE LOCKS
Vera’s crimson scarf with loose knot and frayed end remains identical; the dye drip originates only from the frayed end. Otis’s thin brass circular glasses are removed by his own hand and stay in his possession. The far end of the alley alone dissolves into pixels; the characters and midground stay solid. Pink and cyan holographic light continues to slide across surfaces. Rain falls throughout the shot.
```

Beat 9.

```markdown
SCENE CONTEXT

Dark modern bedroom at night. A smartphone held in an unseen viewer’s hand displays the neon alley as a finished video inside a generation-app interface. A thumb taps the regenerate button; the entire scene glitches white and cuts to black.

ACTIVE REFERENCES

@e298ab73-7284-4783-8a12-718344c9baba : dim modern bedroom lit only by a phone screen, shallow depth of field, everything soft except the phone. 100% matches the reference.

@b9ae27fe-0f0e-470e-becb-158f18a51042 : modern smartphone held in an unseen viewer’s hand, generation-app UI with regenerate button. 100% matches the reference.

@b71ce1c2-29b3-4169-8297-01bf49701181 : the video content playing on the phone screen — dense cyberpunk alley, rain, pink and cyan holographic signage, steam, dark chrome walls. 100% matches the reference.

LOCATION MAP

Foreground: the glowing phone screen filling most of the frame, held at a natural viewing angle. Midground: soft, out-of-focus edge of a bed or nightstand. Background: the rest of the dark bedroom falls into deep soft shadow.

FIRST FRAME / BLOCKING

Close framing on the phone. The screen is bright and sharp, showing the neon alley video at full progress. A thumb rests near the bottom of the screen beside a clearly visible “REGENERATE” button. Everything beyond the phone is soft and dark.

FORMAT MODE

One continuous shot that ends in a hard cut to black, the camera does not cut on its own until the final black.

OPTICS

18° natural portrait compression on the phone, shallow depth of field so only the screen and immediate fingers remain sharp.

CAMERA

Eye-level, locked-off or with minimal handheld micro-movement, held close to the phone so the screen dominates the frame. Operator axis keeps the phone centered.

ACTION

The phone screen plays the neon alley video, progress bar full. A thumb moves in and taps the REGENERATE button. The entire scene — phone, hand, and dark bedroom — immediately glitches with digital noise and color tearing, then floods to pure white. The image cuts to solid black.

PERFORMANCE

Only the thumb and partial fingers are visible; no face or other body. The hand is steady until the deliberate tap.

PHYSICS

The phone is solid and still until the tap. On the tap the whole frame breaks into digital artifacts and washes to white. No other motion in the dark room before the glitch.

LIGHTING

Sole illumination is the phone screen itself at approximately 6500K, casting a cool soft glow onto the fingers and the nearest surfaces. The rest of the bedroom remains in deep shadow until the full-frame white glitch.

STYLE

Photoreal, cinematic, fine film grain, real-time speed until the final cut to black.

POSITIVE LOCKS

The phone screen shows the neon alley as video content inside a generation-app UI with a visible regenerate button and full progress bar. Only fingers and partial palm of one hand appear. After the tap the entire scene glitches white and the shot ends in solid black. No other light sources or figures are present in the bedroom.
```

For longer films with scene or world changes, give each transition its own beat with an explicit visual mechanic. "Vanishes in a cloud of pixels." "Screen glitches to white." They cut clean and they hide residual drift between shots.

## Post Processing.

This is where you will have to do some research. You glue the beats together and add music using any video editor. Capcut is a good choice here. There's also Agent mode in Grok Imagine.

## Where agent mode fits

Grok Imagine also has Agent Mode, in beta on the web app for paid accounts. It replaces the prompt-and-response loop with an infinite canvas where an agent plans, generates, edits, and stitches clips into longer pieces. You give it a one-sentence brief and it decomposes the whole job in front of you, every step a node on the canvas you can click into and reprompt.

Two ways to use it with this pipeline. Hand it the one-liner and let it run the whole thing, which gets you a watchable film fast at the cost of shot-level control. Or use the canvas as your workspace and feed it your own beats one at a time, which keeps the control and gains the organization. The bible and the beat script make you better at both. An agent given a sealed, measurable beat prompt produces a tighter shot than an agent given a vibe, for the same reason a human crew does.
