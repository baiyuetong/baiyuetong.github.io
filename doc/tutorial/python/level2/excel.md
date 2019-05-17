---
title: 读写Excel
---

Excel是我们经常操作的数据文件。

我们往往可以通过Python程序,自动化Excel的数据处理，帮我节省大量的时间。



## 读取Excel中的数据

如果我们只是要**读取**Excel文件里面的数据进行处理，可以使用 xlrd 这个库。

首先我们安装xlrd库，执行下面的命令

```
pip install xlrd
```



---------------

xlrd 库里面的 open_workbook 打开Excel文件，并且返回一个Book对象，这个对象代表打开的 Excel 文件。

可以通过这个Book对象得到Excel文件的很多信息，比如 获取 Excel 文件中表单(sheet) 的数量 和 所有 表单(sheet) 的名字。


请大家
<a target='_blank' href='../code/income.xlsx'> 点击这里，下载 Excel文件  income.xlsx</a>

这个文件里面有 3 个表单，分别记录了2018、2017、2016年 的月收入，如下所示

![白月黑羽Python3教程](https://user-images.githubusercontent.com/36257654/41497394-06e179e8-7187-11e8-9413-fc6445ac4b51.png)

<br>

我们就可以用如下代码，读取 该文件中表单的数量和名称：

```py
import xlrd

book = xlrd.open_workbook("income.xlsx")

print(f"包含表单数量 {book.nsheets}")
print(f"表单的名分别为: {book.sheet_names()}")
```

---

要读取某个表单里单元格中的数据，必须要先获取表单对象。

可以根据表单的索引 或者 表单名获取 表单对象，使用如下对应的方法

```py
# 表单索引从0开始，获取第一个表单对象
book.sheet_by_index(0)

# 获取名为2018的表单对象
book.sheet_by_name('2018')
```


<br>

获取了表单对象后，可以根据其属性得到：

```
表单行数（nrows）
列数（ncols）
表单名（name）
表单索引（number）
```


如下

```py
import xlrd

book = xlrd.open_workbook("income.xlsx")

sheet = book.sheet_by_index(0)
print(f"表单名：{sheet.name} ")
print(f"表单索引：{sheet.number}")
print(f"表单行数：{sheet.nrows}")
print(f"表单列数：{sheet.ncols}")
```

<br>

获取了表单对象后，可以使用 ```cell_value``` 方法，参数为行号和列号，读取指定单元格中的文本内容。如下所示：

```py
import xlrd

book = xlrd.open_workbook("income.xlsx")

sheet = book.sheet_by_index(0)

# 行号、列号都是从0开始计算
print(f"单元格A1内容是: {sheet.cell_value(rowx=0, colx=0)}")
```

运行结果输出  

```
单元格A1内容是: 月份
```




<br>

还可以使用 ```row_values``` 方法，参数为行号，读取指定行所有单元格的内容，存放在一个列表中返回。

如下所示：

```py
import xlrd

book = xlrd.open_workbook("income.xlsx")

sheet = book.sheet_by_index(0)

# 行号、列号都是从0开始计算
print(f"第一行内容是: {sheet.row_values(rowx=0)}")
```

运行结果输出  

```
第一行内容是: ['月份', '收入']
```




<br>

还可以使用 ```col_values``` 方法，参数为列号，读取指定列所有单元格的内容，存放在一个列表中返回。

如下所示：

```py
import xlrd

book = xlrd.open_workbook("income.xlsx")

sheet = book.sheet_by_index(0)

# 行号、列号都是从0开始计算
print(f"第一列内容是: {sheet.col_values(colx=0)}")
```

运行结果输出  

```
第一列内容是: ['月份', 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
```

可以看出，数字以小数的形式返回了。


----

<br>

有了这些方法，我们就可以完成一些数据处理任务了。比如我们要计算 2017年 全年的收入就可以这样

```py
import xlrd

book = xlrd.open_workbook("income.xlsx")

sheet = book.sheet_by_name('2017')

# 收入在第2列
values = sheet.col_values(colx=1)

# 去掉第一行 标题行内容
incomes = values[1:]

print(f"2017年收入为: {sum(incomes)}")
```

<br>

## 创建Excel并写入数据

如果你要创建一个新的Excel并写入数据，可以使用 xlwt库

使用pip安装该库

```
pip install  xlwt
```

<br>

下面的示例代码 将 保存在字典中的年龄表的内容 写入到excel文件中

```py
import xlwt

name2Age = {
    '张飞' :  38,
    '赵云' :  27,
    '许褚' :  36,
    '典韦' :  38,
    '关羽' :  39,
    '黄忠' :  49,
    '徐晃' :  43,
    '马超' :  23,
}

# 创建一个Excel workbook 对象
book = xlwt.Workbook()

# 增加一个名为 '年龄表' 的sheet
sh = book.add_sheet('年龄表')

# 写标题栏
sh.write(0,0, '姓名')
sh.write(0,1, '年龄')

# 写入内容
row = 1

for name,age in name2Age.items():
    sh.write(row,0,name)
    sh.write(row,1,age)
    row += 1

# 保存文件
book.save('年龄表.xls')
```



<br>

## 修改Excel中的数据

如果你想修改已经存在的Excel 文件，可以使用  openpyxl 库。

比如

```py
import openpyxl
wb = openpyxl.load_workbook('income-1.xlsx')

sheet = wb['2017']
sheet['A1'] = '修改一下'
wb.save('income-1.xlsx')
```

但是，openpyxl 库 有个问题： 如果原来的文件中有图片，使用openpyxl 库 修改并保存后，这些图片都会丢失！！

要解决这个问题，在Windows平台上，可以通过 Excel 应用的 COM 接口 来对Excel进行操作。 

这个方法相当于使用Python程序 通过 Excel应用 自己去修改，当然没有任何的副作用。

使用该方法，首先需要安装pywin32库，在命令行窗口输入如下命令：

```py
pip install pywin32
```

比如可以这样修改

```py
import win32com.client
excel = win32com.client.Dispatch("Excel.Application")

# excel.Visible = True     # 可以让excel 可见

# 这里填写要修改的Excel文件的绝对路径
workbook = excel.Workbooks.Open(r"d:\tmp\income1.xlsx")

# 得到 2017 表单
sheet = workbook.Sheets('2017')

# 修改表单第一行第一列单元格内容
# com接口，单元格行号、列号从1开始
sheet.Cells(1,1).Value="你好"

# 保存内容
workbook.Save()

# 关闭该Excel文件
workbook.Close()

# excel进程退出
excel.Quit()

# 释放相关资源
sheet = None
book = None
excel.Quit()
excel = None
```

运行一下可以发现Excel内容修改了，而且其中的图片内容不会丢失。

关于其他使用com接口操作Excel 可以参考下面这篇国外的教程

http://pythonexcels.com/python-excel-mini-cookbook/



{% include sharepost.html %}



<br><br>

[上一页](/doc/tutorial/python/level2/2006/){: .btn .btn--primary .align-left }
[下一页](/doc/tutorial/python/level2/toexe/){: .btn .btn--primary .align-right }