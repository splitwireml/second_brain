---
title: "Agent Skills Framework: How to Create Skills That Actually Work"
created: 2026-05-05
updated: 2026-05-10
type: raw
source_type: x-video
url: https://x.com/ridark_eth/status/2051300137859739861/video/1
author: ridark
date: 2026-05-05
duration: 665.9
tweet_id: 2051300137859739861
platform: x
likes: 66
retweets: 0
replies: 7
tags: [ai-agents, claude-code, skills, prompt-engineering, hermes-agent, productivity]
---

# Agent Skills Framework: How to Create Skills That Actually Work

**Source:** [ridark_eth – X Video](https://x.com/ridark_eth/status/2051300137859739861/video/1) | 11 min 5 sec

---

## Transcript

[0.0–23.4 | Speaker 0]
If you're creating agent skills, you're probably doing it wrong. Most developers blow the context window, over-explain things Claude already knows, and end up with a slow, expensive skill. Over the past few days, I've done almost nothing but build agent skills for my own workflow and for our Pro members. So in this video, I'll show you the exact framework I use every single time so that you can start creating effective and useful agent skills. Let's get started.

[23.4–57.6 | Speaker 0]
So first, let me explain why skills are so important and I think are going to be very important in the upcoming months. And the reason is that skills are modular capabilities that extend Claude's functionality. Skills are used for repetitive tasks. That way, you don't have to prompt the same thing over and over. You can just create instructions with metadata, give it a title, give it a description, what is this skill about, and then Claude or any agent that you're using is going to decide whether the skill is a good fit depending on the context of the conversation that you are having.

[57.6–95.9 | Speaker 0]
You should use skills for reusable tasks or things that you have catch yourself repeating to the agent over and over again. Let me give you a very simple example. Let me spin up Claude and I'm going to say, write a short email saying hi to my friend. So what happened here is that Claude is just going to try to do its best. But there are a couple of things that I like to do about my emails. I usually end my emails with best, Beto, and then you can add my website and stuff like that. So in this case, I would need to ask Claude, please add my name and my website as footer in the email.

[95.9–134.4 | Speaker 0]
And I would need to do this every time that I ask Claude to create an email. This is a perfect repetitive task that we can create a skill for. So we have spotted the repetitive task, let's create a skill. Skills should contain a skill.md with uppercase like that, and then you need a name and description. All right, so for this example, let's just say always end my emails with best, Beto, founder of Code with Beto dev. And that's it. That's all you need to do. Now, if I bring back Claude, and same thing, write a short email for my friend Joe. So as you notice, it detected the short email skill and it's loaded in the context.

[134.4–173.6 | Speaker 0]
and it's asking me now more context, so I'm going to say, say hi, how are you doing? Now, check this out, guys. My email contains the footer that I like for my email. So I can just copy and hit send. At its core, this is what a skill is very useful for. So that's how you quickly create a simple skill. But I wouldn't recommend that you do that manually, especially for more complex skills. And the main reason is that no one really writes better than AI models. So I would delegate that task to Claude or ChatGPT, and then you can refine your skills based on your needs. So I would highly recommend that you use skill creator skill from the Anthropic team.

[173.6–212.8 | Speaker 0]
I'm going to leave the link in the description for this skill. Basically, you can just download it or install it directly using the skill CLI from Vercel. If I go back to my project, you'll notice that I have this skill creator here. You can read more about it if you want, but it's actually pretty long, just laying down the best practices. But once you have it installed, you can just use it. So since I have this skill in the root of my computer, I can use it everywhere in my computer. But let's go to my AI Tattoo application, which is in a different project in my computer. And by the way, if you're curious about the source code of AI Tattoo, it's actually available for Pro members in our private GitHub organization. I'm going to leave it in the description in case you're curious.

[212.8–252.2 | Speaker 0]
It's a real application that it's live in the App Store and it's actually making money, more than a hundred dollars monthly recurring revenue, which is very exciting. And definitely one of the best resources and production examples that we have in the platform. So remember, skills are not for one-time tasks or for simple things like explaining just a piece of code. Just don't use a skill. You can ask the agent directly. Skills are for patterns that you repeat, I don't know, daily or weekly or even monthly, right? And tasks that you might forget how to do. So here in my package.json, I have some scripts for deployment, but it would be nice if I can just ask Claude to deploy the API once I made some changes.

[252.2–289.2 | Speaker 0]
I could even change between preview and production deployment, or even test flight for deploying the iOS application. And then something very annoying when you are developing a mobile app is that you sometimes forget to increase the version, and those things are repetitive that Claude could handle. So let's open terminal and I'm going to use Aqua Voice. It's an application for speech to text. And if you want to try it yourself, you can get one month free using my link in the description. So I can activate it by pressing F N twice. Help me create a skill for deployment. Take a look at the package.json file.

[289.2–310.9 | Speaker 0]
See the scripts, you'll notice that we have some scripts for deploying the API routes, some scripts for deploying to preview, production, and the mobile app. Whenever you use this skill, make sure to ask me what we want to deploy and then go ahead and run the scripts. Keep in mind that when we are deploying the application, sometimes we might need to increase the version, so also ask me about it.

[311.7–322.1 | Speaker 0]
Okay, here we go. Just press enter and it's going to use the skill for creating skills. It took a look at the scripts and it also loaded the skill creator skill. And this is great.

[322.1–335.6 | Speaker 0]
now it's going to ask me. This is kind of like plan mode, but for creating skills. I don't want to do all that at once, so just like that we can press next. How do you typically bump the version? This is a very important question. Only for production deploys. Okay.

[335.6–338.1 | Speaker 0]
And those are the questions. Now we can submit. Alright.

[338.1–377.4 | Speaker 0]
So here's the skill and honestly it's pretty decent. And at first glance, I can see that follows best practices. And just as it is, I think this skill is perfect. So let's talk about some of the best practices. First of all, you need to be very concise. And if you notice, this is great. This is not super long. It's perfectly okay. Just one-liners, a lot of bullet points, a lot of lists. It's very important to be concise in good skills because when the agent detects that it needs to use this skill to perform the task, then it's going to load all this into the context window. So we don't want to mess our context window by loading a bunch of data or documentation, right?

[377.4–416.7 | Speaker 0]
So once the agent loads the skill, now it's going to have the system prompt plus the conversation history plus other skills metadata because all this metadata it's loaded into the context window so that Claude knows which skill to use. And then of course your actual prompt and request. So keeping this lean is very important for better results and also to save money. I want to show you a couple of examples of a good concise skill. This is approximately 50 tokens. It's just the code, right? And this is to extract the PDF text. That's all. And here we have a bad example which would be like a huge paragraph that is going to consume the tokens. Just don't do that.

[416.7–453.5 | Speaker 0]
Claude is very smart already. Give it the code that it needs to run, give it the script, and you'll get better results. You can also set appropriate degrees of freedom, and this depends on the task that you are trying to achieve. You can do things like analyze the code structure and organization or check for potential bugs and edge cases. So in that case, when you give this kind of instructions, the agent is going to go wild and maybe consume a lot of context, but maybe that's what you want, right? Maybe that's what you need for this for the action that you are performing with the skill. And here we have a low freedom example, which you can, you know, explicitly say, run this exact script.

[453.5–489.0 | Speaker 0]
and maybe you can also say just check the folder inside, you know, assets for example, or inside the source folder. That way we prevent the agent from loading other files into the context window. And lastly, when you create skills, you should test your skill with different models. For example, Claude Haiku is fast, economical, but does the skill provide enough guidance for this kind of model? Or Claude Sonnet, it's balanced, is the skill clear and efficient? And we have Opus, which is very powerful. In this case, we want to avoid over-explaining and keep the context window as low as possible because it's very expensive to run this model.

[489.0–528.8 | Speaker 0]
Another thing to keep in mind is that you can also have a folder called references, and then you can add more context and the agent is going to load it depending on the task that it's performing. So you can create skills locally for yourself and your computer, but you might want to also distribute them to your team or your community. In that case, I would encourage you to read the naming conventions to make sure that you're following best practices. And if you're aiming to make your skill available to everyone, I would encourage you to read this document. I'm going to leave the link in the description. It's actually pretty simple. Let me show you an example here. I'm working on some skills for my students, and I'm going to have as well some free skills.

[528.8–567.2 | Speaker 0]
and this is a great example that you can check out. So you are going to distribute this to the community, you need to have a repo that is public, and then you need to configure this folder .cloud plugin with a marketplace.json file. You can copy this and then change the name. And then the plugins are going to be the skills that you have in this repo. It's a skill that generates an app icon for your application. I'm still working on this, this is not ready yet, but the skill is inside plugins/codeveto/app-icon. And then this is a skill by itself, so it has a cloud plugin folder as well, which contains information about me and the name of the skill and description.

[567.2–605.7 | Speaker 0]
It's also good to have a readme that explains what your plugin does or your skill does, when to use it, when not to use it, some tips, and then the actual skill inside the skills folder. This is just a simple skill.md. Name, description, keep it brief, and that's pretty much it. Since this is a public repo, anyone can use it. And you can install them using the skills CLI. My organization is called Viveto, and the repo is skills. And just hit enter in your terminal, anyone can do it. Or if you are restricting this to your organization, as long as they have access to the repo, they should be able to install them. And it found one skill.

[605.7–643.5 | Speaker 0]
The only one that I have it's app icon. So then you can follow the prompt and install it. Remember, skills are for repetitive tasks. Keep them concise and respect the context window. Remember to use references or scripts for detailed documentation, and don't forget to test your skill across different models. If you want to get access to production-ready examples, private skills, plus React Native and Expo codebases with production-ready examples including the AI tattoo application, consider becoming a Pro member at codeveto.dev. I'm going to leave the link in the description. And subscribe to the newsletter for more AI development workflows. Don't forget to give it a like and subscribe. Let me know what you think and what skills you're going to be creating and using. Otherwise, I'll see you in the next one.
