fname = input("Enter file name: ")
num_lines = 0
num_words = 0
num_chars = 0
try:
    fp=open(fname,"r")
    for i in fp:
        words = i.split()
        num_lines += 1
        num_words += len(words)
        num_chars += len(i)
    print("Lines = ",num_lines)
    print("Words = ",num_words)
    print("Characters = ",num_chars)
    fp.close()
except Exception:
    print("Enter valid filename")