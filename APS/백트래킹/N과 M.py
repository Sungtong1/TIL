def go(k):
    if k == m:
        print(*sel)
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = 1
            sel[k] = i
            go(k+1)
            visited[i] = 0
n, m = map(int,input().split())
sel = [0] * m
visited = [0] * (n+1)
go(0)