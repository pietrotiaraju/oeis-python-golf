#!/usr/bin/env bash
# Land branch $1 on main: merge it, run the programs it adds or changes, rebuild the
# records table and push main. Run by .github/workflows/ship.yml; safe to run again.
set -euo pipefail
branch=$1

merge() {
  git fetch -q origin main "$branch"
  git checkout -q -B main origin/main
  if ! git merge -q --no-ff -m "Merge $branch" "origin/$branch"; then
    # Only the records table may clash: it is generated, so keep main's and rebuild it.
    if [ "$(git diff --name-only --diff-filter=U)" != README.md ]; then
      git merge --abort
      echo "$branch conflicts with main outside README.md: rebase it by hand" >&2
      exit 1
    fi
    git checkout -q --ours README.md
    git add README.md
    git commit -q --no-edit
  fi
  python tools/verify.py --since=origin/main --write "$@"
  git diff --quiet || git commit -q -a --amend --no-edit
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
