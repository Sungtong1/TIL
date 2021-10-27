# # 순열
# def type1(k):
#     if k == n:
#         print(*sel)
#         return
#     for i in range(1,len(dice)+1):
#         sel[k] = i
#         type1(k+1)
#
# # 중복 순열
# def type2(idx, s_idx):
#     if s_idx == n:
#         print(*sel)
#         return
#     for i in range(idx,len(dice)+1):
#         sel[s_idx] = i
#         type2(i, s_idx+1)
#
#
# def type3(k):
#     if k == n:
#         print(*sel)
#         return
#     for i in range(len(dice)):
#         if not visited[i]:
#             sel[k] = dice[i]
#             visited[i] = 1
#             type3(k+1)
#             visited[i] = 0
#
#
# n, m = map(int, input().split())
#
# dice = [1,2,3,4,5,6]
# sel = [0] * n
#
# if m == 1:
#     type1(0)
# elif m == 2:
#     type2(1,0)
# elif m == 3 :
#     visited = [0] * len(dice)
#     type3(0)

# from itertools import combinations
#
# print(list(combinations([1,2,3,4], 2)))
#
# from itertools import permutations
#
# print(permutations([1,2,3,4], 2))

def type1(k):
    if k == n:
        print(*sel)
        return
    for i in range(n):
        sel[k] == dice[i]
        type(k+1)

def type2(idx, s_idx):
    if s_idx == n:
        print(*sel)
        return
    for i in range(idx,len(dice)):
        sel[s_idx] = dice[i]
        type2(i,s_idx+1)

# def type2(idx, s_idx):
#     if s_idx == n:
#         print(*sel)
#         return
#     for i in range(idx,len(dice)+1):
#         sel[s_idx] = i
#         type2(i, s_idx+1)
def type3(k):
    if k == n:
        print(*sel)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            sel[k] = dice[i]
            type3(k+1)
            visited[i] = 0


dice = [1,2,3,4,5,6]
n, m = map(int, input().split())

if m == 1:
    sel = [0] * n
    type1(0)
elif m ==2:
    sel = [0] * n
    type2(0,0)
elif m == 3:
    sel = [0] * n
    visited = [0] * len(dice)
    type3(0)
