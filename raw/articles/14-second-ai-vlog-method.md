---
source_url: user-provided://telegram-paste
ingested: 2026-07-21
sha256: 4fed59c31289f7d3aecfe4fed7885ba8e27409d7e918d840c6a532d635cd0a46
---
Not this: "Unlock radiant skin with our advanced formula."
This: "okay these are the ones I've been taking every morning."
Read your line out loud. If you wouldn't say it to a friend, she shouldn't say it to camera.
Prompt cheatsheet
The modifiers that made this clip look real. Steal them.
"handheld selfie POV" and "subtle camera shake": the vlog feel, kills the tripod look
"golden light through sheer curtains": the bedroom glow
"steam in the air": sells the shower
"realistic skin texture": goes in every scene, keeps her off the plastic AI look
"she looks into the lens": the talking-to-you feel
visible text: keep it minimal, your brand name only, then check it in QC
Step 4: QC gate before the next scene
Before you generate the next scene, check the one you just made.
face still matches the last scene
hands have 5 fingers, actually count them
eyes and teeth on her smile frames, that's where faces go wrong
liquid and foam move like liquid and foam, not jelly
motion: nothing floats, nothing morphs between frames
read every label up close, zoom into anything with text on it
That last one matters most. Labels and small text are where these models still slip. In the original clip, freeze frame and zoom on the shampoo bottle: the label isn't real words, it's reaching for something like Lumière and falling apart halfway through. Nobody catches it at normal speed. Check for it anyway.
Step 5: assemble
Once all 3 scenes pass, cut them together in story order: wake, shower, breakfast. Hard cuts, no transitions, this is vlog pacing. Keep the total under 15 seconds.
Export 9:16 vertical for TikTok and Reels, 16:9 wide for X. Any editor works, this is three clips and two cuts. Post the export itself, native to each platform. Never re-upload a compressed rip of your own video, quality dies on the second compression.
Why bother
A real UGC creator for something like this runs $150 to $500 a video, plus 5 to 7 days of briefing and reshoots before you get a take you can use. This is describing 3 scenes to a chat window and checking the output yourself.
That's the whole method. Go make one.

The 14-second AI vlog method
The post that got you here was 14 seconds, 4K, one woman with the same face the whole way through. She wakes up at sunrise, showers, eats breakfast, talks to camera, waves goodbye. Three scenes, cut together. Nobody was on set. No camera, no crew, no talent, no location. Everything in it was generated. This doc is the method: the tools, the steps, and full prompts for every scene, so you can build your own version.
The stack
Claude is the agent. You talk to it in plain English, it drives everything downstream.
The eComrads MCP is the connector that does the generating. Words in, footage out. You add it once inside Claude, covered in step 1.
Seedance 2.0 is the video model that rendered this specific clip, in 4K. It sits behind the MCP doing the actual rendering. You never touch it directly.
The method
Step 1: setup
Add the MCP connector inside Claude:
https://mcp.ecomrads.com/mcp
Where that goes: in Claude, open settings, then connectors, then add custom connector, and paste the URL. Site's ecomrads.com if you want to poke around first. Once it's connected, you're done with dashboards. You just talk to Claude in plain English and it calls the generator for you.
Step 2: cast her once
Before you generate anything, define your character in one message. Here's a full cast block modeled on the woman in the clip. Paste it as is, or swap the details for your own character:
Woman in her late 20s. Long brown hair with lighter sun-kissed lengths falling past her shoulders. Warm tan skin with real texture. A small beauty mark above her lip and another on her chin. Soft natural makeup, warm easy smile. Wearing a cream linen shirt and neutral loungewear. Setting: a bright coastal-modern home, white walls, sheer curtains.
The beauty marks aren't decoration. Small fixed details like that are what lock a face.
Save this block somewhere. Paste it into every scene prompt you write, word for word, forever. That repetition is the whole trick behind the face staying consistent across cuts. Nothing else about it is special.
Step 3: scene by scene, never all at once
Don't generate all 14 seconds in one go. One scene is one shot is one generation. Check it before you move on. These aren't the literal prompts behind the original clip. They're full recipes for recreating each scene, written to paste. Each one opens with your cast block from step 2.
Scene 1, wake up (about 4 seconds)
[PASTE YOUR CAST BLOCK]

Handheld POV selfie video, her arm extended toward the camera. She lies in bed under white bedding with lots of pillows, hair spread on the pillow. Sunrise gold light through the sheer curtains behind her. She stretches one arm overhead, then smiles into the lens. Subtle natural camera shake. Realistic skin texture. 4K.
Scene 2, shower (about 4 seconds)
[PASTE YOUR CAST BLOCK]

Bathroom with white subway tile and a glass shower door, frosted window with condensation on it. She holds a pastel pump bottle up to the camera and smiles. Then a close-up of foam lathering through her wet hair, strand by strand. Steam in the air. Realistic skin texture. 4K.
Scene 3, breakfast (about 6 seconds)
[PASTE YOUR CAST BLOCK]

Bright breakfast nook. She sits behind a stack of pancakes topped with raspberries, blackberries, blueberries and powdered sugar. A glass of orange juice and a woven basket bag on the table. She takes a bite, opens a small frosted supplement bottle, tips a capsule into her palm, says "[WRITE HER LINE HERE]" to the camera, then waves goodbye. Handheld selfie framing. Realistic skin texture. 4K.
Make it yours. Upload a photo of your actual product into the same chat and tell Claude to put that exact bottle in her hand. Keep her cast block word for word. And when you write your own scenes: one action per scene, never two. If a scene really needs two beats, like scene 3 does, give it the most seconds or split it into two generations.
If she talks
You write the spoken line yourself, in quotes, inside the scene prompt. Two short sentences max per scene. And write it the way people actually talk, not ad copy.