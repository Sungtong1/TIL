#https://www.youtube.com/watch?v=FYCGV6F1NuY&t=302s

def hanoi(n,start,target,sub):
    if n == 1:
        result.append((start,target))
        return
    hanoi(n-1,start,sub,target)
    result.append((start,target))
    hanoi(n-1,sub,target,start)

n = int(input())
result = []
hanoi(n,1,3,2)
print(len(result))
for i,j in result:
    print('{} {}'.format(i,j))