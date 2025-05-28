from collections import deque

def bfs(x, y):
    q = deque([(x, y, 0)])
    visited[x][y] = 0

    while q:
        cx, cy, depth = q.popleft()
        depth += 1
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = cx+dx, cy+dy

            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1 and visited[nx][ny] == -1:
                q.append((nx, ny, depth))
                visited[nx][ny] = depth

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i, j)
        elif arr[i][j] == 0:
            visited[i][j] = 0

for v in visited:
    print(*v)