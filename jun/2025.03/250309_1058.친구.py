"""
[BOJ] 1058번: 친구 / 실버2
"""
from collections import deque

def bfs(i):
    visited = [False] * n
    queue = deque([(i, 0)])
    visited[i] = True
    friends = set()

    while queue:
        current, depth = queue.popleft()

        for next in graph[current]:
            if not visited[next]:
                friends.add(next)
                # 친구의 친구 까지만
                if depth < 1:
                    queue.append((next, depth + 1))
                    visited[next] = True

    return len(friends)

n = int(input())  # 50보다 작거나 같은 자연수

graph = [[] for _ in range(n)]
for i in range(n):
    isFriend = input()
    for j in range(n):
        if isFriend[j] == 'Y':
            graph[i].append(j)

answer = max(bfs(i) for i in range(n))
print(answer)