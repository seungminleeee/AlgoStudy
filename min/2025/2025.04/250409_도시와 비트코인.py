from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()

        if cx == M-1 and cy == N-1:
            return 'Yes'

        for dx, dy in [(1, 0), (0, 1)]:
            nx, ny = cx+dx, cy+dy

            if 0<=nx<M and 0<=ny<N and city[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

    return 'No'

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(M)]

visited = [[0]*N for _ in range(M)]

print(bfs(0, 0))