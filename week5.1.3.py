def read_mat(A,r,c):
    for i in range(r):
        t=[]
        for j in range(c):
            val=int(input(f"Enter the A[{i}][{j}]value"))
            t.append(val)
        A.append(t)
mat_A=[]
read_mat(mat_A,2,2)
print("mat_A")
def display_mat(A):
    for i in A:
        print(i)
display_mat(mat_A)

mat_B=[]
read_mat(mat_B,2,2)
print("mat_B")
def display_mat(B):
    for i in B:
        print(i)
display_mat(mat_A)

C=[]
print("Addition of two matrix")
for i in range(2):
    t=[]
    for j in range(2):
        val=mat_A[i][j]+mat_B[i][j]
        t.append(val)
    C.append(t)
display_mat(C)
