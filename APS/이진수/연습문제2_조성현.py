sixteen = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
p = []
input_str = ''
x = input()
for i in x:
    input_str += sixteen[i]
for j in input_str:
    p.append(int(j))

result = []
for i in range(len(p)//7 +1):
    cnt = 0
    tmp = p[i*7 : (i+1)*7]
    if len(tmp) != 7:
        t = len(tmp)
        for j in range(t-1,-1,-1):
            cnt += tmp[t-1-j] * (2**j)
    else:
        for j in range(6,-1,-1):
            cnt += tmp[6-j] * (2**j)
    result.append(cnt)

print(', '.join(map(str, result)))
