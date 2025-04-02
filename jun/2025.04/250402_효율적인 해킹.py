"""
[BOJ] 효율적인 해킹 / 실버1
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])
    count = 0

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                count += 1

    return count

n, m = map(int, input().split())  # N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

res = []
max_count = -1

for i in range(1, n + 1):
    count = bfs(i)

    if count > max_count:
        max_count = count
        res = [i]

    elif count == max_count:
        res.append(i)

print(*sorted(res))