#!/usr/bin/env bash
# Curation-ready Raw inputs require at least one valid curated source reference.
set -u

references_for() {
  awk '
    NR > 1 && $0 == "---" { exit }
    /^source:[[:space:]]*/ {
      value = $0; sub(/^source:[[:space:]]*/, "", value)
      gsub(/^"|"$/, "", value); gsub(/^'\''|'\''$/, "", value)
      if (value != "") print value
      next
    }
    /^sources:[[:space:]]*$/ { in_sources = 1; next }
    in_sources && /^[[:space:]]+-[[:space:]]+/ {
      value = $0; sub(/^[[:space:]]+-[[:space:]]+/, "", value)
      gsub(/^"|"$/, "", value); gsub(/^'\''|'\''$/, "", value)
      print value
      next
    }
    in_sources { in_sources = 0 }
  ' "$1"
}

failed=0
referenced_raw=$(mktemp)
trap 'rm -f "$referenced_raw"' EXIT

while IFS= read -r -d '' page; do
  while IFS= read -r reference; do
    if [[ "$reference" != _raw/* ]]; then
      printf 'ERROR: %s: source reference must start with _raw/: %s\n' "$page" "$reference" >&2
      failed=1
    elif [[ ! -f "$reference" ]]; then
      printf 'ERROR: %s: referenced Raw input does not exist: %s\n' "$page" "$reference" >&2
      failed=1
    else
      printf '%s\n' "$reference" >> "$referenced_raw"
    fi
  done < <(references_for "$page")
done < <(find wiki/pages -type f -name '*.md' -print0 2>/dev/null)

total=0
pending=0
while IFS= read -r -d '' raw; do
  total=$((total + 1))
  if ! grep -Fqx "$raw" "$referenced_raw"; then
    printf 'NEEDS CURATION: Raw input has no curated sources reference: %s\n' "$raw" >&2
    pending=$((pending + 1))
    failed=1
  fi
done < <(
  find _raw/sources _raw/conversations _raw/external -type f ! -name '.gitkeep' -print0 2>/dev/null
  find _raw/research -type f -name report.md -print0 2>/dev/null
)

printf 'Raw curation coverage: %d ready input(s), %d awaiting curation.\n' "$total" "$pending"
exit "$failed"
