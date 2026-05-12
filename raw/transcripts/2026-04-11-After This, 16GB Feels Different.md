---
title: "After This, 16GB Feels Different.json"
created: 2026-04-11
updated: 2026-04-21
type: transcript
tags: []
sources: []
---

# After This, 16GB Feels Different.json


**Speaker 0**


[00:00](#t=0) You probably can't tell the difference between those two images, but the computer can. The image on the left is 14.6 megabytes and the one on the right is compressed to 1.8 megabytes. They look the same to me.

[00:12](#t=13) So if you use compression on a given disk, you can fit a ton more images or videos or whatever it is you're compressing than non-compressed. And same goes for LLMs. This right here is a Mac Mini with 16 gigs of memory. And this one is my daily drive with 128 gigs of memory. I can run pretty decently sized models on the big boy here or even on these with 512 gigabytes of memory each. But on this one with 16?

[00:38](#t=38) I have to be very picky about what I run. For example, a really popular model set that just came out is Qwen 3.5. This whole family of models is really performing well. Look how many downloads in the last month. And I really want to run this nine billion parameter model on this Mac Mini.

[00:56](#t=57) Well, guess what? The full thing is actually 19.3 gigabytes and you want to be able to fit the whole model inside the memory and we just won't be able to do that here. Well, this is the full BF16 unquantized version. What does that mean?

[01:10](#t=71) It's not compressed. That's why people started compressing different things here and there. And TurboQuant helps with that. Now before TurboQuant came about, we had different ways to handle compression. We had quantizations. So for example, BF16 is like a floating point 16-bit models. The weights for the models are basically a bunch of numbers and they're 16 bits. Not only do smaller quantizations take up less space on disk, but when you load those models up into memory, they decrease the memory requirement, allowing you to run it on smaller hardware. But you still have this KV cache issue, which also requires memory. So for example, here is the same model, 9 billion parameters, 8-bit.

[01:49](#t=110) And that one is only 10 gigabytes. We can go even smaller. Four bit. That one's 5.98 gigabytes. Well, just like with those images I showed you, sometimes the models and their compressed versions don't vary too much in quality. But sometimes they do. For example, if you go too low here, let's take Bartowski's quantizations. He's got all these different ones. Look, Q8.

[02:12](#t=133) 8-bit, 6-bit, 5-bit, 4-bit, 3-bit, 2-bit. Now, I'm sure these work, but they're not going to give you the best results. Sometimes the LLM gets into a loop where it just spits out garbage. Usually, quantization of four bits is probably the lowest you'd want to go. And if we take a look at this one, it's six gigabytes. Well, you'd say, oh, six gigabytes fits no problem on this Mac Mini, but wait, what about when you actually run it? I'm using 77 out of 128 gigs on this machine. Jeez.

[02:42](#t=162) That's a lot of gigs.

[02:43](#t=163) I'm going to load up this model and now I'm up to 84. Huh, that doesn't add up. That's because we need to reserve more memory for context and for cache. And this was only 4,000 context length, which is not very useful. This model supports way more than that. So let's crank it up all the way, reload. And now we're suddenly up to 92 gigabytes. And that's without even running any prompts at all.

[03:06](#t=186) Hi, I know you all love that prompt. But let's see how that affects our memory. We're still good. 92. What if we send in a really long prompt? This prompt is uh about 17,000 tokens. So let's send that in. Look at that.

[03:20](#t=200) Processing prompt It's taking a little while. Even on this powerful M5 Max MacBook Pro. And look at our memory. We suddenly have a little bit of a spike there.

[03:29](#t=209) And there it goes, printing out the answer. I'm going to paste in the same prompt again and what happens here is the entire conversation is sent in again for processing. Not just my prompt, but when the LLM is generating text, it doesn't re-read the entire conversation from scratch for every token. Instead, it stores key value pairs, the KV cache. These are basically mathematical summaries of every token it's already seen. Think of it as like short-term memory. And it lives inside the memory alongside of the model weights. With every token, KV cache grows and fills up memory. Now quantization solves for the model weights and shrinks them down.

[04:06](#t=246) Whereas TurboQuant, this new amazing thing, actually works on the KV cache and shrinks that down. This is one of those free Wi-Fi everywhere situations, which sounds great until you remember that everyone else is on it too. That's why Surfshark gets switched on before I do anything else. One click and my git pushes, SSH sessions, and package installs all go through an AES 256 encrypted tunnel. In the meantime, Clean Web quietly filters out all the usual garbage, ads, trackers, all that stuff you don't need. Surfshark keeps no logs, and that's been independently audited and their servers are RAM only, so a reboot wipes everything.

[04:44](#t=285) The feature I like most is unlimited devices. This MacBook, my phone, and the rest of my gear are all covered without me thinking about it. SSH into the lab feels a lot less sketchy on public Wi-Fi. Go to surfshark.com/alexiskin and you'll get four extra months free, plus a 30-day money-back guarantee. Stay private, stay productive. And now back to the video.

Now TurboQuant might not necessarily help you out on a system with a lot of memory, but it will help you out on a system with a little bit of memory. And the amount of noise this MacBook Pro is making is just crazy.

[05:19](#t=320) Listen to that. That's crazy. You're done with your job. What are you doing? Chill out.

[05:26](#t=326) Ah, cheesy jokes.

[05:29](#t=330) You might have heard about TurboQuant recently, it's making some waves, but whether it's going to be a thing or not, we'll see. So far the experiments are promising, and you can check out the official Google research paper there. I did my own experiments though. Llama CPP, a very popular project, lets you run LLMs locally.

[05:48](#t=349) it's pretty cool

[05:49](#t=350) They have not rolled in TurboQuant just yet. So far it's a community effort. Here's one very popular one on GitHub by the Tom, TurboQuant Plus. You can go grab this, run it yourself. Basically, it's a fork of Llama CPP that implements TurboQuant. Now, my initial tests with this were pretty bad. Um, I tried it out on the M5 Max, I tried it out on the M4 Mac Mini, and the KV cache space savings were present already, so that's good. Here's the context depth scaling. I went all the way up to 32k. The problem that I saw was that both pre-fill speed and decode speed suffered a lot. Also, very model dependent.

[06:28](#t=389) For example, I started out with Qwen 2.5, an older model, then I did Qwen 3 8B, and they all kind of showed similar results. As far as Turbo 3 and Turbo 4, there's three different variants of Turbo Quant: Turbo 2, Turbo 3, and Turbo 4. Turbo 2 is the most aggressive one that's supposed to squash it four times. Turbo 3 about two and a half times, and Turbo 4 about 1.9 times. Then I ran Qwen 3.5 35B, which is a mixture of experts model, not a dense model, and I ran it on this one. It's a 34 gig model. Obviously, it's not going to fit on the Mac Mini.

[07:04](#t=424) and that performed the best as far as squashing that KV and not losing too much on the speeds of decode and pre-fill. However, it still was slower. I was like, okay, well, I suppose it's worth the penalty if you're going to be getting such savings in compression. But

[07:22](#t=442) It wasn't over. Tom Turney worked on it a little bit more and gave me some hints. The way I was running it was not exactly the best way to do it. I was running it symmetrically. So K and V can actually be turboed separately. When I ran it, I applied Turbo 4 or Turbo 3 to both the K and the V equally. That's called symmetric when I applied it to both. And Tom suggested I use Q8 for K and then the Turbo 1 for the V part, which would be considered an asymmetric approach.

[07:56](#t=476) And then if you want more aggressive, you'd still keep Q8 for the K and you'd use Turbo 3 for the V part. On the Mac Mini, loading up the Q8 version with a 131,000 context window just crashes. However, Turbo 3 runs 131k context comfortably with 3.6 gigabytes to spare. Same model, same machine, Turbo gives you two times more usable context. And I tried different context lengths: 32k, 65, 131, and at each level we saw a huge difference in the number of gigabytes that were chomped up. And this chart shows a little bit of a breakdown between the model weights and they're about the same.

[08:34](#t=514) Well, they are the same actually, right here between the turbo run and the Q8 run, but here's that pesky KV cache that grows so much when you're running it at Q8, and here's turbo three KV cache, much much smaller, leaving us with some extra headroom. Nice.

[08:49](#t=530) So it kind of does that job, but what about the other thing? The speed. Well, we recovered that too. Hold on a minute.

[08:57](#t=537) Before I get into that, I wanted to do a little bit of a needle in a haystack because not only do you have to worry about the memory, but is TurboQuant going to affect the quality of the output? One test for such a thing is needle in a haystack. There's a lot of different tests, but that's one of them that's an easy one to understand. You have a bunch of text and somewhere inside of that text, you put a little secret and then you ask the model to find it. And you test different lengths of that full text. So that's the context length. 1k all the way up to 32k, 32,000 tokens. Initially, this was a total disaster. Look at this.

[09:33](#t=574) So three out of three at the top means we hid three secrets and found three secrets. That's a hundred percent. This is on the Mac Mini by the way. Quantization of eight got all of them. Turbo turbo, which means we had symmetric turbo for K and turbo for V.

[09:47](#t=588) got a hundred percent. But then we had a huge drop here. Terrible performance. Turbo three got one out of three and Turbo two got one out of three. Furthermore, if we look at Turbo three and Turbo two over here for larger contexts, 8k and 16k, they got nothing.

[10:04](#t=604) They got zero. This was before I listened to Tom's suggestion to do it asymmetrically. And when I switched to asymmetric, look at this, three out of three for all of them, all the way across the board. Beautiful.

[10:16](#t=617) So this shows the quality of the result is actually good when we're using TurboQuant at different levels of TurboQuantization at different context lengths too. Whew. Okay, back to speed.

[10:27](#t=627) There was a surprise. Now the M4 did okay. Um at short context lengths, Turbo doesn't do that well here. It slows down quite a bit. We're about one to four percent difference in the speed for decode here. But

[10:44](#t=644) on the M5 Max. This is where we saw a huge difference. Check out the decode speed here. So on Q8, the full baseline, non-turbo quant, we dropped down from about 54 tokens per second to about 37 tokens per second, going from a depth of zero to a depth of 8k for the context depth. And then we went up a little bit more. For 32k, we went up to 44. But turbo quant stayed relatively flat all the way across the board.

[11:14](#t=674) And this isn't some weird glitch. I ran this many times. So this is an average. This is pretty cool and it's pretty promising. I wish I saw the same kind of curve on the Mac Mini. Now the reason for that is here on the Mac Mini we were compute bound. Reading from KV cache was not the bottleneck here, but the model's matrix multiplications are. So if we speed that up, then we might see a similar curve to what we saw on the M5 Max. And that could mean that when the M5 Mac Minis drop, even if they have 16 gigs, which they probably will, they will have a significant boost and benefit even more from TurboQuant.

[11:49](#t=709) So the takeaway is that every model is going to behave a little bit differently, as usually is the case, but some models perform really poorly. However, the good news is the latest Qwen 3.5 models behave really well and respond really nicely to TurboQuant on the Apple hardware. Now you could try this fork out yourself, or you can wait until this is rolled into Llama Cpp and other tools. I think VLLM is also working on it. And if Llama Cpp gets it, then tools like LM Studio are going to get it. Go ahead and try it on your machine, let me know what you get.

[12:18](#t=738) Do you see good results from this? Also, leave a comment with what models you used as well. Thanks for watching and I'll see you next time.

[12:24](#t=745) [Music]
