import sys
for _ in range(int(sys.stdin.readline())):
    t=(sys.stdin.readline())
    jagi=(int (t))**2
    jagi= jagi%(10**(len(t)-1))
    if jagi == int(t): print("YES")
    else: print("NO")