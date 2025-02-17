def dfs(i):
    visited1[i] = 1
    print(i, end = " ")
    for next in range(1, N + 1):
        if visited1[next] == 0 and graph[i][next] == 1:
            dfs(next) 

def bfs(i):
    queue = []
    queue.append(i)
    visited2[i] = 1
    while queue:
        cur = queue.pop(0)
        print(cur, end = " ")
        for next in range(1, N + 1):
            if visited2[next] == 0 and graph[cur][next] == 1:
                visited2[next] = 1
                queue.append(next)

N, M, V = map(int, input().split())
visited1 = [0] * (N + 1)
visited2 = [0] * (N + 1)
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(V)
print()
bfs(V)