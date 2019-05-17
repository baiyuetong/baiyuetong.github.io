---
title: 进程和线程
toc: true
---

## 调用其它程序，并且判断其返回码


程序执行结束退出，会有一个退出码。
通常表示程序是否正确执行退出
一般来说，返回值为零，表示命令执行成功。

python中，os.system() 可以调用其它程序，
windows 下面，python程序使用 os.system来调用其它程序时，返回值就是被调用程序的退出码

而 Linux下面， python程序使用 os.system来调用其它程序时，返回值是一个16位的数字，
低位字节 表示结束进程的信号数值，如果低8位字节值为0， 高8位字节表示退出码

 

我们使用 Python在其它程序时，判断调用这个程序是否成功。
那么只需要根据调用的返回值是否为零即可判断。

如下：


```py
import os
ret = os.system('dir c:/onefolder')
if ret==0:
    print ('被调用程序正常退出')
else:
    print ('被调用程序异常退出')
```


因为 不管是windows，Linux，  Python使用 os.system 调用 其它程序，该程序的退出码如果是0，os.system 调用 返回码肯定也是0

## 调用其它程序，并且获取输出结果

如果想获取被调用的程序输出到终端的信息 并进行处理，可以使用
subprocess库里面的check_output 函数

比如：

```py
import subprocess
info = subprocess.check_output('dir', shell=True, encoding='gbk')
print(info)
```

注意，参数encoding应该设置为该程序输出信息文本的编码方式。
很多程序通常会根据当前终端使用的字符编码格式来决定 输出文本的编码方式。
比如 通常在中文windows的cmd终端上，字符编码方式为 gbk， 所以这里这样指定： encoding='gbk'

正确指定了字符编码方式， check_output 函数 才能正确将 终端上输出的 文本字节串，解吗为python里面的unicode字符串对象



## 非阻塞式调用其它程序

我们的Python程序 调用  os.system 和 subprocess.check_output 时，都会等待该程序退出后，才会继续执行后续的代码。

如果我们的Python程序本身并不需要等待外部程序结束。
比如，我们启动 wget下载命令， 下载1个文件。让它下载就可以了， 然后我们的程序还要继续去做其他的任务。
这时候， 我们就不能用os.system， 因为它会等待 外部程序结束。
我们可以用subprocess里面的Popen，像这样


```py
from subprocess import Popen
proc = Popen(
        args='wget http://xxxxserver/xxxx.zip',
        shell=True
    )

print ('让它下载，我们接下来做其他事情。。。。')
```




{% include sharepost.html %}
