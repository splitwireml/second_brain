---
title: "Vibe Coders Are Building Apps. Almost None of Them Are Getting Paid."
tweet_url: "https://x.com/DamiDefi/status/2050197937578193153"
author_handle: "@DamiDefi"
author_name: "Dami-Defi"
tweet_id: "2050197937578193153"
created_at: "Fri May 01 12:57:33 +0000 2026"
type: x-article
likes: 399
retweets: 40
replies: 12
article_title: "Vibe Coders Are Building Apps. Almost None of Them Are Getting Paid. (full guide)"
---

## Raw Content

Vibe Coders Are Building Apps. Almost None of Them Are Getting Paid. (full guide)

You built the app. It is live on the App Store. You tell people about it. Some of them download it.

And then nothing happens. No revenue. No payout. No dashboard lighting up.

This is not because the app is bad. It is because getting paid on iOS is a separate system with its own rules, its own setup, and its own ways to get it wrong. Most vibe coders never learn this until after they have already shipped.

I have 10 apps on the App Store. Here is everything I learned about actually getting paid.

## The App Store Is Not Just a Distribution Platform

Most builders treat the App Store like a shop shelf. You put your app there and people buy it. That is not how Apple thinks about it.

Apple is a payment processor, a compliance authority, and a landlord simultaneously. They control what you can charge for, how you can charge for it, who you can charge, and what percentage they take before anything reaches your bank account.

Apple takes 30% of every transaction by default. If you are a small developer earning under $1 million annually you qualify for the Small Business Program which drops that cut to 15%. You have to apply for it manually. Most vibe coders never do.

Before you see a single dollar, Apple also requires you to have a paid developer account at $99 per year, a completed banking and tax profile in App Store Connect, and a signed Paid Applications Agreement. If any of these are missing, your app can be live and generating purchases that Apple holds and never releases to you.

Set up your banking and agreements before you launch. Not after.

## The Three Ways Vibe Coders Try to Monetize (and Which One Apple Will Reject)

There are three common monetization approaches vibe coders attempt. Two work. One will get your app rejected.

The first is the paid app. The user pays once at download and gets full access. Simple, clean, and fully supported by Apple. The downside is conversion. Asking someone to pay before they have used the app is a high friction ask. Works best for utility tools with an obvious and immediate value proposition.

The second is in-app purchases and subscriptions. The app is free to download and users pay for features, content, or ongoing access inside the app. This is the highest earning model on the App Store and the one Apple has built its entire payment infrastructure around. It requires StoreKit integration and proper setup in App Store Connect but it is fully supported and Apple processes everything automatically.

The third is external payments. Stripe inside the app, a link to your website, a button that says "subscribe here." This is the one Apple rejects. Every time.

If your monetization plan involves collecting money outside of Apple's system for digital goods, rebuild it before you submit. There are no exceptions and no negotiations.

## What Apple Actually Requires Before You See a Dollar

This is the setup checklist most people skip because it is not in Xcode. It lives entirely in App Store Connect and your developer account settings.

Developer Account

- Apple Developer Program membership active at $99/year

- Two-factor authentication enabled on your Apple ID

Banking and Tax

- Banking information added under Agreements, Tax, and Banking in App Store Connect

- Tax forms completed for your country of residence

- Paid Applications Agreement signed and active

- Small Business Program applied for if your annual revenue is under $1 million

App Store Connect Setup

- In-app purchase products created and configured with correct price tiers

- Subscription groups set up if offering recurring billing

- Free trial duration set if applicable

- Promotional offers configured if you plan to run them

Testing

- Sandbox testing environment used before submission

- Sandbox tester account created in App Store Connect

- Every purchase flow tested end to end in sandbox mode

- Subscription cancellation and renewal tested in sandbox

None of this is optional. Every unchecked item is either a blocked payout or a rejection.

## When Apple Actually Pays You

Most first-time builders assume money arrives shortly after a purchase. It does not.

Apple operates on a 45-day payment hold after the close of each fiscal month. If a user purchases your app in January, Apple closes that fiscal month on January 31 and holds the revenue for 45 days. You will not see that money until mid-March at the earliest.

This is not a bug. It is Apple's standard payment cycle and it applies to every developer regardless of revenue. The practical implication is that you should not expect to see any money for at least six to ten weeks after your first sale.

Your earnings are visible in App Store Connect under Payments and Financial Reports before they are released. Check there first before assuming something is broken. If your banking setup is complete and your agreements are signed, the money is coming. It is just waiting out the hold period.

## Refunds: What You Cannot Control

Apple processes refunds without asking you. A user requests a refund through Apple directly, Apple reviews it, and if approved the money comes back out of your account. You are not consulted and you cannot appeal individual decisions.

Refunds show up in your financial reports as negative transactions. If your dashboard revenue drops unexpectedly, check your refund report before assuming a technical error.

The practical response to this is building an app experience that makes refund requests unlikely. Clear onboarding, responsive support, and a free trial that sets accurate expectations before the user pays all reduce refund rates significantly. A user who understands what they are buying before they buy it almost never requests a refund.

## Freemium, One-Time Purchase, or Subscription: Which Model Fits Your App

This is the decision most vibe coders make last. It should be made first because it changes how you build the app, not just how you price it.

1. One-time purchase works when the value is immediately obvious and self-contained. A tool that does one thing well. A game with a fixed experience. A utility with no ongoing component. Price it between $0.99 and $4.99 for the best conversion rate on a first app. Higher pricing requires brand trust you have not built yet.

2. Freemium works when the core experience is genuinely useful for free and the paid layer adds meaningful depth. The free tier has to be good enough to attract users and limited enough to create upgrade motivation. If your free tier is too good nobody upgrades. If it is too limited nobody downloads. This balance is the hardest thing to get right in mobile monetization.

3. Subscriptions work when you are delivering ongoing value. Updated content, AI processing costs, live data, cloud sync. If your app does the same thing every time someone opens it and does not require ongoing infrastructure to run, a subscription is a hard sell. Users will churn and leave negative reviews about value.

The question to ask before choosing a model is this: does the value of my app increase over time or is it fixed at the moment of download? Increasing value points to subscription. Fixed value points to one-time purchase. A hybrid with a free core and paid one-time unlock is often the right answer for a first app.

## What Happens After Someone Subscribes

Most builders think the hard part is getting a user to subscribe. The harder part is keeping them.

When a subscription lapses because a payment fails, Apple enters a billing retry period of up to 60 days before cancelling the subscription entirely. During this window the user is in a grace period state. Your app needs to handle this state explicitly. If it does not, a user whose card temporarily failed will open your app, find themselves locked out of paid features, and cancel permanently rather than waiting for the billing to resolve.

When a user cancels, their subscription remains active until the end of the current billing period. Your app needs to respect this. Locking someone out the moment they cancel, before their paid period ends, generates refund requests and negative reviews.

Handle every subscription state in your code: active, grace period, lapsed, cancelled, and expired. Claude can implement all of these states in StoreKit 2 if you ask it to handle the full subscription lifecycle explicitly.

## How to Structure a Free Trial That Actually Converts

Free trials are one of the highest leverage tools in iOS monetization and most vibe coders either skip them or set them up without thinking about conversion.

The standard trial lengths are 3 days, 7 days, and 14 days. Longer trials work better for complex apps where the user needs time to build a habit. Shorter trials work better for simple utility apps where the value is obvious quickly. A 7-day trial is the right default for a first app unless you have a specific reason to go shorter or longer.

The trial period should give the user full access to everything the paid version offers. A restricted trial teaches the user what the app cannot do. A full trial teaches them what they will lose if they do not subscribe.

Send a push notification 24 hours before the trial ends if your app has notification permissions. This single touchpoint recovers a meaningful percentage of users who intended to subscribe but forgot. Apple does not send this notification automatically. You have to build it.

## The One Mistake That Gets Apps Rejected at the Payment Stage

This is the one that catches builders who have done everything else right.

If your app contains any reference to an alternative payment method for digital goods, anywhere in the app, Apple will reject it. Not just a Stripe button. Not just an external payment link. A single sentence that says "subscribe on our website for a better price" is enough. A tooltip that mentions your pricing page. A support email that links to a checkout flow.

Apple's reviewers read your app. They tap through every screen. If they find any language that directs users toward a payment option outside of StoreKit for digital goods, the rejection comes regardless of whether your in-app purchase is also set up correctly.

The rule is not just about the payment mechanism. It is about the mention of one.

Audit every screen, every tooltip, every email template your app sends, and every support link before you submit. Remove any reference to external pricing or payment for digital goods entirely.

Physical goods and services booked through the app are exempt. Everything digital is not.

## How to Set Up StoreKit Without Getting Lost in the Code

This is where most vibe coders stop reading other guides because it gets technical fast. Here is the version that gives you enough to execute without requiring a CS degree.

StoreKit 2 is Apple's current payment framework. It is what handles the entire purchase flow on the iOS side. Your app needs to be able to do four things: display your products, process a purchase, validate that the purchase was successful, and unlock the relevant content or features.

If you are using Claude or any AI coding tool to build this, here is the exact prompt structure that works:

Ask it to implement StoreKit 2 with a products array that matches your App Store Connect product IDs, a purchase function that handles the transaction, a listener that validates transactions on app launch, and an entitlements check that gates your paid content. Give it your specific product IDs from App Store Connect and ask it to handle the sandbox environment for testing.

The most common coding mistake is not implementing the transaction listener on app launch. If a user purchases and then deletes and reinstalls the app, the transaction listener is what restores their purchase. Without it they have paid and lost access and they will request a refund and leave a one star review.

Test every flow in sandbox mode before submitting. Purchase, restore, cancel, and re-subscribe. Every path a user can take through your payment flow needs to work before Apple's reviewer sees it.

## Pricing Across Territories: What You Need to Know

Setting a price in App Store Connect does not mean every user pays that price. Apple converts your price tier into local currency for every territory your app is available in. A $4.99 USD price tier becomes a different number in British pounds, Nigerian naira, and Japanese yen based on Apple's territory pricing tables.

Apple periodically adjusts these local prices when exchange rates shift significantly. When they do, you receive an email notification and a window to accept or modify the new pricing before it goes live. Most builders ignore these emails. Do not. A price increase in a key territory can spike your refund rate overnight.

You can also set custom pricing per territory in App Store Connect. This is worth doing for any market where you have meaningful downloads. A price that feels trivial in the US can feel expensive in markets with lower purchasing power. Apple offers a tool called Global Pricing that lets you set one price and automatically adjust others relative to it.

Check your territory revenue breakdown in App Store Connect monthly. If a specific country is driving downloads but not conversions, your price is probably wrong for that market.

## The Revenue Recovery Tools Most Builders Never Use

Apple offers three promotional tools inside App Store Connect that most vibe coders never configure.

Introductory offers let you give new subscribers a discounted or free period before the standard subscription price begins. This is different from a free trial. A free trial converts to full price automatically. An introductory offer can be a reduced price for a fixed period, a pay-once-and-get-three-months deal, or a free period followed by paid. Use introductory offers to reduce the friction of the first subscription commitment.

Promotional offers let you target existing and lapsed subscribers with special pricing. If a user cancelled three months ago, you can surface a win-back offer inside the app with a discounted renewal price. This requires implementing offer codes in StoreKit 2 but Claude can build this if you ask it to implement promotional offer redemption with a specific offer ID from App Store Connect.

Offer codes are one-time use codes you generate in App Store Connect and distribute outside the app. Useful for social media promotions, newsletter subscribers, or rewarding early supporters. Each code unlocks a specific subscription tier or duration you define.

None of these cost anything to set up. All three recover revenue that would otherwise be lost permanently.

## The Setup Order That Actually Works

Most guides give you the information. Here is the order to action it.

Step 1: Sign into App Store Connect and complete your banking and tax profile before you write a single line of payment code. If the agreements are not signed, nothing else matters.

Step 2: Decide your monetization model based on the framework above. Lock it before you build the payment layer. Changing models after the fact means rebuilding core functionality.

Step 3: Create your products in App Store Connect. In-app purchases, subscription groups, and price tiers are all configured here, not in Xcode. Get your product IDs from here before touching any code.

Step 4: Implement StoreKit 2 using your AI coding tool with the product IDs from Step 3. Test exclusively in sandbox mode until every flow works.

Step 5: Audit every screen for external payment references. Remove everything that mentions pricing, checkout, or payment outside of the in-app purchase flow.

Step 6: Submit. Include sandbox testing notes in your reviewer notes field so Apple's reviewer knows the payment flows have been tested.

Step 7: Apply for the Small Business Program once your app is live if your revenue is under $1 million annually. This drops Apple's cut from 30% to 15% retroactively from the date of your application.

Most vibe coders skip Step 1, get the model wrong in Step 2, and never do Step 7. All three cost real money.

The app was never the hard part. Getting paid was always the hard part. Now you have the full picture before you ship.

Follow @damidefi on X for daily Claude AI tools, crypto analysis, and the full journey to 100K. Bookmark this. Share it with one person who built an app and never turned on monetization.