---
title: Python练习：装饰器
---

## 题目1

某公司要开发一个 系统， 这个系统运行的时候， 用户输入指令，比如，查询价格，就由相应的查询价格的业务代码去处理。

假设你是系统架构师， 你确定了如下的代码文件结构

- Python库模块文件名为 lib.py

  里面包含一个装饰器函数 cmd_dispatch, 这个装饰器函数是给 开发业务工程师使用的。

- 业务代码放在svc.py文件中

  在这个代码文件中，开发业务代码的工程师，可以像下面这样使用你的装饰器 cmd_dispatch

```py
# ** svc.py **
from lib import cmd_dispatch

@cmd_dispatch('查询价格')
def queryPrice():
    # 具体的查询价格处理代码
    print('执行查询价格的业务')


@cmd_dispatch('退货')
def refund():
    # 具体的退货处理代码
    print('执行退货的业务')
```

装饰器参数是 用户指令字符串， 

比如，上面的写法就表示，如果用户输入指令  ```查询价格``` ， 系统就会调用  queryPrice, 用户输入  ```退货``` ， 系统就会调用  refund。

- 启动代码文件是run.py。
  
  我们运行这个run.py 就启动了整个系统。

  代码如下

```py
# ** run.py **

# cmd_route_table 是 lib模块里面的
# 存储了命令对应的业务处理函数
from  lib import  cmd_route_table
import svc

while True:
    op = input('请输入你的操作：')

    # 如果能找到改指令的处理函数
    if op in cmd_route_table:
        # 查找改指令对应的业务处理函数
        svcFunc = cmd_route_table[op]
        # 调用业务处理函数
        svcFunc()

    else:
        print('该指令没有对应业务处理')
```


请你写出 lib.py这个库， 完成上述的功能，包括装饰器函数 和 cmd_route_table。




{% include sharepost.html %}


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

## 题目1-答案


```python
## lib.py
cmd_route_table = {}

def cmd_dispatch(cmd):
    def inner(func):
        cmd_route_table[cmd] = func
        return func            

    return inner
```
