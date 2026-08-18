#!/usr/bin/env bash
# Raw files must declare their origin through one of the dedicated input areas.
set -u

count=$(find _raw -maxdepth 1 -type f ! -name '.gitkeep' -print 2>/dev/null | awk 'END { print NR + 0 }')
if (( count > 0 )); then
  printf 'ERROR: _raw contains %d legacy file(s); move them into _raw/sources/, _raw/conversations/, _raw/external/, or _raw/research/.\n' "$count" >&2
  find _raw -maxdepth 1 -type f ! -name '.gitkeep' -print | sort | while IFS= read -r file; do
    printf 'MIGRATE: %s\n' "$file" >&2
  done
  exit 1
fi
printf 'Legacy Raw layout: clear.\n'
