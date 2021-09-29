p = []
x = input().split()
for i in range(len(x)):
    for j in range(len(x[i])):
        p.append(int(x[i][j]))

result = []
for i in range(len(p)//7):
    cnt = 0
    tmp = p[i*7 : (i+1)*7]
    for j in range(6,-1,-1):
        cnt += tmp[6-j] * (2**j)
    result.append(cnt)

print(', '.join(map(str, result)))