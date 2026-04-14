#!/bin/bash
# GitHub Trending 周更文章生成脚本
# 由 Cron 调用，生成文章后发 Telegram 通知审核

BLOG_DIR="/root/.openclaw/workspace/devmini-blog"
STAGING_DIR="/tmp/trending_pending"
DATE_STR=$(date +%Y-%m-%d)
NEXT_MONDAY=$(date -d "next Monday" +%Y-%m-%d)

mkdir -p "$STAGING_DIR"

# 获取本周日期（周一）
if [ "$(date +%u)" -eq 1 ]; then
  ARTICLE_DATE=$(date +%Y-%m-%d)
else
  ARTICLE_DATE=$(date -d "last Monday" +%Y-%m-%d)
fi

SLUG="github-trending-weekly-${ARTICLE_DATE}"
OUTPUT="$STAGING_DIR/${SLUG}.md"
OG_OUTPUT="$BLOG_DIR/static/og/${SLUG}.png"

# 抓取数据
echo "Fetching GitHub Trending data..."
/usr/bin/python3 /root/.openclaw/workspace/skills/github-trending-stable/scripts/github_trending.py weekly --limit 10 > /tmp/trending_raw.txt 2>&1

if [ $? -ne 0 ]; then
  echo "Failed to fetch trending data"
  exit 1
fi

echo "Data fetched successfully, article will be generated"

# 注意：文章内容由 AI agent 在收到通知后生成写入
# 此脚本只负责触发通知，告知用户草稿已就绪
