# 재귀
def powerset(k):
    if k == n:
        print(*sel)
        return
    sel[k] = 1
    powerset(k+1)
    sel[k] = 0
    powerset(k+1)


dice = [1,2,3,4,5,6]
n = len(dice)
sel = [0] * n
powerset(0)


