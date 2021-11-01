def nCr(k,idx):
    if k == r:
        print(*sel)
        return
    for i in range(idx,n-r+k+1):
        sel[k] = dice[i]
        nCr(k+1,i+1)

n, r = map(int,input().split())
dice = [1,2,3,4,5,6]
sel = [0] * r

nCr(0,0)