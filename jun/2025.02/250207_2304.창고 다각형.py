n = int(input())
xy = sorted([tuple(map(int, input().split())) for _ in range(n)])
max_h = max(xy, key=lambda x: x[1])[1]
max_h_idx = 0

# 최대 높이의 기둥 위치 찾기
for i, (x, y) in enumerate(xy):
    if y == max_h:
        max_h_idx = i
        break

# 왼쪽에서 최대 높이까지 면적 계산
left_area = 0
current_height = xy[0][1]
for i in range(1, max_h_idx + 1):
    left_area += current_height * (xy[i][0] - xy[i-1][0])
    if xy[i][1] > current_height:
        current_height = xy[i][1]

# 오른쪽에서 최대 높이까지 면적 계산
right_area = 0
current_height = xy[-1][1]
for i in range(n - 2, max_h_idx - 1, -1):
    right_area += current_height * (xy[i+1][0] - xy[i][0])
    if xy[i][1] > current_height:
        current_height = xy[i][1]

# 최대 높이의 기둥 면적 추가
total_area = left_area + right_area + max_h

print(total_area)