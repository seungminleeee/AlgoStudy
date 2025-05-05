import sys
input = sys.stdin.readline

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

N = int(input())
point = []
result = 0
for i in range(N):
    x, y = map(int, input().split())
    point.append((x, y))

# 전체 이동 거리
total_dist = 0
for i in range(1, N):
    total_dist += manhattan(point[i-1], point[i])

# 포인트 하나 뺀 거 최소거리
save_dist = 0
for i in range(1, N - 1):
    result = manhattan(point[i - 1], point[i + 1])
    origin = manhattan(point[i - 1], point[i]) + manhattan(point[i], point[i + 1])
    save = origin - result
    save_dist = max(save_dist, save)

print(total_dist - save_dist)