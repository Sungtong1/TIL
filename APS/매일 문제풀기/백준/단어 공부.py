import sys
input = sys.stdin.readline

word = input()
countList = [0] * 91

for i in word:
    if ord(i) == 10:
        continue
    countList[ord(i.upper())] += 1

maxCount = 0
for i in range(len(countList)):
    if countList[i] >= maxCount:
        maxCount = countList[i]
        result = chr(i)

count = 0
for i in range(len(countList)):
    if countList[i] == maxCount:
        count += 1

if count == 1:
    print(result)
else:
    print('?')
