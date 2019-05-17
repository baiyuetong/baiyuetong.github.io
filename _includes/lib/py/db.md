
<br>
## 安装客户端库


目前使用Python语言访问mysql数据库， 推荐使用客户端库 mysqlclient 和 PyMySQL。

mysqlclient 库是C语言开发的，性能比较高。我们这里就使用它。


这个库遵循 Python统一数据库访问接口规范（[参考PEP 249](https://www.python.org/dev/peps/pep-0249/)），支持Python3 并且  抽象层级比较高。

这是个开源的库，官方网址在github上 https://github.com/PyMySQL/mysqlclient-python


使用文档在这里  https://mysqlclient.readthedocs.io/

既然是Python的第三方库，当然是用 pip安装了。

直接 运行： ```pip install mysqlclient``` 

<!-- 
为什么要指定版本==1.3.12？
因为mysqlclient 需要依赖一个c语言开发的库， 1.3.12版本安装包已经将c语言库编译好了，成为可执行代码库，就不需要安装时候编译了。

而最新版本很可能安装时还需要编译C语言库，就可能会出现下面的错误

```py
 C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\BIN\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -Dversion_info=(1,3,13,'final',0) -D__version__=1.3.13 "-IC:\Program Files (x86)\MySQL\MySQL Connector C 6.1\include" -Id:\tools\python36\include -Id:\tools\python36\include "-IC:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\INCLUDE" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.10240.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.10240.0\shared" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.10240.0\um" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.10240.0\winrt" /Tc_mysql.c /Fobuild\temp.win32-3.6\Release\_mysql.obj /Zl
    _mysql.c
    _mysql.c(29): fatal error C1083: Cannot open include file: 'mysql.h': No such file or directory
    error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\cl.exe' failed with exit status 2
``` -->


## 读取数据库表内容

我们来看下面这样的一个读取数据库表的例子。

```py
import MySQLdb

# 创建一个 Connection 对象，代表了一个数据库连接
connection = MySQLdb.connect(
                host="192.168.0.100",# 数据库IP地址  
                user="username",     #  mysql用户名
                passwd="xxxxx",      # mysql用户登录密码
                db="dbname" ,        # 数据库名
                # 如果数据库里面的文本是utf8编码的，
                #charset指定是utf8
                charset = "utf8")   

# 返回一个 Cursor对象
c = connection.cursor()

# 执行一个获取 users 表中所有记录的 sql 语句
c.execute("""SELECT * FROM users """)


# rowcount属性记录了最近一次 execute 方法获取的数据行数
numrows = c.rowcount

for x in range(numrows):
    # fetchone 方法返回的是一个元组，
    # 代表获取的一行记录，元组里面每个元素代表一个字段
    row = c.fetchone()
    print(row)
```

<br>

我们可以发现，对数据库的操作是 ```通过SQL语句``` 进行的。

我们的代码需要先创建一个 Connection 对象 ， 然后再通过Connection 对象创建一个Cursor 对象。

最后使用Cursor对象的execute方法，传入要数据库服务执行的SQL语句。

调用execute执行完SQL语句后，cursor 对象的 fetchone 方法是获取一行记录。

fetchone 方法返回的是一个元组，代表获取的一行记录，元组里面每个元素代表一个字段。

上面的代码通过一个for循环，可以依次获取到数据库的记录行。

<br>

我们还可以用 fetchmany 方法来获取多行记录，该方法的参数就是要获取记录的条数，比如

```py
# 执行一个获取 users 表中所有记录的 sql 语句
c.execute("""SELECT * FROM users """)

# fetchmany方法返回的是一个元组，
# 里面每个元素也是元组，代表一行记录
rows = c.fetchmany(2)
print(rows)
```

我们还可以用 fetchall 方法来获取所有记录，比如

```py
# 执行一个获取 users 表中所有记录的 sql 语句
c.execute("""SELECT * FROM users """)

# fetchall方法返回的是一个元组，
# 里面每个元素也是元组，代表一行记录
rows = c.fetchall()
print(rows)
```


## 插入数据到数据库表

我们来看下面这样的一个插入数据到数据库表的例子。


```py
import MySQLdb

# 创建一个Connection 对象，代表了一个数据库连接
connection = MySQLdb.connect(
                host="192.168.0.100",# 数据库IP地址  
                user="username",     #  mysql用户名
                passwd="xxxxx",      # mysql用户登录密码
                db="dbname" ,        # 数据库名
                # 如果数据库里面的文本是utf8编码的，
                #charset指定是utf8
                charset = "utf8")   

# 返回一个cursor对象
c = connection.cursor()



#  插入一行数据到 user 表中
c.execute(f"""INSERT INTO users ( name, nickname, phone) VALUES ('baiyueheiyu', '白月黑羽', '13312345678')"""
                   )

# 注意 一定要commit，否则添加数据不生效
connection.commit()

connection.close()

```

插入数据操作当然也是通过  Cursor对象的execute方法，传入要数据库服务执行的 ```插入操作对应的SQL语句``` 。

注意， 凡是执行 ```更改``` 数据的SQL语句，包括：插入、修改、删除， 后面一定要调用connection的commit方法，否则不生效。