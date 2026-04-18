# SEO 文章选题池
# 按 pan.devmini.space 实际分类覆盖，顺序即为每日执行顺序
# 周一不执行（周一另有 GitHub Trending 周更）
# 最后更新：2026-04-18

## 选题池（共25篇）

### 工具合集（优先级：高）
1. 程序员免费接单平台汇总：2026版 — https://pan.devmini.space/tools/
2. AI写作工具横评：Claude/ChatGPT/Gemini/DeepSeek — https://pan.devmini.space/tools/

### 课程资料（优先级：高）
3. B站课程合集推荐：各学科系统学习路径大全 — https://pan.devmini.space/curriculum/
4. Coursera/edX 免费旁听方法与证书攻略 — https://pan.devmini.space/curriculum/

### 健康养生（优先级：高）
5. 健身教学视频免费网站推荐：健身入门到进阶 — https://pan.devmini.space/healthy/
6. 中医养生/艾灸/经络学习资源汇总 — https://pan.devmini.space/healthy/

### 传统文化（优先级：中）
7. 国学经典PDF下载：古籍免费阅读网站汇总 — https://pan.devmini.space/chinese-traditional/
8. 书法/国画/诗词学习资源网站推荐 — https://pan.devmini.space/chinese-traditional/

### 游戏资源（优先级：中）
9. 免费Steam游戏推荐：限时免费领取与白嫖攻略 — https://pan.devmini.space/games/
10. 单机游戏下载网站推荐：免Steam/免激活版资源 — https://pan.devmini.space/games/

### 影视媒体（优先级：中）
11. 免费电影/纪录片下载网站推荐 — https://pan.devmini.space/movies/
12. 国内外剧集免费在线看网站汇总 — https://pan.devmini.space/movies/

### 教育知识（优先级：中）
13. 少儿编程学习网站推荐：Scratch/Python入门资源 — https://pan.devmini.space/edu-knowlege/
14. 心理学入门书籍与课程推荐（免费资源）— https://pan.devmini.space/edu-knowlege/

### 书籍资料（优先级：低）
15. 免费电子书下载网站推荐：PDF/EPUB/TXT全格式指南 — https://pan.devmini.space/book/
16. 学术论文资源站推荐：CNKI/万方/免费替代方案 — https://pan.devmini.space/book/

### AI知识（优先级：低）
17. AI提示词资源站汇总：Prompt合集/教程/社区 — https://pan.devmini.space/AIknowledge/
18. GitHub最火开源AI项目Top10逐个点评 — https://pan.devmini.space/AIknowledge/

### 跨境电商（优先级：低）
19. 外贸业务员必备工具清单：选品/沟通/物流 — https://pan.devmini.space/cross-border/

### 自媒体（优先级：低）
20. 小红书运营资源包：素材/工具/课程全攻略 — https://pan.devmini.space/self-media/

### GitHub Trending 周更（周一专用，已独立 cron，此处仅标记）
21. GitHub Trending 本周精选 — https://pan.devmini.space/AIknowledge/ （周一执行）

---

## 执行说明

- 每篇文章必须：写完 → 发 Telegram 审核 → 批准后 → git push → 上线
- 文章结构：开篇痛点 → 问题分析 → 特征标准 → pan站入口推荐 → 使用方法 → 结尾内链
- 内链固定指向：pan.devmini.space/book/、/AIknowledge/、/tools/ 三个子站
- Frontmatter 中的 `images` 和 `thumbnail` 使用格式：`og/slug.png`
- OG 图片用 scripts/generate_og_images.py 按主题配色生成
