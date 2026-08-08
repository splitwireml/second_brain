---
source_url: https://x.com/beechinour/status/2085364884154560549
ingested: 2026-08-08
sha256: 8a2251dd6e0d1bfc8de9d2e673784abb4333871ca107dd2cf7efc8337c5a5886
tweet_id: "2085364884154560549"
tweet_url: https://x.com/beechinour/status/2085364884154560549
source_file: "/Users/mali/Development/x-bookmarks/data/run-2026-08-06/2026-08-06/xarticle-how-to-prompt-seedance-25-the-200iq-guide-2085364884154560549.md"
run: run-2026-08-06
---
---
title: "how to prompt seedance 2.5 (the 200iq guide)"
source: "x-bookmarks"
tweet_id: "2085364884154560549"
tweet_url: "https://x.com/beechinour/status/2085364884154560549"
author_name: "beech"
author_handle: "@beechinour"
tweet_date: "Thu Aug 06 13:58:27 +0000 2026"
bookmark_date: "2026-08-06"
content_type: "x_article"
character_count: 21322
retweet_count: 8
like_count: 122
---

# how to prompt seedance 2.5 (the 200iq guide)

how to prompt seedance 2.5 (the 200iq guide)

almost everyone prompting seedance 2.5 right now is making the same mistake: trying to oneshot the whole video.

ive spent the last few days and probably too much money messing around with it. this is everything i know: the exact prompt structure i use, the workflow that gets usable footage out of it, and the one mental shift that changes everything.

by the end youll have my exact prompt structure and the workflow i run around it.

## the honest verdict, a few days in

first, what you're actually working with:

- its EXPENSIVE. get the prompt right for the first generation, because every extra generation costs real money

- its very good at listening. if the prompt is right, you get a good video in one shot

- the realism is pretty crazy. a lot of the ugc im seeing would genuinely trick me, someone who works with ai every single day, into thinking its real

- its still really bad at text. dont use it for anything with words in frame, add captions and overlays yourself in the edit

- with a bit of creativity and a budget that allows for it, you can make some really sick content, and roi isnt a tough challenge as long as your product and angle are in check

on the expensive part, some actual numbers: api pricing works out to roughly $0.50 to $1.20 for a 5 second clip depending on resolution, and on credit platforms a full 30 second 4k generation runs 2,000+ credits. every rule in this guide exists because of that math.

the biggest one: 50 reference slots that actually remember structure. your entire cast, props, and style refs all go into one generation together. we'll use that.

## stop one-shotting, start aggregating

heres the thing people get wrong with every video model, not just this one. they try to one-shot the whole video. or they try to one-shot the transitions, or the audio.

the key is always going to be aggregating the best shots from the model. prompt way more than you think you need, pull the best moments, and give the model the opportunity to come up with its own ideas.

thats the beauty of ai video: you can pull and aggregate random things together into something beautiful and stylistic.

in practice, for me, that means montages:

1/ take 2 to 5 seconds of your actual script

2/ turn it into one 15 to 30 second montage prompt, fast cuts (use chatgpt to do the breakout)

3/ tell the model straight up: im cutting this myself in premiere, load the montage with extra shots and options

4/ generate around 10 of those

5/ cut all the best moments into one

it comes back with alt angles and coverage you never thought to ask for. fair warning: most of those extra shots will be slop you never touch. but every now and then you get an absolute banger you could have never planned yourself.

i found this out by being lazy. i was making a fighter jet montage, and instead of individually writing out every shot like a good director, i realized the model would just make the montages for me. a generation came back with a shot i didnt write, and it was better than what i wrote. i understood the whole model differently after that. thats not a bug in your prompting, thats the workflow.

same way youd shoot a ton of coverage on a real shoot. more options in the edit, more room for your own taste.

and yes, the math. a batch of ten 15 second montages runs roughly $15 to $35 at the api rates above. that sounds like it goes against getting the prompt right the first time. it doesnt. the structure exists so every generation in the batch comes back usable, and the batch exists so you never pay for the genuinely expensive thing: re-running a broken prompt and hoping it fixes itself. you spend on coverage, never on hope.

on duration: 30 seconds is actually really good for the montages. its more expensive, so theres more at stake if you get the prompt wrong, but if youre in a good flow, 15 to 30 seconds is the sweet spot.

now, how to write the prompt so you get it right the first time.

## the prompt structure

every prompt i write follows the same structure, macro to micro. hard limit for a narrative prompt: under 3,500 characters. (montage prompts run long and loose on purpose, youll see one in a minute.)

copy this structure:

```
SHOT: name it, plus one line on whats happening
REFERENCES: who each @image is. lock this before anything else
CHARACTER @image1: the same exact person description every time, plus what theyre doing and feeling in this shot. clothing locked
SETTING @image2: the place, matched to your environment sheet. light and materials
CAMERA: lens, distance, movement, framing, light
SEQUENCE: the timed beats. this is where the video lives
STYLE PROMPT: your look, pasted identical in every shot. ratio, duration, 24fps
```

four things that go in every single prompt:

- no music. diegetic sound only, described per beat. music gets added in the edit, where you control it

- "face stable throughout, no deformation" written in every prompt, systematically

- @image discipline: every reference gets a named role, numbered by the order it appears in your prompt. never cite an image the model wont receive

- negative prompts stay short and only list problems that have actually shown up in your generations

one more trick that pays for itself: if you have a style prompt you already use in midjourney or gpt image models, add that exact paragraph to the end of every seedance prompt. one style prompt, three tools, one consistent look.

## emotion, physics, sound

the SEQUENCE block is the core. each beat is shot type + action + camera + sound, time coded. four rules i stick to:

1/ emotion is body movement. never "he is angry". write "the jaw clenches, the fist closes". the model renders what a feeling does to a body

2/ physics, not vibes. every action has trajectory, distance, impact, reaction. "three strides, leaps, lands knees deep" beats "he jumps impressively"

3/ sound inline, per beat. never a sound list at the end. each beat carries its own diegetic sound, its what makes the shot feel real

4/ rhythm through contrast. cut between extreme wide and macro, fast and still. impact frames, speed changes, a held freeze. the rhythm is written into the beats

3 to 4 beats per 15 seconds is the ceiling for narrative shots. overstuffed prompts feel rushed. but montage prompts break this rule on purpose, which brings me to the example.

## a prompt from my library

this is the fighter jet montage where all of this clicked for me. 13 beats in 15 seconds, on purpose: its a montage prompt, built to hand me coverage.

four things to watch for as you read it:

- the camera section demands "a large variety of aggressive angles" and lists six lens setups. thats aggregation working inside a single prompt

- the whole prompt runs off one reference image: @image1 carries the pilot, the jet, and the sky all at once. thats the montage exception: fewer references means more freedom to invent shots, and as long as it has the rough environment and the style prompt, it wont break

- the enemy jets are kept simple and distant on purpose. one locked reference subject stays stable when everything around it is allowed to be loose

- every negative at the bottom is a problem ive actually seen come out of the model. thats what a negative list is for

the full prompt, copy paste and reskin it (i wrote this one with an earlier ordering, same pieces):

```
CHARACTER @image1: A disciplined young military test pilot with an athletic compact build, a defined square jaw, calm dark eyes, short dark-brown hair, and a controlled mission-ready presence. He stays emotionally restrained even in extreme combat, reacting through precise eye movements, controlled breathing, and economical control inputs rather than exaggerated performance. Clothing locked: dark flight suit with subtle tactical paneling, black gloves, black combat boots, oxygen mask, and a matte dark pilot helmet with a smoked visor fully lowered.

CINEMATOGRAPHY: ultra-dynamic cinematic aerial-combat coverage using 18mm rigid cockpit mounts, 24mm air-to-air chase cameras, 35mm underside and wingline tracking shots, 50mm pilot close-ups, 85mm explosive near-pass angles, and 135mm long-lens silhouette flybys. Prioritize a large variety of aggressive angles: nose-on closing passes, belly-up overhead flybys, wingtip-mounted bank shots, rear chase, top-down dive coverage, close crossing passes through smoke, and distant long-lens explosions. Camera motion must obey believable aircraft inertia, air resistance, G-force, speed, and combat geometry. The primary jet from @image1 must remain perfectly consistent and sharply readable in every shot. Opposing aircraft should remain secondary, simpler, and often seen as distant or brief fast silhouettes so the reference image stays stable. Bright high-altitude daylight, broken cloud layers, hard metallic edge light, deep blue-grey shadow planes, shock-vapor in hard turns, blast smoke, expanding fireballs, and drifting debris silhouettes. Sound FX only, no music. Face stable throughout, no deformation.

SETTING @image1: high-altitude coastal combat airspace above layered cloud banks and a distant ocean horizon. Preserve the exact sleek dark fighter aircraft from @image1: exact silhouette, wing geometry, tail shape, cockpit shape, surface paneling, colors, markings, and proportions. Multiple hostile aircraft may appear as secondary opposing fighters with simpler distant silhouettes and restrained contrasting markings. Explosions occur in open sky, around cloud gaps, and along enemy flight paths, with expanding smoke rings, burning fragments, and brief fireball blooms. Keep the primary aircraft undamaged and visually locked.

REFERENCE: @image1 is the locked pilot identity, facial anatomy, helmet, visor, oxygen mask, flight suit, gloves, and cockpit behavior reference. @image1 is the locked primary fighter-jet design, cockpit architecture, materials, proportions, markings, sky environment, and lighting reference. Preserve the primary aircraft exactly throughout. Do not reinterpret, redesign, or merge the reference subjects.

SEQUENCE

0–1.2s: Extreme cockpit close-up from the pilot's right side. @image1's eyes flick sharply upward as warning reflections and a fast enemy silhouette flash across the smoked visor. Camera is rigid and close, with only subtle cockpit vibration. Oxygen-mask breathing, radio crackle, urgent targeting alert.

1.2–2.3s: Nose-on closing pass in open sky. The locked primary jet screams straight toward camera while an opposing jet streaks past in the opposite direction only feet away, producing a violent near-miss crossing. Camera holds almost static until both aircraft whip through frame. Two overlapping turbine roars, cracking pass-by, wind blast.

2.3–3.4s: Top-down dive shot from high above. The primary aircraft plunges through a broken cloud gap after a secondary enemy jet below, trailing thin vapor from the wings. Camera follows from above and behind with a steep descending angle. Rising turbine pitch, rushing air, subtle airframe groan.

3.4–4.5s: Wingtip-mounted angle looking inward along the fuselage. The horizon rolls aggressively as the primary jet snaps through a hard bank and a bright explosion blooms far behind in the background cloud layer where a missile detonates near an enemy aircraft. Camera stays rigid to the jet. Vapor rush, distant explosion thump, warning tone.

4.5–5.7s: Ultra-wide underside flyby. The primary fighter roars directly overhead, belly fully visible, while fiery debris falls in the far background from a damaged opposing aircraft. Camera remains low and static as the jet tears past. Jet thunder, debris whistling, distant fire crackle.

5.7–6.8s: Cockpit front three-quarter close-up. @image1 remains composed and focused, making one exact control-stick pull while the canopy reflections spin with the changing horizon. Breathing intensifies, avionics beeps, control-surface rumble.

6.8–7.9s: Rear chase shot extremely close behind the primary jet. An enemy aircraft fills the distance ahead. The primary releases a short burst of missiles or projectiles from beneath the wingline, which streak forward in clean stepped motion-smear arcs. Camera remains aligned to preserve the jet silhouette. Launch clacks, rocket hiss, engine thunder.

7.9–9.0s: Long-lens compression shot through cloud layers. One enemy aircraft is struck mid-turn and erupts into a sharp bright fireball, breaking into burning fragments and black smoke while another hostile silhouette slices across the foreground. Keep the explosion distant and readable, not messy. Explosion crack, tumbling debris hiss, fading engine whine.

9.0–10.0s: Belly-up passing angle from beneath a banking turn. The primary jet rolls above the camera while a second explosion blooms off to the right side of frame, briefly backlighting the aircraft edges with hot orange against cool sky. Jet roar peaks, expanding fireball rumble, wind shear.

10.0–11.1s: Tight cockpit-side close-up. The pilot braces subtly and shoves one control forward, still emotionally restrained. Reflected fire and cloud light slide across the visor. Oxygen-mask breathing, warning tone dropping, avionics hum.

11.1–12.1s: Side-profile chase shot. The primary jet races left to right while an enemy jet streaks toward camera in the opposite direction in the deep background, passing through a cloud of smoke and sparks from a previous detonation. Camera matches the primary briefly for a clean locked silhouette. Crossing turbine roar, smoke turbulence, distant debris impacts.

12.1–13.2s: Near-head-on air-to-air shot. The primary jet cuts diagonally across frame and unleashes defensive flares as another explosion erupts behind and above, creating layered chaos without obscuring the jet design. The flares appear as sharp stepped graphic streaks. Flare pops, blast thump, rushing air.

13.2–15s: Heroic rear three-quarter climb shot. The primary fighter punches up through smoke and broken clouds into hard white sunlight while a large enemy explosion and drifting black plume recede far below in the background. Camera settles into formation behind the locked aircraft and holds it steady as it escapes the battle space. Engine thunder stabilizes, radio static fades, wind softens into distance.

STYLE: [your style prompt goes here, identical in every shot. how to build your own is at the bottom of this article]

negative: no face morph, no identity drift, no helmet redesign, no oxygen-mask deformation, no aircraft redesign, no changing wing geometry, no changing tail shape, no changing markings, no duplicated primary jet, no aircraft merging, no bent wings, no floating aircraft parts, no impossible instant direction changes, no weightless movement, no random extra jets beyond brief enemy silhouettes, no close-detailed enemy cockpit shots, no primary aircraft damage, no pilot ejecting, no graphic injury, no gore, no cockpit explosion, no oversized unrealistic mushroom clouds, no sci-fi lasers, no neon engine glow, no photoreal rendering, no smooth commercial CGI, no motion blur
```

montages are the exception to the beat ceiling. sequences are not, and cutting a longer story into prompts is its own craft.

## cutting a longer story into prompts

when youre generating a sequence rather than a montage, four rules keep the cuts invisible:

1/ one block, one continuity. all prompts from the same narrative block reuse the same references, same environment descriptor, same light. copy paste, dont rewrite

2/ 3 to 4 beats per 15s, maximum. if a block needs more, split it into two prompts

3/ bridge with sound. end prompt A and start prompt B on the same audio cue (a siren, a breath, an impact ringing out). the edit stitches on the sound

4/ match the frame at the cut. if shot B continues shot A's action, write the same framing and eye placement explicitly in both prompts

the rules handle continuity. identity is a different problem, and its where most drift starts.

## character + environment sheets

you can be pretty free with what you upload, but two structures pay off every time:

- a character sheet: three angles of the persons face. then you just tag that image every time you refer to the person in the prompt

- an environment sheet: two to three different angles of the environment

i upload 4 to 10 reference images per prompt. 2.5 takes up to 50 slots and actually remembers the structure and logic behind every file, so you can hand it your whole cast, props, and style refs at once.

but heres the counterintuitive part: for montages, go the other way. the fewer references you put in, the more the model makes its own shots, and it will still hold the style without breaking as long as you give it the rough environment and the style prompt. heavy refs for narrative continuity, light refs for invention.

identity locked. next problem: what it sounds like.

## sound: use the sfx, skip the dialog

after the last few days my read on the native audio: the sound effects are the surprise winner. seedance is really, really good at cars, planes, mechanical stuff, and i keep them in the final cut. lip-sync looks somewhat usable for ugc talking heads, but for the most part i dont use native dialog. and music never goes in the generation. it gets added in the edit, where you control it.

thats the toolkit. heres where the model is already winning.

## where its already winning

a quick map of the styles working right now, with proof:

b-roll taste: 2.5 is much better than 2.0 at coming up with random insert shots on its own, and its cinematography taste jumped.

[Embedded Tweet: https://x.com/i/status/2084692723441811619]

organic vlog content: holds up.

[Embedded Tweet: https://x.com/i/status/2085141769755242580]

animation and motion: my favorite lane, more below.

[Embedded Tweet: https://x.com/i/status/2084652437848363277]

fake vhs and fake broadcast: i think this is going to be a really popular emerging style. a seedance 2.5 vhs clip of a guy dancing on a car literally tricked a french news channel into posting it. tons of viral ideas in this pocket, and the vhs grain is a really unique way to make ai look less sloppy.

[Embedded Tweet: https://x.com/i/status/2083740822814482586]

one style on that map i wont pretend to own:

## ugc (full credit: maximalist)

im not a ugc pro at all. this section is me pointing at someone elses sauce: maximalist wrote the best 2.5 ugc guide ive seen.

[Embedded Tweet: https://x.com/i/status/2084641403422785893]

two moves worth stealing from his prompt: phone-camera honesty ("slight shake, casual autofocus hunting, no gimbal smoothing", the imperfections ARE the realism), and speech direction with real pauses (filler words, trailing off, quiet stretches where shes just doing the action instead of narrating). objects only ever enter frame through a visible hand action. go read the full prompt in his article, its worth it.

and then theres the lane im actually betting on.

## my lane: painted animation

for me, im going all in on anime and painted animation. i think you can get stuff at the same tier as into the spider-verse. thats the style im chasing.

the pipeline:

- midjourney for the base images

- gpt image models to convert everything into my specific style, then upscale and style-lock

- 4 to 10 of those as references into each seedance 2.5 prompt

the glue is the style prompt: one paragraph of text that goes in the midjourney prompt, the gpt prompt, and the seedance prompt. one description of the look, enforced at every stage of the pipeline.

im keeping mine to myself, its the moat. but heres how you build your own: take imagery or cartoons you love and hand them to gemini. have it extract the style details, the exact things that make the look the look, and turn them into keywords. that paragraph becomes your style prompt. one description, reused in midjourney, gpt, and seedance, every single shot.

## the playbook

1/ aggregate, dont one-shot. prompt way more than you think, pull the best moments

2/ montage batches: 2-5s of script becomes one 15-30s fast-cut montage prompt, tell the model youre cutting it yourself, generate ~10

3/ every prompt is the same structure: shot, references, character, setting, camera, sequence, style prompt. under 3,500 characters for narrative

4/ beats are emotion as body movement + physics + inline sound + contrast. 3-4 beats per 15s for narrative, break the rule for montages

5/ in every prompt: no music, face stable line, @image discipline, negatives only for problems youve hit

6/ build your style prompt with gemini (extract the look from imagery you love), then reuse it across midjourney, gpt, and seedance

7/ character sheet = 3 face angles. environment sheet = 2-3 angles. 4-10 refs per prompt, but go light on refs for montages

8/ keep the native sfx, skip the native dialog, music in the edit

9/ text in frame is broken. captions and overlays are your job

## where im taking it

the realism lane is arriving on its own, nobody needs my help there. the interesting question is what you point this at. for me its painted animation and idk ill probably find some more cool styles.

im going to keep dropping what i learn (and the prompts) in my free telegram: t.me/beechhq

what style are you going all in on?
