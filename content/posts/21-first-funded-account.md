---
title: "Two Months Before the First Trade"
date: 2023-03-01
draft: false
tags: ["trading", "propfirms"]
series: ["Getting Funded"]
series_order: 3
summary: "March 2023. I heard about prop firms in January and did not take a trade on one until March. The gap is the story."
---

I heard about prop firms in January. I did not take a trade on one until
March.

Two months without trading, from someone who had been trading most days since
October. It was not patience. It was the first time being wrong had a price
attached before I started.

{{< figure src="/images/funded/21a.jpg" alt="Damocles on a throne beneath a sword hanging by a single hair" caption="Richard Westall, *The Sword of Damocles*, 1812. Damocles envied the king until he was invited onto the throne, under a sword hung by a single hair. Some decisions look different once the cost is hanging over you. Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:The_Sword_of_Damocles_by_Richard_Westall.jpg)." >}}

## Why the fee changed everything

On a demo account you can start now, be wrong, and start again this
afternoon. There is no forcing function, so there is no preparation.

A challenge fee is real money paid in advance for the privilege of being
measured. It changes the question. Not *what do I think the market will do?*
but *do I have something I can repeat under a drawdown limit?*

I did not. So I spent two months getting one.

## What the rules did

The rules did the teaching. A daily loss limit is a circuit breaker: it trips
before the damage spreads. It is a hard stop on exactly the behaviour that
had been quietly costing me since October. Lose, want it back, size up to get
it. You cannot revenge-trade under a 5% daily cap. The account closes before
your feelings do.

{{< chart >}}
type: 'bar',
data: {
  labels: ['Mon','Tue','Wed','Thu','Fri','Mon','Tue','Wed','Thu','Fri'],
  datasets: [
    { type: 'bar', label: 'Daily P&L %', data: [0.8,-1.2,1.5,0.6,-5.0,0.9,-0.7,1.8,0.4,1.1], borderWidth: 1 },
    { type: 'line', label: 'Daily loss limit', data: [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5], borderWidth: 1.5, borderDash: [4,4], pointRadius: 0 }
  ]
},
options: { scales: { y: { min: -6, max: 3, title: { display: true, text: 'Account %' } } } }
{{< /chart >}}

*An illustration. The bad Friday is stopped at the limit, not wherever the
anger would have taken it. Two weeks later the account is still alive, and
slightly up.*

That was the thing I could not impose on myself for five months. The
constraint was external, and it worked precisely because it was external.

| My own account | A funded account |
|---|---|
| a bad day can become a bad month | the day ends when the limit says so |
| position size is a decision | position size is arithmetic |
| no deadline, so no urgency | a target and a window |
| nobody checks | the rules check, every day |

## What it did not fix

It did not make me a better analyst. The entries in March were the entries in
February.

What it did was remove the worst version of me from the equation, and most of
the gap between losing and not losing turned out to be sitting in that
version, not in the setups.

The [[16-the-be-do-have-model-attracting-your-reality|Be-Do-Have]] idea is
easy to dismiss as self-help until you watch external rules produce the
behaviour you could not produce on your own. The firm made me trade like a
professional before I was one. The behaviour came first. The identity
followed.

What came after, years spent inside ICT concepts before I let them go, is
[[22-what-it-cost-to-stop-trading-ict|its own story]].
