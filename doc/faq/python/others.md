---
title: 其他
toc: true
---

## 运行Python程序，提示找不到Python命令

如果你运行python的时候，显示如下

```
c:\>python first.py
'python' 不是内部或外部命令，也不是可运行的程序
或批处理文件。
```

这是因为，你安装Python解释器的时候，没有勾选 add Python to path


所以，命令行程序找不到Python.exe 在什么地方。

怎么解决这个问题呢？

如果你是Windows 操作系统，不需要重装Python， 在Windows环境变量path里面加上 Python解释器所在路径即可。


点击这里，打开windows设置

![image](https://user-images.githubusercontent.com/36257654/56074007-e739ef00-5ddd-11e9-961a-1ac5c0aaf6e8.png)

<br>

然后，如下下图所示，输入 huanj，点击  ```编辑系统环境变量``` 

![image](https://user-images.githubusercontent.com/36257654/56074016-0cc6f880-5dde-11e9-9e15-bd09e3f15d61.png)


<br>

然后，在弹出对话框中，点击 环境变量

![image](https://user-images.githubusercontent.com/36257654/56074033-3f70f100-5dde-11e9-86cc-16df019eb881.png)


<br>

然后，双击系统变量栏目下面的 path 这条

![image](https://user-images.githubusercontent.com/36257654/56074037-62030a00-5dde-11e9-8d41-4064ada88ada.png)


<br>

然后，按照下图操作


![image](https://user-images.githubusercontent.com/36257654/56074076-e6558d00-5dde-11e9-91b2-667c0b879a6e.png)

<br>

注意：

- 你要看看你的python解释器安装在什么目录，填写你的目录。

- 一定是python所在目录 ，不要在最后加上python.exe

- 把python目录中的scripts目录也加上，就是最后要多两条记录，如下所示


![image](https://user-images.githubusercontent.com/36257654/56074096-3d5b6200-5ddf-11e9-8793-eb341e19650e.png)


<br>

最后，很重要，


因为刚才对环境变量的修改，对已经打开的窗口不生效！！！

所以你必须 ```关闭``` 你已经打开的命令行窗口， **重新打开一个窗口** ， 再次执行python程序。

好了，大功告成。 

<br>

## 运行Python程序，提示找不到代码文件


如果你运行python的时候，显示如下

```
c:\>python first.py
python: can't open file 'first.py': [Errno 2] No such file or directory
```

这是什么原因？

要运行一个Python脚本，通常我们需要打开命令行窗口，并 ```进入到该脚本所在的目录``` 。 这样Python解释器才能找到这个程序。

比如我们要运行的Python脚本的全路径 是 'd:\tmp\price.py'

那么我们通常需要进入到 'd:\tmp' 目录下面，然后再执行 命令  ```python price.py```

当然，你也可以 在命令行中使用 脚本的全路径 ， 像这样  ```python d:\tmp\price.py``` 。 就可以在任意目录下面执行成功了。




<br>

## 查看和修改当前工作目录

当前Python程序的工作目录，可以通过 ```os.getcwd``` 获得，如下

```py
import os
curDir = os.getcwd()
```

如果要修改当前工作目录，使用 ```os.chdir```，如下

```py
import os
os.chcwd('d:\\home')
```


<br>

## 查看导入的模块的路径

要知道导入的模块 对应的 代码文件的路径，可以使用模块的 ```__file__``` 属性。

如下所示

```py
>>> import selenium
>>> selenium.__file__
'C:\\Python36\\lib\\site-packages\\selenium\\__init__.py'
>>>
```


<br>

## 查看当前正在执行的代码文件的路径

有时候，我们需要得到 当前执行的代码文件 的 全路径。

这时候，我们可以 使用  ```os.path.realpath(__file__)``` 

如下所示 

```py
import os

# 当前代码文件路径
current_script_path = os.path.realpath( __file__ )
print(current_script_path)

# 代码文件所在目录路径
print(os.path.dirname(current_script_path))
```


<br>

## 查看当前运行的python解释器的路径

有时候，我们需要得到 当前运行的python解释器的路径。

比如，我们需要使用当前的python解释器再运行 另外一个脚本程序

这时候，我们可以 使用  ```sys.executable``` 得到当前运行的python解释器的路径。

如下所示 

```py
import os,sys

pid_or_handle1 = os.spawnl(
    os.P_NOWAIT,
    sys.executable,
    sys.executable, 
    "otherscript.py", 
    'param1',
    'param2')
```

<br>

## 判断一个对象是否可以执行

hasattr函数可以用来判断变量对应的对象是否是可执行的。

返回值为True就是可执行的。

如下所示

```py
def obj1():
    pass

obj2 = 'ok'

hasattr(obj1,'__call__') # 返回 True
hasattr(obj2,'__call__') # 返回 False

```


<br>

## 字符串IP地址转换为 整数IP地址

我们做性能测试时，有时需要让网卡绑定很多IP地址，这时候，需要 把字符串IP地址转换为 整数IP地址。

可以这样做

```py
import socket,struct

strIP = "192.168.0.1"
intIP = socket.ntohl(struct.unpack("I",socket.inet_aton(strIP))[0])
print(intIP)
```

如果反过来，需要把 整数IP转换为字符串IP，可以这样

```py
import socket,struct
intIP = 3232235521
strIP = socket.inet_ntoa(struct.pack('I',socket.htonl(intIP))) 
print(strIP)
```

{% include sharepost.html %}