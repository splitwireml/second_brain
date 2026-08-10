---
source_url: https://x.com/everestchris6/status/2086455451429060984
ingested: 2026-08-10
sha256: c2b973c21049634e1aec05400572346a26bba2de2c7e369824d02a9ef184aac8
---

---
title: "make money with AI agents on reddit (full guide)"
source: "x-bookmarks"
tweet_id: "2086455451429060984"
tweet_url: "https://x.com/everestchris6/status/2086455451429060984"
author_name: "Chris"
author_handle: "@everestchris6"
tweet_date: "Sun Aug 09 14:11:58 +0000 2026"
bookmark_date: "2026-08-09"
content_type: "x_article"
character_count: 18831
retweet_count: 10
like_count: 219
external_urls:
  - "https://t.me/+pbCBBtUEtu1lZDA1"
---

# make money with AI agents on reddit (full guide)

make money with AI agents on reddit (full guide)

i was making about $1,000/ day on reddit just by posting and answering dms. 

here's the whole playbook:

by the end of this you'll know how to find a problem people already pay to solve, how to build the thing that solves it, and how to get in front of those people for free. i'll also show you how to set up an agent that runs about 95% of this process for you.

first, why reddit:

there's a community for every problem a person can have. whatever you're thinking of selling, there are people with that exact problem already gathered in one place and talking about it every day. you don't have to find them or build an audience first.

the posts also rank on google. reddit sits near the top of search results for almost every question people type in, so a post you write once keeps getting found by people who never open reddit at all.

every one of these communities is a running list of things people want and can't find, sitting there in public. so you're not guessing at a product and then hunting for buyers afterwards. you read what they're already asking for, then sell it back to them in the same place.

that's what i did with my saas, a tool that sold websites to local businesses on its own. reddit was the only marketing it ever had and it was doing around $1,000 a day from basically the first post. the post explaining the google sheet method did 1.1 million views and 1.4k upvotes. another one about a $9 PDF did 1.2 million. before that i sold a PDF guide about a health thing i'd dealt with myself. smaller money, but i stopped posting about it almost two years ago and people still message me about it every week.

so here's the whole thing in order, starting with what to sell.

most people do it the wrong way, they build something first and then go looking for people to sell it to.

do it the other way. go and read the subreddit before you make anything.

the same questions come up over and over in every community. people asking how to deal with something, asking if a tool exists for a specific job, asking what worked for anyone else. you'll see the pattern in a few hours of scrolling. those repeated questions are a list of things people want and can't find, and that list is worth more than any idea you'll come up with on your own.

your own knowledge matters here, but only because it lets you answer one of those questions properly.

here's a prompt that brings it out of you

the hard part isn't that you know nothing worth selling. it's that whatever you know stopped feeling like knowledge a long time ago.

paste this into claude/chatgpt and answer it honestly. it'll ask you things, then tell you what's actually in there.

"you are helping me find something i can sell based on what i already know. ask me one question at a time and wait for my answer before moving on. don't summarise or encourage me between questions.

ask me these in order, and follow up on anything vague or general:

1. what do people come to you for help with, even in small ways?

2. what did you have to work out for yourself because nobody would explain it properly?

3. what takes you ten minutes now that used to take you weeks?

4. where have you watched people waste money doing something the wrong way?

5. what do you know that would take someone else a year to learn from scratch?

once i've answered all five, do this:

pull out every specific piece of knowledge i gave you and throw away anything generic.

for each one, tell me exactly who has that problem right now, and what that person would type into google at 2am when it's bothering them.

name the subreddits where those people are.

then tell me which of these are worth pursuing and which aren't, and be blunt about it. if one of them has no audience that pays for anything, say so and tell me why instead of forcing it into a product.

for the ones that survive, give me a search string in the form site:reddit.com/r/[subreddit] "how do i" and tell me to go read the last three months of results before i believe any of this.

do not give me a business name, a plan, or a landing page. stop at the idea and the check."

the last instruction kinda matters because it's supposed to stop at an idea you then go and verify yourself, because an idea that came out of a chat window and never got checked against real people is basically worth nothing

the quick version is google search operators, because reddit's own search is bad. search site:reddit.com/r/subredditname "how do i" and you'll get every thread that starts that way. swap the phrase for whatever people say when they're stuck. "is there a tool that", "does anyone know how to", "i wish there was". then open google's tools menu and filter to the past three months,

that gives you a feel for it,  for the real version you want the actual data.

connect the apify MCP to claude. it's at mcp.apify.com and then tell claude what you need in plain english. something like: using the apify MCP, find me a good reddit scraper, i need every post and comment from r/whatever for the last three months. it'll go and find the right actor, run it, and hand you back the data.

then you point it at the pile. give it something like this:

"here is three months of posts and comments from r/[subreddit]. read all of it and tell me:

the problems that come up over and over, ranked by how often people raise them and how upset they sound when they do.

for each one, quote me two or three real lines from the data so i can see how these people actually describe it.

which of these problems people are already trying to pay someone to solve, and what they're currently using instead.

then tell me which single one i should build for, and what the product should be. a PDF guide or a paid newsletter, nothing more complicated than that. if none of these problems is worth building for, say that instead of forcing one."

so the whole research is built from what people wrote in public over the last three months.

sell to people who need it now

one thing i've noticed across both products. it works far better when the people you're selling to want the problem gone today.

somebody dealing with a health thing that's affecting their week is looking for an answer right now. a business owner losing customers because his website is broken is looking right now. compare that to someone idly wondering if they should learn a skill at some point, who will read your post, agree with it, and do nothing.

so when you're going through those subreddits, pay attention to how the questions are written. the urgency shows up in the wording.

i'll say the other half of this too, because it matters. people in that state are easy to take advantage of and you shouldn't. only sell into a problem you actually understand and can genuinely help with. if you can't, you'll get found out fast in a community like that.

building the thing:

your product is a PDF guide or a paid newsletter. don't build software for your first one. you already have the research from the step above, so tell claude to write the guide from it, using the actual language people used in those threads rather than the words you'd choose. that's what makes it read like it was written for them.

a newsletter is worth considering over a one-off PDF if the audience is on the smaller side, because fewer buyers means you need each one to be worth more than a single sale. i charged $9 a month for mine, which is low enough that someone actively dealing with the problem doesn't stop to think about it.

then you need somewhere to send people. that part i do in cursor with the claude code extension, i've got a skill file with the stack and the components already in it, so you attach that, tell it what the page is for, and it builds the lander. you can find the skill file here: https://t.me/+pbCBBtUEtu1lZDA1

everything else in this article runs in claude on the web or the desktop app. the landing page is the only bit that needs cursor.

after that you have a product and somewhere to buy it, and the only thing left is getting people to it.

how reddit actually works

now the mechanics, because this is where most people's first post dies

followers do almost nothing on reddit. the follow system exists but hardly anyone sees your post because they follow you. i had zero followers when i started and the account only ever picked up 174 of them across posts that did millions of views. it made no difference to anything.

what matters is karma. karma is the points you accumulate when your posts and comments get upvoted, and most subreddits worth posting in set a minimum before they'll let you post at all.

two details people miss. plenty of subreddits check comment karma specifically, not your total, so an account carried by one popular post still won't qualify. and a lot of them also require the account to be a certain age, which no amount of karma fixes.

if you don't meet it, automod removes your post within seconds. you get a message explaining what you missed and not one human being has seen what you wrote.

for reference, the account i used had about 6,800 karma and was five years old. that's not a big number. it's just enough to look real.

aged accounts, and what they actually are:

so people go looking to buy an account that already meets those requirements.

an old account and an account with karma are two different products. what's usually being sold is something registered in the past, used for a few weeks, then left alone. it is genuinely old and it is still useless, because you post from it and automod removes it the same as it would a brand new one.

that's the thing nobody tells you. age alone gets you past almost nothing.

if you're buying anyway, check four things. how old the account is, how much karma is on it, whether that karma came from comments or from posts, and whether the account is already finished.

finished means shadowbanned, or previously used for spam by whoever had it. shadowbans are the nasty one because everything looks normal from inside the account. your posts appear on your own profile and nobody else can see it. you'll assume the post flopped when it was never visible to anyone. open the profile in a private window while logged out, and if the posts are there you're fine, and if the page is blank the account is dead. do it before you pay anyone.

the cheapest accounts on offer have almost always farmed their karma by reposting old content, which reddit is good at detecting, and those get flagged quickly. paying more doesn't fix the underlying problem either, because you're still paying for age when what you need is karma.

warming up your own:

this is what i'd actually tell you to do. get an old account, or buy one purely for the age, and put the karma on it yourself.

for the first two weeks you don't post anything. you comment. around fifteen a day in the big general subreddits, replying to things you genuinely have an answer for. it takes no thought and it clears almost every karma requirement you'll hit.

it does something else too. it leaves the account with a history that reads like a person, which matters when a moderator looks at your profile after you post.

the account i used was one of my own from years back. scroll far enough down it and there's me asking health questions in 2021, none of it connected to anything i was selling later. that's what a real account looks like.

be clear about the rules

reddit's user agreement doesn't allow selling or transferring accounts, so buying one breaks it for both people involved. running several accounts to push the same product goes against how most of these subreddits are meant to work as well.

what that means in practice is that a ban isn't bad luck, it's the eventual outcome.

that account is permanently banned now, it's five years old, 6,800 karma, millions of views across those posts. i knew it was coming and it still went. so treat every account as temporary and keep another one building karma in the background.

what gets you banned when you try to automate

i put real money into test this so you don't need to.

i tried vpns., private proxies then every combination of those i could think of.

every version ended the same way, with the accounts banned, usually within days of the first automated post.

your ip address is the least of what they're looking at. reddit reads browser fingerprints, the timing of your actions, what the account does either side of posting, and how many accounts have ever touched the same setup. i kept believing i was one configuration away from it working and i never was.

what you can actually automate:

almost everything else, though. the research runs on its own. the scraper and the weekly summary of what people are asking for don't need you at all once they're set up.

the writing is mostly automated. i give claude the topic and my angle and let it draft the post, then i rewrite it in my own words. AI writing is obvious to people now and reddit readers are unusually good at spotting it.

the better version is to make it read the subreddit before it writes a word. you already have three months of scraped posts from the research step, so tell claude to look at the ones that actually performed, work out how those people write and what format survives in there, and turn that into a skill file for writing posts in that community's voice. it saves the skill automatically and every draft after that comes out in the right shape instead of the generic voice it defaults to.

every subreddit has its own tone, this is the difference between a post that lands and one that gets four comments telling you it sounds like AI.

then you hand off the posting itself. this is straightforward to hire for on upwork or onlinejobs.ph, either hourly or paid per post. what they need is a doc with the account logins, a schedule of which account posts where on which day, the drafts, and a page of answers to the questions people ask most. keep the recovery email on an address only you control and never hand over that password.

do it by hand for a few weeks first so you know what a good post looks like in that community. once you do, you can put the repeated parts on an agent. i use hermes for this because it runs on a schedule on its own and connects to api's , so it can reach apify etc. the instruction is roughly: scrape these subreddits every week, look at what's performing, and have two posts written and waiting for me every day. then it pings you when they're ready and you read them, fix whatever sounds off, and post them yourself.

so the shape of it is an agent that finds what people want and writes the posts, and you spending like twenty minutes a day checking and submitting.

the dms stay manual and i don't think that changes soon. it's the same detection problem as the posting, and it's also the part where the money actually happens, so it's the last thing you'd want a bot doing badly.

what goes in the post

give away the entire method. not a version with the useful part removed. the real one.

with unloopa i'd write out how to find businesses on google maps, how to build them a site with free tools, how to connect that site to a google sheet so the owner could edit it himself, and the exact email to send. anyone could read that post and go run the whole thing without ever speaking to me.

your instinct says that destroys your sales. it does the opposite. cutting out the useful part is what makes a post feel like an advert, and nobody reads or shares an advert. handing over all of it is the only thing that convinces a stranger you know the subject.

selling information doesn't change this either. my product was a PDF and i still answered everything for free. nobody was paying for a secret i'd withheld. they were paying to have it all in one place instead of reassembling them

find the one detail that makes people stop

writing it so it doesn't read like an ad

the post has to read like help. the moment it sounds like marketing, reddit removes it and the comments come for you.

no link in the post/comments is deliberate. reddit and the moderators will kill a post with one in it, and a link turns the whole thing into an advert in the reader's head so nothing else you wrote lands. making people message you also filters out everyone who wasn't serious.

on the health posts i'd end with a line saying i'd written down everything that helped me and i could send it over if anyone wanted it.

when to post:

post while your people are awake. for a US audience that means their morning, and if a post doesn't go anywhere, try the same one again in their evening around 6pm or 7pm.

but don't just take that as a rule. sit and think about the actual day of the person you're selling to. when are they on their phone, are they up at night with this problem, do they check reddit at work. it sounds like a stupid thing to spend time on and it's the difference between a post that gets seen and one that dies. test a few times and you'll find the window.

the messages are the actual business

no revenue ever came from a post directly. it came from what happened afterwards.

what i'd do instead is put a line at the end saying i'm happy to answer questions.

people read it and message you, and a post that does well brings a lot of those in every day. someone tells you what they're dealing with and asks what to do about it. so you help them properly. i'd go 5-10 messages deep with people, giving real advice for their specific situation.

the ones who dm are the warm ones. think about what they had to do to get there. they read the whole post, went to your profile, opened a chat and typed out their situation to a stranger. nobody does that unless they actually want the problem gone.

the product came up later, once the conversation had already been worth their time. with the guide it was mentioning i'd written the whole thing down in one place.

nobody experienced that as a pitch, because by then they'd already decided i knew what i was talking about.

the traffic that keeps arriving because reddit ranks so well on google, a thread /post you write once keeps pulling in people for years. i'm still on the first page for some of the searches around that old guide and it brings people in every day with no input from me.

the summary

run the prompts/ setup above, then go and read where those people already are and check that the questions really keep coming up. build the answer to one of them. get an account with real karma on it, which takes a couple of weeks of commenting. post the entire method for free with no link in it. answer every message properly and mention the product at the end.

the research and the writing can run on their own. the posting is done by hand or you lose the accounts.
