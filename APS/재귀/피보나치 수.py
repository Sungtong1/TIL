# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# n = int(input())
# print(fibonacci(n))

#memoization

def fibo1(n):

    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0,1]
print(fibo1(998))



#DP => 작은 부분의 해를 구해서 큰 해를 구한다

def fibo2(n) :
    f = [0,1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]


