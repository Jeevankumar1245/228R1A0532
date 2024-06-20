from sys import argv
if len(argv==3):
    try:
        fp1=open("argv[i]","r")
        fp2=open("argv[i]","w+")
        for i in fp1:
              fp2.write(i)
        print("file is copied successfully")
        fp2.seek(0,0)
        cont=fp2.read()
