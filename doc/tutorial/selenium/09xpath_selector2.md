---
title: 第九章 Xpath选择器之高级篇
---

## 测试页面

对如下的web进行选择，可以复制到本地，保存为test.html文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SKNet</title>
    <base target="_blank" />
</head>

<body>
    <h3>Web元素选择测试界面</h3>
    <p>欢迎来到思凯网络学院</p>
    <p>欢迎来到思凯网络 - 思凯网络，专注起点</p>
    <hr />

    <div style="background-color:#99FFFF; color:black; padding:10px; font-family:Comic Sans MS; font-size:16px; text-align:left;">
        <p>段落：我们为什么推荐编程0基础的朋友从<span>python</span>入手学习编程语言？ 为什么不是Java、C、C++、Javascript？因为<span>Python</span>> 易学好用。</p>
        <span>Python</span> 的创造者们，创建出<span>Python</span> 语言，出发点就是希望它 既 简单易用 又 高效又强大。 所以天生就携带 易学好用的基因
    </div>

    <div>
        <h4>超链接测试</h4>
        <a href="http://www.baidu.com" id="baidu">百度搜索</a><br />
        <a href="http://www.python3.vip" id="BYHY">白月黑羽--在线教程</a><br />
        <p>这是为了隔离a标签</p>
        <a href="http://www.baidu.com" id="baidu2">百度搜索2</a>
    </div>

    <div>
        <h5>按钮测试</h5>
        <button name='button' id="BT1">测试按钮1</button><br />
        <button name='button' id="BT2">测试按钮2</button>
        <a href="http://www.baidu.com" id="baidu3">百度搜索3</a><br />
    </div>

    <div class="SKnet">
        <p class="teacher">BYHY</p>
        <p class="teacher">SK</p>
        <p class="teacher">小凯老师</p>
        <p class="teacher">小雷老师</p>
    </div>

    <div>
        <p>===========================================</p>
    </div>
    <p>Xpath test</P>
   </body>
</html>
```

## 选择后代节点

选择所有div节点下的所有后代P节点（'//div//p'）

```py
eleObjList = driver.find_elements_by_xpath("//div//p")

for eleObj in eleObjList:
    print(eleObj.text)
```

输出结果为：

```
段落：我们为什么推荐编程0基础的朋友从python入手学习编程语言？ 为什么不是Java、C、C++、Javascript？因为Python> 易学好用。
Django
Scrapy
这是为了隔离a标签
BYHY
SK
小凯老师
小雷老师
```

## 选择子节点

### 单个直接子节点

选择所有div节点的子节点P（'//div/p'）

```py
eleObjList = driver.find_elements_by_xpath("//div/p")

for eleObj in eleObjList:
    print(eleObj.text)
```

输出结果为：

```
段落：我们为什么推荐编程0基础的朋友从python入手学习编程语言？ 为什么不是Java、C、C++、Javascript？因为Python> 易学好用。
这是为了隔离a标签
BYHY
SK
小凯老师
小雷老师
```

### 所有直接子节点

选择所有div节点的所有直接子节点（'//div/*'）

```py
eleObjList = driver.find_elements_by_xpath("//div/*")

for eleObj in eleObjList:
    print(eleObj.text)
```

输出结果为：

```
段落：我们为什么推荐编程0基础的朋友从python入手学习编程语言？ 为什么不是Java、C、C++、Javascript？因为Python> 易学好用。
Python
Python
Pythonweb开发
Django
Python网络爬虫
Scrapy
超链接测试
百度搜索

白月黑羽--在线教程

这是为了隔离a标签
百度搜索2
按钮测试
测试按钮1

测试按钮2
百度搜索3

BYHY
SK
小凯老师
小雷老师
```

等价于CSS选择器('div > *')

```py
eleObjList = driver.find_elements_by_css_selector("div > *")
for eleObj in eleObjList:
    print(eleObj.text)
```

## 根据属性选择

我们前面介绍的选择器中，有介绍根据class，ID来选择页面元素，在Xpath选择器中，都可以看成是根据属性来选择

### 根据ID

选择Id为baidu2的‘百度搜索2’，可以这样(//*[@id='baidu2'])

```py
eleObjList = driver.find_elements_by_xpath("//*[@id='baidu2']")
for eleObj in eleObjList:
    print(eleObj.text)
```

### 根据class

选择所有div元素中class为sknet的页面元素

```py
eleObjList = driver.find_elements_by_xpath("//div[@class='SKnet']")
for eleObj in eleObjList:
    print(eleObj.text)
```

输出结果为：

```
BYHY
SK
小凯老师
小雷老师
```


可以对比这两种方法的结果

```py
eleObjList = driver.find_elements_by_xpath("//*[@class='teacher']")
for eleObj in eleObjList:
    print(eleObj.text)
```

输出结果为：

```
BYHY
SK
小凯老师
小雷老师
BYHY2
SK2
小凯老师2
小雷老师2
```

### 根据其他属性

同样的道理，我们也可以利用其它的属性选择，比如选择所有具有style属性的所有页面元素

```py
eleObjList = driver.find_elements_by_xpath("//*[@style]")
for eleObj in eleObjList:
    print(eleObj.text)
```

## 根据序数选择

+ 选取第2个P元素

```py
eleObjList = driver.find_elements_by_xpath("//p[2]")
for eleObj in eleObjList:
    print(eleObj.text)
```

+ 选择父元素为div中P元素的第二个p子元素

```py
eleObjList = driver.find_elements_by_xpath("//div/p[2]")
for eleObj in eleObjList:
    print(eleObj.text)
```

+ 选择父元素为div中第二种类型的子元素

```py
eleObjList = driver.find_elements_by_xpath("//div/*[2]")
for eleObj in eleObjList:
    print(eleObj.text)
```

+ 选取最后一个P元素

```py
eleObjList = driver.find_elements_by_xpath("//p[last()]")
for eleObj in eleObjList:
    print(eleObj.text)
```

+ 选取倒数第2个P元素

```py
eleObjList = driver.find_elements_by_xpath("//p[last()-2]")
for eleObj in eleObjList:
    print(eleObj.text)
```

+ 选择父元素为div中P元素的倒数第二个p子元素

```py
eleObjList = driver.find_elements_by_xpath("//div/p[last()-2]")
for eleObj in eleObjList:
    print(eleObj.text)
```

+ 选择父元素为div中倒数第二种类型的子元素

```py
eleObjList = driver.find_elements_by_xpath("//div/*[last()-2]")
for eleObj in eleObjList:
    print(eleObj.text)
```


第几个某类型的子元素

## 组合选择

css选择器有组选择，可以同时选择多个元素，条件之间用**逗号**隔开，xpath选择器则是用**竖线**隔开

```py
eleObjList = driver.find_elements_by_xpath("//h3 | //h4")
for eleObj in eleObjList:
    print(eleObj.text)
```

等同于CSS选择器

```py
eleObjList = driver.find_elements_by_css_selector("h3,h4")
for eleObj in eleObjList:
    print(eleObj.text)
```

## 兄弟选择

css选择器的兄弟选择，条件之间用**波浪线**隔开，xpath选择器则是用**following-sibling加两个冒号**隔开

```py
eleObjList = driver.find_elements_by_xpath("//h4/following-sibling::a")
for eleObj in eleObjList:
    print(eleObj.text)
```

等同于CSS选择器

```py
eleObjList = driver.find_elements_by_css_selector("h4 ~ a")
for eleObj in eleObjList:
    print(eleObj.text)
```

更多Xpath选择器的介绍，可以参考[Xpath选择器参考手册](http://www.w3school.com.cn/xpath/index.asp)


{% include sharepost.html %}



[上一页](/doc/tutorial/selenium/08xpath_selector1/){: .btn .btn--primary .align-left }
[下一页](/doc/tutorial/selenium/10other_skills1/){: .btn .btn--primary .align-right }
