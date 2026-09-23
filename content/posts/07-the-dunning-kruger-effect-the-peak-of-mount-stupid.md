---
title: "The Peak of Mount Stupid"
date: 2025-07-31
draft: false
tags:
  - notes-from-the-edge
series:
  - Notes from the Edge
series_order: 7
summary: "The famous confidence curve is not in the paper it is named after. That turns out to be the best illustration of the effect there is."
---

You have probably seen the chart. Confidence shoots up to a peak labelled
"Mount Stupid", crashes into a "Valley of Despair", then climbs slowly toward
a plateau of real expertise.

{{< figure src="/images/notes/07a.jpg" alt="The popular Dunning-Kruger curve with Mount Stupid and the Valley of Despair" caption="The chart everyone shares. It is not from the paper. Illustration CC0, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Dunning%E2%80%93Kruger_Effect_01.svg)." >}}

It is not in the paper. The label comes from an internet comic, not from
psychology. Millions of people have confidently shared a chart they never
checked, about the danger of confidence without knowledge. It is hard to
imagine a better demonstration of the idea.

## What Kruger and Dunning actually found

In 1999 David Dunning and Justin Kruger gave people tests of humour, grammar
and logic, then asked them to guess how they had done compared with everyone
else.

{{< chart >}}
type: 'line',
data: {
  labels: ['Bottom quartile', 'Second', 'Third', 'Top quartile'],
  datasets: [
    { label: 'Where they thought they ranked', data: [62, 63, 68, 75], borderWidth: 2.5, tension: 0.3, pointRadius: 4 },
    { label: 'Where they actually ranked', data: [12, 37, 62, 87], borderWidth: 2.5, tension: 0.3, pointRadius: 4, borderDash: [6,4] }
  ]
},
options: {
  scales: {
    y: { min: 0, max: 100, title: { display: true, text: 'Percentile' } },
    x: { title: { display: true, text: 'Grouped by actual score' } }
  }
}
{{< /chart >}}

*Approximate. The bottom-quartile figures, 12th percentile actual against 62nd
estimated, are from the paper's abstract; the other points show the shape.*

Two findings, not one:

- **The least skilled overestimate badly.** The skills you need to be good at
  something are the same skills you need to notice you are bad at it.
- **The most skilled slightly underestimate.** They assume what is easy for
  them is easy for everyone.

Later researchers have argued part of the pattern is a statistical artefact.
The practical lesson survives the argument: your confidence is a poor
measurement of your competence, and worst exactly where you know least.

{{< figure src="/images/notes/07b.jpg" alt="Scatter plot of subjective against objective IQ with a shallow trend line" caption="Self-estimates that are merely noisy, plotted against real scores. Noise alone flattens the line: low scorers appear to overestimate and high scorers to underestimate. Simulation by Phlsph7, CC BY-SA 4.0, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Dunning-kruger_effect_-_simulation1.svg)." >}}

> "The fundamental cause of the trouble is that in the modern world the stupid are cocksure while the intelligent are full of doubt."
> Bertrand Russell, *The Triumph of Stupidity*

## The trader's version

In trading, Mount Stupid usually has a specific shape: a small sample in a
friendly market.

Thirty trades in a clean trend, most of them winners. The trader concludes he
has an edge. But thirty trades cannot tell edge from luck, and the trend that
paid him will not last. The confidence arrives long before the evidence
does.

## Staying off the mountain

- **Ask what would prove you wrong.** If nothing could, you are not holding a
  belief, you are holding an identity.
- **Count your sample.** Ten good results is an anecdote.
- **Find people better than you.** Their feedback is the only mirror that
  works when your own judgement is the thing in question.
- **Treat certainty as a warning light**, not a green light.

This is the counterweight to [[06-the-power-of-self-image-who-you-believe-you-are|self-image]].
Believe in your process. Hold your conclusions loosely.
