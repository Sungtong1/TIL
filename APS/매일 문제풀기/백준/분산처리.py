for tc in range(int(input())):
    a, b = map(int,input().split())
    c = a%10

    if c == 0:
        print(10)
    elif c in [1,5,6]:
        print(c)
    elif c in [4,9]:
        d = b%2
        if d :
            print(c)
        else:
            print(c**2%10)
    else :
        d = b%4
        if d == 0:
            print(c**4%10)
        else :
            print(c**d%10)
    # A가 0 부터 10 사이일 때 각각 제곱해서 나올 수 있는 첫자리 수들
    # 1 -> 1
    # 2 4 8 16 32 64 -> 2 4 8 6
    # 3 9 27 81 243 -> 3 9 7 1
    # 4 16 64 -> 4
    # 5 25 125 -> 5
    # 6 36 -> 6
    # 7 9 3 1 7 -> 7 9 3 1
    # 8 4 2 6 8 -> 8 4 2 6
    # 9 1 9 -> 9 1 9
    # 10 0 -> 0
