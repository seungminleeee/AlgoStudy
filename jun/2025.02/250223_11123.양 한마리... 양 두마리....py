"""
[BOJ] 11123번: 양 한마리... 양 두마리... / 실버2

- dfs(recursion error) -> bfs
"""
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(y, x):
    visited[y][x] = True
    queue = deque([(y, x)])

    while queue:
        y, x = queue.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                if grid[ny][nx] == '#':
                    visited[ny][nx] = True
                    queue.appendleft((ny, nx))

t = int(input())  # 0 < t <= 100

for _ in range(t):
    h, w = map(int, input().split())  # 0 < h, w <= 100
    grid = [list(map(str, input().strip())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                answer += 1

    print(answer)