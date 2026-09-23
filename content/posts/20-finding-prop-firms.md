---
title: "Someone Else's Capital"
date: 2023-01-01
draft: false
tags: ["trading", "propfirms"]
series: ["Getting Funded"]
series_order: 2
summary: "January 2023. I heard about FTMO in the same month I started my first engineering job, and it changed what I thought the problem was."
---

January 2023 was a crowded month. I started my first real engineering job,
as a DevOps engineer at Kamioun. And somewhere in the middle of it, I heard
about FTMO.

Until then I thought my problem was capital. A small account means small
positions, small positions mean small money, so the plan was to grow the
account slowly until the numbers were worth the effort. That plan takes
years, and one bad week can undo most of it.

Prop firms change the problem. You are no longer trying to grow capital. You
are trying to prove you can be trusted with someone else's.

{{< figure src="/images/funded/20a.jpg" alt="The trading floor of the Chicago Board of Trade, rows of desks and screens" caption="The trading floor of the Chicago Board of Trade. Firms have always staked traders with the house's money. What changed is that anyone can now apply from a laptop. CC0, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Trading_Floor_in_the_Chicago_Board_of_Trade_Building.png)." >}}

## How it works

You pay a fee and trade a simulated account under fixed rules. Hold to the
rules and hit the target, and you trade a funded account and keep most of
the profit.

FTMO's two-step evaluation, as it stands today:

| Rule | Challenge | Verification |
|---|---|---|
| Profit target | 10% | 5% |
| Max daily loss | 5% | 5% |
| Max total loss | 10% | 10% |
| Minimum trading days | 4 | 4 |

## Read that table again

One rule is about making money. Three are about not losing it.

{{< chart >}}
type: 'line',
data: {
  labels: ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'],
  datasets: [
    { label: 'Passes', data: [0,1.2,0.4,2.1,3.0,2.2,3.8,4.5,3.9,5.6,6.4,5.8,7.3,8.1,7.6,9.2,10.3], borderWidth: 2.5, tension: 0.2, pointRadius: 0 },
    { label: 'Fails', data: [0,2.0,3.5,4.8,6.1,4.2,2.9,1.0,-1.8,-3.5,-5.2,-6.9,-8.4,-10.2], borderWidth: 2.5, tension: 0.2, pointRadius: 0, borderDash: [6,4] },
    { label: 'Target +10%', data: [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], borderWidth: 1, borderDash: [3,3], pointRadius: 0 },
    { label: 'Max loss -10%', data: [-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10], borderWidth: 1, borderDash: [3,3], pointRadius: 0 }
  ]
},
options: { scales: { x: { title: { display: true, text: 'Trading day' } }, y: { title: { display: true, text: 'Account %' } } } }
{{< /chart >}}

*An illustration of two attempts. The one that fails is ahead by 6% on day
four, further ahead than the one that passes ever was at that point. It fails
anyway, because it never stopped the bleeding.*

I had been treating risk management as the boring half of trading, the part
you do so you can keep doing the interesting part. The evaluation says the
opposite. You can hit the target and still fail. You cannot breach the
drawdown and pass on the strength of your entries.

The firm is not asking whether you can predict. It is asking whether you are
consistent enough to be a known quantity. Those are different skills, and
only one of them was what I had been practising since
[[19-the-day-i-started-trading|October]].

## The house is not neutral

It is worth being honest about the business. Most people who buy a challenge
do not pass it, and the fees are a large part of how these firms earn. The
rules are not a favour.

But they are not a trick either. They are a specification, the clearest
description of the job I had ever been given. Most people read a challenge
as an obstacle between them and the money. It is closer to a definition of
what a professional does.

## What I got wrong

I thought passing was the hard part.

Passing is a deadline with a target, and a deadline makes you trade. Keeping
a funded account has neither, which removes the one thing that had been
forcing discipline on me. That lesson came later, and it was not cheap.
