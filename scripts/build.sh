#!/usr/bin/env bash
# Build (or preview) with wikilinks converted, without touching content/.
#
#   ./scripts/build.sh          production build into public/
#   ./scripts/build.sh serve    live preview on :1313
set -euo pipefail
cd "$(dirname "$0")/.."

TMP=.wikilinks-build
rm -rf "$TMP"
# templates/ holds Obsidian placeholder syntax ({{title}}) that is not valid
# YAML, so it must never reach Hugo.
cp -r content "$TMP"
rm -rf "$TMP/templates" "$TMP/.obsidian"
python3 scripts/wikilinks.py --content "$TMP" --static static

if [ "${1:-}" = "serve" ]; then
  # note: edits to content/ are picked up, but wikilinks in them won't be
  # re-converted until you restart. Rerun this script after adding one.
  exec hugo server --contentDir "$TMP" --disableFastRender
fi
exec hugo --minify --contentDir "$TMP" "${@}"
