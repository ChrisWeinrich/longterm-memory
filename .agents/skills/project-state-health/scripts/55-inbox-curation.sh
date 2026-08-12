#!/usr/bin/env bash
# Inbox entries are intentionally unreviewed and need human curation.
set -u

count=$(find wiki/inbox -type f -name '*.md' -print 2>/dev/null | awk 'END { print NR + 0 }')
printf 'Inbox: %d note(s) awaiting human curation.\n' "$count"
if (( count > 0 )); then
  find wiki/inbox -type f -name '*.md' -print | sort | while IFS= read -r note; do
    printf 'NEEDS CURATION: %s\n' "$note" >&2
  done
  exit 1
fi
