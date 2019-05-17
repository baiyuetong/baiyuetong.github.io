---
title: Python开发常见问题集锦
toc: true
---

这里收集了 Python开发时，经常会碰到问题和解决方案。

建议大家在浏览器里面收藏该网页链接。

在开发时，碰到问题，就可以来这里拷贝、粘贴、简单修改，可以大大提高开发效率。

本文会一直更新，加入常见问题和解决方案。

<br>

<h2 id="基本操作"><a href="../basic/" target="_blank" style="text-decoration:none">基本操作</a></h2>

[合并2个列表](/doc/faq/python/basic/#%E5%90%88%E5%B9%B62%E4%B8%AA%E5%88%97%E8%A1%A8){:target="_blank"}

[合并2个字典](/doc/faq/python/basic/#%E5%90%88%E5%B9%B62%E4%B8%AA%E5%AD%97%E5%85%B8){:target="_blank"}

[从列表中过滤元素](/doc/faq/python/basic/#%E4%BB%8E%E5%88%97%E8%A1%A8%E4%B8%AD%E8%BF%87%E6%BB%A4%E5%85%83%E7%B4%A0){:target="_blank"}

[从字典中过滤元素](/doc/faq/python/basic/#%E4%BB%8E%E5%AD%97%E5%85%B8%E4%B8%AD%E8%BF%87%E6%BB%A4%E5%85%83%E7%B4%A0){:target="_blank"}

[产生随机数](/doc/faq/python/basic/#%E4%BA%A7%E7%94%9F%E9%9A%8F%E6%9C%BA%E6%95%B0){:target="_blank"}

[产生随机字符串](/doc/faq/python/basic/#%E4%BA%A7%E7%94%9F%E9%9A%8F%E6%9C%BA%E5%AD%97%E7%AC%A6%E4%B8%B2){:target="_blank"}

[‘/’和‘//’的区别](/doc/faq/python/basic/#和的区别){:target="_blank"}

[单引号，双引号，三引号的区别](/doc/faq/python/basic/#单引号双引号三引号的区别){:target="_blank"}

[删除列表元素的方法](/doc/faq/python/basic/#删除列表元素){:target="_blank"}

[列表排序sort和sorted](/doc/faq/python/basic/#列表排序sort和sorted){:target="_blank"}

[复制列表](/doc/faq/python/basic/#复制列表){:target="_blank"}

[列表去重](/doc/faq/python/basic/#列表去重){:target="_blank"}

[is和==](/doc/faq/python/basic/#isVS==){:target="_blank"}



<h2 id="字符串"><a href="../string/" target="_blank" style="text-decoration:none">字符串</a></h2>

[UNICODE数字转换为字符](/doc/faq/python/string/#unicode%E6%95%B0%E5%AD%97%E8%BD%AC%E6%8D%A2%E4%B8%BA%E5%AD%97%E7%AC%A6){:target="_blank"}

[字符转换为UNICODE数字](/doc/faq/python/string/#%E5%AD%97%E7%AC%A6%E8%BD%AC%E6%8D%A2%E4%B8%BAunicode%E6%95%B0%E5%AD%97){:target="_blank"}

[将字符串切割为多个字符串](/doc/faq/python/string/#%E5%B0%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%88%87%E5%89%B2%E4%B8%BA%E5%A4%9A%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2){:target="_blank"}

[使用正则表达式切割字符串](/doc/faq/python/string/#%E4%BD%BF%E7%94%A8%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E5%88%87%E5%89%B2%E5%AD%97%E7%AC%A6%E4%B8%B2){:target="_blank"}

[使用SPLIT函数从字符串中提取内容](/doc/faq/python/string/#%E4%BD%BF%E7%94%A8split%E5%87%BD%E6%95%B0%E4%BB%8E%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E6%8F%90%E5%8F%96%E5%86%85%E5%AE%B9){:target="_blank"}

[使用正则表达式从字符串中提取内容](/doc/faq/python/string/#%E4%BD%BF%E7%94%A8%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E4%BB%8E%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E6%8F%90%E5%8F%96%E5%86%85%E5%AE%B9){:target="_blank"}

[将列表中的字符串元素合并为一个字符串](/doc/faq/python/string/#%E5%B0%86%E5%88%97%E8%A1%A8%E4%B8%AD%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%85%83%E7%B4%A0%E5%90%88%E5%B9%B6%E4%B8%BA%E4%B8%80%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2){:target="_blank"}

[字符串替换时忽略大小写](/doc/faq/python/string/#%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%9B%BF%E6%8D%A2%E6%97%B6%E5%BF%BD%E7%95%A5%E5%A4%A7%E5%B0%8F%E5%86%99){:target="_blank"}

[字符串的格式化](/doc/faq/python/string/#%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%A0%BC%E5%BC%8F%E5%8C%96){:target="_blank"}

[JSON格式字符串处理](/doc/faq/python/string/#json%E6%A0%BC%E5%BC%8F%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%A4%84%E7%90%86){:target="_blank"}

[字符串的倒序](/doc/faq/python/string/#字符串的倒序){:target="_blank"}



<h2 id="文件和目录操作"><a href="/doc/tutorial/python/level2/file_dir/" target="_blank" style="text-decoration:none">文件和目录操作</a></h2>

创建目录

删除文件或目录

拷贝文件

拷贝目录

修改文件名、目录名

对文件路径名的操作

判断文件、目录是否存在

获取文件的大小和日期

递归的遍历目录下面所有的文件

得到目录中所有的文件和子目录名

得到目录中指定扩展名的文件和子目录



<h2 id="日期和时间"><a href="../date_time/" target="_blank" style="text-decoration:none">日期和时间</a></h2>


[获取当前时间对应的数字](/doc/faq/python/date_time/#%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E6%97%B6%E9%97%B4%E5%AF%B9%E5%BA%94%E7%9A%84%E6%95%B0%E5%AD%97){:target="_blank"}

[指定格式字符串显示时间](/doc/faq/python/date_time/#%E6%8C%87%E5%AE%9A%E6%A0%BC%E5%BC%8F%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%98%BE%E7%A4%BA%E6%97%B6%E9%97%B4){:target="_blank"}

[获取当前时间 对应 的年月日时分秒](/doc/faq/python/date_time/#%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E6%97%B6%E9%97%B4-%E5%AF%B9%E5%BA%94-%E7%9A%84%E5%B9%B4%E6%9C%88%E6%97%A5%E6%97%B6%E5%88%86%E7%A7%92){:target="_blank"}

[获得指定日期对应星期几](/doc/faq/python/date_time/#%E8%8E%B7%E5%BE%97%E6%8C%87%E5%AE%9A%E6%97%A5%E6%9C%9F%E5%AF%B9%E5%BA%94%E6%98%9F%E6%9C%9F%E5%87%A0){:target="_blank"}

[获得指定日期所在周的周一的日期](/doc/faq/python/date_time/#%E8%8E%B7%E5%BE%97%E6%8C%87%E5%AE%9A%E6%97%A5%E6%9C%9F%E6%89%80%E5%9C%A8%E5%91%A8%E7%9A%84%E5%91%A8%E4%B8%80%E7%9A%84%E6%97%A5%E6%9C%9F){:target="_blank"}



<h2 id="进程和线程"><a href="../process_thread/" target="_blank" style="text-decoration:none">进程和线程</a></h2>


[调用其它程序，并且判断其返回码](/doc/faq/python/process_thread/#%E8%B0%83%E7%94%A8%E5%85%B6%E5%AE%83%E7%A8%8B%E5%BA%8F%E5%B9%B6%E4%B8%94%E5%88%A4%E6%96%AD%E5%85%B6%E8%BF%94%E5%9B%9E%E7%A0%81){:target="_blank"}

[调用其它程序，并且获取输出结果](/doc/faq/python/process_thread/#%E8%B0%83%E7%94%A8%E5%85%B6%E5%AE%83%E7%A8%8B%E5%BA%8F%E5%B9%B6%E4%B8%94%E8%8E%B7%E5%8F%96%E8%BE%93%E5%87%BA%E7%BB%93%E6%9E%9C){:target="_blank"}

[非阻塞式调用其它程序](/doc/faq/python/process_thread/#%E9%9D%9E%E9%98%BB%E5%A1%9E%E5%BC%8F%E8%B0%83%E7%94%A8%E5%85%B6%E5%AE%83%E7%A8%8B%E5%BA%8F){:target="_blank"}



<h2 id="类和对象"><a href="../class/" target="_blank" style="text-decoration:none">类和对象</a></h2>

[PRINT自定义对象](/doc/faq/python/class/#print%E8%87%AA%E5%AE%9A%E4%B9%89%E5%AF%B9%E8%B1%A1){:target="_blank"}

[定义PROPERTY 属性](/doc/faq/python/class/#%E5%AE%9A%E4%B9%89property-%E5%B1%9E%E6%80%A7){:target="_blank"}

[子类中调用父类的方法](/doc/faq/python/class/#%E5%AD%90%E7%B1%BB%E4%B8%AD%E8%B0%83%E7%94%A8%E7%88%B6%E7%B1%BB%E7%9A%84%E6%96%B9%E6%B3%95){:target="_blank"}






<h2 id="哈希和加密"><a href="/doc/tutorial/python/level2/hash_encrypt/" target="_blank" style="text-decoration:none">哈希和加密</a></h2>

[计算MD5/SHA1等哈希值](/doc/tutorial/python/level2/hash_encrypt/#python%E8%AF%AD%E8%A8%80%E8%AE%A1%E7%AE%97%E5%93%88%E5%B8%8C%E5%80%BC){:target="_blank"}



[加解密运算](http://localhost:4000/doc/tutorial/python/level2/hash_encrypt/#python%E8%AF%AD%E8%A8%80%E5%8A%A0%E8%A7%A3%E5%AF%86){:target="_blank"}




<h2 id="其他"><a href="../others/" target="_blank" style="text-decoration:none">其他</a></h2>

[命令行提示找不到Python命令](/doc/faq/python/others/#%E8%BF%90%E8%A1%8Cpython%E7%A8%8B%E5%BA%8F%E6%8F%90%E7%A4%BA%E6%89%BE%E4%B8%8D%E5%88%B0python%E5%91%BD%E4%BB%A4){:target="_blank"}

[命令行提示找不到代码文件](/doc/faq/python/others/#%E8%BF%90%E8%A1%8Cpython%E7%A8%8B%E5%BA%8F%E6%8F%90%E7%A4%BA%E6%89%BE%E4%B8%8D%E5%88%B0%E4%BB%A3%E7%A0%81%E6%96%87%E4%BB%B6){:target="_blank"}


[查看和修改当前工作目录](/doc/faq/python/others/#%E6%9F%A5%E7%9C%8B%E5%92%8C%E4%BF%AE%E6%94%B9%E5%BD%93%E5%89%8D%E5%B7%A5%E4%BD%9C%E7%9B%AE%E5%BD%95){:target="_blank"}

[查看导入的模块的路径](/doc/faq/python/others/#%E6%9F%A5%E7%9C%8B%E5%AF%BC%E5%85%A5%E7%9A%84%E6%A8%A1%E5%9D%97%E7%9A%84%E8%B7%AF%E5%BE%84){:target="_blank"}

[查看当前正在执行的代码文件的路径](/doc/faq/python/others/#%E6%9F%A5%E7%9C%8B%E5%BD%93%E5%89%8D%E6%AD%A3%E5%9C%A8%E6%89%A7%E8%A1%8C%E7%9A%84%E4%BB%A3%E7%A0%81%E6%96%87%E4%BB%B6%E7%9A%84%E8%B7%AF%E5%BE%84){:target="_blank"}

[查看当前运行的python解释器的路径](/doc/faq/python/others/#%E6%9F%A5%E7%9C%8B%E5%BD%93%E5%89%8D%E8%BF%90%E8%A1%8C%E7%9A%84python%E8%A7%A3%E9%87%8A%E5%99%A8%E7%9A%84%E8%B7%AF%E5%BE%84){:target="_blank"}