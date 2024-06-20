def palindrome(str):
    for i in range(0,len(str)):
        if(str[i]!=str[len(str)-i-1]):
            return False
        return true
    str=input("Enter string")
    if(palindrome(str)==True):
        print("The given string is palindrome")
    else:
        print("Not a palindrome")