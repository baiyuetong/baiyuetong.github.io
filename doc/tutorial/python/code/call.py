# import os
# cmd = r'd:\tools\wget http://mirrors.sohu.com/nginx/nginx-1.13.9.zip'
# os.system(cmd)

# print('下载完毕')


from subprocess import PIPE, Popen

# 返回的是 Popen 实例对象
proc = Popen(
    'fsutil volume diskfree c:',
    stdin  = None,
    stdout = PIPE,
    stderr = None,
    shell=True)

# communicate 方法返回 输出到 标准输出 和 标准错误 的字节串内容
# 标准输出设备和 标准错误设备 当前都是本终端设备
# 可与简单理解为 就是屏幕
outinfo, errinfo = proc.communicate()

# 注意返回的内容是bytes 不是 str ，我的是中文windows，所以用gbk解码
outinfo = outinfo.decode('gbk')
print (outinfo) 


outputList = outinfo.splitlines()


free  = int(outputList[0].split(':')[1].strip())
total = int(outputList[1].split(':')[1].strip())

if (free/total < 0.1):
    print('!! 剩余空间告急！！')
else:
    print('剩余空间足够')




