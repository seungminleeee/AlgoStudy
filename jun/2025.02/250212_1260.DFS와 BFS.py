"""
[BOJ] 1260번: DFS와 BFS / 실버2

1. dfs와 bfs로 탐색한 결과 출력
"""
from collections import deque

def dfs(v):
    dfs_visited[v] = 1
    print(v, end=" ")
    for next_node in sorted(graph[v]):
        if not dfs_visited[next_node]:
            dfs(next_node)

def bfs(v):
    queue = deque([v])
    bfs_visited[v] = 1
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for next_node in sorted(graph[node]):
            if not bfs_visited[next_node]:
                queue.append(next_node)
                bfs_visited[next_node] = 1

n, m, v = map(int, input().split())

# 인접 리스트 생성
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)

dfs(v)
print()
bfs(v)