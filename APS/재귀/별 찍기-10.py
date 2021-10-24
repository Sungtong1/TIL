def star(n,my_list):
    result = []
    if n == 3:
        return my_list
    for i in my_list:
        result.append(i*3)
    for i in my_list:
        result.append(i + ' '*len(my_list) + i)
    for i in my_list:
        result.append(i*3)
    return star(n//3,result)

n = int(input())
origin = ['***','* *','***']
ans = star(n,origin)
for i in ans:
    print(i)