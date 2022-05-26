x, y, w, h = map(int, input().split())

xtoe = abs(x-w)
xtos = abs(x-0)
ytoe = abs(y-h)
ytos = abs(y-0)

result = min(xtoe, xtos, ytoe, ytos)

print(result)