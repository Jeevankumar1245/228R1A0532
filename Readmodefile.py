fp1=open("CSE-A1.txt","r")
if fp1:
    print("file is open successfully")
    fp1.seek(0,1)
    for i in fp1:
        print(i)

'''    content=fp1.readline()
    print(content)
    content=fp1.readline()
    print(content)
    content=fp1.readline()
    print(content)
'''
fp.close
