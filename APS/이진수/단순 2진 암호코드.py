my_code = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
}
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    flag = 0
    full_password = ''
    p = []
    result = 0
    password = [input() for _ in range(n)]
    for i in range(n):
        for j in range(m-1,-1,-1):
            if password[i][j] == '1':
                full_password = password[i][j-55 : j+1]
                flag =1
                break
        if flag ==1:
            break

    for i in range(8):
        tmp = full_password[i*7 : (i+1)*7]
        p.append(my_code[tmp])

    total = (p[0] + p[2] + p[4] + p[6]) * 3 + p[1] + p[3] + p[5] + p[7]
    if not total % 10:
        result = sum(p)
    print('#{} {}'.format(tc, result))