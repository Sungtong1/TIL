chess = []
result = 0
for i in range(8):
    chess.append(list(input()))

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0 and chess[i][j] == 'F':
            result += 1

print(result)