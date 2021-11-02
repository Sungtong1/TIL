def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result

    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)


N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)


# def nqueen(k):
#     global result
#     if k == n:
#         result += 1
#     else:
#         for i in range(n):
#             if not used[k][i]:
#                 for j in range(i + 1, n):
#                     used[k][j] += 1
#                 for o in range(k + 1, n):
#                     used[o][i] += 1
#                 a = i
#                 b = k
#                 while a < n and b < n:
#                     used[b][a] += 1
#                     a += 1
#                     b += 1
#                 a = i - 1
#                 b = k + 1
#                 while 0 <= a and b < n:
#                     used[b][a] += 1
#                     a -= 1
#                     b += 1
#                 nqueen(k + 1)
#
#                 for j in range(i + 1, n):
#                     used[k][j] -= 1
#                 for o in range(k + 1, n):
#                     used[o][i] -= 1
#                 a = i
#                 b = k
#                 while a < n and b < n:
#                     used[b][a] -= 1
#                     a += 1
#                     b += 1
#                 a = i - 1
#                 b = k + 1
#                 while 0 <= a and b < n:
#                     used[b][a] -= 1
#                     a -= 1
#                     b += 1
#
#
#
# n = int(input())
# used = [[0] * n for _ in range(n)]
# result = 0
# nqueen(0)
# print(result)