### Hi/你好 👋

🔭  欢迎光临我的github数据  🏗🚧👷‍♂️

<!--
**zh3389/zh3389** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

[![zh3389's github stats](https://github-readme-stats.vercel.app/api?username=zh3389)](https://github.com/zh3389/ 'zh3389的信息')

<img src="https://badges.toozhao.com/badges/01EJWJV1BRF0GW9JVCGGNKTSDY/blue.svg" width=400/>


## Pelican Python GitHub blog 搭建
参考教程: [Pelican搭建](https://jiang-hao.com/articles/2018/frontend-%E4%BD%BF%E7%94%A8Pelican%E5%9F%BA%E4%BA%8EGithubPages%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2%E6%95%99%E7%A8%8B.html)

#### 欢迎来到我的blog项目
GitHub博客首页请访问: [GitHub博客页面](https://zh3389.github.io/)

CSDN博客首页请访问: [CSDN博客页面](https://blog.csdn.net/zhanghao3389)

Email: zhanghao_3389@163.com

#### 从github克隆最新代码安装Pelican：

```bash
git clone git://github.com/getpelican/pelican.git
cd pelican
python setup.py install
```

#### 安装Markdown

```bash
pip install markdown
```

#### 搭建Blog骨架

```bash
mkdir blog
cd blog
pelican-quickstart
```

#### 根据提示一步步输入相应的配置项，不知道如何设置的接受默认即可，后续可以通过编辑pelicanconf.py文件更改配置。完成后将会在根目录生成以下文件：

```
.
|-- content                # 所有文章放于此目录
│   └── (pages)            # 存放手工创建的静态页面
|-- Makefile               # 方便管理博客的Makefile
|-- output                 # 静态生成文件
|-- pelicanconf.py         # 配置文件
|-- publishconf.py         # 配置文件
```

#### 测试

```bash
make publish
make serve
# 访问http://127.0.0.1:8000查看效果
```

#### 安装主题

```bash
# 下载主题
https://github.com/getpelican/pelican-themes

# 安装主题
pelican-themes -i ./themes/pelican-clean-blog

# 查看已安装主题
pelican-themes -l

# 修改配置文件pelicanconf.py添加主题选择条目
THEME = '主题名字'

make serve
# 访问http://127.0.0.1:8000查看效果
```

#### 编写文章

```
# 编写markdown
# 存入conten文件夹
# 编译文章为网页源码
make publish
# 本地查看效果
make serve
# 同步本地代码到github即可
```

#### 文章标准开头格式

```
:title: conten title
:date: 2018-08-08 08:08
:author: zh
:category: project
:tags: tags
:slug: page-with-cover-images
:cover: /assets/images/article_cover.jpg
```

#### 更新博客流程

```
1. 把写好的markdown格式的文章放到content中，然后在blog目录下
2. 本地查看效果的话：make html 然后make serve 最后访问：127.0.0.1:8000
3. 发布到github：make github 完成
```
