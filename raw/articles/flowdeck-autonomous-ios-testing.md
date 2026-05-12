---
updated: 2026-04-17
title: Autonomous iOS UI Testing with Claude Code — FlowDeck
source: https://flowdeck.studio/blog/2026/04/08/autonomous-ios-ui-testing-with-claude-code/
type: article
author: FlowDeck
username: FlowDeck
---

# Autonomous iOS UI Testing with Claude Code — FlowDeck

> **Source:** https://flowdeck.studio/blog/2026/04/08/autonomous-ios-ui-testing-with-claude-code/
> **Author:** FlowDeck Studio
> **Date:** 2026-04-08
> **Topic:** Claude Code + iOS Simulator automation via FlowDeck CLI

## The Problem

Claude Code can write XCTest cases and reason about UI logic, but cannot:
- Navigate screens
- Verify visual state
- Tap buttons by label
- See what actually happened on screen

Native iOS testing is painful to automate:
- XCUITest requires test code mirroring production code, breaks on UI changes
- Playwright doesn't reach inside iOS simulator
- Raw `xcrun simctl` gives agents no visibility into what's on screen

## The Solution: FlowDeck

FlowDeck gives Claude Code direct access to the iOS simulator via CLI commands with structured JSON output.

### Installation

```bash
curl -sSL https://flowdeck.studio/install.sh | sh
flowdeck -i
# Press A -> Install Skills -> Claude Code -> Global
```

### Key Commands

```bash
flowdeck ui simulator screen --json          # screenshot + accessibility tree
flowdeck ui simulator tap "Add City"         # tap by label
flowdeck ui simulator type "London"          # type into focused field
flowdeck ui simulator swipe up               # scroll
flowdeck ui simulator assert visible "London"  # verify element exists
flowdeck logs [app-id]                       # runtime output, live
```

### How It Works

Claude Code reads the **accessibility tree** to find elements by label, not coordinates. This means:
- Survives UI changes
- Works across screen sizes
- Agent sees, acts, verifies, repeats

## Autonomous Testing Demo

**Test subject:** Weather app (multiple cities, forecasts, add/remove locations)

**Prompt:**
```
Act as a QA engineer and test this application using FlowDeck UI
1. Review the design and layout of every single screen
2. Test all interactions and features
3. Test UI stability, accuracy and reliability
4. Identify potential edge cases like malformed input, or misuse.
5. Fix every bug found
6. Create a summary report with results.
```

**Results (16 minutes, autonomous):**
1. Screen review — every screen captured, reviewed for layout issues
2. Feature testing — add city, remove city, check forecast, switch locations (end-to-end taps)
3. Bug found and fixed — city removal index bug, traced to source, patched, verified
4. Edge cases — malformed input, rapid additions/removals, back-to-back switches
5. UX observation — Celsius metric display flagged (not forced as fix)
6. Summary report — full rundown delivered

## Comparison: FlowDeck vs XCUITest

| Aspect | XCUITest | FlowDeck + Claude Code |
|--------|----------|------------------------|
| Test definition | Code mirroring production | Plain language prompt |
| UI change resilience | Breaks on every change | Prompt stays the same |
| Maintenance | Large suite = job in itself | Zero maintenance |
| Scope | Critical path coverage | Exploratory pass |
| Time investment | Hours to write/maintain | One prompt, 16 minutes |

**Not a replacement** for unit tests or critical path XCUITest. It's the exploratory pass that never happens because nobody has time.

## Pricing

## See Also

- [[autonomous-ios-ui-testing]] — iOS UI testing patterns and tools
- [[research-code-agent-cli-automation]] — Claude Code CLI for iOS automation


Free trial → $59/yr after trial.