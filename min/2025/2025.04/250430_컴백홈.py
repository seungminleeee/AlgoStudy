def dfs(x, y, cnt):
    global ans
    if x == 0 and y == C-1:
        if cnt == K:
            ans += 1
        return

    visited[x][y] = 1
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = dx+x, dy+y
        if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and arr[nx][ny] == '.':
            dfs(nx, ny, cnt + 1)
    visited[x][y] = 0

R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]

ans = 0
visited = [[0]*C for _ in range(R)]
dfs(R-1, 0, 1)

print(ans)