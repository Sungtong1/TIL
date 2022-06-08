# import sys
# input = sys.stdin.readline

a, b = input().split()

result = 0
for i in a:
    for j in b:
        result += int(i)*int(j)

print(result)

# 시간 초과 날 경우

a= list(map(int,a))
b = list(map(int,b))
print(sum(a) * sum(b))