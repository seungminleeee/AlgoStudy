from collections import deque

def bfs(n):
    q = deque([(n, 0)])
    visited[n] = 0

    while q:
        curr, cnt = q.popleft()

        if curr == N-1:
            return cnt

        for i in range(1, maze[curr]+1):
            next = curr + i
            if next < N and visited[next] == -1:
                q.append((next, cnt + 1))
                visited[next] = cnt + 1

    return -1

N = int(input())
maze = list(map(int, input().split()))

visited = [-1]*N
ans = bfs(0)

print(ans)