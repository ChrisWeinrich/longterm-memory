#!/usr/bin/env bash
# Required files and directories for the rendered project foundation.
set -u

failed=0
for path in README.md AGENTS.md MOC.md .copier-answers.yml .agents/skills \
  _templates _raw _raw/sources _raw/conversations _raw/external _raw/research \
  _research wiki wiki/pages wiki/index.md wiki/log.md; do
  if [[ ! -e "$path" ]]; then
    printf 'ERROR: missing required path: %s\n' "$path" >&2
    failed=1
  fi
done

if [[ ! -f .gitignore ]]; then
  printf 'ERROR: missing .gitignore\n' >&2
  failed=1
elif ! grep -Fqx '/.obsidian/workspace*.json' .gitignore; then
  printf 'ERROR: .gitignore must ignore /.obsidian/workspace*.json\n' >&2
  failed=1
fi

exit "$failed"
