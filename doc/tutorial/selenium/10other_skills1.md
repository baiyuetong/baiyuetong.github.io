---
title: 第十章 实战技巧上篇
---

## 操作元素小结

Web自动化的重点是定位到元素，然后才是操作元素 ，从前面的介绍中学习到的操作元素主要包括以下两个方面：

+ 获取元素的信息，比如常用的：
  1. 用 text属性获取文本信息
  2. 用get_attribute方法获取利用html属性值

+ 模拟用户操作，比如：

  1. 输入字符： send_keys方法
  2. 点击元素：click方法

大家可以看得出来，根据不同的web元素对象，用不同的方法来操作，后面向大家介绍一下其他常见的web元素对象及方法

假设对下面的网页进行操作

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Option select</title>
</head>
<body>
<h3>input box test</h3>
  <div>
   <input id="input1" value="Please input your name here">
   <br><br>
  </div>

<h3>simple selection</h3>
<div id="s_radio">
  <input type="radio" name="teacher" value="SK"> SK<br>
  <input type="radio" name="teacher" value="BYHY"> BYHY<br>
  <input type="radio" name="teacher" value="Lei"> 小雷老师<br>
  <input type="radio" name="teacher" value="Kai" checked="checked"> 小凯老师
</div>
<hr>

<div id="s_checkbox">
  <input type="checkbox" name="teacher" value="Lei"> 小雷老师<br>
  <input type="checkbox" name="teacher" value="Kai" checked="checked"> 小凯老师
</div>


<h3>multiple selection</h3>
<div id="s_multi">
  <input type="checkbox" name="teacher" value="SK" >SK<br>
  <input type="checkbox" name="teacher" value="lemon" >柠檬老师<br>
  <input type="checkbox" name="teacher" value="mi" >小米老师<br>
  <input type="checkbox" name="teacher" value="lei" >小雷老师<br>
  <input type="checkbox" name="teacher" value="Kai" checked>小凯老师<br>
</div>

<h3>drop-down list selection</h3>
<div>
<ul>
    <li>drop-down list selection - single</li>
    <p>姓名:
<select id="single">
    <option value="SK" selected="selected">SK</option>
    <option value="lemon">柠檬老师</option>
    <option value="mi">小米老师</option>
    <option value="Kai">小雷老师</option>
    <option value="Kai">小凯老师</option>
</select></p>

<hr>

<li>drop-down list selection - multi</li>
    <p>课程:
<select  id="multi" multiple>
    <option value="Python" selected="selected">Python Basic</option>
    <option value="Selenium">Selenium</option>
    <option value="BS4">Beautiful soup</option>
    <option value="scrapy">scrapy</option>
    <option value="django">Django</option>
    <option value="pygame">pygame</option>
    <option value="wechatgame">wechat game</option>
</select> </p>
</ul></div>
<hr>
</body>
</html>
```

## 文本输入框

选择id为input1的输入框，并输入：BYHY

1. 如果输入框中存在默认的提示字符，需要先去掉
2. 可以通过get_attribute方法获取内容

示例如下

```py
# select
eleObj = driver.find_element_by_id("input1")

eleObj.clear() # clear the default value
eleObj.send_keys('BYHY') # input the value
print(eleObj.get_attribute('value')) # get the text message
```

在这里大家注意下，获取文本内容的方法和之前是不一样的，之前是通过text属性，输入框是通过get_attribute方法

## 选择框

选择框是我们常见的一种web元素，要对选择框进行选择，还要区分是何种类型的选择框

### 点选框

点选类型的单选框，直接用WebElement的click方法，模拟用户点击就可以了。不管原来该元素是否选中，直接去点击该元素就可以确保该单选框选中

例如：

1. 先打印默认选择的老师
2. 再选择示例网页中的SK

```html
<div id="s_radio">
  <input type="radio" name="teacher" value="SK"> SK<br>
  <input type="radio" name="teacher" value="BYHY"> BYHY<br>
  <input type="radio" name="teacher" value="Lei"> 小雷老师<br>
  <input type="radio" name="teacher" value="Kai" checked="checked"> 小凯老师
</div>
```

示例代码

```py
eleObj = driver.find_element_by_css_selector('#s_radio input[checked=checked]')
print('default select is: ' + eleObj.get_attribute('value'))

eleObj = driver.find_element_by_css_selector('#s_radio input[value=SK]')
eleObj.click()
print('current select is: ' + eleObj.get_attribute('value'))
```

### 勾选框

对勾选框进行选择，直接用WebElement的click方法，模拟用户点击需要注意的一点，必须先获取当前该选择框的状态，如果是已经选择，就不能再点击，如果再次点击已经选中的勾选框，反而会取消选择

例如：
1.反选默认的选项
2 选中期望的选项

```html
<div id="s_checkbox">
  <input type="checkbox" name="teacher" value="Lei"> 小雷老师<br>
  <input type="checkbox" name="teacher" value="Kai" checked="checked"> 小凯老师
</div>
```

示例代码

```py
eleObjList = driver.find_elements_by_css_selector('#s_checkbox input[name=teacher][checked]')

for eleObj in eleObjList:
    eleObj.click()
driver.find_element_by_css_selector("#s_checkbox input[value=Lei]").click()
```

### 下拉列表

单选框及勾选框都是input元素，只是里面的type不同而已，但对于下拉列表来说，则是一个新的select标签，利用select 元素来创建单选或多选菜单，例如

```html
<h3>drop-down list selection</h3>
<div>
<ul>
    <li>drop-down list selection - single</li>
    <p>姓名:
<select id="droplist_single">
    <option value="SK" selected="selected">SK</option>
    <option value="lemon">柠檬老师</option>
    <option value="mi">小米老师</option>
    <option value="Kai">小雷老师</option>
    <option value="Kai">小凯老师</option>
</select></p>

<hr>

<li>drop-down list selection - multi</li>
    <p>课程:
<select  id="droplist_multi" multiple>
    <option value="Python" selected="selected">Python Basic</option>
    <option value="Selenium">Selenium</option>
    <option value="BS4">Beautiful soup</option>
    <option value="scrapy">Scrapy</option>
    <option value="django">Django</option>
    <option value="pygame">pygame</option>
    <option value="wechatgame">wechat game</option>
</select> </p>
</ul></div>
```

对于Select 选择框， Selenium为我们提供了一个方便的Select类,可以利用这个类提供的方法来进行选择和操作

#### 单选

对于单选的select框，操作比较简单，不管原来选的是什么，我只需利用select_by_visible_text方法选择我们要选择的选项即可。
例如，选择小凯老师，示例代码如下

```py
# 导入Select类
from selenium.webdriver.support.ui import Select

#
# 下拉菜单-单选
#

# 获得相应的WebElement
select = Select(driver.find_element_by_id("droplist_single"))
select.select_by_visible_text("小凯老师")
```

#### 多选

对于多选框，如果已经有选择的，我们需要先利用select类提供的deselect_all方法，清除所有已经处于选中状态的选项，然后再通过方法select_by_visible_text，根据选项的内容进行选择。
例如，我们选择课程Django和Scrapy，示例代码如下：

```py
# 导入Select类
from selenium.webdriver.support.ui import Select

#
# 下拉菜单-多选
#

# 选取相应的WebElement
select = Select(driver.find_element_by_id("droplist_multi"))
print(type(select))

# 清除选项
select.deselect_all()

# 选择期望的选项
select.select_by_visible_text("Scrapy")
select.select_by_visible_text("Django")
```


{% include sharepost.html %}



[上一页](/doc/tutorial/selenium/09xpath_selector2/){: .btn .btn--primary .align-left }
[下一页](/doc/tutorial/selenium/11other_skills2/){: .btn .btn--primary .align-right }
