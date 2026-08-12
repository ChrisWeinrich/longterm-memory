#!/usr/bin/env bash
# Every source file in _raw/ needs exactly one traceable wiki-source page.
set -u

frontmatter_value() {
  awk -v key="$2" '
    NR > 1 && $0 == "---" { exit }
    index($0, key ":") == 1 {
      value = substr($0, length(key) + 2)
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", value)
      gsub(/^"|"$/, "", value)
      gsub(/^'\''|'\''$/, "", value)
      print value
      exit
    }
  ' "$1"
}

failed=0
pages=0
while IFS= read -r -d '' page; do
  [[ "$(frontmatter_value "$page" type)" == wiki-source ]] || continue
  source_path=$(frontmatter_value "$page" source)
  if [[ -z "$source_path" ]]; then
    printf 'ERROR: %s: wiki-source page has no source frontmatter path\n' "$page" >&2
    failed=1
    continue
  fi
  if [[ ! -f "$source_path" ]]; then
    printf 'ERROR: %s: source does not exist: %s\n' "$page" "$source_path" >&2
    failed=1
  fi
  pages=$((pages + 1))
done < <(find wiki/sources -type f -name '*.md' -print0 2>/dev/null)

raw_total=0
missing=0
duplicates=0
while IFS= read -r -d '' raw; do
  raw_total=$((raw_total + 1))
  matches=$(
    while IFS= read -r -d '' page; do
      [[ "$(frontmatter_value "$page" type)" == wiki-source ]] || continue
      [[ "$(frontmatter_value "$page" source)" == "$raw" ]] && printf '%s\n' "$page"
    done < <(find wiki/sources -type f -name '*.md' -print0 2>/dev/null)
  )
  count=$(awk 'NF { count++ } END { print count + 0 }' <<< "$matches")
  if (( count == 0 )); then
    printf 'ERROR: raw source not ingested: %s\n' "$raw" >&2
    missing=$((missing + 1))
    failed=1
    continue
  fi
  if (( count > 1 )); then
    printf 'ERROR: raw source has %d wiki-source pages: %s (%s)\n' "$count" "$raw" "$matches" >&2
    duplicates=$((duplicates + 1))
    failed=1
  fi
done < <(find _raw -type f ! -name '.gitkeep' -print0 2>/dev/null)

printf 'Raw source ingestion: %d raw file(s), %d wiki-source page(s), %d missing, %d duplicate mapping(s).\n' \
  "$raw_total" "$pages" "$missing" "$duplicates"
exit "$failed"
