T = int(input())
result = []
answer = ''
for i in range(T):
    result.append(input())

for i in range(len(result[0])):
    flag = True
    for j in range(T):
        if result[0][i] == result[j][i]:
            continue
        else:
            flag = False
    if flag:
        answer += result[0][i]
    else:
        answer += '?'

print(answer)