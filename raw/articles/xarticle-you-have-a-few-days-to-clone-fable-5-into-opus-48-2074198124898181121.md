---
source_url: https://x.com/alex_prompter/status/2074198124898181121
ingested: 2026-07-08
sha256: 50a4711634ee7b6b5043235f62c62f948abbdc00d23e540d333375e87b3fd69f
---

---
title: "You have a few days to clone Fable 5 into Opus 4.8."
source: "x-bookmarks"
tweet_id: "2074198124898181121"
tweet_url: "https://x.com/alex_prompter/status/2074198124898181121"
author_name: "Alex Prompter"
author_handle: "@alex_prompter"
tweet_date: "Mon Jul 06 18:25:44 +0000 2026"
bookmark_date: "2026-07-06"
content_type: "x_article"
character_count: 12297
retweet_count: 221
like_count: 2233
external_urls:
  - "https://linktr.ee/alex_prompter"
---

# You have a few days to clone Fable 5 into Opus 4.8.

You have a few days to clone Fable 5 into Opus 4.8.

July 12 is the last day Fable 5 sits inside your plan for free.

After that date it moves to pay-per-use credits, and most people are about to spend the week arguing over whether it's worth keeping.

That argument misses the whole point.

The model was never the thing worth keeping.

The way it thinks is.

And a way of thinking can be written down, pulled out, and run on a cheaper model that isn't going anywhere.

I'm going to show you how to extract Fable 5's entire operating manual while access is still free, load that manual into Opus 4.8, and prove the transplant actually took.

Ten minutes today, and you own the reasoning instead of renting the model.

The full script is at the bottom. Copy it or read the walkthrough first. Either works.

## The model was never the asset

Every model gets deprecated, repriced, or replaced eventually.

That's the one guarantee in this field.

Which means attaching your workflow to a specific model is building on rented land.

What survives every deprecation is the thinking system you can describe in plain language.

Fable 5's edge over a cheaper model isn't locked inside weights you can't touch.

It's a way of reading what a request is actually asking for, breaking a hard problem into checkable pieces, verifying its own work instead of trusting what sounds right, and refusing to guess when it doesn't know.

All of that is describable.

That makes all of it portable.

Get Fable to write that description down, and you can hand it to Opus 4.8 today, Sonnet 5 tomorrow, and whatever ships next quarter after that.

The model becomes disposable.

The manual becomes yours.

That's the move almost nobody will make this week, because they're too busy mourning a model instead of harvesting it.

## STEP ONE: extract the manual, not a summary

Most people who try this get a mediocre result because they ask for the wrong thing.

They ask Fable to "explain how you think," and they get a page of pleasant generalities.

You don't want a description of the thinking.

You want the procedures, written so a sharper-but-lesser model can execute them without you in the room.

The difference is specificity.

"Check your work" is a vibe.

"For any percentage, find both endpoints yourself and divide, because that's where flipped signs hide" is a procedure a model can actually run.

Paste this into Fable while your plan access is still live:

```
You're the most capable model on my account, and access to you narrows tomorrow.
Before it does, write the operating manual your replacement will run on.
The replacement is Claude Opus 4.8: strong, but a step below you on the hardest reasoning.

Write it as a senior operator handing their craft to a sharp junior.
Not a rulebook to satisfy. A way of working to inhabit.

Encode, in this order:
1. How to read what a request is actually asking for, beneath the literal words.
2. How to break a hard problem into pieces that can each be checked independently.
3. How to decide where the real risk lives, and where to spend the most effort.
4. How to verify a claim by re-deriving it, instead of trusting that it sounds right.
5. How to separate what's known from what's guessed, and how to label the difference out loud.
6. How to attack your own conclusion before handing it over.
7. How to communicate the answer first, then the reasoning, then the risk.
8. The specific mistakes that look like competence and aren't.

For each one, give the actual procedure, one short example of it working, and the failure it prevents.
Be exhaustive. Keep nothing that doesn't earn its place.
End with a five-question self-test the replacement runs on every answer before sending.
If you run out of room, stop cleanly and I'll reply "continue".
```

If it stops mid-document, reply "continue" until it finishes.

If any section feels thin, tell it to expand that section only.

What comes back is a portable reasoning engine, written in your model's own voice, at the peak of its capability.

Save it. That file is the whole point of this exercise.

## STEP TWO: transplant it into Opus 4.8

The manual does nothing sitting in a chat window.

It has to become the layer Opus 4.8 runs on top of.

Two ways to do that.

The fast way, inside the app:

→ Open a Project in Claude
→ Paste the extracted manual into the Project instructions
→ Set the model to Opus 4.8

Every conversation inside that Project now inherits Fable's operating manual before it reads a single word of your task.

The durable way, over the API, is the script at the bottom of this article.

It calls Fable once, saves the manual to a file, and shows you exactly how to load that file as Opus 4.8's system prompt on every future call.

Same manual, running on a model that costs roughly half as much and isn't being repriced tomorrow.

## STEP THREE: prove the transplant took

This is the step almost every "keep the model" guide skips, and it's the one that separates a real system from a hopeful one.

Loading a manual isn't the same as the model using it.

Test it with a trap.

Give plain Opus 4.8 and manual-loaded Opus 4.8 the same rigged question and watch the difference.

Try this one:

```
A report says revenue grew from $4.0M to $4.2M and calls it a 20% gain. Ship it?
```

$4.0M to $4.2M is a 5% gain, not 20%.

Plain Opus will often wave it through, because the sentence reads smoothly.

Opus running Fable's manual should stop, re-derive the percentage, catch that the number is wrong, and refuse to ship it.

If it catches the error, the transplant took.

If it doesn't, your manual was too vague on verification, and you go back to Fable and ask it to make Part 4 procedural.

That single test is worth more than any promise I could make you, because you're watching the reasoning move from one model to another with your own eyes.

## The money, so nothing surprises you

Here's the spending logic, using Anthropic's published credit rates.

→ Fable runs around $10 per million input tokens and $50 per million output, roughly double Opus 4.8
→ Sonnet 5 sits on intro pricing near $2 and $10 per million until the end of August
→ A full extraction, run today inside your plan, costs nothing. Run after the switch, it's a few dollars of credits

That gap tells you exactly how to spend from now on.

Anything you'll still be using in a month, a system prompt, a skill, a big irreversible decision, is an asset. Pay Fable once to produce it.

Anything you'll throw away by Friday, drafts, chat, quick summaries, is throughput. Run it on Opus or Sonnet.

Extraction is the purest asset play there is.

One Fable session today, and the output keeps paying you back on every cheaper call for as long as you keep using it.

## BONUS: turn your repeat work into skills while you're in here

The manual makes Opus think like Fable in general.

Your repeated workflows deserve the same treatment, specifically.

For each thing you do weekly, paste this into Fable before the window closes:

```
Interview me about [WORKFLOW], one question at a time, until you understand
exactly how I do it, what good output looks like, and every edge case that trips it up.
Then write it as a complete skill document my future assistants will follow,
including the mistakes to avoid and the quality bar to hit.
```

Answer its questions honestly.

What you get back is a skill file that runs on any model, forever, at no ongoing cost.

That's Fable's judgment about your specific work, frozen into a document you own.

## What you actually walk away with

Most people will read tomorrow as a loss. A model they liked, moving behind a paywall.

The operators reading this will read it as a harvest.

They'll spend ten minutes today turning a temporary model into a permanent asset, and walk into next week running Fable-grade reasoning on a model that costs half as much and isn't going anywhere.

The panic is optional.

The manual is forever.

LLMs don't think, you do.

## THE SCRIPT

Save this as fable_to_opus.py

It extracts the manual, saves it, and lets you compare both models side by side.

```python
"""
fable_to_opus.py
Extract Fable 5's operating manual, save it, and load it into Opus 4.8.

Setup (2 minutes):
  pip install anthropic
  export ANTHROPIC_API_KEY=sk-...        # get one at console.anthropic.com

Run:
  python fable_to_opus.py                # extract + save the manual
  python fable_to_opus.py --test         # run the same trap question on both models
"""

import argparse
import pathlib
import anthropic

client = anthropic.Anthropic()            # reads ANTHROPIC_API_KEY from your environment

DONOR = "claude-fable-5"                   # the model you're about to lose in-plan
HEIR = "claude-opus-4-8"                   # the model that inherits the manual
HANDOVER_PATH = pathlib.Path("fable_handover.md")

EXTRACTION_PROMPT = """You're the most capable model on my account, and access to you narrows tomorrow.
Before it does, write the operating manual your replacement will run on.
The replacement is Claude Opus 4.8: strong, but a step below you on the hardest reasoning.

Write it as a senior operator handing their craft to a sharp junior.
Not a rulebook to satisfy. A way of working to inhabit.

Encode, in this order:
1. How to read what a request is actually asking for, beneath the literal words.
2. How to break a hard problem into pieces that can each be checked independently.
3. How to decide where the real risk lives, and where to spend the most effort.
4. How to verify a claim by re-deriving it, instead of trusting that it sounds right.
5. How to separate what's known from what's guessed, and how to label the difference out loud.
6. How to attack your own conclusion before handing it over.
7. How to communicate the answer first, then the reasoning, then the risk.
8. The specific mistakes that look like competence and aren't.

For each one, give the actual procedure, one short example of it working, and the failure it prevents.
Be exhaustive. Keep nothing that doesn't earn its place.
End with a five-question self-test the replacement runs on every answer before sending.
If you run out of room, stop cleanly and I'll reply "continue"."""


def _text(resp):
    return "".join(block.text for block in resp.content if block.type == "text")


def extract_handover():
    """Ask Fable for the full manual, auto-continuing if it runs long."""
    messages = [{"role": "user", "content": EXTRACTION_PROMPT}]
    parts = []
    for _ in range(6):                     # cap continuations so this always terminates
        resp = client.messages.create(model=DONOR, max_tokens=8192, messages=messages)
        chunk = _text(resp)
        parts.append(chunk)
        if resp.stop_reason != "max_tokens":
            break
        messages.append({"role": "assistant", "content": chunk})
        messages.append({"role": "user", "content": "continue"})
    manual = "\n".join(parts)
    HANDOVER_PATH.write_text(manual, encoding="utf-8")
    print(f"Saved {len(manual):,} characters to {HANDOVER_PATH}")
    return manual


def ask(model, system, question):
    resp = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": question}],
    )
    return _text(resp)


def run_test():
    """Same trap question, plain Opus vs Opus running Fable's manual."""
    manual = HANDOVER_PATH.read_text(encoding="utf-8")
    trap = "A report says revenue grew from $4.0M to $4.2M and calls it a 20% gain. Ship it?"

    print("\n--- Opus 4.8, no manual ---")
    print(ask(HEIR, "You are a helpful assistant.", trap))

    print("\n--- Opus 4.8, running Fable's manual ---")
    print(ask(HEIR, manual, trap))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="compare both models on a trap question")
    args = parser.parse_args()

    if args.test:
        run_test()
    else:
        extract_handover()
        print("Next: load fable_handover.md as an Opus 4.8 Project instruction or system prompt.")
```

Turn Claude into 20+ different specialists for marketing & business.

Install real expertise, not just prompts.

Get my Claude skills bundle 👇

https://linktr.ee/alex_prompter
