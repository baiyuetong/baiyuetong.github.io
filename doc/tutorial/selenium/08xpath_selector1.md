---
title: 第八章 Xpath选择器之基础篇
---

## Xpath简介

XPath (XML Path Language)是有一个专门负责互联网领域规范制定的一个国际标准化组织W3C( World Wide Web Consortium)提出的，在1999年11月16日成为标准，是用来在XML文档中选择节点的语言。

目前主流浏览器(chrome、firefox，edge，safari)都支持XPath语法，xpath有1.x 和2.x两个版本，目前浏览器支持的主要是xpath 1.X的版本。但不同的浏览器支持的力度还不同， 因为它毕竟不是浏览器渲染界面所必须的。 有些浏览器都不支持它。所以大家使用xpath的时候 不同的浏览器要多测试测试。

所以我们推荐尽量使用CSS选择，而不是用XPath，因为CSS方式通常速度更快，而且相对更容易理解。但是确实有些场景 用 css 选择web 元素 很麻烦，而xpath 却比较方便。而且在实际的工作中，有的公司可能已经大量使用Xpath在自动化脚本中了， 所以我们有必要也去了解一下xpath。

## xpath语法

打开百度（www.baidu.com）,按F12调试窗口，可以看到整个html文档可以看成类似于文件系统一样的树状结构，文件系统树的根节点用'/'表示，在console输入

```
$x('/')
```

点击后就可以发现， 高亮显示的元素对应整个html 文档，如果我们想选择的是根节点下面的html节点，则可以在console输入

```
$x('/html')
```

点击显示的元素，对应html 节点,几乎也是整个文档，这是因为除了开头的doctype说明，就几乎是整个文档的内容了，如果要继续选择html下面的一层层节点，console可以这样输入

```
$x('/html/body/div')  
```

这个表达式表示选择html下面的body下面的div元素， 注意'/'对应的是直接子节点。点击显示的元素，可以发现对应选中/html/body/下面所有的div子元素。

### 绝对路径选择

从上面的例子可以看出，如果Xpath路径以正斜杠(/)开始，就表示从根节点开始，那么该路径始终代表到某元素的**绝对路径**。 如果用CSS来选择的话，等价于css

```
html >body>div
```

这很像Linux里面的绝对路径的概念， 熟悉Linux的同学应该知道，在Linux里面的根节点就是'/',比如Linux下面的网站目录的绝对路径一般类似这样：/var/www/html/htdoc

如果selenium代码里面使用Xpath来选择web元素，则可以这样：

```py
eleObjList = driver.find_elements_by_xpath("/html/body/div")
```

### 相对路径选择

有的时候，我们需要选择web中某一类型的所有web元素，不管它在什么位置。比如，选择baidu搜索页面的所有P元素，在css中我们可以直接这样输入：

```
 $$('p')
```

那xpath怎么实现同样的功能呢？xpath需要前面加// ,  //表示从当前节点往下寻找所有的后代元素,不管它在什么位置。所以我可以这样选择：

```
 $x('//p')
```

在这里和大家说一下，在xpath中有个当前节点的概念，类似文件系统的当前路径的概念。一开始，我们的当前节点就是根节点，所以，如果
我们想当然的认为是如下选择的话，我们得到的是一个空列表

```
 $x('p')
```

因为在html 文档中， 根节点下面的子元素，一般就只有 html这个节点，所以选择其他的元素，肯定会返回一个空列表。

'//' 符号也可以继续加在后面,比如表示选择所有的div元素里面的p元素 ，不管div 在什么位置，则可以这样

```
$x('//div//p')
``` 

表示不管p元素在div下面的什么位置，因为//div就相当于把当前节点就变成了匹配的div 节点了，后面再加//就是表示里面的p元素，不管什么位置都可以被选到。如果使用CSS选择器，等同于

```
$$('div p')
```

前面介绍CSS的时候给大家介绍了很多方法，其实在Xpath里面也可以实现，后面将向大家一一介绍。



{% include sharepost.html %}



[上一页](/doc/tutorial/selenium/07css_selector2/){: .btn .btn--primary .align-left }
[下一页](/doc/tutorial/selenium/09xpath_selector2/){: .btn .btn--primary .align-right }
