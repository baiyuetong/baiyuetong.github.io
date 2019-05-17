---
title: 第十一章 实战技巧中篇
---



## 手机模式进行自动化


我们可以通过  ```desired_capabilities``` 参数，指定以手机模式打开chrome浏览器

参考代码

```py
from selenium import webdriver

mobile_emulation = { "deviceName": "Nexus 5" }

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome( desired_capabilities = chrome_options.to_capabilities())

driver.get('http://www.baidu.com')

input()
driver.quit()
```


## 冻结界面

有些网站上面的元素， 我们鼠标放在上面，会动态弹出一些内容。 

比如，百度首页的右上角，有个 **更多产品** 选项，如下图所示

![白月黑羽Python3教程](https://user-images.githubusercontent.com/36257654/44762007-09953a00-ab78-11e8-979e-da7933a78b54.png)


如果我们把鼠标放在上边，就会弹出 下面的 糯米、音乐、图片 等图标。

如果我们要用 selenium 自动化 点击 糯米图标，就需要 F12 查看这个元素的特征。

但是  当我们的鼠标 从 糯米图标 移开， 这个 栏目就整个消失了， 没办法点击 开发者工具栏的 查看箭头， 再去 点击  糯米图标 ，查看其属性。

怎么办？



可以如下图所示：

![白月黑羽Python3教程](https://user-images.githubusercontent.com/36257654/44762324-3e55c100-ab79-11e8-89af-4a744d775c45.png)

在 开发者工具栏 console 里面执行如下js代码

```js
setTimeout(function(){debugger}, 5000)
```

这句代码什么意思呢？

表示在 5000毫秒后，执行 debugger 命令

执行该命令会 浏览器会进入debug状态。 debug状态有个特性， 界面被冻住，  不管我们怎么点击界面都不会触发事件。


<br>

所以，我们可以在输入上面代码并回车 执行后， 立即 鼠标放在界面 右上角 更多产品处。

这时候，就会弹出  下面的 糯米、音乐、图片 等图标。 

然后，我们仔细等待 5秒 到了以后， 界面就会因为执行了 debugger 命令而被冻住。


然后，我们就可以点击 开发者工具栏的 查看箭头， 再去 点击  糯米图标 ，查看其属性了。





## 获取当前窗口标题

浏览网页的时候，我们的窗口标题是不断变化的，可以使用WebDriver的title属性来获取当前窗口的标题栏字符串。

```py
driver.title
```

## 获取当前窗口URL地址

```py
driver.current_url
```

例如，访问白月黑羽Python在线教程网站，并获取当前窗口的标题

```py
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import  webdriver

driver = webdriver.Chrome(r"G:\Education\BYHY\Courseware\Improvement\Selenium\chromedriver.exe")
driver.implicitly_wait(5)

# open URL
URL = 'https://www.python3.vip/'
driver.get(URL)

print(driver.title) # get title
print(driver.current_url) # get current url

# ==================================================
input('Please input any key to continue......')
# Quit
driver.quit()
```

如果在浏览网页过程中,你想不断的获取窗口标题和URL的变化情况，那么我就可以用while循环（详情可参考[白月黑羽在线教程](http://www.python3.vip/doc/tutorial/python/0011/#while-循环)）就可以了

```py
while True:
    print(driver.title) # get title
    print(driver.current_url) # get current url
```

## 截屏

有的时候，我们需要截取浏览器屏幕的内容， 最常见的一个场景是，测试不通过的时候，比如一个界面预期的值不对，需要截屏，以便后面进行查看，截屏的操作，我们可以使用WebDriver的get_screenshot_as_file方法来截获前窗口内容，并保存为文件。

```py
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import  webdriver
import time

driver = webdriver.Chrome(r"G:\Education\BYHY\Courseware\Improvement\Selenium\chromedriver.exe")
driver.implicitly_wait(5)

# open URL
URL = 'https://www.baidu.com/'
driver.get(URL)
# ==================================================

element_keyword = driver.find_element_by_id('kw') .send_keys('白月黑羽')
element_search_button = driver.find_element_by_id('su').click()
driver.get_screenshot_as_file('1.png')

# ==================================================
input('Please input any key to continue......')
# Quit
driver.quit()
```

## 窗口切换和关闭

浏览网页时经常遇到点击一个超链接或者按钮，打开了一个新窗口，但是 这时候，web driver对象这时指向的还是当前的网页，那么我们如何到指定的窗口，继续模拟用户操作呢？selenium提供了如下 方法来切换新窗口
driver.switch_to.window(handle)

WebDriver对象都有window_handles 属性，它是一个列表对象，里面包括了当前浏览器里面所有的窗口句柄。 句柄可以想象成对应网页窗口的一个变量。这样我们就和driver.title就可以进行切换了

例如：从百度搜索‘白月黑羽’来访问www.python3.vip.

```py
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import  webdriver
import time

driver = webdriver.Chrome(r"G:\Education\BYHY\Courseware\Improvement\Selenium\chromedriver.exe")
driver.implicitly_wait(5)

# open URL
URL = 'https://www.baidu.com/'
driver.get(URL)
# ==================================================
element_keyword = driver.find_element_by_id('kw') .send_keys('白月黑羽')
element_search_button = driver.find_element_by_id('su').click()
print(driver.title)

driver.find_element_by_id('2').find_element_by_partial_link_text('白月黑羽教Python').click()

mainWindow = driver.current_window_handle

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if '白月黑羽学python' in driver.title:
        break

driver.switch_to.window(mainWindow) # switch back to default windows
driver.close() # 关闭默认窗口

# ==================================================
input('Please input any key to continue......')
# Quit
driver.quit()
```

当打开多个窗口的时候，我们确定不再需要某个窗口，进行操作，可以关闭它，就可以使用WebDriver的close方法来关闭当前窗口，上面的代码中就是这样

```py
driver.switch_to.window(mainWindow) # switch back to default windows
driver.close() # 关闭默认窗口
```

和quit方法不同，quit是关闭整个浏览器和webdriver进程， 而close 仅仅关闭当前的窗口（浏览器可以打开很多窗口），当然如果浏览器只打开一个窗口，就会关闭浏览器了。

## 弹窗确认

有的时候，我们经常会在操作界面的时候，出现一些弹出的对话框，这种类型的对话框有三种,分别是警告信息、确认信息和提示输入

### Alert

alert通常就是一个通知只需我们点击 OK 就可以了，selenium提供如下方法进行操作

```py
driver.switch_to.alert.accept()
```

**注意**：如果我们不去点击它，页面的其它元素是不能操作的。这时如果想验证弹出对话框中的信息内容  是不是我们预期，可以通过 如下方法获取其中的信息

```py
driver.switch_to.alert.text
```

### confirm

确认弹窗，一般会有两个选择供用户选择，分别是OK和cancel。
如果我们想选择 确定 ok 按钮， 可以用刚才的accept， 如果我们想选择 取消cancel 按钮， 可以用 dismiss方法

```py
driver.switch_to.alert.dismiss()
```

### prompt

prompt类型的弹窗需要用户输入一些信息，再点击prompt按钮提交，可以调用如下方法

```py
driver.switch_to.alert.send_keys()
```

例如，有如下测试网页，我们来进行测试

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pop up windows Test</title>
</head>
<script>

function appendEle(info) {
    var node = document.createElement("LI");
    var textNode = document.createTextNode(info);
    node.appendChild(textNode);
    document.getElementById("add").appendChild(node);
}

function clickResponse() {
    if (confirm("我要和白月黑羽一起学Python") == true) {
        appendEle("你选择和白月黑羽一起学Python");
    } else {
        appendEle("你取消学习Python课程");
    }
}


function clickPrompt() {
    var PythonCourse = prompt("请输入你想学习的Python课程", "Python基础");

    if (PythonCourse == null ) {
        appendEle("你没有输入想要学习的课程");
    } else {
        appendEle("你想学习:" + PythonCourse);
    }
}

</script>
<body>

<br>
<br>
<button id="b1" onclick='alert("现在开始和白月黑羽一起学Python!");'>alert</button>

<br>
<br>
<button id="b2" onclick='clickResponse()'>confirm</button>

<br>
<br>
<button id="b3" onclick='clickPrompt()'>prompt</button>

<div id="add"></div>
</body>
</html>
```

测试代码为

```py
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import  webdriver
import time

driver = webdriver.Chrome(r"G:\Education\BYHY\Courseware\Improvement\Selenium\chromedriver.exe")
driver.implicitly_wait(5)

# open URL
URL = r'file:///G:/Education/BYHY/Courseware/Improvement/Selenium/10Selenium_advance_skill1/popup.html'
driver.get(URL)
# ==================================================

#
# case for alert
#
driver.find_element_by_id('b1').click()
print(driver.switch_to.alert.text) # get alert text
time.sleep(2)
print('waiting for 2 seconds and then click OK button')

# driver.find_element_by_id('other').click()
driver.switch_to.alert.accept()

#
# case for confirm
#
# OK
driver.find_element_by_id('b2').click()
time.sleep(2)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()

# cancel
driver.find_element_by_id('b2').click()
time.sleep(2)
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

#
# case for prompt
#

# OK
driver.find_element_by_id('b3').click()
time.sleep(2)

alert = driver.switch_to.alert
print (alert.text)
alert.send_keys('web自动化 - selenium')
alert.accept()

# cancel
driver.find_element_by_id('b3').click()
time.sleep(2)

alert = driver.switch_to.alert
print (alert.text)
alert.dismiss()

# ==================================================
input('Please input any key to continue......')
# Quit
driver.quit()
```

**注意**：
这里需要提醒一下大家，有些弹窗并非浏览器的alert 窗口，而是**html元素**，这种对话框，只需要通过之前介绍的选择器选中并进行常规的Selenium操作就可以了。


## 窗口控制

有时间我们需要获取窗口的属性和相应的信息，并对窗口进行控制

+ 获取窗口大小

```py
driver.get_window_size()
```

+ 改变窗口大小

```py
driver.set_window_size(x, y)
```

## 鼠标移动

之前我们对web元素做的操作一直就是**选择**，然后**点击**或者**输入**字符串。有的时候,当我们移动鼠标到某个元素上，会导致界面的一些出现一些变化，下面我们看看这种情况如何处理。



{% include sharepost.html %}



[上一页](/doc/tutorial/selenium/10other_skills1/){: .btn .btn--primary .align-left }
[下一页](/doc/tutorial/selenium/12other_skill3/){: .btn .btn--primary .align-right }
