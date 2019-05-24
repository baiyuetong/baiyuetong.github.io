inputfiles = [
'36257654_37151636-49e02664-2311-11e8-90af-944325bcb6c6.png',
'36462795_36406714-b4485264-1633-11e8-9cff-21340e5328ff.png',
'36462795_36406607-146d4542-1633-11e8-9b94-4e0451588c03.png',
'36462795_36406563-c5af3fe6-1632-11e8-9807-4464513f5faa.png',

]

waterFile=r'd:\gsync\workspace\others\sk\etc\water.png'
ffmpegEXE = r'd:\tools\ffmpeg20190403\bin\ffmpeg.exe'

    
inputDir ='d:/'
outputDir =  'd:/tmp/'

import os

def handle(inputfile):
    
    outputfile = f"{inputfile.rsplit('.',1)[0]}_wm.png"

        
    cmd = f'{ffmpegEXE} -y -i {inputDir}{inputfile} -i {waterFile} -filter_complex  "[1]lut=a=val*0.03[a];[0][a]overlay=(main_w-overlay_w)/2.3:(main_h-overlay_h)/2.3"   {outputDir}{outputfile}'
    print(cmd)
    os.system(cmd)

for inputfile in inputfiles:
    handle(inputfile)