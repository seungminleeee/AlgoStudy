from collections import deque

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(H)]

    visited = [[0]*W for _ in range(H)]

    def bfs(x, y):
        q = deque([(x,y)])
        visited[x][y] = 1

        while q:
            cx, cy = q.popleft()

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = cx + dx, cy + dy

                if 0<=nx<H and 0<=ny<W:
                    if visited[nx][ny] == 0 and arr[nx][ny] == '#':
                        q.append((nx, ny))
                        visited[nx][ny] = 1

    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)

    print(cnt)