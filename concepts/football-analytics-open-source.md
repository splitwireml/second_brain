---
title: Football Analytics Open Source
created: 2026-04-29
updated: 2026-05-03
type: concept
tags: [open-source, machine-learning, analytics, football, prediction, sports-betting]
sources: [raw/articles/xarticle-10-repos-that-mass-replace-a-100000year-football-a-2048841418592940126.md]
related_entity: [[zostaff]]
author: [[zostaff]]
---

# Football Analytics Open Source

> 10 free, open-source repositories that collectively replace a $100,000/year professional football analytics department. Curated by [[zostaff]].

## The 10 Repos

| # | Repo (t.co link) | Replaces | What It Does |
|---|------------------|----------|--------------|
| 1 | [t.co/f88gBwzDuG](https://t.co/f88gBwzDuG) | Hawkeye / Second Spectrum | YOLO player + ball tracking from any broadcast feed; assigns teams by jersey color; calculates speed, distance, possession — no sensors needed |
| 2 | [t.co/It40HRL56i](https://t.co/It40HRL56i) | Entire quant sports desk | Stacked ensemble: LightGBM + XGBoost + Neural Networks + Random Forest; auto-scrapes FBRef; ELO with dynamic K-factor; Poisson xG; MongoDB backend |
| 3 | [t.co/HBy8KHg5Vq](https://t.co/HBy8KHg5Vq) | Paid prediction platforms ($30/mo) | Full GUI app with 7 ML algorithms; downloads data from football-data.co.uk; predicts upcoming fixtures; exports to Excel; one-click operation |
| 4 | [t.co/fbX02JGfYL](https://t.co/fbX02JGfYL) | Manual feature engineering | XGBoost with 354 hand-crafted features; works for any European league; data from football-data.co.uk; plug-and-predict |
| 5 | [t.co/N4NBKWJ8yr](https://t.co/N4NBKWJ8yr) | Value bet scanners ($50/mo) | ELO + expected goals + offensive/defensive ratings; compares model probability vs Vegas lines; flags when you have edge |
| 6 | [t.co/FEGRoaWs0x](https://t.co/FEGRoaWs0x) | Bookmaker calibration tools | Gradient Boosting tuned to output probabilities matching real bookmaker odds; calibrated confidence, not just accuracy |
| 7 | [t.co/LFzoWs4dcD](https://t.co/LFzoWs4dcD) | StatsBomb xG subscription | xG model from KU Leuven researchers; LogReg + XGBoost pipelines; supports Wyscout, StatsBomb, Opta data; academic grade |
| 8 | [t.co/ZPQMuCwcAZ](https://t.co/ZPQMuCwcAZ) | xG analytics dashboards | xG on StatsBomb open data; SHAP explanations for every prediction; proper calibration; tested on FIFA World Cup 2022 |
| 9 | [t.co/tKj2sBOVzc](https://t.co/tKj2sBOVzc) | Basic prediction models | Poisson distribution for goal simulation; classical approach that still beats most ML models on draw prediction |
| 10 | [t.co/Kp046GL1KL](https://t.co/Kp046GL1KL) | Premier League prediction services | XGBoost + AdaBoost + SVM on EPL data; detailed EDA; confusion matrices; honest 56% accuracy — because football is hard |

## Stack Breakdown

### Tracking & Vision
- **Repo 1** uses YOLO for broadcast-based player/ball tracking — replaces expensive sensor systems like Hawkeye

### Prediction & Modeling
- **Repos 2, 3, 4, 10** cover the full prediction pipeline: ensemble methods, GUI apps, feature engineering, and league-specific models
- **Repo 9** is the classical baseline: Poisson distribution still competitive for draw prediction

### Betting & Calibration
- **Repo 5** finds value bets by comparing model probabilities to market odds
- **Repo 6** calibrates models to match bookmaker probability distributions

### Expected Goals (xG)
- **Repo 7** is an academic-grade xG model from KU Leuven
- **Repo 8** adds SHAP explainability and World Cup 2022 validation on StatsBomb open data

## Key Insight

The thread's central claim: a solo operator or small team can replicate a professional football analytics department using only open-source tools. The honest 56% accuracy in Repo 10 underscores that even professional-grade models struggle with football's inherent unpredictability.

## Sources

- Primary: `raw/articles/xarticle-10-repos-that-mass-replace-a-100000year-football-a-2048841418592940126.md` (zostaff, 1,003 likes, 88 RT)

## Related

- [[zostaff]] — curator of the original thread
- [[football-simulation-engine]] — related football analytics and simulation topic
