# n = int(input())
# result = 0
# for i in range(1,n): # n 216 => 216 -27 => 189
#     tmp = i
#     nums = i
#     while nums > 0:
#         tmp += nums%10
#         nums = nums//10
#     if tmp == n:
#         result = i
#         break
#
# print(result)




n = input()
a = len(n)
n = int(n)
result = 0
for i in range(n-(9*a),n):
    tmp = i
    nums = i
    while nums > 0:
        tmp += nums%10
        nums = nums//10
    if tmp == n:
        result = i
        break

print(result)