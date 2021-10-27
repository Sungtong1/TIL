n = int(input())
result = 0
for i in range(1,n):
    tmp = i
    nums = i
    while nums > 0:
        tmp += nums%10
        nums = nums//10
    if tmp == n:
        result = i
        break

print(result)