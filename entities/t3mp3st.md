---
title: T3MP3ST
created: 2026-07-06
updated: 2026-07-06
type: entity
tags: [product, open-source, ai-agent, security, tools]
sources: [raw/articles/xarticle-introducing-t3mp3st-autonomous-hackbot-strike-forc-2073579120135664102.md]
---

# T3MP3ST

T3MP3ST is an open-source offensive-security harness introduced by [[elder-plinius]] as an "autonomous hackbot strike force" for coding agents. The project wraps agents such as [[claude-code]], [[codex]], and [[hermes-agent]] with security prompts, exploit-oriented workflows, and a Kali-style tool arsenal so an operator can point an agent at an authorized target and have it perform reconnaissance, scanning, exploitation attempts, source audits, CTF work, or reporting.

The launch positions T3MP3ST as both a single-agent exploit loop and an experimental [[autonomous-red-team-agent-swarms]] system. Its advertised arsenal includes nmap, nuclei, semgrep, ffuf, gobuster, a CLI and HTTP API, MCP-exposed recon, and gated higher-risk tools such as metasploit and hydra. The source repeatedly frames use as authorized-only testing, not unsanctioned intrusion.

## Reported benchmarks

The launch post reports author-claimed benchmark results rather than independently verified performance: 90.1% pass@1 on XBOW's 104-challenge XBEN black-box suite, 98.7% pass@1 on a staged white-box version, 23/40 on Cybench without hints or writeups, and successful localization of 2026 CVE issues after the model training cutoff. Treat these as directional claims until reproduced outside the project artifacts.

## Related

- [[elder-plinius]]
- [[autonomous-red-team-agent-swarms]]
- [[multi-agent-orchestration]]
- [[agent-teams]]
