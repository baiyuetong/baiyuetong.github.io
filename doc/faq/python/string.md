---
title: 字符串操作
toc: true
---

## unicode数字转换为字符

把 unicode数字转换为字符， 使用chr(), 比如：

```py
>>> chr(50)
'2'
>>> chr(20013)
'中'
>>> chr(0x4e2d)  # 0x开头表示数字是16进制
'中'
```


## 字符转换为unicode数字

反过来，要把 字符转换为对应的unicode数字，使用 ord()
该函数参数字符串里面只能有一个字符

```py
>>> ord('2')
50
>>> ord('中')
20013
```


## 直接用16进制数字创建 字符串

```py
>>> '\u767d\u6708\u9ed1\u7fbd'
'白月黑羽'
```


## 直接用16进制数字创建 bytes

```py
>>> b'\xb0\xd7\xd4\xc2\xba\xda\xd3\xf0'
b'\xb0\xd7\xd4\xc2\xba\xda\xd3\xf0'

>>> b'\xb0\xd7\xd4\xc2\xba\xda\xd3\xf0'.decode('gbk')
'白月黑羽'
```

## 字节串 和 16进制表示字节的字符串

```py
>>> a = b'hello,123'
>>> a.hex()
'68656c6c6f2c313233'
```

反向操作，把 16进制表示字节的字符串 转化为 字节串就是

```py
>>> bytes.fromhex('68656c6c6f2c313233')
b'hello,123'
```

##  将字符串切割为多个字符串

[请点击这里，参考我们教程](/doc/tutorial/python/0009/#split)




##  使用正则表达式切割字符串

字符串 对象的 split() 方法只适应于非常简单的字符串分割情形。当你需要更加灵活的切割字符串的时候，就不好用了。

比如，下面字符串中包含的名字， 有的是分号隔开 ，有的是逗号隔开，有的是空格隔开， 而且分割符号周围还有不定数量的空格
```py
names = '关羽; 张飞, 赵云,马超, 黄忠  李逵'
```

这时，最好使用正则表达式里面的 split  方法：

```py
import re

names = '关羽; 张飞, 赵云,   马超, 黄忠  李逵'

namelist = re.split(r'[;,\s]\s*', names)
print(namelist)
```

正则表达式 ```[;,\s]\s*``` 指定了，分割符为 分号、逗号、空格 里面的任意一种均可，并且 该符号周围可以有不定数量的空格。






##  使用split函数从字符串中提取内容

比如：从下面格式的字符串中提取出 UID号

```
添加用户 byhy(UID 5533)成功
```

可以这样写

```py
uid = content.split('(UID ')[1].split(')')[0]
print(f'uid is :{uid}')
```


##  使用正则表达式从字符串中提取内容

使用正则表达，可以从多种可能格式的字符串中，提取我们想要的内容
比如，我们想要从下面这几种可能格式的字符串中提取 用户对应的UID号

```
添加用户 byhy(UID 5533)成功
添加用户 byhy(UID: 5533)成功
添加用户 byhy(UID     5533)成功
```


使用下面代码就可以了

```py
import  re
uid =  re.findall(r'\(UID\W*(\d*)\)', content)[0]
```

其中  ```\(UID\W*(\d*)\)```   是正则表达式， 
 ```content```  是被搜索的字符串
 ```findall```  方法会获取所有匹配该正则表达式的 子字符串，所以返回的是一个列表

关于Python中的正则表达式用法可以参考[Python官方文档](https://docs.python.org/3/library/re.html){:target="_blank"}


也可以[参考我们的教程](/doc/tutorial/python/level2/2006/){:target="_blank"}



##  将列表中的字符串元素合并为一个字符串

我们常常使用 使用字符串的 join 方法 把 列表中的字符串元素合并为一个字符串

[请点击这里，参考我们教程](/doc/tutorial/python/0009/#join){:target="_blank"}



##  字符串替换时忽略大小写

如果我们要替换字符串的时候， 不管大小写都需要替换，就可以使用 re 模块的sub函数

比如：

```py
import re

text = 'UPPER PYTHON, lower python, Mixed Python'

print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
```



##  字符串的格式化


[请点击这里，参考我们教程](/doc/tutorial/python/0010/){:target="_blank"}


## json格式字符串处理

我们如果需要将一个json格式的字符串转换为 Python中的对象进行处理，可以这样

```py
jsonStr = '''{
    "account1": 13, 
    "account2": 12, 
    "account3": 15}
'''

import json
membersObj = json.loads(jsonStr)
```

<br>

反之，可以这样将一个Python中的对象转换为 一个 json格式的字符串

```py
members = {
    'account1'  : 13 ,
    'account2'  : 12 ,
    'account3'  : 15 ,
}

import json
jsonStr = json.dumps(members)
```


## 字符串的倒序

要得到一个字符串的 倒序字符串，只需要使用切片操作 [::-1]

 ```::```  表示切片字符串的从头到尾，也就是全部内容， 而 步长 为 -1 表示，颠倒过来取元素

如下， 

```py
str1 = '字符串的倒序'
reverse = str1[::-1]
print(reverse)
```


{% include sharepost.html %}