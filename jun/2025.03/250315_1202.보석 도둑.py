"""
[BOJ] 1202번: 보석 도둑 / 골드2
"""
import heapq, sys

input = sys.stdin.readline
n, k = map(int, input().split())

gems = []
for _ in range(n):
    m, v = map(int, input().split())
    gems.append((m, v))
gems.sort()

bags = []
for _ in range(k):
    c = int(input())
    bags.append(c)
bags.sort()

max_heap = []
answer = 0
idx = 0

for bag in bags:
    while idx < n and gems[idx][0] <= bag:
        heapq.heappush(max_heap, -gems[idx][1])
        idx += 1

    if max_heap:
        answer += -heapq.heappop(max_heap)

print(answer)