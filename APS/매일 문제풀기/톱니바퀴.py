# 백준 톱니바퀴
cogwheel = []
for i in range(4):
    a = input()
    wheel = []
    for i in list(a):
        wheel.append(int(i))
    cogwheel.append(wheel)

turn = int(input())
for i in range(turn):
    idx, d = map(int, input().split())
    idx -= 1
    turn_cogwheel = []
    turn_cogwheel.append((idx,d))
    right_d = d
    right_idx = idx
    while True:
        if right_idx == 3:
            break
        next_wheel = right_idx + 1
        if cogwheel[right_idx][2] != cogwheel[next_wheel][6]:
            right_d *= -1
            turn_cogwheel.append((next_wheel,right_d))
            right_idx += 1
        else:
            break
    left_d = d
    left_idx = idx
    while True:
        if left_idx == 0:
            break
        prev = left_idx -1
        if cogwheel[left_idx][6] != cogwheel[prev][2]:
            left_d *= -1
            turn_cogwheel.append((prev,left_d))
            left_idx -= 1
        else:
            break
    # print(turn_cogwheel)
    for j in turn_cogwheel:
        if j[1] == 1:
            wheel_idx = j[0]
            tmp = cogwheel[wheel_idx][:]
            for i in range(8):
                cogwheel[wheel_idx][i] = tmp[(i-1)]
        if j[1] == -1:
            wheel_idx = j[0]
            tmp = cogwheel[wheel_idx][:]
            for i in range(8):
                cogwheel[wheel_idx][i] = tmp[(i+1)%8]
# print(cogwheel)
result = 0
for i in range(4):
    if cogwheel[i][0] == 1:
        result += 2**i
print(result)
