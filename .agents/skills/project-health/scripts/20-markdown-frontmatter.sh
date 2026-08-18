#!/usr/bin/env bash
# Curated Markdown documents have the standard frontmatter and a valid state.
set -u

failed=0
while IFS= read -r -d '' file; do
  if [[ "$(head -n 1 "$file")" != "---" ]]; then
    printf 'ERROR: %s: missing opening YAML frontmatter delimiter\n' "$file" >&2
    failed=1
    continue
  fi
  if ! awk 'NR > 1 && $0 == "---" { found = 1; exit } END { exit !found }' "$file"; then
    printf 'ERROR: %s: missing closing YAML frontmatter delimiter\n' "$file" >&2
    failed=1
    continue
  fi
  for key in title type tags state; do
    if ! awk -v key="$key" 'NR > 1 && $0 == "---" { exit } index($0, key ":") == 1 { found = 1 } END { exit !found }' "$file"; then
      printf "ERROR: %s: missing frontmatter key '%s'\\n" "$file" "$key" >&2
      failed=1
    fi
  done
  state=$(awk 'NR > 1 && $0 == "---" { exit } index($0, "state:") == 1 { print $2; exit }' "$file")
  case "$state" in
    draft|accepted|archived) ;;
    *) printf "ERROR: %s: invalid state '%s' (use draft, accepted, or archived)\\n" "$file" "$state" >&2; failed=1 ;;
  esac
done < <(find . -type f -name '*.md' ! -path './.git/*' ! -path './_raw/*' ! -path './_templates/raw-*.md' ! -path '*/.venv/*' -print0)

exit "$failed"
