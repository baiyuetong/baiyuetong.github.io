---
title: Python练习：日期和时间操作
toc: true
---



## 题目1

请写一个程序，打印出从当天开始，在一年内，所有的周日对应的日期

## 题目2


[点击这里](http://v.python666.vip/file/py/esn.log){:target="_blank"} 下载一个日志文件 esn.log

该文件记录了购物平台的购物记录，文件格式如下

```
1456190061> buy product id=vscwg9mg0rg0vt44z1aq
1456071815> buy product id=35u0c7v9jccbbooabssf
1456622256> buy product id=62amh5za0wp2u7rirz75
1456203485> buy product id=m3m6ctfjqy2ykby20gzi
1456439890> buy product id=gpjr76jn74k287fgvj8f
1456021921> buy product id=d53xy60flulobpxyk95c
```

其中 每行 尖括号之前为数字时间戳，表示记录该行信息的时间，也就是用户购物的时间。

请写一个程序，分析该日志文件，得出一张表，记录每一天合计的购物次数，输出格式如下：


```
2016-02-21 : 购物 66 次
2016-03-01 : 购物 99 次
2016-02-23 : 购物 87 次
2016-03-03 : 购物 58 次
```


[答案与解析](#题目1-答案)



{% include sharepost.html %}


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

## 题目1-答案


```python
from datetime import datetime,timedelta
today = datetime.now().date()

for i in range(365):
    thatDay = today + timedelta(days=i)
    if thatDay.weekday() == 6:
        print(thatDay.strftime('%Y-%m-%d'))
```



<br><br><br>


## 题目2-答案


```python
import time

buyTable = {}

with open('esn.log') as f:
    lines = f.readlines()

    for line in lines:
        # 如果是空行
        if not line.strip():
            continue

        timestamp = int(line.split('>')[0])

        # 转化为字符串时间，包含年月日即可
        # 方便判断是否是某天
        ymd = time.strftime('%Y-%m-%d',time.localtime(timestamp))

        # 表中已经有当天记录，+1次
        if ymd in buyTable:
            buyTable[ymd] += 1
        else:
            buyTable[ymd] = 1

for date,times in buyTable.items():
    print(f'{date} : 购物 {times} 次')
```