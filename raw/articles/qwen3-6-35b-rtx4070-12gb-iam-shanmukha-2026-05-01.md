---
title: "Qwen3.6-35B-A3B running on RTX 4070 12GB at 128K context — 60 tok/sec"
author: "Shanmukha Vishnu"
username: "@iam_shanmukha"
created: 2026-05-01
source: "https://x.com/iam_shanmukha/status/2050098256424927491"
type: thread
tags: [qwen, llama.cpp, moe, consumer-gpu, gguf]
---

# Thread

## 1. Shanmukha Vishnu (@iam_shanmukha)
- URL: https://x.com/iam_shanmukha/status/2050098256424927491
- Date: Fri May 01 06:21:27 +0000 2026
- Character count: 387

QWEN 3.6 + NVIDIA RTX 4070 12GB V RAM  (64GB RAM)

60 tok/sec, 128k context + Q4_K_M

llama-server \
    -m Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_M.gguf \
    --alias qwen3.6-35b-128k \
    --host 0.0.0.0 \
    --port 8083 \
    -ngl 999 -ncmoe 25 -fa on \
    --cache-type-k q8_0 --cache-type-v q8_0 \
    -c 131072 -np 1 -t 12 \
    --no-warmup --jinja --metrics

#QWEN #llm #ai

## 2. Deepak Kumar (@deepakaryan1988)
- URL: https://x.com/deepakaryan1988/status/2050182881134469172
- Date: Fri May 01 11:57:44 +0000 2026
- Character count: 98

@iam_shanmukha I do have 32GB DDR4 3600mhz RAM with 3060ti 8GB VRAM, would it be possible on that?

## 3. Shanmukha Vishnu (@iam_shanmukha)
- URL: https://x.com/iam_shanmukha/status/2050191021456363877
- Date: Fri May 01 12:30:04 +0000 2026
- Character count: 193

@deepakaryan1988 Yes.  Of course it should be possible. Try playing around with the ncmoe parameter , make it 60 and gradually reduce. With 40 ncmoe i am just using 4GB of VRAM out of 12GB VRAM

## 4. shigeo (@Walalers)
- URL: https://x.com/Walalers/status/2050313428720316862
- Date: Fri May 01 20:36:29 +0000 2026
- Character count: 269

@iam_shanmukha I've been working with this, I've lowkey found the best flags on my 4070 ti. Full 262k context, just reducing the kv cache to q4_0 but Qwen models are excellent at this tune. It's damn near q8_0, been using it for three days haven't noticed any drop off.

## 5. DZ (@prodbitz)
- URL: https://x.com/prodbitz/status/2050341658525397132
- Date: Fri May 01 22:28:39 +0000 2026
- Character count: 68

@iam_shanmukha same pc same model with you，LMstudio only 20 tokens/s

## 6. Lotto (@LottoLabs)
- URL: https://x.com/LottoLabs/status/2050342876480188462
- Date: Fri May 01 22:33:29 +0000 2026
- Character count: 37

@iam_shanmukha Get it on localmaxxing

## 7. Shanmukha Vishnu (@iam_shanmukha)
- URL: https://x.com/iam_shanmukha/status/2050347455401881971
- Date: Fri May 01 22:51:41 +0000 2026
- Character count: 62

@prodbitz Try buillding llama server 

https://t.co/q6WDejz9g2

## 8. /// // (@marcsh)
- URL: https://x.com/marcsh/status/2050351254606635515
- Date: Fri May 01 23:06:47 +0000 2026
- Character count: 147

@iam_shanmukha This is super cool cause I can keep Qwen3.6 up and running while testing my C# Comfy-like application on my 3090

Thanks for posting

## 9. Janvitos (@janvitos)
- URL: https://x.com/janvitos/status/2050351582848450733
- Date: Fri May 01 23:08:05 +0000 2026
- Character count: 222

@iam_shanmukha Have you tried using --fit-target 256 (replaces -ngl 999)? I've had the best results with that parameter, same GPU as yours. Got over 80 tok/sec with Unsloth IQ4_XS. Now using Q4_K_XL with around 60 tok/sec.

## 10. MVP (@_MVPi)
- URL: https://x.com/_MVPi/status/2050354850127298941
- Date: Fri May 01 23:21:04 +0000 2026
- Character count: 61

@iam_shanmukha Comment tu desactives le Thinking mode natif ?

## 11. Serhii Y. (@desugar_64)
- URL: https://x.com/desugar_64/status/2050355506233880613
- Date: Fri May 01 23:23:41 +0000 2026
- Character count: 38

@iam_shanmukha https://t.co/LYfFxI1lm1

## 12. toji (@tojinonzenin)
- URL: https://x.com/tojinonzenin/status/2050358821831516234
- Date: Fri May 01 23:36:51 +0000 2026
- Character count: 56

@iam_shanmukha Same gpu with 32 gb ram works for me well

## 13. Shanmukha Vishnu (@iam_shanmukha)
- URL: https://x.com/iam_shanmukha/status/2050361097925062749
- Date: Fri May 01 23:45:54 +0000 2026
- Character count: 29

@tojinonzenin Great to hear 😊

## 14. Shanmukha Vishnu (@iam_shanmukha)
- URL: https://x.com/iam_shanmukha/status/2050361657424249106
- Date: Fri May 01 23:48:07 +0000 2026
- Character count: 52

@janvitos Not yet. Will try that. Thanks for posting

## 15. unbug (@unbug)
- URL: https://x.com/unbug/status/2050372380753895528
- Date: Sat May 02 00:30:44 +0000 2026
- Character count: 26

@iam_shanmukha Wild, 60tps

## 16. Victor (@rotorB)
- URL: https://x.com/rotorB/status/2050375079251390499
- Date: Sat May 02 00:41:27 +0000 2026
- Character count: 36

@iam_shanmukha m4 max 64Gb, 85 tok/s

## 17. Andro (@AndrokillsAndro)
- URL: https://x.com/AndrokillsAndro/status/2050377740470178057
- Date: Sat May 02 00:52:02 +0000 2026
- Character count: 64

@iam_shanmukha Is it possible to run in 8 gb vram and 32 gb ram.

## 18. Shanmukha Vishnu (@iam_shanmukha)
- URL: https://x.com/iam_shanmukha/status/2050377950827348342
- Date: Sat May 02 00:52:52 +0000 2026
- Character count: 40

@AndrokillsAndro https://t.co/QCs4nmTrrF

## 19. Buildingabot (@buildingabot)
- URL: https://x.com/buildingabot/status/2050378872500154871
- Date: Sat May 02 00:56:32 +0000 2026
- Character count: 232

@iam_shanmukha This is really cool. I feel like pivoting full force into this right now.

Side note unrelated and unrequested.

Every time I'm scanning code and I read "ngl" My inner monologue says not gonna lie and chuckles. 

Bye.

## 20. Phat Nguyen (@pnxnormal)
- URL: https://x.com/pnxnormal/status/2050409673854177429
- Date: Sat May 02 02:58:55 +0000 2026
- Character count: 104

@iam_shanmukha how ? Qwen3.6-35B-A3B-UD-Q4_K_M.gguf it self already 22.1G , it cant not fit in 12G VRAM.

## 21. Rumburak (@Kutaadaw)
- URL: https://x.com/Kutaadaw/status/2050442320818974834
- Date: Sat May 02 05:08:39 +0000 2026
- Character count: 48

@iam_shanmukha How about  Q6 Q8 at lower speed ?

## 22. Dev Patel (@devnp2007)
- URL: https://x.com/devnp2007/status/2050442909217087564
- Date: Sat May 02 05:10:59 +0000 2026
- Character count: 162

@iam_shanmukha I am looking to buy a legion with 64gb ram 2tb SSD what graphics card should I buy it with targetting aiml profiles next year for job/internships ?

## 23. Tahj (@Tahjzx)
- URL: https://x.com/Tahjzx/status/2050548325380657417
- Date: Sat May 02 12:09:52 +0000 2026
- Character count: 295

@iam_shanmukha Thank you so much for posting this,  I'm super new to this stuff but learned so much. I never understood the idea that everything has to fit vram, maybe im still mistaken in some way but im getting 50 tok/sec now!

5080 16gb /32 gb of ram and I probably could do more, with tuning

## 24. RopeBourgeX (@RopeBourgeX)
- URL: https://x.com/RopeBourgeX/status/2050563192913330597
- Date: Sat May 02 13:08:57 +0000 2026
- Character count: 97

@iam_shanmukha @grok, can you explain these settings to me as they would be applied in LM Studio?

## 25. edba (@baed555)
- URL: https://x.com/baed555/status/2050630020473774357
- Date: Sat May 02 17:34:30 +0000 2026
- Character count: 179

@iam_shanmukha I got mac pro 7,1 with 768gb ecc, speed dont care, can i run it on for quality long context? Thanks! I could put inside a rtx 6000 w/ 96gb. 

But without, possible?

## 26. WaitState (@quartercpu)
- URL: https://x.com/quartercpu/status/2050630114891674088
- Date: Sat May 02 17:34:52 +0000 2026
- Character count: 300

@iam_shanmukha Same GPU, but I have 32GB RAM.
Tried similar settings in LM Studio. Told Hermes to run a test with these settings. It ran ~15 prompts, took 10-15 minutes, and everything passed. Got 50-52 tokens/sec.
So yeah, don't shy away just because you don't have 64GB RAM. https://t.co/8qUnb4V11W

## 27. Eduardo (@educaron)
- URL: https://x.com/educaron/status/2050649520430526473
- Date: Sat May 02 18:51:59 +0000 2026
- Character count: 111

@iam_shanmukha good number. Thats the double output tokens I get on a 3060 with same model and parameter as you
