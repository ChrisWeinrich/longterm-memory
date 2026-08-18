#!/usr/bin/env bash
# The active wiki index may refer only to accepted pages.
set -u

[[ -f wiki/index.md ]] || exit 0

failed=0
while IFS= read -r link; do
  target=${link%%#*}
  target=${target%%|*}
  target=${target#./}
  page="${target}.md"
  [[ -f "$target" ]] && page=$target
  if [[ ! -f "$page" ]]; then
    page=$(find wiki -type f -name "${target##*/}.md" -print -quit 2>/dev/null)
  fi
  [[ -n "$page" && -f "$page" ]] || continue
  state=$(awk 'NR > 1 && $0 == "---" { exit } index($0, "state:") == 1 { print $2; exit }' "$page")
  if [[ "$state" != accepted ]]; then
    printf 'ERROR: wiki/index.md links to non-accepted page: %s (%s)\n' "$page" "$state" >&2
    failed=1
  fi
done < <(grep -oE '\[\[[^]]+\]\]' wiki/index.md 2>/dev/null | sed -E 's/^\[\[//; s/\]\]$//')

exit "$failed"
