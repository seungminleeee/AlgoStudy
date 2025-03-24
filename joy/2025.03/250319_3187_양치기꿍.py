import sys 
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    global w, s
    visited[r][c] = 1

    if arr[r][c] == 'v':
        w += 1
    elif arr[r][c] == 'k':
        s += 1

    for i in range(4):
        nr, nc = r + dr[i] , c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and arr[nr][nc] != '#':
            dfs(nr, nc)


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
wolf = 0
sheep = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] != '#' and visited[i][j] == 0:
            w, s = 0, 0
            dfs(i, j)
            if s > w:
                sheep += s
            else:
                wolf += w

print(sheep, wolf)