import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    sheep = 0
    wolf = 0

    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()

        if arr[cx][cy] == 'k':
            sheep += 1
        elif arr[cx][cy] == 'v':
            wolf += 1

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy

            if 0<=nx<R and 0<=ny<C and arr[nx][ny] != '#' and visited[nx][ny] ==0:
                q.append((nx, ny))
                visited[nx][ny] = 1

    return sheep, wolf


R, C = map(int, input().strip().split())
# k : 양, v : 늑대
arr = [list(map(str, input().strip())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

sheep , wolf = 0, 0

for i in range(R):
    for j in range(C):
        if (arr[i][j] =='k' or arr[i][j] == 'v') and visited[i][j] == 0:
            s, w = bfs(i, j)

            if s > w:
                sheep += s
            else:
                wolf += w

print(sheep, wolf)
