---
title: "We're open-sourcing Hy-MT1.5-1.8B-1.25bit — a 440MB translation model that runs fully offline on your phone, supports 33"
source: x-bookmarks
tweet_id: "2049487799850840334"
tweet_url: "https://x.com/TencentHunyuan/status/2049487799850840334"
author_name: Tencent Hy
author_handle: "@TencentHunyuan"
tweet_date: "Wed Apr 29 13:55:43 +0000 2026"
bookmark_date: "2026-04-29"
content_type: thread
character_count: 845
retweet_count: 276
like_count: 2218
reply_count: 59
images:
  - path: raw/assets/tencent-hunyuan-2049487799850840334/HHE-FfTaUAAs4fr.jpg
    caption: "Hy-MT1.5-1.8B-1.25bit benchmark comparison chart"
    source: "https://pbs.twimg.com/media/HHE-FfTaUAAs4fr.jpg"
  - path: raw/assets/tencent-hunyuan-2049487799850840334/HHE-GfeacAAPBOP.jpg
    caption: "Model size and language coverage overview"
    source: "https://pbs.twimg.com/media/HHE-GfeacAAPBOP.jpg"
  - path: raw/assets/tencent-hunyuan-2049487799850840334/HHE-HguaIAAYR6d.mp4
    caption: "Animated demo GIF"
    source: "https://video.twimg.com/tweet_video/HHE-HguaIAAYR6d.mp4"
external_urls:
  - "https://t.co/DbcwLBe6vw"
  - "https://t.co/NgXKeNZz4L"
  - "https://t.co/b6DqGKDelf"
  - "https://t.co/1a6repNrnt"
type: article
tags: [model, quantization, translation, mobile, inference, chinese-ai]
---

We're open-sourcing Hy-MT1.5-1.8B-1.25bit — a 440MB translation model that runs fully offline on your phone, supports 33 languages, and outperforms Google Translate.

At 1.8B parameters, it matches commercial translation APIs and 235B-scale models on standard benchmarks. By quantizing to 1.25-bit, memory drops from 3.3GB (FP16) to 440MB — 25% smaller and ~10% faster than prior 1.67-bit approaches, with no accuracy loss.

Covers 33 languages, 5 dialects, and 1,056 translation directions including minority languages like Tibetan and Mongolian.

Our translation model has won 30 first-place rankings in international MT competitions and is already deployed across multiple Tencent products.🏆

📲Demo APK (Android): https://t.co/DbcwLBe6vw
🤗Hugging Face:: https://t.co/NgXKeNZz4L
🔗GitHub: https://t.co/b6DqGKDelf
📄Paper: https://t.co/1a6repNrnt