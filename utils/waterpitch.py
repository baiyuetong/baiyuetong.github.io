inputfiles = [
'prac11-1-1',
'prac11-1-2',

]


import os

def handle(inputfile):
    output = f"p{inputfile}"

    try:
        os.remove('tmp.mp4')
    except:
        pass
        
    cmd = f'ffmpeg -y -i {inputfile}.mp4 -i water.png -filter_complex  "[1]lut=a=val*0.07[a];[0][a]overlay=(main_w-overlay_w)/2.3:(main_h-overlay_h)/2.3"   -c:v libx264 -c:a copy  tmp.mp4'
    os.system(cmd)

    cmd = f'ffmpeg -i tmp.mp4 -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy -movflags +faststart m{output}.mp4'
    os.system(cmd)

for inputfile in inputfiles:
    handle(inputfile)