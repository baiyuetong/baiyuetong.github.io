---
title: Python练习：目录和文件操作
toc: true
---


[点击这里](http://v.python666.vip/file/py/source.zip){:target="_blank"} 下载一个zip包，解压后，得到一个目录source。


## 题目1

请写一个程序，在当前工作目录下，创建 如下的目录层级结构 


backup/new/


然后把整个下载的source目录 内容，拷贝到 backup/new/source 目录里面去。

## 题目2

请写一个程序，计算出 下载的source目录里面（不包含子目录）所有的文件的大小之和

## 题目3

请写一个程序，删除掉 下载的source目录里面（不包含子目录）所有的扩展名为bmp的文件

## 题目4

请写一个程序，找出下载的source目录里面（不包含子目录）所有扩展名为.avi的文件，扩展名改为.dll


## 题目5

请写一个程序，找出下载的source目录里面（包含子目录）所有扩展名为.avi的文件，扩展名改为.dll




[答案与解析](#题目1-答案)



{% include sharepost.html %}


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

## 题目1-答案


```python
from shutil import copytree
import os

os.makedirs('backup/new')

copytree('source', 'backup/new/source')
```



## 题目2-答案


```python
import os
from os.path import isfile, join

# 目标目录
targetDir = 'source'

totalsize = 0
for f in os.listdir(targetDir):
    filePath = join(targetDir, f)
    if isfile(filePath):
        totalsize += os.path.getsize(filePath)

print(f'合计大小为 {totalsize} 字节')
```



## 题目3-答案


```python
import os
from os.path import isfile, join

targetDir = 'source'

totalsize = 0
for f in os.listdir(targetDir):
    filePath = join(targetDir, f)
    if isfile(filePath) and filePath.endswith('.bmp'):
        print(f'删除文件{filePath}')
        os.remove(filePath)
```


## 题目4-答案

```python
import os
from os.path import isfile, join

targetDir = 'source'

totalsize = 0
for f in os.listdir(targetDir):
    filePath = join(targetDir, f)
    if isfile(filePath) and filePath.endswith('.avi'):
        newname = filePath[:-3] + 'dll'
        os.rename(filePath,newname)
```



## 题目5-答案

```py
import os
from os.path import join

# 目标目录
targetDir = r'source'
files = []

# 下面的三个变量 dirpath, dirnames, filenames
# dirpath 代表当前遍历到的目录名
# dirnames 是列表对象，存放当前dirpath中的所有子目录名
# filenames 是列表对象，存放当前dirpath中的所有文件名

for (dirpath, dirnames, filenames) in os.walk(targetDir):
    for fn in filenames:
        filePath = join(dirpath, fn)
        if filePath.endswith('.avi'):
            newname = filePath[:-3] + 'dll'
            os.rename(filePath,newname)
```