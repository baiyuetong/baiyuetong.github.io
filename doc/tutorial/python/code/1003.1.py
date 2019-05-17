import time

def sayLocal(func):
    def wrapper(*args,**kargs):
        curTime = func(*args,**kargs)
        return f'当地时间： {curTime}'
    return wrapper

@sayLocal
def getCurTimeFormat1(name):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} '

@sayLocal
def getCurTimeFormat2(name,place):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} , 采集地：{place}'

print (getCurTimeFormat1('张三'))    
print (getCurTimeFormat2('张三','北京'))    