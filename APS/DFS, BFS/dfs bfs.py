
from collections import deque

v = int(input())
e = int(input())
adj = [[] for _ in range(v+1)]
for i in range(e):
    st, ed = map(int,input().split())
    adj[st].append(ed)
    adj[ed].append(st)

def dfs(st):
    cnt = 0
    visited = [0]*(v+1)
    stack = [st]
    visited[st] = 1
    while stack:
        curr = stack.pop()
        for i in adj[curr]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                stack.append(i)
    return cnt
print(dfs(1))

def bfs(st):
    cnt = 0
    visited = [0] * (v+1)
    q = deque()
    q.append(st)
    visited[st] = 1
    while q:
        curr = q.popleft()
        for i in adj[curr]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt

print(bfs(1))

cnt = 0
visited = [0] * (v+1)
def dfs2(st):
    global cnt
    visited[st] = 1
    for i in adj[st]:
        if not visited[i]:
            cnt += 1
            dfs2(i)
dfs2(1)
print(cnt)