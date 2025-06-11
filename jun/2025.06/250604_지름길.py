"""
[BOJ] 지름길 / 실버1
"""
import heapq

n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]
distance = [float('inf')] * (d + 1)

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    start, end, length = map(int, input().split())

    if end <= d:
        graph[start].append((end, length))

heap = []
heapq.heappush(heap, (0, 0))
distance[0] = 0

while heap:
    dist, now = heapq.heappop(heap)

    if dist > distance[now]:
        continue

    for next_node, length in graph[now]:
        new_dist = dist + length
        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heapq.heappush(heap, (new_dist, next_node))

print(distance[d])