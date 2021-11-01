n = int(input())
my_tuple = [tuple(map(int,input().split())) for _ in range(n)]

for i in range(n):
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        if my_tuple[i][0] < my_tuple[j][0] and my_tuple[i][1] < my_tuple[j][1]:
           cnt +=1
    print(cnt,end=' ')