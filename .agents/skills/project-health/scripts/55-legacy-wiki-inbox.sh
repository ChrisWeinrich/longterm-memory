#!/usr/bin/env bash
# Existing wiki/inbox entries must move to the Raw external queue before curation.
set -u

count=$(find wiki/inbox -type f -name '*.md' ! -name '.gitkeep' -print 2>/dev/null | awk 'END { print NR + 0 }')
if (( count > 0 )); then
  printf 'ERROR: legacy wiki/inbox contains %d note(s); move them to _raw/external/.\n' "$count" >&2
  find wiki/inbox -type f -name '*.md' ! -name '.gitkeep' -print | sort | while IFS= read -r note; do
    printf 'MIGRATE: %s\n' "$note" >&2
  done
  exit 1
fi
printf 'Legacy wiki inbox: empty.\n'
