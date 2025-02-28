"""
[BOJ] 2151번: 거울 설치 / 골드3
"""
import heapq

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(n, start, end, grid):
    pq = []
    # 거울 개수 저장
    mirrors = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]

    for d in range(4):
        # 시작은 모든 방향
        heapq.heappush(pq, (0, start[0], start[1], d))
        # 문에는 거울 없음
        mirrors[start[0]][start[1]][d] = 0

    # 최단 + 가중이기에 다익스트라 사용
    while pq:
        mirror_count, y, x, direction = heapq.heappop(pq)

        # 현재 이미 최소가 아니면 스킵
        if mirror_count > mirrors[y][x][direction]:
            continue

        # 도착 하면 리턴
        if (y, x) == end:
            return mirror_count

        dy, dx = directions[direction]
        ny, nx = y + dy, x + dx

        if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] != '*':
            # 다음 위치가 거울 설치 가능 위치면 반사
            if grid[ny][nx] == '!':
                for new_dir in range(4):
                    new_count = mirror_count
                    if new_dir != direction:
                        new_count += 1

                    if new_count < mirrors[ny][nx][new_dir]:
                        mirrors[ny][nx][new_dir] = new_count
                        heapq.heappush(pq, (new_count, ny, nx, new_dir))

            # ! 아니면 방향 유지
            else:
                if mirror_count < mirrors[ny][nx][direction]:
                    mirrors[ny][nx][direction] = mirror_count
                    heapq.heappush(pq, (mirror_count, ny, nx, direction))

n = int(input())  # (2 ≤ N ≤ 50)
grid = [list(input().strip()) for _ in range(n)]
doors = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == '#': doors.append((i, j))

# 문은 항상 두 곳
door1, door2 = doors[0], doors[1]

print(bfs(n, door1, door2, grid))