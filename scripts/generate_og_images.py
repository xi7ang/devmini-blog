from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap

OUT_DIR = Path('/root/.openclaw/workspace/devmini-blog/static/og')
OUT_DIR.mkdir(parents=True, exist_ok=True)
FONT_PATH = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
W, H = 1280, 640

CARDS = [
    {
        'name': 'home.png',
        'title': 'DevMini 博客',
        'subtitle': '免费资源网站、电子书资料、AI学习与工具推荐',
        'tag': '资源导航 / SEO 内容集群',
        'url': 'devmini.space/blog'
    },
    {
        'name': 'book-resources.png',
        'title': '书籍资料专题',
        'subtitle': '电子书资源、学习资料与精品书单导航',
        'tag': 'BOOK HUB',
        'url': 'devmini.space/blog/book-resources/'
    },
    {
        'name': 'ai-learning-resources.png',
        'title': 'AI学习资源专题',
        'subtitle': '提示词、教程、课程与工作流资料导航',
        'tag': 'AI HUB',
        'url': 'devmini.space/blog/ai-learning-resources/'
    },
    {
        'name': 'tools-resources.png',
        'title': '工具资源专题',
        'subtitle': '效率工具、软件网站与工作流导航',
        'tag': 'TOOLS HUB',
        'url': 'devmini.space/blog/tools-resources/'
    },
    {
        'name': 'free-resource-sites-guide.png',
        'title': '免费网盘资源网站推荐',
        'subtitle': '如何高效找到高质量资料下载站',
        'tag': '主文章',
        'url': 'devmini.space/blog/posts/free-resource-sites-guide/'
    },
    {
        'name': 'ebook-resource-sites-guide.png',
        'title': '电子书资源网站推荐',
        'subtitle': '书籍资料、学习资料哪里找更靠谱',
        'tag': '主文章',
        'url': 'devmini.space/blog/posts/ebook-resource-sites-guide/'
    },
    {
        'name': 'ai-knowledge-resource-sites-guide.png',
        'title': 'AI知识资料下载网站推荐',
        'subtitle': '提示词、教程、课程资源一站式获取',
        'tag': '主文章',
        'url': 'devmini.space/blog/posts/ai-knowledge-resource-sites-guide/'
    },
    {
        'name': 'tools-resource-sites-guide.png',
        'title': '工具资源网站推荐',
        'subtitle': '效率工具、软件资源与工作流网站导航',
        'tag': '主文章',
        'url': 'devmini.space/blog/posts/tools-resource-sites-guide/'
    },
    {
        'name': 'free-learning-sites-guide.png',
        'title': '免费学习网站推荐',
        'subtitle': '如何找到靠谱的在线学习资源平台',
        'tag': '主文章',
        'url': 'devmini.space/blog/posts/free-learning-sites-guide/'
    },
    {
        'name': 'free-resources-navigation-guide.png',
        'title': '免费资源网站导航',
        'subtitle': '电子书、AI工具、学习课程与效率资源的综合入口',
        'tag': '主文章',
        'url': 'devmini.space/blog/posts/free-resources-navigation-guide/'
    },
    {
        'name': 'cross-border-ecommerce-resources-guide.png',
        'title': '跨境电商资源网站推荐',
        'subtitle': '免费工具、课程与运营资料一站搞定',
        'tag': '主文章',
        'url': 'devmini.space/blog/posts/cross-border-ecommerce-resources-guide/'
    },
    {
        'name': 'self-media-resources-guide.png',
        'title': '自媒体资源网站推荐',
        'subtitle': '内容创作、运营工具与变现资料大全',
        'tag': '主文章',
        'url': 'devmini.space/blog/posts/self-media-resources-guide/'
    },
]


def hex_rgb(value: str):
    value = value.lstrip('#')
    return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))


def make_gradient(size, c1, c2):
    img = Image.new('RGB', size, c1)
    px = img.load()
    for y in range(size[1]):
        ratio = y / (size[1] - 1)
        for x in range(size[0]):
            xr = x / (size[0] - 1)
            blend = min(1.0, 0.18 + ratio * 0.72 + xr * 0.15)
            px[x, y] = tuple(int(c1[i] * (1 - blend) + c2[i] * blend) for i in range(3))
    return img


def wrap_text(draw, text, font, max_width):
    words = list(text)
    lines = []
    current = ''
    for ch in words:
        test = current + ch
        if draw.textbbox((0, 0), test, font=font)[2] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


for idx, card in enumerate(CARDS):
    base = make_gradient((W, H), hex_rgb('#0b1020'), hex_rgb('#1d4ed8'))
    draw = ImageDraw.Draw(base)

    accent = [(34, 211, 238), (96, 165, 250), (168, 85, 247), (244, 114, 182)][idx % 4]
    warm = [(59, 130, 246), (16, 185, 129), (245, 158, 11), (239, 68, 68)][idx % 4]

    draw.rounded_rectangle((64, 56, W - 64, H - 56), radius=36, fill=(255, 255, 255, 18), outline=(255, 255, 255, 38), width=2)
    draw.rounded_rectangle((72, 64, W - 72, H - 64), radius=34, outline=(255, 255, 255, 20), width=1)
    draw.ellipse((W - 330, -40, W + 70, 360), fill=accent + (0,) if False else accent)
    draw.ellipse((-120, H - 250, 260, H + 120), fill=warm)
    draw.rectangle((88, 92, 242, 102), fill=accent)

    title_font = ImageFont.truetype(FONT_PATH, 74)
    subtitle_font = ImageFont.truetype(FONT_PATH, 34)
    tag_font = ImageFont.truetype(FONT_PATH, 28)
    url_font = ImageFont.truetype(FONT_PATH, 26)
    brand_font = ImageFont.truetype(FONT_PATH, 24)

    draw.text((96, 126), card['tag'], font=tag_font, fill=(226, 232, 240))

    title_lines = wrap_text(draw, card['title'], title_font, 860)
    y = 188
    for line in title_lines[:2]:
        draw.text((96, y), line, font=title_font, fill=(255, 255, 255))
        y += 88

    subtitle_lines = wrap_text(draw, card['subtitle'], subtitle_font, 860)
    for line in subtitle_lines[:3]:
        draw.text((96, y + 12), line, font=subtitle_font, fill=(219, 234, 254))
        y += 46

    badge_w = draw.textbbox((0, 0), card['url'], font=url_font)[2] + 52
    badge_y = H - 146
    draw.rounded_rectangle((96, badge_y, 96 + badge_w, badge_y + 54), radius=18, fill=(15, 23, 42))
    draw.text((122, badge_y + 11), card['url'], font=url_font, fill=(191, 219, 254))

    draw.text((96, H - 86), 'DevMini Blog · SEO Cover / Open Graph', font=brand_font, fill=(226, 232, 240))

    base.save(OUT_DIR / card['name'], format='PNG', optimize=True)
