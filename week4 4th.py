def nbit(n,arr,i):
    if i == n:
        print(*arr)
        return
    arr[i]=0
    nbit(n,arr,i+1)
    arr[i]=1
    nbit(n,arr,i+1)

n=int(input())
arr=[0]*n
nbit(n,arr,0)