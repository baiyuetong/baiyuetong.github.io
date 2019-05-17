---
title: Python练习：正则表达式
---

## 题目1


这个网址 [https://www.listeningexpress.com/studioclassroom/ad/](https://www.listeningexpress.com/studioclassroom/ad/){:target="_blank"}

包含了优质的英语学习音频文件。

这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：

![image](https://user-images.githubusercontent.com/36257654/56080767-d0c08180-5e37-11e9-88c4-14bd09fd9f22.png)



<br>
要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址，并且调用外部程序wget依次下载下来。

Windows上的wget可以[点击这里](https://eternallybored.org/misc/wget/1.19.4/32/wget.exe) 下载。 这个程序不用安装，直接在命令行里使用即可

注意：

- 获取的音频网址前面需要加上 前缀  ```https://www.listeningexpress.com/studioclassroom/ad/```  才是完整的下载地址

- MP3文件中有空格字符，组成下载网址时，需要进行url编码，否则空格会被当成命令行分隔符。参考代码如下所示

```py
>>> from urllib.parse import quote
>>> quote('2019-04-13 NEWSworthy Clips.mp3')
'2019-04-13%20NEWSworthy%20Clips.mp3'
```

 

[答案与解析](#题目1-答案)

### 答案视频讲解-1

<video src="http://v.python666.vip/video/py/mpprac2006-1-1.mp4"  style="width: 85%;" controls controlsList="nodownload" oncontextmenu="return false;" preload="metadata" poster="{{ site.video_cover }}"></video>


### 答案视频讲解-2

<video src="http://v.python666.vip/video/py/mpprac2006-1-2.mp4"  style="width: 85%;" controls controlsList="nodownload" oncontextmenu="return false;" preload="metadata" poster="{{ site.video_cover }}"></video>



{% include sharepost.html %}


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

## 题目1-答案


```python
import requests,re,os
from urllib.parse import quote

pageUrl = 'https://www.listeningexpress.com/studioclassroom/ad/'
WGET_EXE = r'd:\wget.exe'

res = requests.get(pageUrl)
content = res.text

p = re.compile(r"javascript:p\('(.*?\.mp3)'\)")
mp3links = p.findall(content)

print('获取到如下mp3文件:')
for link in mp3links:
    print(link)



for link in mp3links:
    fullAddr = pageUrl + quote(link)
    print(f'\n\n下载{fullAddr}')
    os.system(f'{WGET_EXE} {fullAddr}')
    print(f'ok')

```
