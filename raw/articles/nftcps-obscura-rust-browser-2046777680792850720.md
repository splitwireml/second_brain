---
title: "兄弟们，Headless Chrome 该退休了！有人用 Rust 搓了个专给 AI Agent 和爬虫用的无头浏览器引擎——Obscura"
author: "鸟哥 | 蓝鸟会🕊️"
username: "@NFTCPS"
created: "2026-04-22"
source: "https://x.com/NFTCPS/status/2046777680792850720"
type: thread
tags: [browser-automation, rust, ai-agents, scraping, tools]
---

兄弟们，Headless Chrome 该退休了！

有人用 Rust 搓了个专给 AI Agent 和爬虫用的无头浏览器引擎——Obscura，性能直接把 Chrome 按地上摩擦：

① 内存只吃 30MB（Chrome 吃你几个G）
② 启动只要 85ms，快得离谱
③ 整包才 70MB，Chrome 装完硬盘哭了

还支持 CDP 协议，Puppeteer、Playwright 无缝接，你原来的脚本不用改一行。

最绝的是 stealth 模式——随机化指纹、主动拦截追踪器，爬站被封概率直接拉低一个档次。

CLI 一条命令搞定单页抓取，想并行跑多个 URL 也行，起个 WebSocket 服务给自动化脚本挂着用也没问题。

Rust 写的性能怪物，爬虫党和 AI Agent 开发者必须看一眼。

🔗 https://github.com/obscura-browser/obscura
