---
title: 基本数据类型操作
toc: true
---


## 合并2个列表
列表中要添加另外一个列表的内容很简单，用加号就可以了
```py
>>> a = [1,2,3]
>>> a += [4,5,6]
>>> a
[1, 2, 3, 4, 5, 6]
```


## 合并2个字典
字典x 中要添加 另外一个字典y的内容，可以使用字典的update方法
```py
>>> x = {'a':1, 'b': 2}
>>> y = {'b':10, 'c': 11}
>>> x.update(y)
>>> x
{'a': 1, 'b': 10, 'c': 11}
```

从上例中可以发现，如果有重复的key， 会被字典y中的内容取代

如果我们想将合并后的内容放到一个新的字典对象里面， 而不去修改x，y的内容，该怎么办呢？
可以使用下面的方法：

```py
z = dict(x.items() + y.items())
```

## 列表中去掉 重复的元素

### 循环遍历法

这是最原始，也是最基本的一种方法，定义一个新列表，依次循环旧列表，如果没在新列表中，就插入，如果在，则不插入，这种方法思路简单，容易实现，而且不会改变原列表元素顺序，测试代码如下：

```py
list1 = [1 ,2,3, 5,0,1 ,2,3, 5,0]
list2 = []

print(f'list1: {list1}')
for item in list1:
    if item not in list2:
        list2.append(item)
print(f'list2: {list2}')
```

输出结果：
```
list1: [1, 2, 3, 5, 0, 1, 2, 3, 5, 0]
list2: [1, 2, 3, 5, 0]
```


### set方法

set集合的元素是唯一的、不重复的，所以可以直接使用set转换list列表去重。

要注意的是，这种方法，原列表的元素顺序可能会发生改变，如下，

```py
list1 = [1 ,2,3, 5,0,1 ,2,3, 5,0]
list2 = list(set(list1))
print(f'Before: {list1}')
print(f'after: {list2}')
```

输出结果
```
Before: [1, 2, 3, 5, 0, 1, 2, 3, 5, 0]
after: [0, 1, 2, 3, 5]
```


### 使用itertools的groupby方法

对旧列表的元素进行分组，最后循环获取分组的信息，就能直接获取到去重后的新列表

```py
import itertools

list1 = [1 ,2,3, 5,0,1 ,2,3, 5,0]
list2 = []

print(f'list1: {list1}')
list1.sort()
tmp = itertools.groupby(list1)
for k,v in tmp:
    list2.append(k)
print(f'list2: {list2}')
```

输出结果

```
list1: [1, 2, 3, 5, 0, 1, 2, 3, 5, 0]
list2: [0, 1, 2, 3, 5]
```

### 使用Series的unique方法

Series是pandas的一种数据结构，我们可以将旧列表转换为series对象，直接调用unique方法实现列表的去重

```py
from pandas import Series

list1 = [1 ,2,3, 5,0,1 ,2,3, 5,0]
temSeries = Series(list1)
list2 = list(temSeries.unique())
print(f'list1: {list1}')
print(f'list2: {list2}')
```
输出结果

```
list1: [1, 2, 3, 5, 0, 1, 2, 3, 5, 0]
list2: [0, 1, 2, 3, 5]
```


## 从列表中过滤元素

有时候，你想从一个列表中，根据某些条件过滤掉一些元素，生成一个新的列表。

比如：下面的列表

```py
numbers = [-5, 66, -4, -10, 97, 21, 13, -51]
```

你想从将该列表中所有的正数提取出来放到一个新的列表中，该怎么做？


简单的方法就是使用列表推导式（list comprehension）

```py
numbers = [-5, 66, -4, -10, 97, 21, 13, -51]
positives = [num for num in numbers if num > 0]
```

<br>

如果过滤的处理比较复杂，可以自己定义一个 函数用来判断 参数 是否符合过滤条件。

比如：如下一个列表变量 names，其中保存了一个班级学生的姓名。

现在需要得到其中可以评为三好学生的学生列表。

程序需要将每个学生姓名打印在屏幕上，给老师来判断，如果老师输入yes表示是三好学生，输入否则就不是。

可以这样做

```py
# 定义一个 过滤函数
def isExcellent(name):
    excellent = input(f'{name} 是三好学生吗？')
    if excellent == 'yes':
        return True
    else:
        return False

names = ["关羽", "张飞", "赵云", "马超", "黄忠"]

# filter函数 会将 names 里面的每个元素 传递给 过滤函数 isExcellent
# 过滤函数 返回 True 就会保存下来， 返回False 就过滤掉
excellentStudents = filter(isExcellent, names)



'''
filter 返回的是一个 iterator，而且是lazy（懒）的。
执行上面那行代码时，并不会立即 调用isExcellent处理 names里面的每个元素。

而是在后面使用到 excellentStudents 这个 iterator的时候，比如像下面这样
产生一个列表 : 

excellentStudentList = list(excellentStudents)


或者 直接用for循环来处理其中的元素:

for one in excellentStudents:
   print(one)

'''


# 要注意的是， excellentStudents 这个 iterator只能使用一次
# 如果你已经像这样使用过了

excellentStudentList = list(excellentStudents)
print(excellentStudentList)

# 下面这样再次使用，excellentStudents 里面就取不出元素来了。
for one in excellentStudents:
   print(one)

```




## 从字典中过滤元素

有时候，你想从一个字典中，根据某些条件过滤掉一些元素，生成一个新的字典。

比如：下面的字典，记录了三国武将的武力值

```py
guys = {
    '关羽' : 96, 
    '张飞' : 96, 
    '赵云' : 97, 
    '马超' : 96, 
    '黄忠' : 94, 
    '魏延' : 90, 
    '马岱' : 82, 
}
```

你想把 武力值 在 95 以上的 武将 放到一个新的字典中，该怎么做？


简单的方法就是使用字典生成式（dict comprehension）

```py
toughGuys = {guy:level for guy,level in guys.items() if level > 95}
print(toughGuys)
```

<br>

如果过滤的处理比较复杂，可以自己定义一个 函数用来判断 参数 是否符合过滤条件。
然后用 filter对其中元素进行过滤，做法和上面的 列表的过滤处理类似，这里不再赘述。




## 产生随机数 

如果想产生某个范围内的随机数字，可以使用random库里面的randint方法。

比如，要在0,9之间产生一个随机数：

```py
from random import randint 
print randint(0,9)
```



## 产生随机字符串

如果要产生一个随机的字符串，里面可以有大写字母和数字，

```py
''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
```

其中 range(4) 指定了字符串的长度为4


python3.6以后，可以更简短一些，这样写

```py
import string,random
''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
```

其中参数k指定了字符串的长度


如果随机字符串里面，可以有小写字母和数字，python3.6以后，可以这样写

```py
import string,random
''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
```


详细内容，参考 
https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python


## ‘/’和‘//’的区别

" / " 表示浮点数除法，返回浮点结果

" // " 表示整数除法,返回不大于结果的一个最大的整数

```py
print(10/4) #结果2.5
print(10//4) #结果为2
```

## 单引号，双引号，三引号的区别

简单的来说都是定义一段字符串

单引号和双引号是等效的，但是，如果在字符串中需要换行的话，需要用转移字符(\n)强制换行,如果包含相同的引号，可以使用反斜杠

三引号则可以直接换行，并且可以包含注释

例如定义一个字符串：Welcome to www.python3.vip, let's start to enjoy "python" world

单引号

```py
s1 = 'Welcome to www.python3.vip, let\'s start to enjoy "python" world'
s2 = 'Welcome to www.python3.vip, \nlet\'s start to enjoy "python" world'
print(s1)
print(s2)
```

```
>>> s1 = 'Welcome to www.python3.vip, let\'s start to enjoy "python" world'
>>> s1
'Welcome to www.python3.vip, let\'s start to enjoy "python" world'
>>> print(s1)
Welcome to www.python3.vip, let's start to enjoy "python" world
>>> s2 = 'Welcome to www.python3.vip, \nlet\'s start to enjoy "python" world'
>>> print(s2)
Welcome to www.python3.vip,
let's start to enjoy "python" world

```

双引号：

```py
s3 = “Welcome to www.python3.vip, let's start to enjoy \"python\" world”
s4 = “Welcome to www.python3.vip, \n let's start to enjoy \"python\" world”
print(s3)
print(s4)
```

```
>>> s3 = "Welcome to www.python3.vip, let's start to enjoy \"python\" world"
>>> print(s3)
Welcome to www.python3.vip, let's start to enjoy "python" world
>>> s4 = "Welcome to www.python3.vip, \n let's start to enjoy \"python\" world"
>>> print(s4)
Welcome to www.python3.vip,
 let's start to enjoy "python" world
```

三引号

```py
s5 = '''
Welcome to www.python3.vip, 
let's start to enjoy "python" world
'''
print(s5)
```

```
>>> s5 = '''
... Welcome to www.python3.vip,
... let's start to enjoy "python" world
... '''
>>> print(s5)

Welcome to www.python3.vip,
let's start to enjoy "python" world

>>>
```

## 删除列表元素

从列表中删除元素的方法可以分为两大类，共有三种方法：

1. 根据索引删除元素
  + del：该语句删除元素后，就无法再访问该元素
  + pop：该语句删除元素后，可以继续使用该元素
2. remove：根据元素的值删除元素,但需要注意亮点
  + 只删除第一个指定的元素值，如果有多个，则需要使用循环来判断删除其余的元素
  + 该方法删除元素时，也可以继续使用它的值

例如，定义个列表如下：

 ```py
 >>>students = ['Alex','Tom','Jerry','Michale']
 >>>print(students)
 ['Alex', 'Tom', 'Jerry', 'Michale']

 ```

 ```py
 # 如果知道元素索引，则可以调用del元素
 # 删除后就无法再访问该元素了
 >>> del students[0]
 >>> print(students)
['Tom', 'Jerry', 'Michale']
 ```

```py
# 从列表删除元素，并想继续使用他的值，则可以使用pop方法
>>> students = ['Alex','Tom','Jerry','Michale']
>>> last_student = students.pop()
>>> print(last_student)
Michale

# 也可以弹出列表中任何位置的元素
# 方法pop(index)
>>> first_student = students.pop(0)
>>> print(first_student)
Alex
>>> print(students)
['Tom', 'Jerry']

```

```py
# 根据值来删除元素
# 方法：remove(value)
>>> students = ['Alex','Tom','Jerry','Michale','Alex']
>>> students.remove('Tom')
>>> print(students)
['Alex', 'Jerry', 'Michale', 'Alex']

# 有多个相同值的元素时，只能删除第一个
# 需要用到循环删除其余的元素
>>> students = ['Alex','Tom','Jerry','Michale','Alex']
>>> print(students)
['Alex', 'Tom', 'Jerry', 'Michale', 'Alex']
>>> for student in students:
...     if student == 'Alex':
...         students.remove('Alex')
...
>>>
>>> print(students)
['Tom', 'Jerry', 'Michale']
>>>

```

## 列表排序sort和sorted

1. sort：该方法对列表进行永久性排序
2. sorted：对列表进行临时性排序

```py
# sort
# list.sort()
students1 = ['Alex','Tom','Jerry','Michale','Alex']
print(f'before sort: {students1}')
students1.sort()
print(f'after sort: {students1}')

# sorted
# sorted(list)
students2 = ['Alex','Tom','Jerry','Michale','Alex']
print(f'before sorted: {students2}')
sorted(students2)
print(f'after sorted: {students2}')
```

output
```py
before sort: ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex']
after sort: ['Alex', 'Alex', 'Jerry', 'Michale', 'Tom']
before sorted: ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex']
after sorted: ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex']
```

## 复制列表

见示例：

```py

# copy list
students = ['Alex','Tom','Jerry','Michale','Alex']
print(f' before: {students}')

# 方法1：错误的方法
newStudents1 = students
print(f' before: {newStudents1}')

newStudents1.append('Jack')
print(f' after :  {newStudents1}')

students.append('Steven')
print(f' after: {students}')

print('******'*8)
students = ['Alex','Tom','Jerry','Michale','Alex']
print(f' before:  {students}')
# 方法2
newStudents2 = students[:]
print(f' before: {newStudents2}')

newStudents2.append('Jack')
print(f' after:  {newStudents2}')

students.append('Steven')
print(f' after:  {students}')
```

output

```py
 before: ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex']
 before: ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex']
 after :  ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex', 'Jack']
 after: ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex', 'Jack', 'Steven']
 ************************************************
 before:  ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex']
 before: ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex']
 after:  ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex', 'Jack']
 after:  ['Alex', 'Tom', 'Jerry', 'Michale', 'Alex', 'Steven']
```

说明：复制列表不能将列表名直接复制给一个新的变量，因为他不会将该列表的副本存储到新的变量中

1. 方法1: **错误的方法**,该方法只是将新的变量newStudents1关联到列表students，即两个变量皆指向同一个列表，所有的操作皆是对同一个列表进行操作
2. 方法2：将列表students复制到新的newStudents2中，后面的操作分别对各自的列表进行操作

## 列表去重

可以调用内置函数set()来快速去重，示例如下：

```py
list1 = [1 ,2,3, 5,0,1 ,2,3, 5,0]
list2 = list(set(list1))
print(f'Before: {list1}')
print(f'after: {list2}')
```

```
Before: [1, 2, 3, 5, 0, 1, 2, 3, 5, 0]
after: [0, 1, 2, 3, 5]
```

## isVS==

is：是比较两个对象的**地址**，及id()的返回值

==：是判读两个对象的**内容**是否相等，

示例1如下：

```py
list1 = ['a','b','c']
list2 = list1

print(f' list1 address: {id(list1)}')
print(f' list2 address: {id(list2)}')
print(list1 is list1)
print(list1 == list2)
```

输出结果

```
 list1 address: 58187368
 list2 address: 58187368
True
True
```
因为赋值其实就是引用，所以值和地址皆相同，返回为True

示例2如下：

```py

list1 = ['a','b','c']
list3 = list1[:]

print(f' list1 address: {id(list1)}')
print(f' list3 address: {id(list3)}')
print(list1 is list3)
print(list1 == list3)
```

输出结果：
```
 list1 address: 58187368
 list3 address: 58295320
False
True
```

通过切片赋值，虽然内容相同，但因其地址不一样，所以返回的结果也不一样。


## for循环得到索引

```py
alist = ['a','b','c','d']
for idx, val in enumerate(alist):
    print(idx, val)
```

{% include sharepost.html %}