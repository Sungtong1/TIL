def comb(k,idx):
    if k == r:
        print(*sel)
        return
    for i in range(idx,n-r+k+1): # n
        sel[k] = arr[i]
        comb(k+1,i+1)

def powerset(k):
    if k == n:
        print(*sel)
        return
    sel[k] = 1
    powerset(k+1)
    sel[k] = 0
    powerset(k+1)


n, r = map(int,input().split())
arr = [1,2,3,4,5,6]
sel = [0] * n
# comb(0,0)
powerset(0)
for i in range(1<<n):
    tmp = []
    for j in range(n):
        if i & 1<<j:
            tmp.append(arr[j])
    print(*tmp)