# dos窗口，进入到项目根目录，使用下面的命令 找出所有图片链接
# findstr /S "https://user-images.githubusercontent.com" *.md > d:\info.txt

import os,sys


# cmd = 'findstr /S "https://user-images.githubusercontent.com" *.md > d:\info.txt'
# print(cmd)
# os.system(cmd)

# choice = input('新的文件已经生成，继续吗？')
# if choice.lower()!='y':
#     sys.exit(0)

URL_PREFIX = 'https://user-images.githubusercontent.com/'

thisTimeDocName = None
urls = []
with open(r'd:\info.txt',encoding='utf8') as f:
    
    lines = f.read().splitlines()
    for line in lines:
        if URL_PREFIX not in line:
            continue
        
        # 文档名
        docName = line.split(":")[0]
        if thisTimeDocName is None:
            thisTimeDocName = docName
        else:
            if docName != thisTimeDocName: 
                break

        fileName = line.split(URL_PREFIX)[1].split(')')[0]

        url = URL_PREFIX + fileName

        print(url)

        urls.append([url,fileName])




for url,fileName in urls:

    newFileName = fileName.replace('/','_')
        
    # print(newFileName)
    cmd = f'wget -O d:/{newFileName} {url}'
    print(cmd)
    os.system(cmd)


    print('\n\n=============\n\n')
