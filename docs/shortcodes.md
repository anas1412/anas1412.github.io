# Blowfish shortcodes

Every shortcode available in the installed theme (v3.6.0) — 46 of them,
verified against `layouts/shortcodes/` in the module, not just the website.

Upstream docs: <https://blowfish.page/docs/shortcodes/>

Shortcodes go in the body of any `.md` file in `content/`. They do **not**
work in frontmatter. `{{< … >}}` passes content through raw; `{{% … %}}`
renders it as markdown first.

## Layout and structure

| Shortcode | What it does | Key parameters |
|---|---|---|
| `accordion` / `accordionItem` | collapsible panels | `mode` (collapse/open), `separated`; item: `title`, `open`, `icon`, `align` |
| `tabs` / `tab` | tabbed variants of the same content | `group`, `default`; tab: `label`, `icon`, `md` |
| `steps` / `step` | numbered process | step: `number`, `title` |
| `timeline` / `timelineItem` | vertical timeline | item: `icon`, `header`, `badge`, `subheader`, `md` |
| `feature-grid` / `feature` | responsive feature section | grid: `columns` (3 or 4); feature: `icon`, `title`, `url`, `label` |
| `stats` / `stat` | metrics grid | stat: `value`, `label` |
| `keywordList` / `keyword` | highlighted terms | keyword: `icon` |
| `ltr` / `rtl` | direction switch for mixed scripts | — |

```
{{< steps >}}
  {{< step number="1" title="Configure" >}}What to do.{{< /step >}}
  {{< step number="2" title="Deploy" >}}What happens next.{{< /step >}}
{{< /steps >}}
```

## Callouts and emphasis

| Shortcode | What it does | Key parameters |
|---|---|---|
| `alert` | coloured message box | `icon`, `iconColor`, `cardColor`, `textColor` |
| `badge` | small metadata pill | none |
| `lead` | emphasised opening paragraph | none |
| `button` | styled button | `href` or `pageRef`, `target`, `rel` |
| `cta` | call-to-action button | `url`, `label`, `style` (primary/outline) |
| `typeit` | typewriter effect | `tag`, `speed`, `loop`, `lifeLike`, `startDelay` |

Admonitions need no shortcode — Hugo renders GitHub/Obsidian syntax natively:

```
> [!TIP]
> This works in plain markdown, and in Obsidian too.
```

## Media

| Shortcode | What it does | Key parameters |
|---|---|---|
| `figure` | optimised image with caption | `src`, `alt`, `caption`, `href`, `class`, `nozoom` |
| `gallery` | grid of images | inner `<img class="grid-w33">` |
| `carousel` | image slider | `images` (glob), `captions`, `aspectRatio`, `interval` |
| `video` | local or remote video | `src`, `poster`, `autoplay`, `loop`, `muted`, `controls`, `start`, `end`, `ratio` |
| `youtubeLite` | lightweight YouTube embed | `id`, `label`, `params` |
| `icon` | inline SVG icon at text size | icon name |
| `swatches` | colour palette strip | up to 3 hex codes |

## Data and diagrams

| Shortcode | What it does |
|---|---|
| `chart` | Chart.js — body is a Chart.js config |
| `mermaid` | Mermaid diagrams |
| `katex` | maths, inline `\(…\)` or block `$$…$$` |

```
{{< chart >}}
type: 'line',
data: { labels: ['Jan','Feb'], datasets: [{ label: 'R', data: [1.2, -0.4] }] }
{{< /chart >}}
```

```
{{< mermaid >}}
graph LR
  Sheet --> Script --> Site
{{< /mermaid >}}
```

## Embeds and cards

| Shortcode | What it embeds | Key parameters |
|---|---|---|
| `github` | repo card with live stats | `repo` (`user/name`), `showThumbnail` |
| `gitlab` | project card | `projectID`, `baseURL` |
| `gitea` / `forgejo` / `codeberg` | self-hosted git cards | `repo`, `server` |
| `gist` | GitHub gist | username, gist id, optional filename |
| `huggingface` | model or dataset card | `model` or `dataset` |
| `ansible` | Galaxy role or collection | `role` or `collection` |
| `article` | another page on this site | `link`, `showSummary`, `compactSummary` |
| `list` | recent articles | `limit`, `title`, `cardView`, `where`, `value` |
| `codeimporter` | remote source file | `url`, `type`, `startLine`, `endLine` |
| `mdimporter` | remote markdown | `url` |
| `email` | obfuscated mailto | `email`, `text`, `subject` |

## Notes

- **Block shortcodes carry no outer margin.** `github`, `button`, `cta`,
  `chart` and friends render as bare `<div>`/`<a>` elements, not paragraphs,
  so a blank line between two of them produces **zero** visual gap. Wrapping
  in `<p>` does *not* work — goldmark drops it. Wrap in a `<div>` with one of
  the theme's spacing classes instead; these are confirmed present in the
  compiled CSS: `mt-4 mt-6 mt-8 my-8 mb-6 mb-8 pt-8`.

  ```
  ![screenshot](…)

  <div class="mt-8">{{< button href="…" >}}Open the live version{{< /button >}}</div>
  ```

- Shortcodes render only through Hugo. **Obsidian shows them as raw text** —
  expected, not a bug.
- `{{< … >}}` vs `{{% … %}}` matters: use the percent form when the body is
  markdown you want parsed.
- `chart`, `mermaid` and `typeit` pull JavaScript at runtime; they inflate the
  page and don't render in an RSS reader.
- Cards that fetch live stats (`github`, `gitlab`, `huggingface`) hit those
  APIs when the page loads, so they fail quietly offline and can rate-limit.
