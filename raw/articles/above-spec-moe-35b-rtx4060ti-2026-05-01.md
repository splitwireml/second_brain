---
title: "AboveSpec: 35B MoE on RTX 4060 Ti 8GB"
created: 2026-05-01
type: raw
source: x-thread
tweet_id: "2050003701033529347"
author: "@above_spec"
platform: x
tags: [local-llm, moe, quantization, llama.cpp, qwen]
---

# Raw: AboveSpec Thread — 35B MoE on RTX 4060 Ti 8GB

**URL:** https://x.com/above_spec/status/2050003701033529347
**Author:** @above_spec (AboveSpec)
**Date:** 2026-05-01
**Platform:** X/Twitter
**Thread size:** 38 tweets

## Tweet Breakdown

### Tweet 1 (ID: 2050003701033529347)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 00:05:44 +0000 2026
**Media:** https://pbs.twimg.com/media/HHMRzQ_XsAEYoz1.png

"You need a 24 GB GPU for serious local LLMs in 2026."

Everyone repeats this. It's not true anymore.

Just ran a 35B-parameter model on an RTX 4060 Ti 8 GB: • 41 tok/s at 16k context • 24 tok/s at 200k context
Recipe + benchmarks below 🧵 https://t.co/sr1VjNMe4f

_Engagement: 71 replies, 118 RTs, 1581 likes_

---

### Tweet 2 (ID: 2050003703336231271)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 00:05:44 +0000 2026

How to make it work:

MoE offload. Qwen3.6-35B activates only 3 B params per token. Keep attention + shared weights on GPU, push the cold expert FFNs to system RAM. In llama.cpp: -ngl 99 -ncmoe 99.

q8_0 KV cache. ~10 KB/token. 200k  fits in 2 GB VRAM with FlashAttention on.

_Engagement: 6 replies, 2 RTs, 93 likes_
_In reply to: 2050003701033529347_

---

### Tweet 3 (ID: 2050003705584292102)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 00:05:45 +0000 2026
**Media:** https://pbs.twimg.com/media/HHMTCtVX0AAAGF1.jpg

Receipts. Qwen3.6-35B-A3B Q4_K_S, q8_0 KV, single-batch, FA on. Same machine, same model, varying context depth:

PP barely moves (332 t/s even at 200 k tokens). TG decays ~linearly with depth — attention scan over the full KV is the bottleneck, as expected. https://t.co/WY45lmQ2Nz

_Engagement: 3 replies, 2 RTs, 31 likes_
_In reply to: 2050003703336231271_

---

### Tweet 4 (ID: 2050003711338979613)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 00:05:46 +0000 2026

Why RTX 3070 8GB owners shouldn't write the card off:
The real bottleneck is host-RAM bandwidth for the MoE experts (~3 B active × Q4 ≈ 1.5 GB/token of streaming reads from DDR5), not GPU compute. The 3070 actually has higher memory bandwidth than the 4060 Ti (448 vs 288 GB/s).

_Engagement: 1 replies, 2 RTs, 34 likes_
_In reply to: 2050003705584292102_

---

### Tweet 5 (ID: 2050003712945397911)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 00:05:47 +0000 2026

If you have 64 GB RAM and a half-decent CPU, MoE + 8GB is arguably the new home-LLM sweet spot.

What setup are you running?

_Engagement: 13 replies, 0 RTs, 47 likes_
_In reply to: 2050003711338979613_

---

### Tweet 6 (ID: 2050144763127492707)
**Author:** @g4m3r0ps (g4m3r0ps)
**Time:** Fri May 01 09:26:16 +0000 2026

@above_spec Sorry, but 16k context isn't even enough to fit the system prompt of some harnesses, it's not usable in real life.

_Engagement: 1 replies, 0 RTs, 17 likes_
_In reply to: 2050003701033529347_

---

### Tweet 7 (ID: 2050171927323619663)
**Author:** @ItsmeAjayKV (AJ)
**Time:** Fri May 01 11:14:12 +0000 2026

@above_spec I have a 3060 12 GB. This is exaclty my run configuration, MoE offload on Qwen3.6-35B 5 bit version,and got  ~44t/s for 128k context.

Were you using og llama.cpp or any other repo like the turboquant version from @no_stp_on_snek  (TheTom).

_Engagement: 3 replies, 0 RTs, 23 likes_
_In reply to: 2050003701033529347_

---

### Tweet 8 (ID: 2050182115178991820)
**Author:** @thethiny (thethiny 🐰🍉)
**Time:** Fri May 01 11:54:41 +0000 2026

@above_spec Do you have a Llama.cpp cli command we can try? I have an 8GB but obviously I can't fully use the 8GB due to some being used, so I wanted to see what u have.

_Engagement: 2 replies, 0 RTs, 1 likes_
_In reply to: 2050003701033529347_

---

### Tweet 9 (ID: 2050182377922605182)
**Author:** @Coder9420948594 (Coder)
**Time:** Fri May 01 11:55:44 +0000 2026

@above_spec the thing there is that dense vs a3b quality is't same, also how you were able to test it on 200K context window? with 8gb vram

_Engagement: 1 replies, 0 RTs, 4 likes_
_In reply to: 2050003701033529347_

---

### Tweet 10 (ID: 2050183646120739018)
**Author:** @T_Wrex_Baby (T.Rex-Baby)
**Time:** Fri May 01 12:00:46 +0000 2026

Anyone after AI must skip Window altogether.

Buy any Mac and you'll easily end up with 64GB unified memory giving you 60GB as VRAM.

Also, Nvidia is a terrible choice, they can only run lobotomised quantised 4-bit models. They don't have support for full and even if they did, they can't handle the size, unlike Mac.

_Engagement: 5 replies, 0 RTs, 6 likes_
_In reply to: 2050003701033529347_

---

### Tweet 11 (ID: 2050184067342041250)
**Author:** @sakurayukiai (Sakura Yuki)
**Time:** Fri May 01 12:02:26 +0000 2026
**Media:** https://pbs.twimg.com/media/HHO3hxyWoAAJWDJ.jpg

@above_spec 41 tok/s perfectly matches the 288 GB/s memory bandwidth of a 4060 Ti if the model is ~7GB. Cramming a 35B model into under 2 bits without trashing the perplexity is wild. What's the quant? https://t.co/JTKsqiw4Dh

_Engagement: 1 replies, 0 RTs, 6 likes_
_In reply to: 2050003701033529347_

---

### Tweet 12 (ID: 2050185960235606413)
**Author:** @digitalnoah (Noah King)
**Time:** Fri May 01 12:09:58 +0000 2026

@above_spec I think we can agree that Q4_K_S is going to take a big hit on intelligence quality.

Being able to run a 30b model isn't the goal. Its being able to run it reliably without excessive hallucination.

_Engagement: 4 replies, 0 RTs, 36 likes_
_In reply to: 2050003701033529347_

---

### Tweet 13 (ID: 2050189710522187887)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 12:24:52 +0000 2026

@digitalnoah I need to test q4_k_m version

_Engagement: 1 replies, 0 RTs, 3 likes_
_In reply to: 2050185960235606413_

---

### Tweet 14 (ID: 2050190564532879384)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 12:28:15 +0000 2026

@Coder9420948594 Only 3b active parameters + context cached at q8 are loaded on the gpu.

_Engagement: 1 replies, 0 RTs, 5 likes_
_In reply to: 2050182377922605182_

---

### Tweet 15 (ID: 2050193219304980743)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 12:38:48 +0000 2026

@T_Wrex_Baby Yes, my brother has m4 max with 128gb and can run 27b at 20 tps. The advantage of 5090 is that it can do about 3x the speed.

_Engagement: 1 replies, 0 RTs, 12 likes_
_In reply to: 2050183646120739018_

---

### Tweet 16 (ID: 2050193894978035982)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 12:41:29 +0000 2026

@sakurayukiai Q4_k_s

_Engagement: 0 replies, 0 RTs, 5 likes_
_In reply to: 2050184067342041250_

---

### Tweet 17 (ID: 2050194652410556607)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 12:44:30 +0000 2026

@ItsmeAjayKV @no_stp_on_snek Llama.cpp, i did use thetom's turboquant to test turbo3 for kv cache. I could fit all 262k context with turbo3 but token generation got slower.

_Engagement: 2 replies, 0 RTs, 6 likes_
_In reply to: 2050171927323619663_

---

### Tweet 18 (ID: 2050195762051506373)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 12:48:55 +0000 2026

@g4m3r0ps Did you see the table? I tested all the way to 200k

_Engagement: 0 replies, 0 RTs, 8 likes_
_In reply to: 2050144763127492707_

---

### Tweet 19 (ID: 2050198908274348505)
**Author:** @scorpion7slayer (0xAdo)
**Time:** Fri May 01 13:01:25 +0000 2026

@above_spec And what do you think of a GTX 1050?

_Engagement: 1 replies, 0 RTs, 2 likes_
_In reply to: 2050003701033529347_

---

### Tweet 20 (ID: 2050199621557764555)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 13:04:15 +0000 2026

@scorpion7slayer Haha 2gb vram? That's tough. Maybe test 0.8b version of qwen3.5?

_Engagement: 1 replies, 0 RTs, 5 likes_
_In reply to: 2050198908274348505_

---

### Tweet 21 (ID: 2050202740198907915)
**Author:** @NicW_AI (Nic Wienandt)
**Time:** Fri May 01 13:16:38 +0000 2026

@above_spec You said Serious. 16k context isn’t actually serious. It’s child’s play

_Engagement: 1 replies, 0 RTs, 12 likes_
_In reply to: 2050003701033529347_

---

### Tweet 22 (ID: 2050211988601458882)
**Author:** @KingDDev (Daniel King)
**Time:** Fri May 01 13:53:23 +0000 2026

@above_spec Have you run it inside anything?
OpenCode? 
Hermes?

_Engagement: 3 replies, 0 RTs, 1 likes_
_In reply to: 2050003701033529347_

---

### Tweet 23 (ID: 2050219787461050687)
**Author:** @allinasecond (allinasecond)
**Time:** Fri May 01 14:24:23 +0000 2026

@above_spec Is there anything I can do with a 5060 in terms of coding?

_Engagement: 1 replies, 0 RTs, 2 likes_
_In reply to: 2050003701033529347_

---

### Tweet 24 (ID: 2050229752322031621)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 15:03:59 +0000 2026
**Media:** https://pbs.twimg.com/media/HHPg-IFWgAAJDTp.jpg

@MikelEcheve made a cool image for this post! https://t.co/0s6FjBzJLk

_Engagement: 0 replies, 0 RTs, 5 likes_
_In reply to: 2050003701033529347_

---

### Tweet 25 (ID: 2050232583212990648)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 15:15:13 +0000 2026

@NicW_AI 200k context max. Check the table in the OP

_Engagement: 0 replies, 0 RTs, 3 likes_
_In reply to: 2050202740198907915_

---

### Tweet 26 (ID: 2050232938906697911)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 15:16:38 +0000 2026

@allinasecond you can test similar 35b model. Maybe go for q4_k_m, it's slightly bigger but should be more accurate.

_Engagement: 0 replies, 0 RTs, 0 likes_
_In reply to: 2050219787461050687_

---

### Tweet 27 (ID: 2050233019571577248)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 15:16:58 +0000 2026

@thethiny ~/llama-cpp-turboquant/build/bin/llama-server \
  --model ~/models/unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_S.gguf \
  --mmproj ~/models/unsloth/Qwen3.6-35B-A3B-GGUF/mmproj-F32.gguf \
  --alias qwen3.6-35b-a3b \
  --host 127.0.0.1 --port 8080 \
  --ctx-size 200000 \

_Engagement: 2 replies, 0 RTs, 4 likes_
_In reply to: 2050182115178991820_

---

### Tweet 28 (ID: 2050244199224680599)
**Author:** @above_spec (AboveSpec)
**Time:** Fri May 01 16:01:23 +0000 2026

@KingDDev Chained calls with real data dependency (search_flights → pick cheapest → book_flight with that flight_id) — ✅

Next going to run Hermes agent now.

_Engagement: 1 replies, 0 RTs, 1 likes_
_In reply to: 2050211988601458882_

---

### Tweet 29 (ID: 2050288209712529699)
**Author:** @Drowlord101 (Drowlord101)
**Time:** Sat May 02 10:32:50 +0000 2026

@above_spec Sounded sketchy. But I have a Qwen3.6-35B-A3B-UD-Q4_K_M.gguf that is 22GB, and I imported that into Ollama, and it seems to work pretty good. My laptop has an Nvidia RTX A5000 with 16gb vram and 96gb system ram.

It appears to be perfectly useable and fast.

_Engagement: 2 replies, 0 RTs, 2 likes_
_In reply to: 2050003701033529347_

---

### Tweet 30 (ID: 2050289034589622340)
**Author:** @above_spec (AboveSpec)
**Time:** Sat May 02 10:41:20 +0000 2026

@Drowlord101 Nice, what are your token generation speeds?

_Engagement: 1 replies, 0 RTs, 0 likes_
_In reply to: 2050288209712529699_

---

### Tweet 31 (ID: 2050357975135449151)
**Author:** @GeekProxy (GeekProxy)
**Time:** Sat May 02 22:06:59 +0000 2026

@above_spec I remember when trying to fit even a 13B model into 8GB VRAM was a nightmare, let alone hitting 40+ tokens a second on a 35B architecture.

_Engagement: 1 replies, 0 RTs, 5 likes_
_In reply to: 2050003701033529347_

---

### Tweet 32 (ID: 2050359309171593319)
**Author:** @above_spec (AboveSpec)
**Time:** Sat May 02 22:20:18 +0000 2026

@GeekProxy It doesn't all fit on the gpu, just active parameters and context.

_Engagement: 0 replies, 0 RTs, 1 likes_
_In reply to: 2050357975135449151_

---

### Tweet 33 (ID: 2050365553466888423)
**Author:** @ElbertePlinio (ElbertePlinio)
**Time:** Sun May 03 00:30:29 +0000 2026

@above_spec I have an AMD RX 9070 XT 16gb + 32gb RAM DDR4

Do you think it's possible?

_Engagement: 1 replies, 0 RTs, 1 likes_
_In reply to: 2050003701033529347_

---

### Tweet 34 (ID: 2050497411328422309)
**Author:** @19ManKo86 (19ManKo86)
**Time:** Sun May 03 21:10:52 +0000 2026

@above_spec I run Qwen3.6-35B-A3B Q4_K_M on rtx5070ti, Ryzen9 9900x3d, 64gb ddr5 6000ram, but it runs very slow. Where di i find the mentioned Qwen3.6-35B-A3B Q4_K_S q_8? Thx

_Engagement: 1 replies, 0 RTs, 1 likes_
_In reply to: 2050003701033529347_

---

### Tweet 35 (ID: 2050518343048724488)
**Author:** @above_spec (AboveSpec)
**Time:** Mon May 04 01:02:52 +0000 2026

@19ManKo86 https://t.co/QXrZYgDMDU you can use K_M version from here. q_8 is kv cache = for context. You should see ~100 tps which goes down to ~50 as context fills up. I just tested this gpu with Ryzen 9 7900x yesterday, need to post about it.

_Engagement: 0 replies, 0 RTs, 2 likes_
_In reply to: 2050497411328422309_

---

### Tweet 36 (ID: 2050545357990588527)
**Author:** @SakshamMittal05 (SakshamMittal05)
**Time:** Mon May 04 05:20:22 +0000 2026

@above_spec Is it possible to do this with a smaller model on a RTX 3050 (4GB)? Any MoE models I can run? I am able to run Qwen-3.5-4B-Q4-K-M at very decent speed (without the mmproj, with mmproj speed degrades considerably but everything still fits on the GPU).

_Engagement: 1 replies, 0 RTs, 1 likes_
_In reply to: 2050003701033529347_

---

### Tweet 37 (ID: 2050575546812190749)
**Author:** @above_spec (AboveSpec)
**Time:** Mon May 04 09:18:55 +0000 2026

@SakshamMittal05 Maybe if you have enough ram, but you habe to accept much slower generation speeds

_Engagement: 0 replies, 0 RTs, 1 likes_
_In reply to: 2050545357990588527_

---

### Tweet 38 (ID: 2050866492929904848)
**Author:** @above_spec (AboveSpec)
**Time:** Tue May 05 09:40:52 +0000 2026

@ElbertePlinio Yeah for sure, you shiuld get evem better performance!

_Engagement: 0 replies, 0 RTs, 0 likes_
_In reply to: 2050365553466888423_

---

