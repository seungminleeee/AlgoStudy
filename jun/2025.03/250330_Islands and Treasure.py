"""
[NCD] Islands and Treasure / Mid
"""
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            y, x = queue.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == INF:
                    grid[ny][nx] = grid[y][x] + 1
                    queue.append((ny, nx))