from collections import deque

def bfs(n):
    q = deque([n])
    cnt = 0
    visited[n] = 1

    while q:
        curr = q.popleft()

        for next in graph[curr]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1
                cnt += 1

    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0]*(N+1)

    ans = bfs(1)
    print(ans)