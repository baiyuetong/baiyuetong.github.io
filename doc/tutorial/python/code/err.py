# while True:
#     try:
#         miles = input('请输入英里数:')
#         km = int(miles) * 1.609344
#         print(f'等于{km}公里')
#     except ValueError:
#         print('你输入了非数字字符')

# try:
#     choice = input('输入你的选择:')
#     if choice == '1':
#         100/0
#     else:
#         [][2]
# except ZeroDivisionError:
#     print ('出现 ZeroDivisionError')
# except IndexError  :
#     print ('出现 IndexError  ')



import traceback

def level_3():
    print ('进入 level_3')
    a = [0]
    b = a[1]
    print ('离开 level_3')

def level_2():
    print ('进入 level_2')
    level_3()
    print ('离开 level_2')

def level_1():
    print ('进入 level_1')
    level_2()
    print ('离开 level_1')

try:
    level_1()
except :
    print(f'未知异常:{traceback.format_exc()}')

print('程序正常退出')