import sys
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

def dfs(V, visited):
    visited[V] = 1
    print(V, end=' ')
    for i in graph[V]:
        if visited[i] == 0:
            dfs(i,visited)

visited = [0]*(N+1)
dfs(V, visited)
print()

def bfs(V, visited):
    queue = deque([V])
    visited[V] = 1

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if visited[i]==0:
                queue.append(i)
                visited[i] = 1

visited = [0]*(N+1)
bfs(V, visited)