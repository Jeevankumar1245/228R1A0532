'''

open()
read()
readline()
write()
writeline()
close()
fseek()
tell()

'''
fp=open("CSE-A1.txt","w")
if fp:
    print("file is created successfully")
    fp.write("hi student welcome to cmrec\n today smart interview class\n today python is on files")
    fp.close()