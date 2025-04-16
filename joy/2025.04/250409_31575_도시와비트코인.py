import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = 1

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                dfs(nx, ny)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
dx = [0, 1]
dy = [1, 0]


dfs(0, 0)

if visited[M - 1][N - 1]:
    print("Yes")
else:
    print("No")