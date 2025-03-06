"""
[BOJ] 2638번: 치즈 / 골드3
"""
from collections import deque

def air_contact(y, x):
    visited = [[0] * m for _ in range(n)]
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] == 0:
                visited[ny][nx] = True
                queue.append((ny, nx))
    return visited

def count_cheeze(visited):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                cnt = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if visited[ni][nj]:
                        cnt += 1
                count_grid[i][j] = cnt

def melt_cheeze():
    melted = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and count_grid[i][j] >= 2:
                grid[i][j] = 0
                melted = True
    return melted

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = map(int, input().split())  # (5 ≤ N, M ≤ 100)
grid = [list(map(int, input().split())) for _ in range(n)]
count_grid = [[0] * m for _ in range(n)]

time = 0
while True:
    # 공기 접촉
    contact = air_contact(0, 0)
    # 치즈 카운트
    count_cheeze(contact)
    # 녹이기
    if not melt_cheeze():
        break
    time += 1

print(time)