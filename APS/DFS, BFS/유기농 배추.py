from collections import deque

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    arr[i][j] =0
    while q:
        curr_r, curr_c = q.popleft()
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if 0 <= nr < sero and 0 <= nc < garo and arr[nr][nc]:
                arr[nr][nc] = 0
                q.append((nr,nc))



for tc in range(1,int(input())+1):
    garo, sero, baechus = map(int,input().split())
    arr = [[0]*garo for _ in range(sero)]
    result = 0
    for i in range(baechus):
        r, c = map(int,input().split())
        arr[c][r] = 1

    for i in range(sero):
        for j in range(garo):
            if arr[i][j]:
                result += 1
                bfs(i,j)
    print(result)
