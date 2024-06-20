def remove_word(str,word):
    str2=str.replace(str,word,'')
    return str2
str3="hello good mrng hi hello good mrng"
print("Before remove")
print(str3)
str4=remove_word(str3,"hello")
print(str4)