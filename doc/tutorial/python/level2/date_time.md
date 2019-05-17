---
title: 日期和时间
toc: true
---

Python中，对日期和时间的操作，主要使用这3个内置模块： datetime 、 time 和 calendar

## 获取当前时间对应的数字

开发程序时，经常需要获取两个代码位置在执行时的时间差，比如，我们想知道某个函数执行大概耗费了多少时间，就可以使用time.time()来做。

```py
import time
before = time.time()
func1()
after = time.time()
print(f’调用func1，花费时间{before-after}’)
```

time.time() 会返回 从 1970年1月1日0点（所谓的epoch时间点） 到 当前时间的 经过的秒数 ，可以简称为秒数时间。
关于该函数的详细解释，请参考官方文档
https://docs.python.org/3/library/time.html#time.time



### 视频讲解


<video src="http://v.python666.vip/video/py/mpdate_time-1.mp4"  style="width: 90%;" controls controlsList="nodownload" oncontextmenu="return false;" preload="metadata" poster="{{ site.video_cover }}"></video>


## 指定格式字符串显示时间

以指定格式字符串显示时间，是非常常用的，比如日志里面的时间戳。

要得到 ```当前时间``` 对应的字符串，可以这样实现：

```py
from datetime import datetime
str(datetime.now())
```

得到类似这样的字符串：'2018-06-30 23:10:08.911420'

如果要指定输出的时间格式，可以像下面这样

```py
datetime.now().strftime('%Y-%m-%d ** %H:%M:%S')
```

得到类似这样的字符串： '2019-02-24 ** 16:56:55'

<br>

当然，也可以使用time库来格式化显示字符串

```py
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) 
```

### 数字表示的时间转化为字符串表示

如果要将某个指定秒数时间（从epoch时间点开始计算），而不是当前时间，转化为字符串格式，可以这样写

```py
time.strftime('%Y%m%d %H:%M:%S',time.localtime(1434502529)) 
```
<br>


### 视频讲解


<video src="http://v.python666.vip/video/py/mpdate_time-2.mp4"  style="width: 90%;" controls controlsList="nodownload" oncontextmenu="return false;" preload="metadata" poster="{{ site.video_cover }}"></video>

## 字符串时间转化为整数时间

反过来，如果要将字符串指定的时间，转化为秒数时间，可以这样

```py
int(time.mktime(time.strptime('2015-08-01 23:59:59', '%Y-%m-%d %H:%M:%S')))
```



## 获取某个时间 对应 的年月日时分秒数字

要获取  ```当前时间```  的 年、月、日、时、分、秒、星期几 对应的数字，可以使用datatime库

```py
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2018, 6, 30, 23, 3, 54, 238947)

# 年
>>> datetime.now().year
2018

# 月
>>> datetime.now().month
6

# 日
>>> datetime.now().day
30

# 时
>>> datetime.now().hour
23

# 分
>>> datetime.now().minute
7

# 秒
>>> datetime.now().second
58

# 毫秒
>>> datetime.now().microsecond
151169

# 获取星期几用 weekday方法
# 0 代表星期一，1 代表星期二 依次类推
>>> datetime.now().weekday() 
5
```



## 获得指定时间字符串对应星期几

如果要获取的是 某个指定时间，比如 "2018-6-24"，而不是当前时间，对应的星期几，怎么办？

可以使用 datetime类的 strptime方法，先产生对应的 datetime对象


```py
# 要计算出 2018年6月24日 是星期几 
thatDay = "2018-6-24"
from datetime import datetime
# 先把字符串表示的日期转化为 datetime 对象
theDay = datetime.strptime(thatDay, "%Y-%m-%d")
#再获取星期几
theDay.weekday()  
```



## 从某个时间点往前或者后推 一段时间

如果我们想知道，2018年6月24日 往后推120天，是什么日期？星期几？

往前推120天，又是什么日期？星期几？

可以这样计算

```py
thatDay = "2018-6-24"
from datetime import datetime,timedelta
theDay = datetime.strptime(thatDay, "%Y-%m-%d").date()

# 后推120天 就是 + timedelta(days=120)
target = theDay + timedelta(days=120)

print(target)
print(target.weekday())

# 前推120天 就是 - timedelta(days=120)
target = theDay - timedelta(days=120)

print(target)
print(target.weekday())
```

## 获得指定日期那周的周一

```py
thatDay = "2018-6-30"
from datetime import datetime,timedelta
theDay = datetime.strptime(thatDay, "%Y-%m-%d").date()

# 这就是 2018-6-30 那一周的周一
weekMonday = theDay - timedelta(days=theDay.weekday())
```

## 获取某个月总共有多少天

最方便的方法是使用 calendar 模块里面的 函数 

```py
from calendar import monthrange
# monthrange返回的是元组
# 第一个元素是指定月第一天是星期几
# 第二个元素是指定月有多少天
mr = monthrange(2011, 2)

# 得到2011年2月有多少天
print(mr[1])
```

关于 calendar 的详细用法，[参考官网](https://docs.python.org/3/library/calendar.html){:target="_blank"}


{% include sharepost.html %}