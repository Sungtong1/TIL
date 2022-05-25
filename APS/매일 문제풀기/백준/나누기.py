N = input()
F = int(input())
if F == 100:
    print('00')
else:
    nN = int(N[0:-2] + '00')

    for i in range(F+1):
        if (nN + i) % F == 0:
            if 0 <= i < 10:
                print('0'+str(i))
            else:
                print(i)
            break