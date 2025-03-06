"""
[BOJ] 1261번: 알고스팟 / 골드4
"""
import heapq

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dijkstra():
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    count_grid = [[float('inf')] * m for _ in range(n)]
    count_grid[0][0] = 0

    while pq:
        count, y, x = heapq.heappop(pq)

        if (y, x) == (n - 1, m - 1):
            return count

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                new_count = count + grid[ny][nx]

                if new_count < count_grid[ny][nx]:
                    count_grid[ny][nx] = new_count
                    heapq.heappush(pq, (new_count, ny, nx))

m, n = map(int, input().split())  # (1 ≤ N, M ≤ 100)
grid = [list(map(int, input().strip())) for _ in range(n)]

print(dijkstra())