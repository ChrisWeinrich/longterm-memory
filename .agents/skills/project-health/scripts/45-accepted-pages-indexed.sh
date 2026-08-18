#!/usr/bin/env bash
# Accepted curated pages must be reachable from the active wiki index.
set -u

[[ -f wiki/index.md ]] || exit 0

state_of() {
  awk 'NR > 1 && $0 == "---" { exit } index($0, "state:") == 1 { print $2; exit }' "$1"
}

failed=0
accepted=0
unindexed=0
while IFS= read -r -d '' page; do
  [[ "$(state_of "$page")" == accepted ]] || continue
  accepted=$((accepted + 1))
  name=${page##*/}
  name=${name%.md}
  if ! grep -Fq "[[$name]]" wiki/index.md && ! grep -Fq "[[$name|" wiki/index.md && ! grep -Fq "[[$page]]" wiki/index.md; then
    printf 'ERROR: accepted page is not linked from wiki/index.md: %s\n' "$page" >&2
    unindexed=$((unindexed + 1))
    failed=1
  fi
done < <(find wiki/pages -type f -name '*.md' -print0 2>/dev/null)

printf 'Active wiki coverage: %d accepted source page(s), %d unindexed.\n' "$accepted" "$unindexed"
exit "$failed"
