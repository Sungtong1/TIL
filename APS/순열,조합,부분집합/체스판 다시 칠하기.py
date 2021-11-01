def check(str,stc):
    cnt_b = 0
    cnt_w = 0
    for i in range(8):
        for j in range(8):
            if arr[str+i][stc+j] != startb[i][j]:
                cnt_b += 1
            if arr[str+i][stc+j] != startw[i][j]:
                cnt_w += 1
            if cnt_w > result and cnt_b > result:
                tmp = 64
                return tmp
    tmp = min(cnt_w, cnt_b)
    return tmp
r, c = map(int,input().split())
arr = [input() for _ in range(r)]
startb = []
startw = []
result = 64

for i in range(8):
    if i%2 == 0:
        startb.append('BWBWBWBW')
    else:
        startb.append('WBWBWBWB')

for i in range(8):
    if i%2 == 0:
        startw.append('WBWBWBWB')
    else:
        startw.append('BWBWBWBW')

for i in range(r-7):
    for j in range(c-7):
        tmp1 = check(i,j)
        if tmp1 < result:
            result = tmp1
        if result == 0:
            break
    if result ==0:
        break
print(result)