---
title: 隐藏py文件
toc: false
---

有的时候，你用python给别人（企业）开发了一个软件工具。出于某种原因，你的可能不希望别人看到工具里面的python代码。


怎么办？

我们可以把代码目录中所有的py文件都转化为pyc文件。然后删除掉所有的py文件。


<br><br>

首先，我们进入到代码文件所在的最上层目录。

假如，我们有一个目录  ```e:\byhy\stats``` 

stats 目录 里面包含了工具对应的Python源代码。

目录结构如下所示

```
E:\BYHY\STATS
│  entry.py
│
└─libs
    │  getaddress.py
    │  getissue.py
    │
    └─thirdparty
            alilib.py
            hostinfo.py
```

我们发现，stats目录 里面有好几层目录，它们中都有python代码文件。

怎么才能一起转化为pyc文件呢？

按照如下步骤操作：

- 打开命令行窗口进入到 代码根目录，本例中就是 stats 目录

- 输入python并回车，运行python交互式命令行


```
e:\>cd byhy\stats

e:\byhy\stats>python
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

- 输入如下命令


```
>>> import compileall
>>> compileall.compile_dir('./', force=True,legacy=True)
```

即可把 当前目录下所有的py文件全部编译为pyc文件，包括子目录里面的py文件。

运行显示如下内容

```
>>> import compileall
>>> compileall.compile_dir('./', force=True,legacy=True)
Listing './'...
Compiling './entry.py'...
Listing './libs'...
Compiling './libs\\getaddress.py'...
Compiling './libs\\getissue.py'...
Listing './libs\\thirdparty'...
Compiling './libs\\thirdparty\\alilib.py'...
Compiling './libs\\thirdparty\\hostinfo.py'...
True
>>>
>>>exit() # 输入exit() 退出
```

打开目录，你就可以发现，每个py文件都相应的产生了pyc文件。

<br>

最后结果如下

```
E:\BYHY\STATS
│  entry.py
│  entry.pyc
│
└─libs
    │  getaddress.py
    │  getaddress.pyc
    │  getissue.py
    │  getissue.pyc
    │
    └─thirdparty
            alilib.py
            alilib.pyc
            hostinfo.py
            hostinfo.pyc
```

<br>

现在还有一个问题， 我们还要删除所有的 py 文件， 一个个的删太麻烦了，怎么办？

在Windows上很简单，就是执行命令  ```DEL /S /Q *.py``` 即可。

这个命令就是删除当前目录中所有扩展名为py的文件，也包括子目录。

注意，一定要进入到 正确的代码根目录，千万不要进错目录。

进错了目录，可能会删除掉你辛辛苦苦写的代码！！！！！ 千万注意！！！！

```
e:\>cd byhy\stats

e:\byhy\stats>DEL /S /Q *.py
删除文件 - e:\byhy\stats\entry.py
删除文件 - e:\byhy\stats\libs\getaddress.py
删除文件 - e:\byhy\stats\libs\getissue.py
删除文件 - e:\byhy\stats\libs\thirdparty\alilib.py
删除文件 - e:\byhy\stats\libs\thirdparty\hostinfo.py
```


{% include sharepost.html %}




<br><br>

[上一页](/doc/tutorial/python/level2/excel/){: .btn .btn--primary .align-left }
[下一页](/doc/tutorial/python/level2/1007/){: .btn .btn--primary .align-right }