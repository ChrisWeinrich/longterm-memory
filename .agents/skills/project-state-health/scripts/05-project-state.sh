#!/usr/bin/env bash
# Compact, read-only inventory of the rendered project's Markdown knowledge.
set -u

records=$(
  while IFS= read -r file; do
    state=$(awk 'NR > 1 && $0 == "---" { exit } index($0, "state:") == 1 { print $2; exit }' "$file")
    type=$(awk 'NR > 1 && $0 == "---" { exit } index($0, "type:") == 1 { print $2; exit }' "$file")
    printf '%s\t%s\n' "${state:-invalid}" "${type:-unclassified}"
  done < <(find . -type f -name '*.md' ! -path './.git/*' ! -path '*/.venv/*' -print)
)

count_state() {
  awk -F '\t' -v state="$1" '$1 == state { count++ } END { print count + 0 }' <<< "$records"
}

total=$(awk 'NF { count++ } END { print count + 0 }' <<< "$records")
accepted=$(count_state accepted)
draft=$(count_state draft)
archived=$(count_state archived)
invalid=$((total - accepted - draft - archived))
non_accepted=$((total - accepted))

printf '%s\n' 'Project state'
printf '%s\n' '-------------'
printf 'Markdown documents: %d\n' "$total"
printf 'Accepted:           %d\n' "$accepted"
printf 'Draft:              %d\n' "$draft"
printf 'Archived:           %d\n' "$archived"
printf 'Invalid/unclassified: %d\n' "$invalid"
printf 'Non-accepted:       %d\n' "$non_accepted"
printf '%s\n' 'Document types:'
awk -F '\t' '{ count[$2]++ } END { for (type in count) print type "\t" count[type] }' <<< "$records" | sort | while IFS=$'\t' read -r type count; do
  printf '  %s: %s\n' "$type" "$count"
done

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  changes=$(git status --porcelain | awk 'END { print NR + 0 }')
  printf 'Uncommitted paths:  %d\n' "$changes"
fi
