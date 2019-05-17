from threading import Thread,Lock
from random import randint
from time import sleep

# 银行账号类
class BankAccount:

    def __init__(self):
        # 账户余额，初识值为0
        self.balance = 0  

        # 创建锁对象，保护共享数据 balance
        self.balanceLock = Lock()

    #  存款
    def  deposit(self,amount):
        print('存款操作开始')
        # 访问共享数据前必须申请锁
        self.balanceLock.acquire()

        #为了演示效果，随机等待一段时间，
        sleep(randint(1,3))
        # 操作共享数据
        self.balance += amount

        # 访问共享数据后必须释放锁
        self.balanceLock.release() 
        print('存款操作结束')

    # 取款
    def withdrawal(self,amount):
        print('取款操作开始')
        # 访问共享数据前必须申请锁
        self.balanceLock.acquire()

        #为了演示效果，随机等待一段时间，
        sleep(randint(1,3))
        
        # 操作共享数据 
        self.balance -= amount

        # 访问共享数据后必须释放锁
        self.balanceLock.release()
        print('取款操作结束')
        
# 我的银行账号
myaccount = BankAccount()


# 创建一个新线程，执行存款2000操作
thread1 = Thread(target=myaccount.deposit,    
                 args=(2000,))

# 再创建一个新线程，执行取款500操作
thread2 = Thread(target=myaccount.withdrawal,  
                 args=(500,))

# 启动上面的两个子线程，
# 在两个子线程里面，分别执行存款 和取款 方法
thread1.start()
thread2.start()

# 等待两个子线程执行结束
thread1.join()
thread2.join()

print (f'最后我们的账号余额为 {myaccount.balance}')
