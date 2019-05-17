---
title: 日期和时间
toc: true
---

## 获取当前时间对应的数字

开发程序时，经常需要获取两个代码位置在执行时的时间差，比如，我们想知道某个函数执行大概耗费了多少时间，就可以使用time.time()来做。

```py
before = time.time()
func1()
after = time.time()
print(f’调用func1，花费时间{before-after}’)
```

time.time() 会返回 从 1970年1月1日0点 到 当前时间的 经过的秒数 ，可以简称为秒数时间。
关于该函数的详细解释，请参考官方文档
https://docs.python.org/3/library/time.html#time.time


## 指定格式字符串显示时间

以指定格式字符串显示时间，是非常常用的，比如日志里面的时间戳。

可以这样实现：

```py
from datetime import datetime
str(datetime.now())
```

得到类似这样的字符串：'2018-06-30 23:10:08.911420'

如果要指定格式

```py
datetime.now().strftime('%Y-%m-%d %H:%M:%S')
```
得到类似这样的字符串： '2018-06-30 23:10:08'

也可以使用time库

```py
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) 
```

<br>

如果要将指定秒数时间转化为字符串格式，可以这样写

```py
time.strftime('%Y%m%d %H:%M:%S',time.localtime(1434502529)) 
```
<br>



## 字符串时间转化为整数时间

反过来，如果要将字符串指定的时间，转化为秒数时间，可以这样

```py
int(time.mktime(time.strptime('2015-08-01 23:59:59', '%Y-%m-%d %H:%M:%S')))
```



## 获取当前时间 对应 的年月日时分秒

要获取 当前时间 对应 的 年月日时分秒，可以使用datatime库

```py
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2018, 6, 30, 23, 3, 54, 238947)
>>> datetime.now().year
2018
>>> datetime.now().month
6
>>> datetime.now().day
30
>>> datetime.now().hour
23
>>> datetime.now().minute
7
>>> datetime.now().second
58
>>> datetime.now().microsecond
151169

>>> datetime.now().weekday()
5
```




## 获得指定日期对应星期几

```py
# 要计算出 2018年6月24日 是星期几 
thatDay = "2018-6-24"
from datetime import datetime
# 先把字符串表示的日期转化为 date 对象
theDay = datetime.strptime(thatDay, "%Y-%m-%d").date()
#再获取星期几
theDay.weekday()   # 0 代表星期1
```


## 获得指定日期所在周的周一的日期

```py
thatDay = "2018-6-30"
from datetime import datetime,timedelta
theDay = datetime.strptime(thatDay, "%Y-%m-%d").date()
weekMonday = theDay - timedelta(days=theDay.weekday())
```



{% include sharepost.html %}