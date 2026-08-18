#!/usr/bin/env bash
# Research workspaces need accepted plans before source gathering starts.
set -u

state_of() {
  awk 'NR > 1 && $0 == "---" { exit } index($0, "state:") == 1 { print $2; exit }' "$1"
}

failed=0
workspaces=0
ready=0
while IFS= read -r -d '' workspace; do
  workspaces=$((workspaces + 1))
  outline="$workspace/outline.md"
  query="$workspace/query.md"
  if [[ ! -f "$outline" || ! -f "$query" ]]; then
    printf 'ERROR: %s: requires both outline.md and query.md\n' "$workspace" >&2
    failed=1
    continue
  fi
  outline_state=$(state_of "$outline")
  query_state=$(state_of "$query")
  if [[ "$outline_state" == accepted && "$query_state" == accepted ]]; then
    ready=$((ready + 1))
  else
    printf 'NEEDS REVIEW: %s: outline=%s, query=%s (both must be accepted before research)\n' \
      "$workspace" "${outline_state:-missing}" "${query_state:-missing}" >&2
  fi
done < <(find _research -mindepth 1 -maxdepth 1 -type d -print0 2>/dev/null)

printf 'Research workspaces: %d total, %d ready, %d awaiting review.\n' \
  "$workspaces" "$ready" "$((workspaces - ready))"
exit "$failed"
