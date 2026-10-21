#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
OWNER="${OWNER:-AIPMAndy}"
REPO="${REPO:-intj-high-salary-guide}"
if ! command -v gh >/dev/null 2>&1; then echo '需要安装 GitHub CLI: https://cli.github.com/' >&2; exit 1; fi
if ! gh auth status >/dev/null 2>&1; then echo '请先执行 gh auth login 完成登录。' >&2; exit 1; fi
python3 scripts/build.py --check
python3 -m unittest discover -s tests -v
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  EXISTING="$(git remote get-url origin 2>/dev/null || true)"
  if [[ -n "$EXISTING" && "$EXISTING" != *"$OWNER/$REPO"* ]]; then
    echo "当前 origin 指向 $EXISTING；为避免覆盖其它仓库，中止。" >&2; exit 1
  fi
else
  git init -b main
fi
git add .
if ! git diff --cached --quiet; then git -c user.name="${GIT_AUTHOR_NAME:-AI Andy}" -c user.email="${GIT_AUTHOR_EMAIL:-no-reply@example.com}" commit -m "Launch INTJ high salary career guide"; fi
if gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  echo "目标仓库已存在，将只推送到 $OWNER/$REPO。"
  if ! git remote get-url origin >/dev/null 2>&1; then git remote add origin "https://github.com/$OWNER/$REPO.git"; fi
else
  gh repo create "$OWNER/$REPO" --public --description 'INTJ职场拿高薪保姆级攻略：职业定位、晋升、求职、谈薪与互动工具' --source . --remote origin
fi
git branch -M main
git push -u origin main
if gh api "repos/$OWNER/$REPO/pages" >/dev/null 2>&1; then
  gh api -X PUT "repos/$OWNER/$REPO/pages" -f build_type=workflow >/dev/null || echo '自动调整Pages失败：请到Settings → Pages选择GitHub Actions。'
else
  gh api -X POST "repos/$OWNER/$REPO/pages" -f build_type=workflow >/dev/null || echo '自动启用Pages失败：请到Settings → Pages选择GitHub Actions。'
fi
gh workflow run deploy-pages.yml --repo "$OWNER/$REPO" --ref main >/dev/null 2>&1 || echo '请到Actions手动运行 Deploy GitHub Pages。'
printf '\n仓库: https://github.com/%s/%s\n预计网站: https://%s.github.io/%s/\n' "$OWNER" "$REPO" "${OWNER,,}" "$REPO"
echo '注意：请检查GitHub Actions部署状态，并实际访问网站后再对外公布。'
