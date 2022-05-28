origin = input()
if len(origin) == 1:
    origin = '0' + origin

result = 0
new = origin
while True:
    result += 1
    tmp = str(int(new[0]) + int(new[1]))
    if len(tmp) == 1:
        tmp = '0'+tmp
    new = new[1] + tmp[1]
    if new == origin:
        break

print(result)