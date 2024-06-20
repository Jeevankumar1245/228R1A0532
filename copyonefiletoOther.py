fp1=open("CSE=A1.txt","r")
fp2=open("CSE-A.txt","r")
if fp1:
    print("file open successfully")
for i in fp1:
    fp2.write(i)
    print("file is copied successfully")
    fp2=seek(0,1)
    content=fp2.read()
    print(content)
    fp1.close()
    fp2.close()