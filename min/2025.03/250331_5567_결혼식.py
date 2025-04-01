from collections import deque

def bfs(n):
    q = deque([(n, 0)])
    visited[n] = 0

    while q:
        curr, cnt = q.popleft()

        cnt += 1
        for i in friend[curr]:
            if visited[i] == -1:
                q.append((i, cnt))
                visited[i] = cnt


N = int(input())
M = int(input())

friend = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

visited = [-1]*(N+1)
bfs(1)

ans = 0
for v in range(1, N+1):
    if 1 <= visited[v] <= 2:
        ans += 1

print(ans)