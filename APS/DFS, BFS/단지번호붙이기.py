from collections import deque

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(r,c):
    cnt = 1
    q = deque()
    q.append((r,c))
    visited[r][c] = danGGGGGGI
    while q:
        curr_r, curr_c = q.popleft()
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and arr[nr][nc]:
                    visited[nr][nc] = danGGGGGGI
                    cnt += 1
                    q.append((nr,nc))
    return cnt

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
visited= [[0]*n for _ in range(n)]
danGGGGGGI = 0
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            danGGGGGGI += 1
            result.append(bfs(i,j))
result.sort()

print(len(result))
for i in result:
    print(i)