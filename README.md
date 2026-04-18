# DevMini 博客

> [devmini.space](https://devmini.space) 的源码仓库，托管于 GitHub，线上地址：[https://devmini.space](https://devmini.space)

使用 [Hugo](https://gohugo.io) + Mainroad 主题构建，通过 GitHub Actions 自动构建并部署到服务器。

## 站点架构

```
devmini.space（主站，Nginx 直接服务）
├── /posts/          → Hugo 博客文章列表
├── /posts/[slug]/   → 单篇文章
├── /book-resources/ → 书籍资料专题页
├── /ai-learning-resources/ → AI学习资源专题页
└── /tools-resources/    → 工具资源专题页

pan.devmini.space（独立站点，夸克网盘资源聚合）
├── /book/         → 书籍资料
├── /AIknowledge/ → AI知识
├── /tools/        → 工具合集
└── ...（共11个分类）
```

## 内容发布流程

```
1. 撰写文章  →  content/posts/[slug].md
2. 生成 OG 图 →  static/og/[slug].png
3. git push  →  GitHub Actions 自动构建
4. GitHub Actions → 构建产物推送到 gh-pages 分支
5. 服务器 cron（每15分钟）→ 拉取 gh-pages 到 /var/www/devmini.space/
6. 上线      →  https://devmini.space/posts/[slug]/
```

## 文章格式规范

每篇文章采用 **6段式 SEO 友好结构**：

```
## H2：核心回答（3-4句，直接给答案）
## H2：背景与现状
## H2：为什么值得推荐（3个H3子标题）
## H2：入口推荐
## H2：使用建议
## H2：常见问题FAQ（3条Q&A）
## H2：相关资源
```

详细规范见 [scripts/seo_topic_pool.md](scripts/seo_topic_pool.md)。

## 快速开始

```bash
# 本地预览
hugo server

# 构建静态文件（输出到 public/）
hugo

# 仅构建草稿
hugo --buildDrafts
```

## 自动化脚本

| 文件 | 说明 |
|------|------|
| `scripts/seo_topic_pool.md` | SEO 文章选题池（含扩展区） |
| `scripts/generate_og_images.py` | OG 封面图批量生成（Python PIL） |
| `scripts/trending_weekly.sh` | GitHub Trending 周更抓取脚本 |
| `devmini-blog-sync.sh` | 服务器同步脚本（部署侧 cron） |

## 部署说明

- **构建端**：GitHub Actions（`.github/workflows/deploy.yml`），构建产物推送到 `gh-pages` 分支
- **同步端**：服务器 cron 每15分钟执行 `devmini-blog-sync.sh`，从 `gh-pages` 拉取到 `/var/www/devmini.space/`
- **Base URL**：`https://devmini.space/`
- **主题**：Mainroad（Hugo）

## 文章内链规范

每篇文章结尾固定内链：
- [pan.devmini.space/book/](https://pan.devmini.space/book/)
- [pan.devmini.space/AIknowledge/](https://pan.devmini.space/AIknowledge/)
- [pan.devmini.space/tools/](https://pan.devmini.space/tools/)

## 自动化发布

SEO 文章每日 cron：每天 09:00（周二至周日）自动生成草稿 → Telegram 审核 → 批准后上线。
