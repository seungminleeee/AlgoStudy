import sys
input = sys.stdin.readline
from collections import deque

# 도착지점 구하는 함수
def goal():
    global start
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 2:
                arr[r][c] = 0
                start = (r, c)
                return

def bfs(i, j):
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((i, j))
    visited[i][j] = 1
    
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not visited[ni][nj]:
                arr[ni][nj] = arr[ni][nj] + arr[x][y]
                visited[ni][nj] = 1
                Q.append((ni, nj))
    return visited


N, M = map(int, input().split())  # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
start = (0, 0)
goal()
visited = bfs(start[0], start[1])
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1 and not visited[r][c]:
            arr[r][c] = -1

for line in arr:
    print(*line)