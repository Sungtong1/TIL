import sys
input = sys.stdin.readline

n = int(input())
players = []
for i in range(n):
    players.append(input()[0])

first = set(players)
result = []
for i in first:
    if players.count(i) >= 5:
        result.append(i)

if result :
    print(''.join(sorted(result)))
else:
    print('PREDAJA')