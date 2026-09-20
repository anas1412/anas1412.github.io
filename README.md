# anas1412.github.io

Personal site. Plain markdown in, static site out — [Hugo](https://gohugo.io)
with the [Blowfish](https://github.com/nunocoracao/blowfish) theme, deployed to
GitHub Pages on every push to `main`.

## Writing from Obsidian

Open **`content/`** as your Obsidian vault. Notes go in `content/notes/`.

```sh
git add -A && git commit -m "new note" && git push   # ~1 min to live
```

**Every note needs frontmatter** — without a `title:` Hugo publishes an
untitled page. Set it up once so you never think about it again:

1. Obsidian → Settings → Core plugins → enable **Templates**
2. Templates → Template folder location → `templates`
3. New note → `Ctrl+P` → *Insert template* → `note`

Set `draft: true` to keep a note private; it stays in the repo but is never
built. Remove it to publish.

## Local preview

```sh
hugo server     # localhost:1313, live reload
```

## Layout

| Path | What |
|---|---|
| `content/_index.md` | home page bio |
| `content/about.md` | experience, education, skills |
| `content/notes/` | your notes — add `.md` files here |
| `content/projects.md` | projects |
| `content/templates/` | Obsidian templates (never published) |
| `config/_default/params.toml` | `colorScheme` — 15 options ship with the theme |

The theme is a Hugo Module, not vendored code — update with
`hugo mod get -u`.
