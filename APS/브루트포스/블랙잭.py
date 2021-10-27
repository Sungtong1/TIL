n, m = map(int, input().split())
card = list(map(int, input().split()))
r = 3
sel = [0] * r
result = 0


def comb(idx, s_idx):
    global result
    if s_idx == r:
        x = sum(sel)
        if x <= m and x >=result:
            result = x
        return
    elif idx == n:
        return
    else:
        sel[s_idx] = card[idx]
        comb(idx + 1, s_idx + 1)
        comb(idx + 1, s_idx)


comb(0, 0)
print(result)