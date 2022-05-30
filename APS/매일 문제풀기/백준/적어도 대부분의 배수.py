import sys
input = sys.stdin.readline

num_list = list(map(int, input().split()))

num_list.sort()

for i in range(num_list[2],100**3):
    cnt = 0
    for j in num_list:
        if i % j == 0:
            cnt +=1

        if cnt == 3:
            print(i)
            exit(0)
