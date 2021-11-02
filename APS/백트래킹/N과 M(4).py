def go(k,idx):
    if k == m:
        print(*sel)
        return
    for i in range(idx,n+1):
        sel[k] = i
        go(k+1,i)


n, m = map(int,input().split())

sel=[0] * m
go(0,1)