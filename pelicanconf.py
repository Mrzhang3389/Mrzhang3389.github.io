#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'zh'
SITENAME = '此时此刻即是最好的~'
SITESUBTITLE = '这世界只来一次,让我们尽兴而归~'
SITEURL = 'https://Mrzhang3389.github.io'
HOME_COVER = 'https://raw.githubusercontent.com/Mrzhang3389/Mrzhang3389.github.io/master/assets/hold/header.jpg'
PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SHOW_FULL_ARTICLE = False  # 可在index.html上显示文章的全部内容，而不是摘要

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)
DEFAULT_PAGINATION = 10
MENUITEMS = (('我的GitHub主页', 'https://github.com/Mrzhang3389'),
             ('我的csdn主页', 'https://blog.csdn.net/zhanghao3389'),
             ('发email给我', 'mailto:zhanghao_3389@163.com'))

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

AUTHORS_BIO = {
  "zh": {
    "name": "zh",
    "cover": "https://raw.githubusercontent.com/Mrzhang3389/Mrzhang3389.github.io/master/assets/hold/header.jpg",
    "image": "https://raw.githubusercontent.com/Mrzhang3389/Mrzhang3389.github.io/master/assets/hold/head.jpg",
    "website": "https://Mrzhang3389.github.io",
    "github": "Mrzhang3389",
    "location": "ChengDu",
    "bio": "欢迎来到我的blog, 这里用于存放一些成品的项目..."
  }
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'attila'
SCHEM_CSS_LIST = ['tomorrow.css', 'tomorrow_night.css', 'monokai.css', 'github.css', 'darkly.css']
COLOR_SCHEME_CSS = SCHEM_CSS_LIST[3]
