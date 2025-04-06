import sys
from collections import deque

input = sys.stdin.readline
      
def bfs(start):
    queue = deque([start])
    visited = [0] * (N + 1)
    visited[start] = 1
    cnt = 1
    
    while queue:
        com = queue.popleft()
        for next in graph[com]:
            if visited[next] == 0:
                visited[next] = 1
                queue.append(next)
                cnt += 1
    return cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[y].append(x)

result = [0] * (N + 1)
max_value = 0

for i in range(1, N + 1): 
    result[i] = bfs(i)
    max_value = max(max_value, result[i])

for i in range(1, N + 1):
    if result[i] == max_value:
        print(i, end=" ")


# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# def dfs(idx):
#     visited[idx] = 1
#     cnt = 1

#     for next in graph[idx]:
#         if visited[next] == 0:
#             cnt += dfs(next)
    
#     return cnt         

# N, M = map(int, input().split())
# graph = [[] for _ in range(N + 1)]
# for i in range(M):
#     x, y = map(int, input().split())
#     graph[y].append(x)

# result = [0] * (N + 1)
# for i in range(1, N + 1): 
#     visited = [0] * (N + 1)
#     result[i] = dfs(i)

# max_value = max(result)

# for i in range(1, N + 1):
#     if result[i] == max_value:
#         print(i, end=" ")