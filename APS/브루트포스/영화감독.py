n = int(input())
num = '666'
cnt = 0
while True:
    if '666' in num:
        cnt += 1
    if cnt == n:
        break
    num = str(int(num)+1)

print(num)

