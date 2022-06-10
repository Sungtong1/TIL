N = int(input())
pictures = []
minimum = 36
ans1 = ans2 = 0

for i in range(N):
    row = []  # i+1 번째 그림의 행
    for _ in range(5):
        row.append(input())
    pictures.append(row)

for pic1 in range(N):
    for pic2 in range(pic1 + 1, N):
        cnt = 0
        for r in range(5):
            for c in range(7):
                # 그림이 다르다면
                if pictures[pic1][r][c] != pictures[pic2][r][c]:
                    cnt += 1
        # 이 때까지의 비교 중 가장 비슷하다면 다른 칸 개수, 그림 2개 저장
        if minimum > cnt:
            minimum = cnt
            ans1 = pic1
            ans2 = pic2

print(f'{ans1 + 1} {ans2 + 1}')