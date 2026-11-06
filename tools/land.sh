#!/usr/bin/env bash
# Land branch $1 on main: merge it, check it with guard.py, run the programs it adds or
# changes, rebuild the records tables and push main. Run by .github/workflows/ship.yml,
# which takes this script and guard.py from main so a branch cannot loosen them; safe
# to run again.
set -euo pipefail
branch=$1
guard=${GUARD:-tools/guard.py}

merge() {
  git fetch -q origin main "$branch"
  git checkout -q -B main origin/main
  if ! git merge -q --no-ff -m "Merge $branch" "origin/$branch"; then
    # Only the records tables (README.md, seq/AXXXxxx/README.md) may clash: they are
    # generated, so keep main's and rebuild them.
    clashes=$(git diff --name-only --diff-filter=U)
    if [ -z "$clashes" ] || grep -qvE '^(README\.md|seq/[^/]+/README\.md)$' <<<"$clashes"; then
      git merge --abort
      echo "$branch conflicts with main outside the records tables: rebase it by hand" >&2
      exit 1
    fi
    git checkout -q --ours -- $clashes
    git add -- $clashes
    git commit -q --no-edit
  fi
  python "$guard" origin/main --strict
  python tools/verify.py --since=origin/main --write "$@"
  git add -- README.md ':(glob)seq/*/README.md'  # a new folder's table is a new file
  git diff --cached --quiet || git commit -q --amend --no-edit
}

merge
for try in 1 2 3 4 5; do
  if git push -q origin main; then
    git push -q origin --delete "$branch"
    exit 0
  fi
  sleep $((try * 10))
  merge --no-run  # main moved meanwhile: merge again; the programs already passed
done
echo "main kept moving: push $branch again to retry" >&2
exit 1
