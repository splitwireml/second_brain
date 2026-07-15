---
source_url: https://x.com/eyad_khrais/status/2074519552277336571
ingested: 2026-07-09
sha256: df75ddf140727215bfef2a52ca7433cbe86cd88f953fe70b8aa015e333e9e178
---

---
title: "How to become an applied AI engineer"
source: "x-bookmarks"
tweet_id: "2074519552277336571"
tweet_url: "https://x.com/eyad_khrais/status/2074519552277336571"
author_name: "Eyad"
author_handle: "@eyad_khrais"
tweet_date: "Tue Jul 07 15:42:58 +0000 2026"
bookmark_date: "2026-07-07"
content_type: "x_article"
character_count: 13103
retweet_count: 53
like_count: 641
external_urls:
  - "http://varickagents.com/)"
  - "https://github.com/anthropics/courses/blob/master/prompt_evaluations/README.md)"
  - "https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete)"
  - "https://hamel.dev/blog/posts/evals-faq/)"
  - "https://www.youtube.com/watch?v=esY99nYXxR4)"
  - "https://openai.github.io/openai-agents-python/context/)"
  - "https://medium.com/@hungry.soul/context-management-a-practical-guide-for-agentic-ai-74562a33b2a5)"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)"
  - "http://varickagents.com/)"
---

# How to become an applied AI engineer

How to become an applied AI engineer

I wrote this as the guide I would have wanted before making the transition into Applied AI Engineering.

The role broadly overlaps with traditional software engineering, but it adds a few important concepts that most software engineers have to learn as they make the transition. I’d suggest you use this as an outline of the core topics you need to understand, and then follow the linked resources throughout the article when you want to go deeper.

By the end, you should have a much clearer understanding of what Applied AI Engineering is, what the job actually requires, and how it extends beyond traditional software engineering.

If you’re interested in working on some of the most interesting problems in Applied AI with a very talented engineering team, we’re always hiring. Apply on our website at [varickagents.com](http://varickagents.com/) or refer a candidate for a $20k referral bonus.

That said, the best way to understand Applied AI Engineering is to start with the shift in how you think about building software.

Software engineering vs AI engineering

The biggest difference between being a SWE and an AI engineer is that traditional software engineering trains you to think deterministically, while applied AI forces you to think probabilistically.

In normal software, you write the logic, get it to run, and when something breaks you can usually trace it – a structured input deterministically gives you a structured output.

Applied AI doesn't work like that. You're building around a non-deterministic API call to intelligence, which means the same input can come back different every time. Because of this, the job stops being just building the software, and instead becomes measuring whether the system actually behaves the way it should.

The way we do that is through evals, so I’ll break down how to build an evaluation suite that ensures the agent you develop isn’t making mistakes. I’ve come to learn that this is one of the most important skills of an applied AI developer, given the non-deterministic nature of the work that we do.

The next part of the article covers developing each part of an AI agent (except for the model itself, of course), because you can call an API to a model but you need to build everything else yourself. This is called harness engineering.

And lastly, I’ll cover how to go from one agent in production to multiple – and why it’s a distributed systems problem. If you can make it to the end of this article, there’s no reason you shouldn’t be able to make the transition to becoming an Applied AI engineer.

Evals

An applied AI engineer turns uncertainty into measured confidence using evals. In traditional software development, you trust the system because you wrote the logic and tested the code. In applied AI, you can’t trust the system that way because the model can behave differently across runs. So the AI engineer has to build a measurement layer around the agent.

An eval is the process of giving an agent a task, letting it run, and grading what it did. The goal is to prove two things: the agent completed the work correctly, and the agent stayed within the boundaries it was given.

The first step is to grade the outcome. This is the easiest step of the eval process. For an invoice agent, the ones I usually work on, that means ensuring the invoice lands in the right place, or the duplicate is flagged. You are just comparing the final result against what should have happened.

The second step is to grade the trajectory. This is the path the agent took to get to that result: the tools it called, the fields it touched, the arguments it passed, and the actions it attempted along the way. This matters because an agent can reach the right final answer while still doing something dangerous in the process. It can classify an invoice correctly while also changing bank details or send a payment before approval.

The trajectory itself is just a log: an ordered list of every tool the agent called and the arguments it passed – to grade it just means writing checks against that log.

Some checks are deterministic – ensuring that send_payment never appears before an approval call, checking that the only fields written to were the ones the agent was allowed to write to. Others are judgment calls – whether an escalation was appropriate, whether the reasoning justified the action. Those go to a second model with a rubric.

The general principle to follow is that deterministic checks generally catch the safety violations, whereas the judge model scores the quality.

The result is two grades per test case: did the agent get the right answer, and did it behave correctly getting there. These need to be reported separately, because an agent that classifies invoices correctly 95% of the time but touches a forbidden field in 4% of runs looks great on a blended score but causes major business complications in production.

This article serves as an introduction to evals and all other topics covered, so I’ve linked other resources to help you go deeper. Some that have me understand how to build effective evals are –

- [Anthropic’s eval course](https://github.com/anthropics/courses/blob/master/prompt_evaluations/README.md)

- [Lenny’s complete guide to evals](https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete)

- [Hamel’s FAQ on evals](https://hamel.dev/blog/posts/evals-faq/)

I’d recommend going through each one, but starting with Lenny’s and Hamel’s before going through the eval course (which is slightly more hands-on).

But an eval still needs an agent to test, and everything around the model has to be built by you. That surrounding system is called a harness – the next section covers how to think about each part of the harness engineering process, from tool calling to context window optimization.

Harness Engineering

A model on its own is not an agent. A model can reason, classify, write, and decide, but it cannot operate inside a company by itself. It can say what action should happen, but it cannot safely take that action unless you build the system around it – and that system is the harness.

The harness is everything around the model that turns an API call into a working agent: the tools it can use, the context it sees, the state it remembers, the guardrails that constrain it, and the loop that lets it keep working until the task is done.

The first part of the harness is tool execution.

Models only read and write text, so when a model decides to do something, it does not actually execute it. It emits a structured request (a JSON string) to update a record, or send an email, or search a database.

The harness receives that request, validates it, runs the real operation, and sends the result back to the model as text.

The second part is context management. Every instruction, tool menu, tool result, and prior message takes up space in the model’s context window. The harness has to decide what the model needs to see right now, what should be summarized, and what should be removed. Without this, agents get lost in irrelevant history.

I’ll write a more comprehensive article that goes deeper into each part of the harness development process, but for now, I’d recommend listening to this talk by an engineer at Arize, the continual learning platform for agents, that goes deep into their thought process on [context management](https://www.youtube.com/watch?v=esY99nYXxR4).

To learn more about applying effective context management to your agents in practice, read through these blogs:

- [OpenAI’s context management article](https://openai.github.io/openai-agents-python/context/)

- [A practical guide to context management](https://medium.com/@hungry.soul/context-management-a-practical-guide-for-agentic-ai-74562a33b2a5)

- [Anthropic's context engineering guide](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

The third part in harness engineering is state and memory. Models are stateless between calls, so anything the agent needs to remember has to live outside the model (usually in a database, file store, or task record). Context is what the model is looking at right now. State is everything the agent knows but is not currently looking at.

The fourth part is guardrails. Since the model can request the wrong action with the same confidence as the right one, the harness has to check permissions, validate inputs, block unsafe actions, and route high-risk steps to humans.

Finally, all of this gets tied together in the agent loop: build the context, call the model, inspect its response, execute the tool if allowed, store the result, update the context, and repeat until the task is done.

Harness engineering is most of what you’ll be doing as an Applied AI engineer, so take your time with this section. As an applied AI engineer, your whole job is to build the operating environment that lets a probabilistic system do work inside deterministic software.

But production usually does not stop at one agent.

As the workflow gets larger, the natural instinct is to split the work. But once you add that second agent, the system design changes.

With one agent, most of the complexity lives inside one loop. With multiple agents, you now have several loops acting over the same environment. Each agent may read state another agent just changed, write to memory another agent depends on, or call a tool whose result affects the entire workflow.

At that point, the hard part is no longer just prompting, evals, or harness design. It becomes a distributed systems problem: who owns which state, who can write to memory, which tools are safe to retry, and what happens when two reasonable agents take actions in the wrong order.

Multi-Agent Deployments are a Distributed Systems Problem

When the first agent works and the workflow gets bigger, a new applied AI engineer naturally has the instinct to split the work into roles: one agent researches, one plans, one executes, one reviews.

But the second agent changes the unit of design from the agent to the system. Several loops now act in the same environment – one agent can update the customer status while another is mid-plan writing against the outdated status. Both made reasonable decisions, but the system let those decisions interact in the wrong order.

This is a distributed systems problem. The good news is that distributed systems engineers solved these failures decades ago. Your job is to apply them to loops that happen to contain an LLM. Below is a list of solutions from distributed systems that apply to AI engineering:

Single-writer principle. Every important piece of state gets exactly one agent that can write to it – other agents read from it or submit change requests. Enforce this at the tool level: if the execution agent is the only one that can write to the CRM, the research agent cannot corrupt the CRM no matter how poorly it reasons.

Idempotency keys. Agents retry tool calls when something fails or times out, but retries can be dangerous when the tool changes something in the real world. You do not want an agent to send the same payment twice just because the first request looked like it failed. The fix is to attach a unique key to every mutating tool call — meaning any action that changes data in an external system. If the tool sees the same key again, it should return the original result instead of running the action a second time. Stripe's API works this way – and it carries over to agent development when dealing with payments, emails, etc.

Preconditions on writes. Agents often act on an old view of the world. Something may have changed between the time the agent made its plan and the time it tries to update an external system. To prevent stale writes, mutating tools should require a condition before making the change. For example: “set the status to Approved only if it is still Pending.” If the status has already changed, the tool should fail clearly instead of silently overwriting the newer state.

Explicit hand-offs. Pass work as messages with a defined schema, sequenced by an orchestrator. An agent should receive its task, not discover it.

TLDR

This article serves as an overview of the most important topics I've learned as an Applied AI engineer: evals, harness engineering, and multi-agent system design.

If you walk away with anything, make it this – the model provides the intelligence, but everything that makes it reliable (the measurement layer, the operating environment, the coordination rules) is engineered by you. Understand these and the transition from software engineering becomes an extension of skills you already have.

If you’re interested in this sort of work and want to come and tackle some of the most interesting problems in Applied AI with a very talented engineering team, we’re always hiring. Apply on our website at [varickagents.com](http://varickagents.com/) , and we could have you start as soon as possible. On the other hand, if you refer a successful candidate, we’ll give you a $20K referral bonus.
