# N = 몇분
# m = 최소값
# M = 최대값
# T = 운동 할때 맥박
# R = 휴식 맥박

import sys
input = sys.stdin.readline

N,m,M,T,R = map(int,input().split())
pulse = m
result = 0

while N > 0:
    if m + T > M:
        print(-1)
        exit(0)

    if pulse + T > M:
        result += 1
        pulse -= R
        if pulse < m:
            pulse = m
        continue
    result += 1
    N -= 1
    pulse += T

print(result)

