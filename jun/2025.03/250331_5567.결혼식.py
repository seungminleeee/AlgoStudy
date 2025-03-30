"""
[BOJ] 결혼식 / 실버2
"""
from collections import deque

n = int(input())
m = int(input())

friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [False] * (n + 1)
queue = deque([(1, 0)])
visited[1] = True
answer = 0

while queue:
    node, depth = queue.popleft()

    if depth >= 2:
        continue

    for friend in friends[node]:
        if not visited[friend]:
            visited[friend] = True
            queue.append((friend, depth + 1))
            answer += 1

print(answer)