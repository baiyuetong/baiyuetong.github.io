---
title: 第十二章 实战技巧下篇
---

Web自动化的难点是如何准确快速地选择到想要的页面元素，如果页面元素开发完成之后，一直不变还好，但通常不是这样的，在没有产品之前，是不断变化的，这也变相的提高了web自动化的难度，有没有更好的方法处理html 格式的字符串呢？这里给大家介绍一个优秀的第三方库BeautifulSoup4，如何利用它来帮助解决这些问题。

## BeautifulSoup4介绍

Beautiful Soup是一个可以从HTML或XML文件中提取数据的Python库。它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式。BeautifulSoup常用在网络爬虫中，和Request库一起配合使用，能大大提高爬虫效率。当然我们也可以利用它，先将某个节点的html,或者整个页面的html 获取回来，然后再利用BS在本地做分析。

BeautifulSoup4的使用方法，大家可以参考官方参考手册[中文手册](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/),[英文手册](https://www.crummy.com/software/BeautifulSoup/bs4/doc/),下面简单的和大家介绍一下如何使用Beautiful soup

## BeautifulSoup4 安装

python第三方库的标准安装方法

```py
pip install beautifulsoup4
pip install html5lib
```

因为bs里面缺省的库对html的兼容性不够，所以通常还需要安装html5lib，这个库对html的兼容性比较好

## 常见方法

以“爱丽丝”文档作为例子:

```py
html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)
```

### find and find_all

+ find( name , attrs , recursive , text , **kwargs )

该方法直接返回第一个符合条件的tag，找不到目标时,返回 None,详情参考[这里-find](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find)

```py
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>
```

+ find_all( name , attrs , recursive , text , **kwargs )

该方法将返回文档中符合条件的所有tag，没有找到目标是返回空列表,详情参考[这里-find_all](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find_all)

```py
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

### 获取tag信息

#### 获取tag名

用法为：tag.name

```py
soup.title.name)
soup.find('title').name
```

#### 获取tag属性值

用法为：

 1. 单个属性：tag.attrs
 2. 多个属性：tag[attrs]

详细用法可以参考[这里-tag](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#tag)

```py
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.p['class']
# ["body", "strikeout"]

css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class']
# ["body"]
```

### 获取文本信息

方法1：tag.string 详情参考[这里-string](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#string)

方法2：tag.get_text() 详情参考[这里-get_text](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#get-text)

```py
title_tag.string
# u'The Dormouse's story'

markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

soup.get_text()
u'\nI linked to example.com\n'
soup.i.get_text()
u'example.com'
```

### 百度首页

访问百度首页，打印相关信息，源码如下：

```py
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import  webdriver

driver = webdriver.Chrome(r"G:\Education\BYHY\Courseware\Improvement\Selenium\chromedriver.exe")
driver.implicitly_wait(5)

# ================================================
# open URL
driver.get('https://www.baidu.com/')

ele = driver.find_element_by_tag_name("html")
html_doc = ele.get_attribute('innerHTML')

#
# BeautifulSoup
#
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html5lib")

# title
print('==title=='*4)
print(soup.find('title'))
print(soup.title)
print(soup.title.string)

# get tag name
print('==tag=='*4)
print(soup.title.name)
print(soup.find('title').name)

# get tag text
print('==tag text=='*4)
print(soup.title.string)
print(soup.title.get_text())

# get web element attribute value
print('==tag attribute value=='*4)
print(soup.div['id'])
print(soup.div['style'])
print(soup.div.get('style'))

# get the first tag a
print(soup.find('a'))

# get all tag a
# return a list, then get specified tag by list index
# print(soup.find_all('a'))
print(soup.find_all('a')[2]) # third tag

# by tag and attribute
print('==tag and attribute =='*4)
print(soup.find('input', id="su"))

# ================================================
input('Please input any key to continue......')
# Quit
driver.quit()
```


{% include sharepost.html %}



[上一页](/doc/tutorial/selenium/11other_skills2/){: .btn .btn--primary .align-left }
[下一页](/doc/tutorial/selenium/13suggestions_on_the_end/){: .btn .btn--primary .align-right }
