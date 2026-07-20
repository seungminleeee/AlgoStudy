import sys
from collections import deque
input=sys.stdin.readline

def bfs(n):
    q = deque([n])
    visited = [0]*(N+1)
    visited[n] = 1
    cnt = 1

    while q:
        curr = q.popleft()

        for next in computer[curr]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1
                cnt += 2

    return cnt

N, M = map(int, input().strip().split())

computer = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().strip().split())
    computer[b].append(a)

mx_cnt = 0
lst = []
for i in range(1, N+1):
    cnt = bfs(i)
    mx_cnt = max(mx_cnt, cnt)
    lst.append([i, cnt])

ans = []
for j in range(N):
    if lst[j][1] == mx_cnt:
        ans.append(lst[j][0])

print(*ans)