# 백준 드래곤 커브

def draw_dragon(x,y,d,g):
    history = []
    array[y][x] = 1
    if d == 0:
        x += 1
    elif d == 1:
        y -= 1
    elif d == 2:
        x -= 1
    elif d == 3:
        y += 1
    array[y][x] = 1
    history.append(d)
    cur_gen = 1
    while cur_gen <= g:
        a = len(history)-1
        for i in range(a,-1,-1):
            d = (history[i] + 1)% 4
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
            if 0 <= x <= 100 and 0<= y <= 100:
                array[y][x] = 1
            history.append(d)
        cur_gen += 1

dragon_population = int(input())
array = [[0]*101 for _ in range(101)]
for i in range(dragon_population):
    X, Y, D, G = map(int, input().split())
    draw_dragon(X,Y,D,G)

result = 0
for i in range(100):
    for j in range(100):
        if array[i][j] == 1:
            if array[i+1][j] * array[i][j+1] * array[i+1][j+1] == 1:
                result +=1
        else: continue
print(result)
