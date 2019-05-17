---
title: css表达式选择元素 
---

前面我们看到了根据 id、class属性、tag名 选择元素。

如果我们要选择的 元素 没有id、class 属性，或者有些我们不想选择的元素 也有相同的 id、class属性值，怎么办呢？

 这时候我们通常可以通过 CSS selector 语法选择元素。

<br>

## CSS Selector 语法选择元素

HTML中经常要 为 某些元素 指定 **显示效果**，比如 前景文字颜色是红色， 背景颜色是黑色， 字体是微软雅黑等。

那么CSS必须告诉浏览器：要 **选择哪些元素** ， 来使用这样的显示风格。

CSS Selector 语法就是用来选择元素的。

既然 CSS Selector 语法 天生就是浏览器用来选择元素的，selenium自然就可以使用它用在自动化中，去选择要操作的元素了。


只要 CSS Selector 的语法是正确的， Selenium 就可以选择到该元素。


通过 CSS Selector  选择单个元素的方法是 

```
find_element_by_css_selector(CSS Selector参数)
```

选择所有元素的方法是 

```
find_elements_by_css_selector(CSS Selector参数)
```

CSS Selector 选择元素非常灵活强大， 大家可以从下面的例子看出来。


<br>

### 根据 tag名、id、class 选择元素

CSS Selector 同样可以根据tag名、id 属性和 class属性 来 选择元素， 


根据 tag名 选择元素的 CSS Selector 语法非常简单，直接写上tag名即可， 

比如 要选择 所有的tag名为div的元素，就可以是这样

```py
elements = driver.find_elements_by_css_selector('div')
```

等价于
```py
elements = driver.find_elements_by_tag_name('div')
```

<br>

-----
<br>

根据id属性 选择元素的语法是在id号前面加上一个井号： ```#id值```

比如 这个网址 http://www.python3.vip/doc/tutorial/selenium/code/sample1.html

有下面这样的元素：

```html
<input  type="text" id='searchtext' />
```

就可以使用  ```#searchtext``` 这样的 CSS Selector 来选择它。


比如，我们想在  ```id 为 searchtext```  的输入框中输入文本  ```你好```  ，完整的Python代码如下

```py
from selenium import webdriver

driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

driver.get('http://www.python3.vip/doc/tutorial/selenium/code/sample1.html')

element = driver.find_element_by_css_selector('#searchtext')
element.send_keys('你好')
```

<br>

-----
<br>

根据class属性 选择元素的语法是在 class 值 前面加上一个点： ```.class值```

比如 这个网址 http://www.python3.vip/doc/tutorial/selenium/code/sample1.html

要选择**所有** class 属性值为 animal的元素 动物 除了这样写

```py
elements = driver.find_elements_by_class_name('animal')
```

还可以这样写

```py
elements = driver.find_elements_by_css_selector('.animal')
```

因为是选择 ```所有符合条件的``` ，所以用  ```find_elements```  而不是  ```find_element``` 


<br><br>

### 选择 子元素 和 后代元素

HTML中， 元素 内部可以 **包含其他元素**， 比如 下面的 HTML片段

```html
<div id='container'>
    
    <div id='layer1'>
        <div id='inner11'>
            <span>内层11</span>
        </div>
        <div id='inner12'>
            <span>内层12</span>
        </div>
    </div>

    <div id='layer2'>
        <div id='inner21'>
            <span>内层21</span>
        </div>
    </div>
    
</div>
```

下面的一段话有些绕口， 请 大家细心 阅读：

id 为 ```container``` 的div元素 包含了 id 为  ```layer1``` 和  ```layer2``` 的两个div元素。 
这种包含是直接包含， 中间没有其他的层次的元素了。 所以  id 为  ```layer1``` 和  ```layer2``` 的两个div元素 是 id 为 ```container``` 的div元素 的 **直接子元素** 

而 id 为  ```layer1``` 的div元素 又包含了 id 为  ```inner11``` 和  ```inner12``` 的两个div元素。 中间没有其他层次的元素，所以这种包含关系也是 **直接子元素** 关系

id 为  ```layer2``` 的div元素  又包含了 id 为  ```inner21``` 这个div元素。 这种包含关系也是 **直接子元素** 关系

<br>

而对于 id 为 ```container``` 的div元素来说， id 为  ```inner11``` 、```inner12``` 、```inner22``` 的元素  和 两个  ```span类型的元素```   都不是 它的直接子元素， 因为中间隔了 几层。 

虽然不是直接子元素， 但是 它们还是在  ```container```  的内部， 可以称之为它 的 **后代元素**

后代元素也包括了直接子元素， 比如 id 为  ```layer1``` 和  ```layer2``` 的两个div元素 也可以说 是 id 为 ```container``` 的div元素 的 **直接子元素，同时也是后代子元素** 


<br>

如果  ```元素2```   是 ```元素1```  的 直接子元素，
CSS Selector  选择子元素的语法是这样的  

```
元素1 > 元素2
``` 

中间用一个大于号 （我们可以理解为箭头号）

注意，最终选择的元素是 **元素2**， 并且要求这个 **元素2** 是 **元素1** 的直接子元素

<br>

也支持更多层级的选择， 比如 

```
元素1 > 元素2 > 元素3 > 元素4
``` 

就是选择  ```元素1```  里面的子元素  ```元素2```  里面的子元素  ```元素3```  里面的子元素  ```元素4``` ， 最终选择的元素是 **元素4**


<br>
<br>

如果  ```元素2```   是 ```元素1```  的 后代元素，
CSS Selector  选择后代元素的语法是这样的  

```
元素1   元素2
``` 

中间是一个或者多个空格隔开

最终选择的元素是 **元素2** ， 并且要求这个 **元素2** 是 **元素1** 的后代元素。

<br>
也支持更多层级的选择， 比如 

```
元素1   元素2   元素3  元素4
``` 

最终选择的元素是 **元素4**


<br>


### 根据属性

+ [attribute]选择具有[ ]内属性的所有元素
+ *[style] 表示选择所有具有style属性的元素
+ div[class='SKnet'] 选择所有具有div元素且class属性值为SKnet的元素

<br>

### 选择语法联合使用

CSS selector的强大之处 就是 选择语法 可以 联合使用

比如， 我们要选择 下面的 html 中的元素  ```<span class='copyright'>版权</span>``` 

```html
<div id='bottom'>
    <div class='footer1'>
        <span class='copyright'>版权</span>
        <span class='date'>发布日期：2018-03-03</span>
    </div>
    <div class='footer2'>
        <span>备案号
            <a href="http://www.miitbeian.gov.cn">苏ICP备88885574号</a>
        </span>
    </div>        
</div>         
```

CSS selector 表达式 可以这样写：   

```
div.footer > span.copyright
``` 

就是 选择 一个class 属性值为 copyright 的 span 节点， 并且要求其 必须是   class 属性值为 footer 的 div节点 的子节点

<br>

也可以更简单： 

```
.footer > .copyright
```


就是 选择 一个class 属性值为copyright 的节点（不限类型）， 并且要求其 必须是   class 属性值为 footer 的节点的  子节点


<br>

当然 这样也是可以的： 

```
.footer  .copyright
``` 

因为子元素同时也是后代元素



<br>


### 多表达式选择

同时选择所有div元素**和**id为BYHY的元素， 使用逗号

```html
div,#BYHY{color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('div,#BYHY')
for eleObj in eleObjList:
    print(eleObj.text)
```

**注意**：元素标签之间为**逗号**隔开

### 相邻兄弟选择器

选择h4元素之后紧跟的a元素

```html
h4+a{color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('h4+a')
for eleObj in eleObjList:
    print(eleObj.text)
```

**注意**：元素标签之间为**加号**连接

### 后续兄弟选择器

选择h4元素之后所有**兄弟关系**的a元素,即选择所有具有**相同的父元素**中在h4元素之后的所有a元素

```html
h4~a{color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('h4~a')
for eleObj in eleObjList:
    print(eleObj.text)
```

**注意**：元素标签之间为**波浪线**连接

## 否定选择器

选择所有a标签中ID不是BYHY的元素

```html
a:not(#BYHY){color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('a:not(#BYHY)')
for eleObj in eleObjList:
    print(eleObj.text)
```

## nth-child选择器

### p:first-child

选择属于其父元素的**首个**子元素为P的所有P元素

```html
p:first-child{color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:first-child')
for eleObj in eleObjList:
    print(eleObj.text)
```

### p:last-child

选择属于其父元素的**最后一个**子元素为P的每个p元素

```html
p:last-child{color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:last-child')
for eleObj in eleObjList:
    print(eleObj.text)
```

### p:only-child

选其父元素的只有**唯一**一个子元素且元素为P的每个 p 元素

```html
p:only-child{color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:only-child')
for eleObj in eleObjList:
    print(eleObj.text)
```

### p:nth-child(n)

选择属于其父元素的第二个子元素为P元素的每个P元素

```html
p:nth-child(2){color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:nth-child(2)')
for eleObj in eleObjList:
    print(eleObj.text)
```

### p:nth-child(even)

选择属于其父元素的序数为偶数(even)的子元素为P元素的每个P元素

```html
p:nth-child(even){color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:nth-child(even)')
for eleObj in eleObjList:
    print(eleObj.text)
```

选择属于其父元素的序数为序数为奇数(odd)的子元素为P元素的每个P元素

```html
p:nth-child(odd){color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:nth-child(odd)')
for eleObj in eleObjList:
    print(eleObj.text)
```

### p:nth-last-child(n)

选择属于其父元素的倒数第二个子元素为P元素的所有P元素

```html
p:nth-last-child(2){color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:nth-last-child(2)')
for eleObj in eleObjList:
    print(eleObj.text)
```

## nth-of-type选择器

### p:first-of-type

选择属于其父元素的第一个为P元素的所有P元素

```html
p:first-of-type{color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:first-of-type')
for eleObj in eleObjList:
    print(eleObj.text)
```

### p:last-of-type

选择属于其父元素的最后一个为P元素的所有P元素

```html
p:last-of-type{color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:last-of-type')
for eleObj in eleObjList:
    print(eleObj.text)
```

### p:only-of-type

选其父元素只有**唯一**一个元素且元素为P的每个p元素，如果有多个也不会被选中

```html
p:only-of-type{color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:only-of-type')
for eleObj in eleObjList:
    print(eleObj.text)
```

### p:nth-of-type(n)

选其父元素第二个元素且元素为P的每个p元素，如果有多个也不会被选中

```html
p:nth-of-type(2){color:red;font-size:20px;background-color:yellow;}
```

```py
eleObjList = driver.find_elements_by_css_selector('p:nth-of-type(2)')
for eleObj in eleObjList:
    print(eleObj.text)
```

更多CSS选择器的介绍，可以参考[CSS 选择器参考手册](http://www.w3school.com.cn/cssref/css_selectors.asp)


<br>

##  验证 CSS  Selector 
那么我们怎么验证  CSS Selector 的语法是否正确选择了我们要选择的元素呢？

当然可以像下面这样，写出Python代码，运行看看，能否操作成功

```py
element = driver.find_element_by_css_selector('#searchtext')
element.input('输入的文本')
```             

如果成功，说明选择元素的语法是正确的。

<br>

但是这样做的问题就是：太麻烦了。

当我们进行自动化开发的时候，有大量选择元素的语句，都要这样一个个的验证，就非常耗时间。

<br>

由于 CSS Selector 是浏览器直接支持的，可以在浏览器 **开发者工具栏** 中验证。

比如我们使用Chrome浏览器打开 http://www.python3.vip/doc/tutorial/selenium/code/sample1.html

按F12 打开 开发者工具栏


如果我们要验证 下面的表达式  

```
#bottom > .footer2  a
```  

能否选中 这个元素

```html
<a href="http://www.miitbeian.gov.cn">苏ICP备88885574号</a>
```

可以这样做：

点击 Elements 标签后， 同时按 Ctrl 键 和 F 键， 就会出现下图箭头处的 搜索框

![白月黑羽Python3教程](https://user-images.githubusercontent.com/36257654/38160687-1fe71db4-34f4-11e8-81e7-b65b5edd5e69.png)

我们可以在里面输入任何 CSS Selector 表达式 ，如果能选择到元素， 右边的的红色方框里面就会显示出类似
 ```2 of 3``` 这样的内容。 

of 后面的数字表示这样的表达式 ```总共选择到几个元素``` 

of 前面的数字表示当前黄色高亮显示的是 ```其中第几个元素``` 

上图中的  ```1 of 1```  就是指 ： CSS 选择语法   ```#bottom > .footer2  a``` 



在当前网页上共选择到 1 个元素， 目前高亮显示的是第1个。

如果我们输入 ```.plant```  就会发现，可以选择到3个元素

![白月黑羽Python3教程](https://user-images.githubusercontent.com/36257654/38160817-d286d148-34f5-11e8-8488-db5bf83bc7f3.png)




{% include sharepost.html %}