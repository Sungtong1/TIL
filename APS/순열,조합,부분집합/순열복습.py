def dice1(k):
    if k == n:
        print(*sel)
        return
    for i in range(len(dice)):
        sel[k] = dice[i]
        dice1(k+1)
def dice2(idx, s_idx):
    if s_idx == n:
        print(*sel)
        return
    for i in range(idx,len(dice)):
        sel[s_idx] = dice[i]
        dice2(i,s_idx+1)
def dice3(k):
    if k == n:
        print(*sel)
        return
    for i in range(len(dice)):
        if not visited[i]:
            visited[i] = 1
            sel[k] = dice[i]
            dice3(k+1)
            visited[i] = 0

n, m = map(int,input().split())
dice = [1,2,3,4,5,6]
sel = [0] * n
visited = [0] * len(dice)

if m == 1:
    dice1(0)
elif m ==2:
    dice2(0,0)
elif m ==3:
    dice3(0)