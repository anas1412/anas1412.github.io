---
title: "What It Cost to Stop Trading ICT"
date: 2026-09-20
draft: false
tags: ["trading", "systems", "vwap"]
series: ["Getting Funded"]
series_order: 4
summary: "Years inside a framework that could explain every loss, and the simpler one that replaced it because it could not."
showTableOfContents: true
---

Getting [[21-first-funded-account|funded]] changed how I behaved. It did not
change what I believed about the market, and for years what I believed was
ICT: inversion fair value gaps, change in state of delivery, stop hunts, SMT
divergence, m1 and m3 and m5 alignment.

Nobody argued me out of it. My own journal did, and I can show you the four
months where it happened.

## The notes were the evidence

I log every trade. That turned out to be what killed the method, because
somewhere along the way the notes stopped being about the market and started
being about the rules.

| Date | What I wrote |
|---|---|
| 26 Nov 2025 | hesitation, waiting for m3 cisd is useless, m1 cisd with m3 ifvg |
| 27 Nov 2025 | never wait for m3 cisd. m1 stop hunt and cisd with m3 ifvg entry are enough |
| 3 Dec 2025 | did not wait for a stop hunt or m3 ifvg proper close |
| 16 Dec 2025 | small ifvg? against bias? idk |
| 13 Jan 2026 | 50/50 area where both condition for longs and shorts are present |
| 10 Feb 2026 | plateform is shit first its fake confirmation |

Read them in order. In late November I rewrite the entry rules twice in two
days. A week later I break the version I have just written. By December I am asking myself a question I cannot answer. By
January the setup is signalling long and short in the same place. By February
I am blaming the platform.

That is not a trader improving. That is a framework failing and a person
patching it.

## Epicycles

This has happened before, on a much larger scale.

For about fourteen centuries, astronomy ran on Ptolemy's model, with the Earth
at the centre and everything circling it. It predicted the sky reasonably
well, until it did not: planets drifted, stalled, ran backwards. Each time an
observation disagreed, astronomers added another circle riding on the first,
an epicycle, and the model fitted again.

{{< figure src="/images/funded/22a.jpg" alt="Engraved plate of the Earth-centred Ptolemaic universe" caption="Andreas Cellarius, the Ptolemaic system, from *Harmonia Macrocosmica*, 1660. It fitted the sky well enough, as long as you kept adding circles. Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cellarius_ptolemaic_system.jpg)." >}}

It never broke, and that was the problem. A model that can absorb any
observation by adding one more circle can never be shown to be wrong, and a
model that cannot be wrong cannot get better.

ICT concepts work the same way. They are not wrong as descriptions. Price
does sweep liquidity, and gaps do fill. The trouble is that they are
**descriptive, not decidable**.

A fair value gap is obvious afterwards. In the moment there are four
candidates across three timeframes, and the rule for which one counts is your
own judgement. So every loss comes with an explanation already attached:
wrong gap, wrong timeframe, did not wait for the close. The method is never
falsified, only re-specified. Each new rule in my journal was an epicycle.

A system you cannot be wrong about is a system you cannot improve. It is the
same test as in [[07-the-dunning-kruger-effect-the-peak-of-mount-stupid|Mount Stupid]]:
ask what would prove you wrong. If the answer is nothing, you are not holding
a method. You are holding a story.

## What replaced it

Astronomy was not fixed by a better epicycle. It was fixed by simpler models
that made sharp predictions and could fail in public. Copernicus moved the
Sun to the centre, though he still needed some circles of his own. Kepler's
ellipses finally let them go.

{{< figure src="/images/funded/22b.jpg" alt="Engraved plate of the Sun-centred Copernican universe" caption="Andreas Cellarius, the Copernican system, from the same atlas, 1660. The sky did not change. The model did. Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Andreas_Cellarius_-_Scenographia_Systematis_Copernicani.jpg)." >}}

Mine was VWAP fades. One instrument, one setup, one target.

**VWAP** is the volume-weighted average price: the average price actually paid
across the session, weighted by how much traded at each level. It is where
the market's money has, on average, changed hands. Bands drawn a set distance
above and below it mark where price has stretched unusually far from that
average.

The idea is simple. Price leaves the mean, stays away long enough to prove it
was not noise, then comes back. I take the come-back.

### The long

{{< chart >}}
type: 'line',
data: {
  labels: ['','','','','','','','','','','','','','','','','','','',''],
  datasets: [
    { label: 'Price', data: [100.2,99.8,99.4,99.0,98.6,98.2,97.9,97.6,97.5,97.6,97.5,97.7,97.6,97.8,98.1,98.4,98.7,98.9,99.2,99.5], borderWidth: 2.5, tension: 0.25, pointRadius: 0 },
    { label: 'VWAP', data: [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100], borderWidth: 1.5, borderDash: [6,4], pointRadius: 0 },
    { label: 'Lower band', data: [98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98], borderWidth: 1, pointRadius: 0 },
    { label: 'Target 1R', data: [98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8,98.8], borderWidth: 1, borderDash: [3,3], pointRadius: 0 },
    { label: 'Stop', data: [97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4,97.4], borderWidth: 1, borderDash: [3,3], pointRadius: 0 }
  ]
},
options: { scales: { y: { title: { display: true, text: 'Price' } }, x: { title: { display: true, text: 'M5 candles' } } } }
{{< /chart >}}

Candles 7 to 14 close below the lower band. That is the part that matters.
Candle 15 is the first M5 candle to **close** back above it, and that close is
the entry. The stop goes under the extreme. The target is 1R, which the fade
reaches well before it gets anywhere near VWAP.

### The short

The same thing upside down: price pushes above the upper band, holds there,
then an M5 candle closes back below.

{{< chart >}}
type: 'line',
data: {
  labels: ['','','','','','','','','','','','','','','','','','','',''],
  datasets: [
    { label: 'Price', data: [99.8,100.2,100.6,101.0,101.4,101.8,102.1,102.4,102.5,102.4,102.5,102.3,102.4,102.2,101.9,101.6,101.3,101.1,100.8,100.5], borderWidth: 2.5, tension: 0.25, pointRadius: 0 },
    { label: 'VWAP', data: [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100], borderWidth: 1.5, borderDash: [6,4], pointRadius: 0 },
    { label: 'Upper band', data: [102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102], borderWidth: 1, pointRadius: 0 },
    { label: 'Target 1R', data: [101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2,101.2], borderWidth: 1, borderDash: [3,3], pointRadius: 0 },
    { label: 'Stop', data: [102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6,102.6], borderWidth: 1, borderDash: [3,3], pointRadius: 0 }
  ]
},
options: { scales: { y: { title: { display: true, text: 'Price' } }, x: { title: { display: true, text: 'M5 candles' } } } }
{{< /chart >}}

## The rule that does the work

It is not a reversal trade. I am not calling a top or a bottom.

Price has to **break the band, stay outside it, and then revert**. The staying
is the whole filter. A wick through the band that snaps straight back is not
acceptance. It is noise, and it is the trade that looks most like the setup
while being nothing like it.

{{< mermaid >}}
graph TD
  A[Price reaches the band] --> B{Did it close outside?}
  B -- no, only a wick --> X[No trade]
  B -- yes --> C{Did it stay outside<br/>for several candles?}
  C -- no, snapped straight back --> X
  C -- yes, acceptance --> D{M5 candle closes<br/>back inside the band?}
  D -- no --> E[Wait]
  E --> D
  D -- yes --> F[Enter on that close<br/>stop beyond the extreme<br/>target 1R]
{{< /mermaid >}}

| | Qualifies | Does not |
|---|---|---|
| Contact with band | closes outside it | wick only |
| Time outside | several candles, held | one candle, snapped back |
| Approach | extended away, returning | already at the mean |
| Trigger | M5 **close** back inside | trading the wick in real time |
| Target | 1R | held for the full move to VWAP |

## Why it is better, and it is not the win rate

The win rate is not obviously higher. The difference is that **I can be wrong
about it**.

Every part of the setup is something a computer could check. Did the candle
close outside the band, yes or no. Did it stay outside for several candles,
yes or no. Did an M5 candle close back inside, yes or no. There is no
timeframe to argue with afterwards, and no fourth gap I should have used
instead.

That turns a losing month into information rather than an excuse. If the edge
stops working, the data will show it, because the data is answering the same
question every time. Under ICT I could never tell a bad month from a
misapplication, so I always concluded misapplication, and I always added
another circle.

The value of a system is not how well it describes the market. It is whether
it can tell you that you are wrong.
