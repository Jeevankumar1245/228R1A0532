def OR(a,b):
    if a==1 and b==1:
        return True
    else:
        return False
print(("A=True|B=True|A OR B=True",OR(True,True)))
print(("A=True|B=False|A OR B=False",OR(True,True)))
print(("A=False|B=True|A OR B=False",OR(True,True)))
print(("A=False|B=False|A OR B=False",OR(True,True)))
#print(OR(1,1))
