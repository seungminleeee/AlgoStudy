from collections import deque

def bfs(n):
    q = deque([(n, 0)])
    visited[n] = 1

    while q:
        curr, cnt = q.popleft()

        if bridge[curr] == 2:
            return cnt

        for next in [curr+1, curr-1, curr+A, curr-A, curr+B, curr-B, curr*A, curr*B]:
            if 0 <= next < 100001 and visited[next] == 0:
                q.append((next, cnt + 1))
                visited[next] = 1

A, B, N, M = map(int, input().split())

bridge = [0]*(100001)
bridge[N] = 1
bridge[M] = 2

visited = [0]*(100001)

ans = bfs(N)
print(ans)
