"""
[BOJ] 2573번: 빙산 / 골4

조건:
1. 시간 제한 1초
2. 동서남북으로 바다가 둘러 싸면 싸여진 만큼 빙산 -1 씩
3. 두 덩어리로 나눠지는 최초 시간 구하기
4. 3 <= n, m <= 300

풀이:
1. bfs로 덩어리 탐색해서 덩어리 개수 세기
2. 덩어리 개수가 2 이상이면 최초 시간 출력 모두 녹으면 0
3. 두 조건이 아니면 빙산 녹이기
"""
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 빙산 탐색
def bfs(i, j, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] > 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))

# 덩어리 개수 세기
def cnt_iceberg():
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1
    return count

# 빙산 녹이기
def melt():
    melt_cnt = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                sea_count = 0
                for dy, dx in directions:
                    ny, nx = i + dy, j + dx
                    if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                        sea_count += 1
                melt_cnt[i][j] = sea_count

    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j] - melt_cnt[i][j])

time = 0
while True:
    cnt = cnt_iceberg()
    if cnt >= 2:
        print(time)
        break
    if cnt == 0:
        print(cnt)
        break
    melt()
    time += 1