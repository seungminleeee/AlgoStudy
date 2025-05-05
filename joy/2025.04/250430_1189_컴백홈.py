import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, dist):
    global cnt

    if (x, y) == (0, C - 1): # 오른쪽 위는 (0, 3) 임 
        if dist == K:
            cnt += 1
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny< C:
            if arr[nx][ny] != 'T' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = 0

R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = 0

visited[R - 1][0] = 1 # 왼쪽아래는 (2, 0) 임 
dfs(R - 1, 0, 1)

print(cnt)