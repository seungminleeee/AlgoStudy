def dfs(start, now, cnt, cost):
    global ans
    if cnt == N and city[now][start] != 0:
        ans = min(ans, cost + city[now][start])
        return

    for i in range(N):
        if visited[i] == 0 and city[now][i] != 0:
            visited[i] = 1
            dfs(start, i, cnt+1, cost + city[now][i])
            visited[i] = 0

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]

visited = [0]*N
ans = float('inf')

for i in range(N):
    visited[i] = 1
    dfs(i, i, 1, 0)
    visited[i] = 0

print(ans)