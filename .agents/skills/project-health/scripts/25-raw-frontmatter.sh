#!/usr/bin/env bash
# Managed Raw Markdown records preserve provenance but deliberately have no state.
set -u

has_key() {
  awk -v key="$2" 'NR > 1 && $0 == "---" { exit } index($0, key ":") == 1 { found = 1 } END { exit !found }' "$1"
}

failed=0
while IFS= read -r -d '' file; do
  if [[ "$(head -n 1 "$file")" != "---" ]]; then
    printf 'ERROR: %s: managed Raw Markdown needs YAML frontmatter\n' "$file" >&2
    failed=1
    continue
  fi
  for key in title type tags origin; do
    if ! has_key "$file" "$key"; then
      printf "ERROR: %s: missing Raw frontmatter key '%s'\\n" "$file" "$key" >&2
      failed=1
    fi
  done
  if ! has_key "$file" created && ! has_key "$file" received_at; then
    printf 'ERROR: %s: Raw Markdown needs created or received_at provenance\n' "$file" >&2
    failed=1
  fi
  if has_key "$file" state; then
    printf 'ERROR: %s: Raw Markdown must not declare state\n' "$file" >&2
    failed=1
  fi
done < <(find _raw/sources _raw/conversations _raw/external _raw/research -type f -name '*.md' ! -name '.gitkeep' -print0 2>/dev/null)

exit "$failed"
