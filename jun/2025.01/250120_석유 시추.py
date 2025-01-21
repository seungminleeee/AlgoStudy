"""
[PGS] 석유 시추 / LV2
"""
from collections import deque

def solution(land):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]

    # 각 열 석유 카운트 리스트
    oil_cnt = [0] * m

    def bfs(y, x):
        queue = deque([(y, x)])
        visited[y][x] = True
        cnt = 1

        # 석유 있는 열 체크를 위한 set
        oil_x = set()

        oil_x.add(x)

        while queue:
            y, x = queue.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and land[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    cnt += 1
                    oil_x.add(nx)

        # 해당 열에 석유 크기 추가
        for i in oil_x:
            oil_cnt[i] += cnt

    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                bfs(i, j)

    return max(oil_cnt)