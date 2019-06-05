

commonFileList = [
    r'index.md',     
    r'_config.yml',
    r'_data\navigation.yml',        
]

switchTable = [
    # free
    {
        'prefix' : 'free',
        'fileList' : commonFileList
    },

    # v1
    {
        'prefix' : 'v1',
        'fileList' : commonFileList
    }
]

from shutil import copyfile
import os

# 查看以往使用什么前缀
default = ''
historyFile = r'd:\tmp\byhy_switch'
if os.path.exists(historyFile):
    f = open(historyFile)
    default = f.readline()
    f.close()

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


found = False
for one in switchTable:
    if one['prefix'] != toWhich:
        continue
    
    found = True
    for filePath in one['fileList']:
        parts = filePath.rsplit('.',1)
        newPath = f'{parts[0]}_{toWhich}.{parts[1]}'

        print(newPath)
        if not REVERSE:
            copyfile(newPath,filePath)
        else:
            print('reverse copy >>')
            copyfile(filePath,newPath)


if not found:
    print(f'no such config:{toWhich}')