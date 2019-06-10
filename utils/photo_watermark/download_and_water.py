# dos窗口，进入到项目根目录，使用下面的命令 找出所有图片链接
# findstr /S "https://user-images.githubusercontent.com" *.md > d:\info.txt

import os,sys

# 把项目中github图片链接 行 放到 info.txt中
cmd = 'findstr /S "https://user-images.githubusercontent.com" *.md > d:\info.txt'
print(cmd)
os.system(cmd)

choice = input('新的文件已经生成，继续吗？')
if choice.lower()!='y':
    sys.exit(0)


# 分析文件，取出图片链接 并产生对应的 新文件名
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
        # 发现图片在不同文档中，就退出循环，确保一个文档一个文档的处理
        else:
            if docName != thisTimeDocName: 
                break

        fileName = line.split(URL_PREFIX)[1].split(')')[0]

        url = URL_PREFIX + fileName

        print(url)

        urls.append([url,fileName])



# 下载图片文件到 D:\，并以新名字保存 规则为：
# https://user-images.githubusercontent.com/36462795/36407230-c700aea2-1637-11e8-89a9-bd754be563f3.png
# 转为 36257654_37151636-49e02664-2311-11e8-90af-944325bcb6c6.png
inputfiles = []
for url,fileName in urls:

    newFileName = fileName.replace('/','_')
    inputfiles.append(newFileName)
        
    # print(newFileName)
    cmd = f'wget -O d:/{newFileName} {url}'
    print(cmd)
    ret = os.system(cmd)
    if ret !=0:
        print('\n！！ 出现错误，退出 ！！')
        sys.exit(2)


    print('\n\n=============\n\n')


# 将下载下来的图片加上水印


waterFile=r'd:\gsync\workspace\others\sk\etc\others\water4.PNG'
ffmpegEXE = r'd:\tools\ffmpeg20190403\bin\ffmpeg.exe'

    
inputDir ='d:/'
outputDir =  'd:/tmp/'

import os

def waterpng(inputfile):
    
    outputfile = f"{inputfile.rsplit('.',1)[0]}.png"

        
    cmd = f'{ffmpegEXE} -y -i {inputDir}{inputfile} -i {waterFile} -filter_complex  "[1]lut=a=val*0.03[a];[0][a]overlay=(main_w-overlay_w)/2.3:(main_h-overlay_h)/2.3"   {outputDir}{outputfile}'
    print(cmd)
    os.system(cmd)

for inputfile in inputfiles:
    waterpng(inputfile)