#!/usr/bin/env python3
"""Generate OG images as WebP for DevMini Blog"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT_DIR = Path(__file__).parent.parent / 'static' / 'og'
FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'  # fallback: no CJK in runner
W, H = 1280, 640

PALETTES = {
    'brand':   {'bg1':'#0b1020','bg2':'#1d4ed8','accent':'#22d3ee','accent2':'#a855f7','muted':'#dbeafe','surface':'#0f172a','chip':'#132238'},
    'book':    {'bg1':'#111827','bg2':'#1d4ed8','accent':'#f59e0b','accent2':'#f97316','muted':'#ffedd5','surface':'#1f2937','chip':'#3b2a12'},
    'ai':      {'bg1':'#08111f','bg2':'#0f766e','accent':'#2dd4bf','accent2':'#22d3ee','muted':'#ccfbf1','surface':'#0f172a','chip':'#113730'},
    'tools':   {'bg1':'#0f172a','bg2':'#4338ca','accent':'#60a5fa','accent2':'#22c55e','muted':'#dbeafe','surface':'#111827','chip':'#14253b'},
    'learning':{'bg1':'#102a43','bg2':'#0f766e','accent':'#34d399','accent2':'#38bdf8','muted':'#dcfce7','surface':'#12314a','chip':'#17374b'},
    'crossborder':{'bg1':'#1f2937','bg2':'#7c2d12','accent':'#fb7185','accent2':'#f59e0b','muted':'#ffe4e6','surface':'#2d1b12','chip':'#412316'},
    'selfmedia':{'bg1':'#1e1b4b','bg2':'#be185d','accent':'#f472b6','accent2':'#fb7185','muted':'#fce7f3','surface':'#31124a','chip':'#4a1741'},
    'navigation':{'bg1':'#111827','bg2':'#0369a1','accent':'#38bdf8','accent2':'#818cf8','muted':'#e0f2fe','surface':'#15263d','chip':'#163249'},
}

CARDS = [
    {'name':'home.png','kind':'home','palette':'brand','title':'DevMini 博客','subtitle':'免费资源网站、电子书资料、AI学习与工具推荐','eyebrow':'资源导航 / SEO 内容集群','url':'devmini.space/blog','bullets':['书籍资料','AI学习资源','工具资源','内容导航']},
    {'name':'book-resources.png','kind':'hub','palette':'book','title':'书籍资料专题','subtitle':'电子书资源、学习资料与精品书单导航','eyebrow':'BOOK HUB','url':'devmini.space/blog/book-resources/','section':'书籍 / 阅读'},
    {'name':'ai-learning-resources.png','kind':'hub','palette':'ai','title':'AI学习资源专题','subtitle':'提示词、教程、课程与工作流资料导航','eyebrow':'AI HUB','url':'devmini.space/blog/ai-learning-resources/','section':'AI / Workflow'},
    {'name':'tools-resources.png','kind':'hub','palette':'tools','title':'工具资源专题','subtitle':'效率工具、软件网站与工作流导航','eyebrow':'TOOLS HUB','url':'devmini.space/blog/tools-resources/','section':'Tools / Systems'},
    {'name':'free-resource-sites-guide.png','kind':'post','palette':'navigation','title':'免费网盘资源网站推荐','subtitle':'如何高效找到高质量资料下载站','eyebrow':'主文章','url':'devmini.space/blog/posts/free-resource-sites-guide/','section':'资源导航'},
    {'name':'ebook-resource-sites-guide.png','kind':'post','palette':'book','title':'电子书资源网站推荐','subtitle':'书籍资料、学习资料哪里找更靠谱','eyebrow':'主文章','url':'devmini.space/blog/posts/ebook-resource-sites-guide/','section':'书籍资料'},
    {'name':'ai-knowledge-resource-sites-guide.png','kind':'post','palette':'ai','title':'AI知识资料下载网站推荐','subtitle':'提示词、教程、课程资源一站式获取','eyebrow':'主文章','url':'devmini.space/blog/posts/ai-knowledge-resource-sites-guide/','section':'AI知识'},
    {'name':'tools-resource-sites-guide.png','kind':'post','palette':'tools','title':'工具资源网站推荐','subtitle':'效率工具、软件资源与工作流网站导航','eyebrow':'主文章','url':'devmini.space/blog/posts/tools-resource-sites-guide/','section':'工具资源'},
    {'name':'free-learning-sites-guide.png','kind':'post','palette':'learning','title':'免费学习网站推荐','subtitle':'如何找到靠谱的在线学习资源平台','eyebrow':'主文章','url':'devmini.space/blog/posts/free-learning-sites-guide/','section':'学习资源'},
    {'name':'free-resources-navigation-guide.png','kind':'post','palette':'navigation','title':'免费资源网站导航','subtitle':'电子书、AI工具、学习课程与效率资源的综合入口','eyebrow':'主文章','url':'devmini.space/blog/posts/free-resources-navigation-guide/','section':'综合导航'},
    {'name':'cross-border-ecommerce-resources-guide.png','kind':'post','palette':'crossborder','title':'跨境电商资源网站推荐','subtitle':'免费工具、课程与运营资料一站搞定','eyebrow':'主文章','url':'devmini.space/blog/posts/cross-border-ecommerce-resources-guide/','section':'跨境电商'},
    {'name':'self-media-resources-guide.png','kind':'post','palette':'selfmedia','title':'自媒体资源网站推荐','subtitle':'内容创作、运营工具与变现资料大全','eyebrow':'主文章','url':'devmini.space/blog/posts/self-media-resources-guide/','section':'自媒体'},
    {'name':'free-movie-documentary-download-sites.png','kind':'post','palette':'navigation','title':'免费电影/纪录片下载网站推荐','subtitle':'高清资源获取完整指南','eyebrow':'主文章','url':'devmini.space/blog/posts/free-movie-documentary-download-sites/','section':'影视资源'},
]

def h(v):
    v = v.lstrip('#')
    return tuple(int(v[i:i+2], 16) for i in (0, 2, 4))

def rgba(v, a=255):
    return h(v) + (a,)

def canvas(p):
    img = Image.new('RGBA', (W, H), rgba(p['bg1']))
    px = img.load()
    bg1, bg2 = h(p['bg1']), h(p['bg2'])
    for y in range(H):
        for x in range(W):
            rx, ry = x/(W-1), y/(H-1)
            mix = min(1.0, 0.12 + ry*0.70 + rx*0.18)
            px[x,y] = tuple(int(bg1[i]*(1-mix) + bg2[i]*mix) for i in range(3)) + (255,)
    return img

def font(s):
    return ImageFont.truetype(FONT_PATH, s)

def wrap(draw, text, font_obj, max_w):
    lines, cur = [], ''
    for ch in list(text):
        test = cur + ch
        if draw.textbbox((0,0), test, font=font_obj)[2] <= max_w:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = ch
    if cur: lines.append(cur)
    return lines

def chip(draw, x, y, text, font_obj, fill, txt_fill, px=18, py=10, r=18):
    bbox = draw.textbbox((0,0), text, font=font_obj)
    w, h2 = bbox[2]+px*2, bbox[3]+py*2
    draw.rounded_rectangle((x, y, x+w, y+h2), radius=r, fill=fill)
    draw.text((x+px, y+py-2), text, font=font_obj, fill=txt_fill)
    return w, h2

def shell(img, draw, p):
    draw.rounded_rectangle((46,42,W-46,H-42), radius=42, outline=rgba('#ffffff',45), width=2)
    draw.rounded_rectangle((62,58,W-62,H-58), radius=36, outline=rgba('#ffffff',24), width=1)
    draw.ellipse((W-360,-80,W+60,320), fill=rgba(p['accent'],120))
    draw.ellipse((-180,H-250,220,H+140), fill=rgba(p['accent2'],90))
    for x in range(86, W-80, 56):
        draw.line((x,88,x,H-88), fill=rgba('#ffffff',10), width=1)
    for y in range(88, H-88, 56):
        draw.line((86,y,W-86,y), fill=rgba('#ffffff',8), width=1)

def footer(draw, p, url, left=96, bottom=80, right_text='DevMini Blog · Share Card System'):
    ufont, bfont = font(24), font(24)
    chip(draw, left, H-bottom-18, url, ufont, rgba(p['surface'],225), rgba(p['muted']))
    rb = draw.textbbox((0,0), right_text, font=bfont)
    draw.text((W-96-rb[2], H-bottom), right_text, font=bfont, fill=rgba('#ffffff',220))

def home(card, p):
    img = canvas(p)
    draw = ImageDraw.Draw(img, 'RGBA')
    shell(img, draw, p)
    ef, tf, sf, bf = font(28), font(86), font(36), font(28)
    draw.rectangle((96,92,280,102), fill=rgba(p['accent'],255))
    draw.text((96,126), card['eyebrow'], font=ef, fill=rgba(p['muted']))
    y = 196
    for line in wrap(draw, card['title'], tf, 620)[:2]:
        draw.text((96,y), line, font=tf, fill=rgba('#ffffff')); y += 98
    for line in wrap(draw, card['subtitle'], sf, 620)[:3]:
        draw.text((96,y+8), line, font=sf, fill=rgba(p['muted'])); y += 48
    panel = (760,126,1142,492)
    draw.rounded_rectangle(panel, radius=34, fill=rgba(p['surface'],200), outline=rgba('#ffffff',30), width=1)
    draw.text((800,168), '内容矩阵', font=font(30), fill=rgba('#ffffff'))
    draw.text((800,214), 'Homepage / Brand Layer', font=font(24), fill=rgba(p['muted']))
    cy = 276
    for b2 in card['bullets']:
        chip(draw, 800, cy, b2, bf, rgba(p['chip'],235), rgba('#ffffff'), px=20, py=12); cy += 62
    draw.rounded_rectangle((800,486,1098,536), radius=16, fill=rgba(p['accent2'],215))
    draw.text((824,498), '首页 / 专题 / 文章 分层展示', font=font(26), fill=rgba('#ffffff'))
    footer(draw, p, card['url'])
    return img

def hub(card, p):
    img = canvas(p)
    draw = ImageDraw.Draw(img, 'RGBA')
    shell(img, draw, p)
    ef, tf, sf, lf, sf2 = font(26), font(72), font(34), font(26), font(32)
    draw.rounded_rectangle((96,96,248,146), radius=18, fill=rgba(p['chip'],230))
    draw.text((118,108), card['eyebrow'], font=ef, fill=rgba('#ffffff'))
    y = 186
    for line in wrap(draw, card['title'], tf, 710)[:2]:
        draw.text((96,y), line, font=tf, fill=rgba('#ffffff')); y += 86
    for line in wrap(draw, card['subtitle'], sf, 700)[:3]:
        draw.text((96,y+6), line, font=sf, fill=rgba(p['muted'])); y += 46
    draw.rounded_rectangle((830,116,1138,520), radius=40, fill=rgba(p['surface'],210), outline=rgba('#ffffff',36), width=1)
    draw.text((878,160), '专题页', font=font(54), fill=rgba('#ffffff'))
    draw.text((878,236), 'HUB', font=font(88), fill=rgba(p['accent']))
    draw.text((878,350), card['section'], font=sf2, fill=rgba(p['muted']))
    draw.line((878,404,1086,404), fill=rgba(p['accent2'],230), width=6)
    draw.text((878,430), '聚合入口 / 内链中心 / SEO 支点', font=lf, fill=rgba('#ffffff'))
    footer(draw, p, card['url'], right_text='DevMini Blog · Hub Sharing Template')
    return img

def post(card, p):
    img = canvas(p)
    draw = ImageDraw.Draw(img, 'RGBA')
    shell(img, draw, p)
    tf, sf, sf2, ef, bf = font(64), font(32), font(26), font(24), font(92)
    draw.rounded_rectangle((84,90,116,H-90), radius=16, fill=rgba(p['accent'],255))
    draw.rounded_rectangle((148,102,1140,538), radius=34, fill=rgba(p['surface'],180), outline=rgba('#ffffff',32), width=1)
    chip(draw, 184, 138, card['eyebrow'], ef, rgba(p['chip'],240), rgba('#ffffff'), px=18, py=10)
    chip(draw, 320, 138, card['section'], ef, rgba(p['accent2'],220), rgba('#ffffff'), px=18, py=10)
    y = 226
    for line in wrap(draw, card['title'], tf, 650)[:2]:
        draw.text((184,y), line, font=tf, fill=rgba('#ffffff')); y += 78
    for line in wrap(draw, card['subtitle'], sf, 650)[:3]:
        draw.text((184,y+8), line, font=sf, fill=rgba(p['muted'])); y += 44
    draw.text((920,182), 'ARTICLE', font=font(28), fill=rgba(p['muted']))
    draw.text((912,226), '01', font=bf, fill=rgba(p['accent']))
    draw.line((916,346,1088,346), fill=rgba(p['accent2'],220), width=6)
    draw.text((916,372), '可分享 / 可识别 / 可点击', font=sf2, fill=rgba('#ffffff'))
    draw.text((916,416), 'Open Graph · Summary Large Image', font=sf2, fill=rgba(p['muted']))
    footer(draw, p, card['url'], right_text='DevMini Blog · Article Sharing Template')
    return img

for card in CARDS:
    p = PALETTES[card['palette']]
    if card['kind'] == 'home': img = home(card, p)
    elif card['kind'] == 'hub': img = hub(card, p)
    else: img = post(card, p)
    name_webp = card['name'].rsplit('.', 1)[0] + '.webp'
    img.convert('RGB').save(OUT_DIR / name_webp, format='WEBP', quality=85, method=6)
    print(f'  rendered: {name_webp}')

print('Done. All OG images generated as WebP (Q85).')