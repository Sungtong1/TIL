def go(s_idx):
    if s_idx == m:
        print(*sel)
        return
    for i in range(1,n+1):
        sel[s_idx] = i
        go(s_idx+1)


n, m = map(int,input().split())
sel = [0] * m
go(0)