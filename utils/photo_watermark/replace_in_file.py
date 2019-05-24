inputfiles = [
'36257654_37151636-49e02664-2311-11e8-90af-944325bcb6c6.png',
'36462795_36406714-b4485264-1633-11e8-9cff-21340e5328ff.png',
'36462795_36406607-146d4542-1633-11e8-9b94-4e0451588c03.png',
'36462795_36406563-c5af3fe6-1632-11e8-9807-4464513f5faa.png',

]


for inputfile in inputfiles:
    oripath = inputfile.replace('_','/')
    oripath = 'https://user-images.githubusercontent.com/' + oripath

    newpath = 'http://v.python666.vip/img/wm/'+ inputfile

    print('\n\n============\n\n')
    print(oripath)