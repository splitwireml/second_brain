---
source_url: https://x.com/elder_plinius/status/2073579120135664102
ingested: 2026-07-06
sha256: 7dab7a1f3ab2f04199ccc01f6b2e86c5b644fa215449fbfd67643a25fa5309cb
---

---
title: "⚡ INTRODUCING: T3MP3ST!!! ⚡\n\nAUTONOMOUS HACKBOT STRIKE FORCE 🌩️ BRING THE STORM 🌩️\n\nyour favorite coding agent is now a "
source: "x-bookmarks"
tweet_id: "2073579120135664102"
tweet_url: "https://x.com/elder_plinius/status/2073579120135664102"
author_name: "Pliny the Liberator 🐉󠅫󠄼󠄿󠅆󠄵󠄐󠅀󠄼󠄹󠄾󠅉󠅭"
author_handle: "@elder_plinius"
tweet_date: "Sun Jul 05 01:26:02 +0000 2026"
bookmark_date: "2026-07-05"
content_type: "x_article"
character_count: 4440
retweet_count: 344
like_count: 3433
external_urls:
  - "https://t.co/k0SXmPAFaD"
export_error: "bird read --json failed for https://x.com/elder_plinius/status/2073579120135664102"
---

> Export note: bird read --json failed for https://x.com/elder_plinius/status/2073579120135664102

⚡ INTRODUCING: T3MP3ST!!! ⚡

AUTONOMOUS HACKBOT STRIKE FORCE 🌩️ BRING THE STORM 🌩️

your favorite coding agent is now a full-stack red team 🫡⚔️

https://t.co/k0SXmPAFaD

that AI agent already humming in your terminal? well now it has FANGS. strap a full offensive-security harness onto the agents you already pay for — Claude Code, Codex, Hermes, etc. — point it at an authorized target, and in a few clicks you're watching it hunt real vulns autonomously!

T3MP3ST is a harness of harnesses, with prompting that unlocks offensive-cyber workflows + a full arsenal of exploit tooling that'd make any seasoned hacker smirk. simple, yet powerful. 🦾

support for:
🕸️ web apps, APIs, OWASP Top 10
🔌 network recon + fingerprinting (live nmap/DNS/HTTP); lateral + privesc experimental
📂 source code audits, white-box vuln hunting
🚩 CTFs, wargames, challenge ranges
💰 smart contracts / DeFi / Solidity (reproduction — Damn Vulnerable DeFi, not novel discovery)
🤖 embedded, IoT, OT/SCADA, robotics OSS
… and more in development!

now let's talk numbers 👇

📊 XBEN — XBOW's own 104-challenge suite:
• black-box: 90.1% pass@1 from the single-agent exploit loop (worst single sweep 91/104 = 87.5%) — clearing XBOW's past self-reported 85% on their own suite. gpt-5.5.
• white-box (source staged, reported separately): 98.7% pass@1, worst single sweep 102/104 = 98.1%. 🎯
every solved flag graded reported-vs-expected against the challenge's own committed flag oracle — `verify-claims` recomputes the pass/fail from committed artifacts. looks like we need new benchmarks 😏

🧩 Cybench — the 40-task academic bench (Opus 4.8, hints + writeups stripped): 23/40 = 58% single-run, hint-free pass@1 — real exploits (format-string pwn, eval-jail escapes, crypto oracles), every flag graded vs a committed oracle. (Anthropic reports 76.5% pass@10)

🕳️ CVE-Zero — we pointed it COLD at real CVEs disclosed in 2026, AFTER the model's training cutoff:
10 unseen 2026 CVEs across 7 languages — prompts never tuned on them. a single agent pinned 8/10 to exact file/line/CWE (stable under re-scoring); the full pack surfaced all 10.
memorization AND overfitting, both off the table — it's finding real vulns whose disclosures landed AFTER the model's training cutoff. (n=10, reported honest & directional)

🧠 the architecture: either run as a SINGLE agent (already the benchmarked, incredibly-capable path) — or pack-hunt with dozens of agents running on 8 specialist operator classes keyed to Cyber Kill Chain + MITRE ATT&CK phases: recon → scan → exploit → lateral → exfil → persistence → C2 → report. 

⚓️an Op Admiral plans the whole op from a plain-english target. flip on coordination (experimental) and the operators share a blackboard — a tool-verified finding spawns the next move. full swarm or solo one operator, your call. the admiral can also update the prompts, tools, and configs of the other agents on the fly, and T3MP3ST gets stronger the more memories you build!

🧰 the Arsenal is comprehensive — nmap / nuclei / semgrep / ffuf / gobuster + more. 35 wired by default (the clean bench runs bash-only for a comparable number), 83 with the opt-in full arsenal (T3MP3ST_FULL_ARSENAL), and the spicy post-ex drivers (metasploit, hydra) gated behind human approval. exposed via CLI + HTTP API; recon (security_recon) is also live over MCP so your agent invokes it natively. 🔗

🛰️ where this goes: a self-improving swarm of specialist operators wielding a full Kali+ arsenal, learning which loadouts + configs are the most efficient tactics available, WITH a held-out train/test split baked in so it can never fool itself on its own eval. built in the open, one re-derivable number at a time.

🚧 this is v1, and parts are still under active development. chunks of the arsenal, the coordinated swarm, and some ranges are still being wired up. it's built in the open, and the receipts tell you exactly what's live vs what's roadmap.

offensive security shouldn't be pay-to-play. T3MP3ST puts a red team in the hands of anyone with a coding agent.

what's the first target you're feeding it? 👇

⚠️ DISCLAIMER: FOR AUTHORIZED USE ONLY. point it only at systems you own or have explicit written permission to test. unauthorized access can be a crime, and that call is yours alone. shipped as-is under AGPL-3.0: no warranty, no liability, zero endorsement of misuse. get permission. stay in scope.

open source. AGPL-3.0. 100% free.

FORTES FORTUNA IUVAT 🌩️

gg 🫡
