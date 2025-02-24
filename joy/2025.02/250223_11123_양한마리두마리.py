import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r, c):
    sheep[r][c] = 0
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < H and 0 <= nc < W and sheep[nr][nc] == '#':
            dfs(nr, nc)

T = int(input())
for _ in range(1, T + 1):
    H, W = map(int, input().split())
    sheep = [list(input()) for _ in range(H)]
    cnt = 0

    dr = [0, 1, 0, -1] # 우하좌상
    dc = [1, 0, -1, 0]

    for i in range(H):
        for j in range(W):
            if sheep[i][j] == '#':
                dfs(i, j)
                cnt += 1

    print(cnt)