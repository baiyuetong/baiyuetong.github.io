
<br>
## 安装客户端库


目前使用Python语言访问mysql数据库， 推荐使用客户端库 mysqlclient 和 PyMySQL。

mysqlclient 库是C语言开发的，性能比较高。我们这里就使用它。


这个库遵循 Python统一数据库访问接口规范（[参考PEP 249](https://www.python.org/dev/peps/pep-0249/)），支持Python3 并且  抽象层级比较高。

这是个开源的库，官方网址在github上 https://github.com/PyMySQL/mysqlclient-python


使用文档在这里  https://mysqlclient.readthedocs.io/

既然是Python的第三方库，当然是用 pip安装了。 运行命令 ```pip install mysqlclient``` 安装

有时，我们可能需要指定mysqlclient库的版本为1.3.12，像这样  pip install mysqlclient==1.3.12    。因为mysqlclient 需要依赖一个c语言开发的库， 1.3.12版本安装包已经将c语言库编译好了，成为可执行代码库，就不需要安装时候编译了。
{: .notice--primary}

<br>

如果你想使用 的客户端库是PyMySQL ，运行命令  ```pip install PyMySQL``` 安装


<br>

- ```视频讲解``` 

<video src="http://v.python666.vip/video/o/mysql/mpmysql-06-2.mp4"  style="width: 90%;" controls controlsList="nodownload" oncontextmenu="return false;" preload="metadata" poster="{{ site.video_cover }}"></video>

<br>


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



<br>

- ```视频讲解``` 

<video src="http://v.python666.vip/video/o/mysql/mpmysql-06-3-1.mp4"  style="width: 90%;" controls controlsList="nodownload" oncontextmenu="return false;" preload="metadata" poster="{{ site.video_cover }}"></video>



<br>

- ```视频讲解``` 

<video src="http://v.python666.vip/video/o/mysql/mpmysql-06-3-2.mp4"  style="width: 90%;" controls controlsList="nodownload" oncontextmenu="return false;" preload="metadata" poster="{{ site.video_cover }}"></video>

<br>


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


<br>

- ```视频讲解``` 

<video src="http://v.python666.vip/video/o/mysql/mpmysql-06-4.mp4"  style="width: 90%;" controls controlsList="nodownload" oncontextmenu="return false;" preload="metadata" poster="{{ site.video_cover }}"></video>

<br>