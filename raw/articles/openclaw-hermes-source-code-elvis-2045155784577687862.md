---
updated: 2026-04-19
title: "i spent 9 hours studying the source code of openclaw and hermes side by side.\n\nhere's everything i learned.\n\npost 1/n: s"
author: "Elvis"
username: "@elvissun"
created: "2026-04-17"
source: "https://x.com/elvissun/status/2045155784577687862"
type: "xarticle"
tags: []
---


i spent 9 hours studying the source code of openclaw and hermes side by side.

here's everything i learned.

post 1/n: skills

@NousResearch hermes first. the hook is that the agent self-improves by writing its own skills.

the system prompt has a nudge baked in: every N tool calls, consider saving a skill. after task completion, a background review scans for skill-worthy patterns. before context compression kicks in, durable knowledge gets flushed to disk. the prompt is blunt - if an existing skill covers this, patch it in place. only create new if nothing matches.

and it works. i watched it create a extract-social-testimonial skill on its own and its proven useful. I had a /save command in OpenClaw that'll do this when prompted, but this is the kind of skill I never would have thought to create. first time seeing this worked like magic.

---

the other half of why hermes feels productive out of the box: the opinionated bundled library is massive.

i counted 123 SKILL.md files shipped on my install before hermes wrote a single one of its own. github PR workflows, obsidian, google workspace, linear, notion, typefully, perplexity, deep research, minecraft modpack server (lol) - huge surface area of "somebody already figured this out for you."

this is what opinionated actually means. you're not getting a blank agent and a framework, you're getting an agent that already knows how to do 100+ things on day one and a self-improvement loop that learns more as you go. 

strong defaults as a product. when the opinions are good, the leverage is massive. (think tailwind or rails)

and they literally just doubled down on this with a "tool gateway" yesterday - one subscription, 300+ models, plus first-party web scraping, browser automation, image gen, cloud terminal, text-to-speech. one accounts. 

hermes' direction is unambiguous: more batteries, fewer decisions the user has to make. this is the rails move - own the whole stack so the default path is the happy path.

---

so here's the thing I don't see anyone talking about yet with hermes: self-authored skills have a skill explosion problem.

real example from my own ~/.hermes/skills/ directory. the agent wanted to read an image from my desktop. Tried browser read and vision skill, nothing worked. so it wrote a third skill read-local-image skill lol. these are 3 skills all adjacent to "image + local filesystem + model can see it." the skill grows and become mutually non-exclusive very quickly.

this is the long-tail failure mode. the agent is great at spotting "i should bottle this up." it's less great at spotting "I already bottled this up three folders over." you end up with a corpus that grows faster than it consolidates.

net impact over time: you accumulate a lot of skills. some brilliant, some redundant, some that overlap three other skills nobody remembers exist.

i'm sure @Teknium already knows this and it's just a product prioritization decision right now. (this is my favorite part, more on this later) they'll prob solve this soon as more users turn into power users and their skills accumulate - something like consolidation pass with invocation metrics + stronger dedupe on skill creation.

---

@openclaw doesn't have this problem. partly because it doesn't auto-generate skills at the same rate, so there's less to dedupe in the first place. and partly because it has more mechanisms to solve it structurally.

what it does differently:

openclaw takes the opposite stance on skills. from their VISION.md: "we still ship some bundled skills for baseline UX. new skills should be published to ClawHub first, not added to core by default. core skill additions should be rare and require a strong product or security reason." anti-bloat by policy. cleaner, but the authoring is on you.

so their skills are explicit artifacts with governance at every layer. five sources ranked by precedence (workspace > user global > managed > bundled > extra), so you always know what is loaded. when something breaks at 3am, you can trace it in one grep instead of guessing which skill the agent triggered.

discovery is bounded at multiple levels - byte caps, candidate caps, symlink rejection, verified file opens. eligibility checks separate from discovery, different agents can see different subsets - your coding agent doesn't need your email skills in its context.

smaller surface area = cheaper runs, sharper responses, less drift on long tasks.

and the governance piece is explicit product policy: bundled skills are baseline only, new skills go to clawhub first, core additions should be rare. the corpus doesn't rot because nothing gets added without user intention - every skill has to earn its spot.

this is what primitives actually means. you're not getting defaults, you're getting guarantees. openclaw does exactly what you told it to do, nothing more, nothing less. boring in the best way. when you're shipping this in production or running it inside a team, boring is the whole product. (think linux, kubernetes)

---

and here's the practical thing that shipped results for me on @openclaw: i combined the TOOLS.md  with vercel's AGENTS.md optimization pattern. tool activation correctness is better on openclaw than hermes for me on tasks where the agent has to pick the right cli/api from ~50 options.

vercel has a nice writeup on this, send it to your agents: https://t.co/IRQZ2kYLwU

tldr is explicit > implicit. the agent doesn't have to decide "is this skill-worthy enough to load," because the routing rules are already in the system prompt.

---

so my current read:

both harnesses will do everything you want. pick either, you'll be fine. but if you're picking fresh:

> getting started quickly → hermes. opinionated defaults mean you're productive on day one and stays productive with little maintenance overhead.

> users who want 100% control→ openclaw. legibility and scope control matter more than self-improvement does.

> builders → it depends.. and i'm here. some things openclaw does better, some things hermes does better. honest move is to use one daily and steal patterns from the other.

---

but the more interesting question isn't which to pick - it's what you can learn from each:

@steipete gave the world a new layer in the stack and put a claw in everyone's hand. that's foundational work. you don't even need to use openclaw to benefit from openclaw - the patterns will show up in everything downstream for years. (plus the way he does agentic engineering should really be studied by everyone writing software right now)

@NousResearch is giving a masterclass in product positioning live right now. and this is the part that deserves its own post, but briefly:

openclaw had the audience. the mindshare, the github stars, the "it's basically the standard now" energy.

look at what happened to everyone who tried to fight that fight head-on. nanoclaw. nullclaw, picoclaw, zeroclaw. i can name ten more. all of them trying to out-openclaw openclaw - smaller, lighter, more minimal, more composable, better governance, whatever. none of them got hermes's traction.

because when you compete with a category-definer by being a cheaper/cleaner version of them, the category-definer just wins by default. you're playing their game on their board.

hermes made their own game. self-authoring. bundled-by-default. maximalist on purpose. the tool gateway as lock-in. every launch reinforces the same thesis: we are not the minimalist primitives company, we are the batteries-included agent-as-a-product company.

this is textbook product positioning. every single release - and the way they release it - should be studied. 

that's the founder lesson. the user lesson is simpler.

pick either. learn from both. then go make something useful.
