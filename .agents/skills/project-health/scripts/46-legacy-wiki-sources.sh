#!/usr/bin/env bash
# Curated pages use wiki/pages; old wiki/sources content needs an explicit move.
set -u

count=$(find wiki/sources -type f -name '*.md' ! -name '.gitkeep' -print 2>/dev/null | awk 'END { print NR + 0 }')
if (( count > 0 )); then
  printf 'ERROR: wiki/sources contains %d legacy page(s); move them to wiki/pages/.\n' "$count" >&2
  find wiki/sources -type f -name '*.md' ! -name '.gitkeep' -print | sort | while IFS= read -r page; do
    printf 'MIGRATE: %s\n' "$page" >&2
  done
  exit 1
fi
printf 'Legacy wiki sources: clear.\n'
