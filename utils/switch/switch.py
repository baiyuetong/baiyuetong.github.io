commonFileList = [
    r'index.md',     
    r'_config.yml',
    r'_data\navigation.yml',        
]

Path_Prefix = r'utils\switch'


switchTable = ['free','v1']

from shutil import copyfile
import os,sys


# 检查当前工作目录是否为项目根目录
if not (os.path.exists('byhy_run.bat') and os.path.exists('CNAME')):
    print('必须在项目根目录下面运行')
    sys.exit(2)


# 查看以往使用什么前缀
default = ''
historyFile = r'd:\tmp\byhy_switch'
if os.path.exists(historyFile):
    f = open(historyFile)
    default = f.readline()
    f.close()

# 用户输入操作
toWhich = input(f'please input target[{default}]:')
if toWhich is '':
    toWhich = default
else:
    f = open(historyFile,'w')
    f.write(toWhich)
    f.close()

# 检查是否反向覆盖
REVERSE = False
if toWhich.endswith('-'):
    REVERSE = True
    toWhich = toWhich[:-1]


if toWhich not in switchTable:
    print(f'no such config:{toWhich}')
    sys.exit(2)



    
for filePath in commonFileList:
    parts = os.path.basename(filePath).rsplit('.',1)
    source = f'{parts[0]}_{toWhich}.{parts[1]}'
    sourcePath = os.path.join(Path_Prefix,source)


    if not REVERSE:
        print(f"{sourcePath} -> {filePath}")
        copyfile(sourcePath,filePath)
    else:
        print(f"{filePath} -> {sourcePath}")
        copyfile(filePath,sourcePath)
