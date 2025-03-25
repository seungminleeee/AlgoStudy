"""
[BOJ] 3178번: 양치기 꿍 / 실버1
"""
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(y, x):
    visited = [[False] * c for _ in range(r)]
    queue = deque([(y, x)])
    visited[y][x] = True

    cur_sheep = 0
    cur_wolf = 0

    if graph[y][x] == 'k':
        cur_sheep += 1
    else:
        cur_wolf += 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c:
                if graph[ny][nx] != '#' and not visited[ny][nx]:
                    visited[ny][nx] = True

                    if graph[ny][nx] == 'k':
                        cur_sheep += 1
                        graph[ny][nx] = '.'

                    elif graph[ny][nx] == 'v':
                        cur_wolf += 1
                        graph[ny][nx] = '.'

                    queue.append((ny, nx))

    if cur_sheep > cur_wolf:
        return cur_sheep, 0
    else:
        return 0, cur_wolf

r, c = map(int, input().split())  # (3 ≤ R, C ≤ 250)
graph = [list(input()) for _ in range(r)]

sheep = 0
wolf = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'k' or graph[i][j] == 'v':
            k, v = bfs(i, j)
            sheep += k
            wolf += v

print(sheep, wolf)