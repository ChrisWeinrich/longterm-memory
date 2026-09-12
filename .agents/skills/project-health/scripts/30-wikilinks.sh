#!/usr/bin/env bash
# Foundation documentation and curated Wiki wikilinks resolve to an existing
# Markdown page by path or filename. Project-local domain artifacts may define
# their own link conventions and validation.
set -u

link_exists() {
  local target=$1 normalized
  normalized=${target%%#*}
  normalized=${normalized%%|*}
  normalized=${normalized#./}
  [[ -z "$normalized" ]] && return 0
  [[ "$normalized" == http://* || "$normalized" == https://* ]] && return 0
  [[ -f "$normalized" || -f "$normalized.md" ]] && return 0
  find . -type f -name '*.md' ! -path './.git/*' ! -path '*/.venv/*' \
    -exec sh -c 'for file; do [ "${file##*/}" = "$1.md" ] && exit 0; done; exit 1' sh "$normalized" {} + >/dev/null 2>&1
}

failed=0
while IFS= read -r -d '' file; do
  while IFS= read -r link; do
    if ! link_exists "$link"; then
      printf 'ERROR: %s: broken wikilink [[%s]]\n' "$file" "$link" >&2
      failed=1
    fi
  done < <(grep -oE '\[\[[^]]+\]\]' "$file" 2>/dev/null | sed -E 's/^\[\[//; s/\]\]$//')
done < <(
  find README.md AGENTS.md MOC.md wiki _research _mcp/wiki-mcp/README.md \
    -type f -name '*.md' ! -path '*/.venv/*' -print0
)

exit "$failed"
