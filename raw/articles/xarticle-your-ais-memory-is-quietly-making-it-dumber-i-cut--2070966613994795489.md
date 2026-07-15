---
source_url: https://x.com/mvanhorn/status/2070966613994795489
ingested: 2026-06-29
sha256: 71079572ff87f4d08e40c4ec8a2a762afa8dfaaad9f41b2b84e22d25df79c825
---

---
title: "Your AI's Memory Is Quietly Making It Dumber (I Cut Mine to 6 Files)"
source: "x-bookmarks"
tweet_id: "2070966613994795489"
tweet_url: "https://x.com/mvanhorn/status/2070966613994795489"
author_name: "Matt Van Horn"
author_handle: "@mvanhorn"
tweet_date: "Sat Jun 27 20:24:52 +0000 2026"
bookmark_date: "2026-06-27"
content_type: "x_article"
character_count: 18665
retweet_count: 30
like_count: 348
external_urls:
  - "https://github.com/raiyanyahya/recall)"
  - "https://www.tiktok.com/@aidecipher/video/7653690354025106701)"
  - "https://www.youtube.com/watch?v=rFWxRZ5D-lM)"
  - "https://www.tiktok.com/@goldst.ai/video/7652770990308560158)"
  - "https://github.com/EveryInc/compound-engineering-plugin)"
  - "https://printingpress.dev)"
  - "https://code.claude.com/docs/en/memory)"
  - "https://agents.md)"
  - "https://www.tiktok.com/@agenticamit/video/7655796379117243649)"
  - "https://github.com/garrytan/gbrain)"
  - "https://github.com/supermemoryai/supermemory)"
  - "https://github.com/mem0ai/mem0)"
  - "https://github.com/letta-ai/letta)"
  - "https://github.com/getzep/zep)"
  - "https://github.com/topoteretes/cognee)"
---

# Your AI's Memory Is Quietly Making It Dumber (I Cut Mine to 6 Files)

Your AI's Memory Is Quietly Making It Dumber (I Cut Mine to 6 Files)

I gave a talk last week and said it out loud: delete that memory, agent. When your agent learns a lesson, do not park it in some private memory file. Make a pull request that improves the skill, so the fix helps you and everyone else who uses that skill. Someone messaged me afterward that there was probably a banger piece of content buried in the idea. So here it is.

My agent's memory had quietly grown to 218 files. A 46-kilobyte index that was so big the harness had started silently dropping the back half of it every single session. I cut it to 6 files, moved those into my CLAUDE.md, and turned auto-memory off. Then I audited the CLAUDE.md they landed in. This is the whole system, because your agent's memory and your CLAUDE.md are the same problem wearing two hats: standing instructions that load every session and rot the moment you stop looking.

Before I cleaned any of this up, I ran [last30days](https://x.com/slashlast30days) on the whole topic, ten sweeps across Reddit, X, YouTube, TikTok, and Hacker News. The first thing the research told me is that I was about to argue with the entire internet.

## The loud advice is "build a memory system." I went the other way.

Open any feed right now and the memory pitch is everywhere:

> 90% of people coding with AI lose hours a day to one problem nobody talks about. The agent has no memory. Every session starts from zero. It forgets your codebase, your decisions, your context. The people shipping fastest fixed this for $0.

- [@Nyra_nx](https://x.com/Nyra_nx/status/2070879439945159150), X, 11 likes

There is a whole cottage industry forming around this. "[Show HN: Recall, local project memory for Claude Code](https://github.com/raiyanyahya/recall)" hit 136 points and 86 comments on Hacker News the same week. The instinct is understandable: the agent forgets, so bolt on a bigger brain.

Here is where I want to be precise, because the instinct behind that is correct. A stateless agent that starts cold every morning is a real problem. The mistake is not wanting memory. The mistake is answering it by loading more into every session instead of letting the agent query a store on demand. Hold that distinction, I come back to it. For the always-loaded layer this article starts with, more is not the fix, and one creator said why better than I have:

> Hard limits on memory force an AI agent to distill what actually matters. Enforced scarcity is the mechanism that creates focused, useful long-term memory instead of bloated, useless context.

- [aidecipher on TikTok](https://www.tiktok.com/@aidecipher/video/7653690354025106701), 8 likes

That is the whole philosophy. A memory with no budget is not a brain, it is a landfill.

## Why a fat memory makes your agent dumber

This is not a vibe, it is mechanical. Your CLAUDE.md and your memory get injected into the context window at the start of every session, and a context window that is filling up is a context window that performs worse. The most-watched explainer I found put a real number on the rule:

> The default behavior of Claude Code is, when you start a session, it injects the full claude.md, and that is why we want to keep the claude.md ideally under 200 lines.

- [Simon Scrapes on YouTube](https://www.youtube.com/watch?v=rFWxRZ5D-lM), 870 likes

A [472-like TikTok](https://www.tiktok.com/@goldst.ai/video/7652770990308560158) said the consequence in plainer language: the longer you let Claude's context clog up, the dumber it gets. My memory index was 46 kilobytes. It was so far past the limit that the harness was loading only part of it and dropping the rest, which means the file had stopped steering anything and become a work journal that happened to cost tokens. The bloat was not theoretical. Half of it already was not loading.

HACKS

Your memory and CLAUDE.md inject every session. Past a point, more text means worse adherence, not more knowledge. Keep each file under 200 lines.

## The audit: it was not 90% junk, it was 90% misfiled

I had three readers go through all 218 files line by line and bucket each one. The split surprised me:

- About 14% was true trash: records of shipped PRs and finished videos, lessons already encoded in tooling. Git history already has all of it.

- About 39% was durable, useful lessons, but each one was tied to exactly one skill. A fix for a specific tool, sitting in a global memory that the tool never reads.

- The rest was genuinely cross-cutting steering, plus a pile of in-flight project trackers that would rot the day the work shipped.

That middle bucket is the entire point. The question was never "what percentage do I delete." It was "where should each lesson live." A lesson about one skill belongs inside that skill, as a PR, where it changes behavior for everyone and gets version-controlled like the code it is. Parked in memory, it is private tribal knowledge that silently goes stale. This is the skills-over-memory idea in one sentence: stop journaling lessons, start shipping them into the skill.

HACKS

Bucket every memory entry: trash (git has it), skill-tied (PR it into the skill), or genuinely cross-cutting (keep). Most "memory" is a misfiled skill PR.

## Where the lessons actually go: write your own skills

So if a skill-tied lesson does not belong in memory, where does it go? Into a skill. This is the half of skills-over-memory that matters more than the deleting, and it is the single highest-leverage habit I have. I wrote up my whole workflow in a piece that did [over a million views](https://x.com/mvanhorn/status/2061877533885473181), and the hack people took away most was this one: write your own skills.

The rule is simple. Anything I do more than twice becomes a skill, a reusable command my agents can run forever. A lesson the agent learned the hard way does not get journaled into memory where it rots. It gets written into the skill, as a PR, so the next run already knows it and so does everyone else who uses that skill. That is the same move as shipping a memory entry into the tool it belongs to, just made permanent.

You do not write them from scratch. The trick that unlocked this for me is to point the agent at a skill that already works and have it copy the shape. Literally: "look at the [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) skill and help me make one like this for whatever I am automating." It reads a great example, learns the structure, and scaffolds yours. I have built a pile of skills this way, and most of my open-source work now is skills and the tools around them. last30days and [Printing Press](https://printingpress.dev) both started as skills I wanted for myself.

That is the compounding part. Write the skill once and every session after is faster, and the lesson lives somewhere version-controlled instead of somewhere that silently goes stale. Deleting memory only works because the lessons have a better home to go to.

HACKS

Anything you do more than twice, make a skill. Do not write from scratch: point the agent at a skill that already works and say "make one like this for X." A lesson belongs in the skill as a PR, not in memory.

## Back up fearlessly, then cut to the bone

The only way to delete aggressively is to make deletion reversible first. I copied the entire memory store to an archive directory and a tarball, 222 files, sitting outside the auto-loaded memory folder so it never loads or gets recalled but is always recoverable. Once deleting cost nothing, the real exercise got easy: nominate the handful of files that genuinely steer behavior across many skills, encode who I am, or are scar tissue from real damage. Everything that failed that bar was presumed garbage.

I landed on 6 survivors. The bar each one cleared:

- The safety rail I learned the hard way: never quit a live environment I am working in. Quitting Chrome once to read a token nuked 12,552 cookies and logged me out of everything mid-work. I extended it during this very cleanup to cover cmux, where I actually write code: warn me, get an okay, quit only if there is no other way. That one has no skill to live in and I never want to rediscover it.

- The rules that govern everything the agent writes: a formatting rule (no em dashes, no en dashes, no bold) and a hard secrecy boundary about what never goes into public content.

- The stable facts I hit constantly: the canonical paths to the few repos I touch every day.

That is it. Six files. Everything else, all 212 of them, got archived. My memory index went from 46 kilobytes to about 1.4. For the first time in months, the whole thing actually loads.

HACKS

Archive the full store first (outside the loaded dir), so deletion is fearless. Then keep only what steers across skills, defines you, or is scar tissue. Archive, do not hoard.

## The auto-memory trap, and the bridge to CLAUDE.md

Here is the catch that almost broke the whole plan. I wanted to turn auto-memory off so the store could never silently regrow into another 200-file swamp. I am not alone in wanting this:

> I too disable Claude's auto memory by setting the env var CLAUDE_CODE_DISABLE_AUTO_MEMORY=1. It is too easy to be out of date and steers the agents wrong.

- [@trevin](https://x.com/trevin), X

But auto-memory is a single switch for reading AND writing the memory folder. Flip it off and your 6 lovingly-curated survivors stop loading too. The fix is the bridge between the two halves of this article: move the survivors out of memory and into CLAUDE.md, which always loads and never auto-prunes and never rots from background writes. Then disable auto-memory entirely. The handful of real steering facts live in always-on instructions, and the lossy feature that grew the swamp is off for good. (If you only want to find the toggle: open Claude Code in the terminal, run `/memory`, and switch off Auto-memory. The in-app settings do not do it.)

So the six facts are now a small block at the top of my `~/.claude/CLAUDE.md`. Which raised the obvious next question: is that file any good?

## Auditing the file the survivors moved into

I assumed my CLAUDE.md was a mess too. It was the opposite. The whole always-on surface is short by design, and the audit turned into a quality pass, not a prune. Here is what actually holds up, grounded in the same research and in Anthropic's own docs.

Keep the global file short, because you pay for every line on every session. Anthropic's [memory docs](https://code.claude.com/docs/en/memory) say to keep each CLAUDE.md under 200 lines, because "longer files consume more context and reduce adherence." My global file is 19 lines. The bluntest take in 30 days of research said the same thing about the failure mode:

> Your CLAUDE.md is probably hurting your Claude Code more than helping it. The more instructions you give Claude, the more it ignores them. Claude's system prompt already comes with around 50 built-in instructions. Every line you add pushes it further over the limit.

- [@Vishaldej](https://x.com/Vishaldej/status/2070837214276390955), X

HACKS

Keep `~/.claude/CLAUDE.md` under 200 lines. Mine is 19. It holds only what is true in every repo.

## Stop using CLAUDE.md like a trash can either

The exact mistake I made in memory is the one people make in CLAUDE.md. The sharpest line on it:

> STOP USING CLAUDE.md LIKE A TRASH CAN. The mistake: people dump everything in. Tech stack. Generic coding rules. Obvious conventions. Giant workflow docs. Stuff the model can infer from the repo.

- [@s1rozha_](https://x.com/s1rozha_/status/2070893085177909521), X, 18 likes

When I read my older project files against that list, half of what was in them was framework names the agent can read in `package.json`, "write clean code" filler, conventions any model infers in seconds. None of it changes a decision. All of it dilutes the lines that do. The cut list is always longer than the keep list.

HACKS

Delete anything the model can infer from the repo: tech stack, obvious conventions, generic rules. If a line does not change a decision, it is trash.

## One instruction file for every agent: import AGENTS.md

The pattern I had right by accident, and now do on purpose: 48 of my 68 project CLAUDE.md files contain exactly one line.

```
@AGENTS.md
```

I run most of my builds through Codex, not just Claude Code. Codex reads [AGENTS.md](https://agents.md). Claude Code reads CLAUDE.md. I refuse to maintain two files that drift apart by Tuesday, so the real conventions live once in AGENTS.md and CLAUDE.md just imports it.

> Claude reads CLAUDE.md. Codex reads AGENTS.md, the cross-tool standard that Cursor and others also read. Two terminal agents, two files, same job.

- [@WenchangYue](https://x.com/WenchangYue/status/2068545674002747542), X

A 32K-view explainer named the cost of getting it wrong: every agent ships its own rule format, so your repo becomes a drawer of instruction files that does not translate from one agent to the next. One [post counted 60,000 repos](https://x.com/LumenSignifier/status/2070922609584124147) now carrying an AGENTS.md, read by Claude Code, Codex, Cursor, Aider, Devin, Copilot, Gemini CLI, Windsurf, and Amazon Q. Claude Code does not read AGENTS.md on its own, but a CLAUDE.md can import it with an `@` line, so `@AGENTS.md` pulls the whole thing in. Anthropic's docs recommend exactly this. A symlink does the same job: `ln -s AGENTS.md CLAUDE.md`.

HACKS

Project CLAUDE.md is one line: `@AGENTS.md`. Write conventions once, every agent reads them. Or symlink: `ln -s AGENTS.md CLAUDE.md`.

## Every surviving line should be gold-standard

Once the trash is gone, the test for what stays is whether it earns its slot:

> Every line in AGENTS.md should be gold-standard. Period.

- [@cxprakash](https://x.com/cxprakash/status/2070056497548304649), X

His example was a single rule that killed a recurring failure: "close all servers you run at the end of a session," added once to stop port-locking forever. That is the shape. My printing-press AGENTS.md does not say "fix bugs carefully," it says where a fix belongs and tells the agent to claim an issue before starting so two agents do not collide. Those are decisions the agent would otherwise get wrong, written down once. It is the same bar I used to pick the 6 memory survivors: does this line change what happens next? If not, it is gone.

HACKS

Every line earns its slot or gets cut. "Close servers at end of session" beats "write clean code." Encode the decisions the agent keeps getting wrong.

## If you still want recall, that is a different kind of memory

Now the distinction I told you to hold. Turning off auto-memory and pruning CLAUDE.md kills one kind of memory: the kind pushed into context every session whether you need it or not. It does not mean your agent goes amnesiac. There are two kinds of memory and people constantly conflate them. Push memory is loaded for you, CLAUDE.md and native auto-memory, injected at session start, and its failure mode is the whole subject of this article. Pull memory is the opposite: it sits in a store and the agent retrieves only the slice it needs, when it needs it, by asking. One creator drew the line cleanly:

> AI agents have the memory of a goldfish, and the obvious fix, giving it a bigger memory, quietly makes things worse. The problem was never size. It is the context window itself. Cram in too much history and the oldest facts just slide out the other side.

- [agenticamit on TikTok](https://www.tiktok.com/@agenticamit/video/7655796379117243649), 42 likes

The fix is not a bigger brain you carry everywhere, it is a brain you can query. That is what the dedicated memory-layer tools are, and they are not competitors to deleting auto-memory, they are where recall goes after you delete it. A quick map of the field, all retrieved on demand rather than force-loaded:

- [gbrain](https://github.com/garrytan/gbrain), from Garry Tan, is a markdown-and-git knowledge base with vector, keyword, and knowledge-graph retrieval and a synthesis layer on top, exposed as a CLI and an MCP server.

- [supermemory](https://github.com/supermemoryai/supermemory) is a memory API that extracts facts, reconciles contradictions, and expires stale ones, with connectors into Drive, Gmail, Notion, and GitHub, available as an SDK, an MCP server, and a local binary.

- [mem0](https://github.com/mem0ai/mem0), [Letta](https://github.com/letta-ai/letta), [Zep](https://github.com/getzep/zep), and [Cognee](https://github.com/topoteretes/cognee) are the rest of the field people benchmark together, each a self-hostable retrieval layer with its own take on facts versus documents versus graphs.

Where each fits depends on the surface, and that is a real decision, not a default. I run gbrain inside Hermes, and not in Claude Code or Codex, because on-demand recall earns its place in some workflows and not others. The point is not which tool you pick. The point is that "delete your memory" and "give your agent a real memory" stop being opposites the moment you separate push from pull.

One caution, and it is just this article's thesis applied one layer down: a pull store is not a license to hoard. Retrieval memory still goes stale, still fills with things that mattered once, still rewards pruning. Move recall to a queryable brain, then keep that brain as honest as you keep CLAUDE.md. Enforced scarcity does not stop mattering because the storage got bigger.

## The throughline

Memory and CLAUDE.md are the same fight. Both load every session, both cost context, both quietly fill with stuff that made sense once and steers you wrong now. The discipline is identical: keep it short, keep only what changes a decision, push skill-specific lessons into the skill where they help everyone, and prune it like code. CLAUDE.md is the most expensive real estate your agent reads, because it reads it every single time. Pay for signal, not square footage.

If you want to run this yourself, paste this article into your agent and tell it to do two audits. One: grade your memory store, flag every entry that is a finished-work record (delete), a single-skill lesson (PR it into the skill), or genuinely cross-cutting (keep), and back the whole thing up before touching anything. Two: grade your CLAUDE.md and AGENTS.md, flag any file over 200 lines, anything the model could infer from the repo, and any project file that duplicates instructions instead of importing them. I assumed both of mine were a disaster. The memory was. The CLAUDE.md was already lean. You will not know which is which until you look.
