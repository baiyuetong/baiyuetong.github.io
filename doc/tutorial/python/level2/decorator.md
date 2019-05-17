---
title: 装饰器
---

## 装饰器的定义

<!-- 前面我们在学习自定义对象的时候，类里面的静态方法是这样写的
```py
class AccordCar:    
    
    @staticmethod
    def pressHorn(): 
        print('嘟嘟~~~~~~')
```

这个pressHorn 方法的上面有个 ```@staticmethod``` 的修饰。

这种 函数定义前面 @开头 后面的这个staticmethod，本身就是一个函数， 用来修改下面pressHorn 这个方法。

被修改后的方法pressHorn -->


 ```装饰器``` ，英文称之为**decorator**。

我们开发Python代码，会经常碰到装饰器。

Python中装饰器通常用来装饰函数、或者类的方法。

通常被装饰后的函数， 会在原有的函数基础上，增加一点功能。

比如 前面我们在学习到类里面的静态方法，就是使用了staticmethod 这个装饰器，被装饰的方法 就增加了一层含义，表示这个方法是个静态方法。



通常装饰器本身是也一个函数。 那么装饰器是怎么装饰另外的函数的呢？


假设你进入一个公司，领导要求你在老代码的基础上继续开发。

假设代码里面有好多函数，都是返回时间的，比如像下面这样。

```py
import time
def getXXXTime():
    print()
    return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())
```

如果我们需要在所有这样的函数 返回字符串前面 都加上开头: 当地时间



这时候，我们完全可以 ```不去修改原来的函数``` ， 而是 ```使用装饰器``` ，像这样


{% highlight py linenos %}
import time

# 定义一个装饰器函数
def sayLocal(func):
    def wrapper():
        curTime = func()
        return f'当地时间： {curTime}'
    return wrapper

def getXXXTime():
    return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())

# 装饰 getXXXTime
getXXXTime = sayLocal(getXXXTime)

print (getXXXTime())   
{% endhighlight %}

执行代码到第 14 行代码之前 ，  getXXXTime 这个名字 对应一个函数对象 内容如下

```py
return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())
```

但是当解释器执行完第 14 行代码， 它重新定义了 getXXXTime 这个变量 为  后面 ```sayLocal(getXXXTime)``` 调用的返回值。

```sayLocal(getXXXTime)``` 调用的返回值是什么呢？

我们看到 ```sayLocal(getXXXTime)``` 函数的定义是这样的：

```py
def sayLocal(func):
    def wrapper():
        curTime = func()
        return f'当地时间： {curTime}'
    return wrapper
```

所以， 它的参数 func 传入的是一个函数对象 ，就是原来的 getXXXTime 函数。

然后这个函数 内部 又定义了一个函数 wrapper， 这个内部的函数 实现了在原来的getXXXTime 函数 调用的结果前面加上 ```当地时间：``` 这样的前缀。

这个sayLocal 函数调用的返回值 就是 这个内部函数 wrapper。

那么getXXXTime 经过装饰后，**其实 已经变成了 内部函数 wrapper**

所以后面我执行调用 getXXXTime 函数，其实就是调用 wrapper。


所以我们说 sayLocal 函数 就是一个装饰器，它装饰了参数函数的行为。


而  第 14行代码，就是 把一个函数名 对应的行为改变为 装饰后的 行为。

Python 中 对应第14行代码， 可以有更方便的写法，如下


{% highlight py linenos %}
import time

def sayLocal(func):
    def wrapper():
        curTime = func()
        return f'当地时间： {curTime}'
    return wrapper

@sayLocal
def getXXXTime():
    return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())

print (getXXXTime())   
{% endhighlight %}

第 9 行代码， 以 @sayLocal 开头后面接装饰器函数 的这种写法，是一种 ```语法糖``` ，也就是便捷写法。

当Python解释器执行 完 下面语句的时候，
```py
@sayLocal
def getXXXTime():
    ....
```

就等于执行了这样的一条语句

```py
getXXXTime = sayLocal(getXXXTime)
```

这样写起来比较方便快捷。


### 视频讲解

---
```白月黑羽教Python学习视频``` - 装饰器

<video src="http://v.python666.vip/video/py/mp1003_1.mp4"  style="width: 90%;" controls controlsList="nodownload" oncontextmenu="return false;" preload="metadata"></video>



<br>
可能有的读者会问，干嘛要这么麻烦？ 我们直接改这个函数的内容，不是更简单吗？像这样

```py
import time
def getXXXTime():
    curTime = time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())
    return f'当地时间： {curTime}'
```

装饰器经常被用在库和框架中， 给别的开发者使用。 这些库的开发者预料到 使用者 开发的函数可能需要 一些增强的功能。 因为他们没法去改使用者的代码，  就可以把这些增强的部分做在 装饰器函数中。

这样使用者，只需要在他们的函数前面上@xxx 就使用了这些增强的功能了。





## 被装饰的函数有参数

如果要装饰函数有 未知个数的参数， 怎么办呢？

像这样的2个函数，都要装饰

```py
import time
def getXXXTimeFormat1(name):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} '


def getXXXTimeFormat2(name,place):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} , 采集地：{place}'
```

这时，可以使用函数的可变参数，像这样

```py
import time

def sayLocal(func):
    def wrapper(*args,**kargs):
        curTime = func(*args,**kargs)
        return f'当地时间： {curTime}'
    return wrapper

@sayLocal
def getXXXTimeFormat1(name):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} '

@sayLocal
def getXXXTimeFormat2(name,place):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} , 采集地：{place}'

print (getXXXTimeFormat1('张三'))    
print (getXXXTimeFormat2('张三',place='北京'))    
```

其中  ```*args```  可以接受一切 **不指定参数名** 的传参方式 ， 比如 ```'张三'```

 ```**kargs```  可以接受一切 **指定参数名** 的传参方式 ， 比如 ```place='北京'```


 

{% include sharepost.html %}




<br><br>

[上一页](/doc/tutorial/python/level2/1002/){: .btn .btn--primary .align-left }
[下一页](/doc/tutorial/python/level2/2001/){: .btn .btn--primary .align-right }