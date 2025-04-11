"""
[BOJ] 도시와 비트코인 / 실버3
"""
from collections import deque

def bfs():
    visited = [[False] * n for _ in range(m)]
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        y, x = q.popleft()

        if y == m - 1 and x == n - 1:
            return 'Yes'

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and graph[ny][nx] != 0:
                visited[ny][nx] = True
                q.append((ny, nx))
    return 'No'

directions = [(0, 1), (1, 0)]

n, m = map(int, input().split())  # 1 <= N, M <= 300
graph = [list(map(int, input().split())) for _ in range(m)]

print(bfs())