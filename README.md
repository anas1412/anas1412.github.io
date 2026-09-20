# anas1412.github.io

Personal site — notes, microblog, projects. Built with [Hugo](https://gohugo.io)
and the [Blowfish](https://github.com/nunocoracao/blowfish) theme, deployed to
GitHub Pages on every push to `main`.

## Write

Content is plain markdown in `content/`. Add a file, push, it's live.

```sh
hugo server          # local preview at localhost:1313
hugo --minify        # production build into public/
```

## Structure

| Path | What |
|---|---|
| `content/_index.md` | home page bio |
| `content/about.md` | experience, education, skills |
| `content/notes/` | longer pieces |
| `content/microblog.md` | short dated entries |
| `content/projects.md` | projects |
| `config/_default/` | site config — `params.toml` holds the colour scheme |

The theme is a Hugo Module, not vendored code, so updating it is
`hugo mod get -u`. Change the look with `colorScheme` in
`config/_default/params.toml` — 15 schemes ship with the theme.

The previous Alpine.js site is preserved on the `old-site-backup` branch.
