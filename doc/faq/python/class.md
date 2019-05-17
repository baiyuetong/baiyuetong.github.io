---
title: 类和对象
toc: true
---

## print自定义对象

我们有时候需要打印出自定义类型的实例对象的信息, 比如下面这样的类型：

```py
class Car:
    def __init__(self,weight,color):
        self.weight = weight
        self.color  = color


car = Car(1500,'红色')
```

我们可能想输出对象的信息，包括car 的 重量 weight 和 颜色 color。

但是，如果我们直接这样打印 car

```py
print(car)
```

输出的结果就像下面这样：

```
<__main__.Car object at 0x021801D0>
```

并不会包含car 的重量和颜色信息。

Python中打印对象，输出的字符串内容，是由该对象所属类 的 **__str__** 方法决定的。

 **__str__** 方法返回什么，打印的结果就是什么。

所以，我们可以这样定义


```py
class Car:
    def __init__(self,weight,color):
        self.weight = weight
        self.color  = color

    def __str__(self):
        return f'本车是{self.color}的，重量为{self.weight}公斤'

car = Car(1500,'红色')
print(car)
```


再运行一下，发现输出结果为

```
本车是红色的，重量为1500公斤
```

----

Python中有个内置函数 repr，该函数会返回参数对象的 代码表示形式。

但是如果，repr 的参数是上面的自定义对象，比如

```py
print(repr(car))
```

输出的结果还是像下面这样：

```
<__main__.Car object at 0x021801D0>
```

我们可以通过定义一个 ```__repr__``` 方法来 决定 repr 函数的 输出结果

```py
class Car:
    def __init__(self,weight,color):
        self.weight = weight
        self.color  = color

    def __str__(self):
        return f'本车是{self.color}的，重量为{self.weight}公斤'

    def __repr__(self):
        return f'<Car> 本车是{self.color}的，重量为{self.weight}公斤'

car = Car(1500,'红色')
print(repr(car))
```

再运行一下，发现输出结果为
```
<Car> 本车是红色的，重量为1500公斤
```


<br>

## 定义Property 属性

下面定义了一个车这样的类

```py
class Car:
    def __init__(self,weight):
        self.weight = weight
```

该类有一个属性 weight 表示车的重量。


但是，如果 开发者这样实例化
```py
car = Car('abc')
```

又或者 实例化后， 开发者这样进行赋值

```py
car = Car('abc')
```

为 weight 属性 赋予了一个字符串值，显然就会有问题。

那么，我们有没有方法 在这种赋值产生的时候， 就报错呢？

我们可以这样

```py
class Car:
    def __init__(self,weight=1000):
        self.weight = weight

    # Getter function
    @property
    def weight(self):
        return self._weight

    # Setter function
    @weight.setter
    def weight(self, value):
        if not isinstance(value, int):
            raise TypeError('weight must be a integer')
        self._weight = value
```

一旦像这样定义
```py
    @property
    def weight(self):
        return self._weight
```

就是 将 weight 属性设置为 Property 属性。

这个 weight 方法被称之为 getter 方法。

以后，执行到 **获取** 该类实例的 weight 属性的 代码，比如

```py
print(car.weight)
```

其实，就会调用 上面的 这个weight 方法，使用其返回值作为 weight 属性的值。

----

如果，执行到为 weight 属性 **赋值**的 代码，比如

```py
car.weight = 'abc'
```

其实，就会调用 下面的 这个weight 方法

```py
    # Setter function
    @weight.setter
    def weight(self, value):
        if not isinstance(value, int):
            raise TypeError('weight must be a integer')
        self._weight = value
```

这个 weight 方法被称之为 setter 方法。

这个方法 传入的参数 value 就是要赋予的值， 这个方法里面会对 该值 做一个检查，如果不是int 类型就抛出异常。
这样做到第一时间对错误的赋值进行报错。 防止bug 被埋藏进代码。

<br>

大家可以试着运行一下这样的代码

```py
class Car:
    def __init__(self,weight=1000):
        self.weight = weight

    # Getter function
    @property
    def weight(self):
        return self._weight

    # Setter function
    @weight.setter
    def weight(self, value):
        if not isinstance(value, int):
            raise TypeError('weight must be a integer')
        self._weight = value

car = Car('hello')
```

运行结果如下

```py
Traceback (most recent call last):
  File "e:/tmp/task/t2.py", line 17, in <module>
    car = Car('hello')
  File "e:/tmp/task/t2.py", line 3, in __init__
    self.weight = weight
  File "e:/tmp/task/t2.py", line 14, in weight
    raise TypeError('weight must be a integer')
TypeError: weight must be a integer
```

可以发现，即使是在初始化函数中的赋值，也会调用setter函数， 进行赋值有效性检验。

----

<br>

另外一种定义 getter 和 setter 的方法如下

```py
class Car:
    def __init__(self,weight=1000):
        self.set_weight(weight)

    # Getter function
    def get_weight(self):
        return self._weight

    # Setter function
    def set_weight(self, value):
        if not isinstance(value, int):
            raise TypeError('weight must be a integer')
        self._weight = value

    weight = property(get_weight,set_weight)

car = Car()
car.weight = 'abc'
```

## 子类中调用父类的方法

有的时候，我们需要在子类中调用父类的 **已经被子类覆盖的方法**。

这时候，我们就可以使用   ```super``` 函数。 

典型的应用场景就是初始化方法里面。

比如

```py
class Car:
    def __init__(self,price):
        # 价格
        self.price = price

class ElectricCar(Car):
    def __init__(self,price,chargetime):
        
        #  充电时间
        self.chargetime = chargetime
        super().__init__(price)
```


<br>

## 通过类的实例对象得到类和类名

```py
instance.__class__  # 得到的就是类
instance.__class__.__name__ # 得到的就是类的名称

```


<br>

## 如果调用了类里面没有定义的方法

我们开发一个类给别人使用，如果我们希望别人调用了这个类中不存在的方法时，我们的代码能做一些处理，比如返回一个就可以通过 ```__getattr__``` 方法。

python解释器发现调用了一个类不存在的方法，就会调用```__getattr__```。

并且```__getattr__```的返回值是另外一个函数，会被解释器作为 替代方法去执行。

看下面的示例

```py
class Foo:
    def __getattr__(self, attr):
        print ('你调用了 %s' % attr)
        return self.other
		
    def other(self,p1,p2):
        print(f'另外的函数,参数为{p1},{p2}')
		
f = Foo()

f.bar(1,2)	
```

执行结果为

```
你调用了 bar
另外的函数,参数为1,2
```


{% include sharepost.html %}