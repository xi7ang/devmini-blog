#!/bin/bash
# DevMini Blog 自动同步脚本
# 从 GitHub gh-pages 分支拉取构建产物，同步到 /var/www/devmini.space
# 原来同步到 /var/www/devmini.space/blog（2026-04-18 迁移到根目录）
# 需要先配置 SSH: /root/.ssh/devmini-blog-deploy

set -eu

REPO_DIR="/tmp/devmini-blog-sync-repo"
DEPLOY_DIR="/var/www/devmini.space"
LOCK_FILE="/tmp/devmini-blog-sync.lock"
LOG_FILE="/tmp/devmini-blog-sync.log"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# Prevent concurrent runs
if [ -f "$LOCK_FILE" ]; then
  log "another sync already running, skipping"
  exit 0
fi
trap "rm -f $LOCK_FILE" EXIT

touch "$LOCK_FILE"

log "=== starting sync ==="

# Clone gh-pages branch into temp dir
if [ -d "$REPO_DIR/.git" ]; then
  cd "$REPO_DIR"
  git fetch origin gh-pages
  git reset --hard origin/gh-pages
else
  rm -rf "$REPO_DIR"
  git clone -b gh-pages --depth 1 git@github.com:xi7ang/devmini-blog.git "$REPO_DIR"
fi

# Rsync to deploy dir (root, not /blog/)
rsync -a --delete "$REPO_DIR/" "$DEPLOY_DIR/"
log "deployed to $DEPLOY_DIR"

# Count pages
PAGE_COUNT=$(find "$DEPLOY_DIR" -name 'index.html' | wc -l)
log "site has $PAGE_COUNT pages"

# Clean up old /blog subdirectory if it exists (migration from /blog/ to root)
if [ -d "$DEPLOY_DIR/blog" ]; then
  rm -rf "$DEPLOY_DIR/blog"
  log "removed old /blog subdirectory"
fi

log "=== sync complete ==="
