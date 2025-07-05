def dfs(n, prev, lst):
    global ans
    if n == N:
        ans += 1
        return

    for i in range(N):
        if visited[i]:
            continue
        if i > 0 and S[i] == S[i-1] and visited[i-1] == 0:
            continue
        if prev == S[i]:
            continue
        visited[i] = 1
        dfs(n+1, S[i], lst+[S[i]])
        visited[i] = 0

S = list(input())
S.sort()
N = len(S)

visited = [0]*N
ans = 0

dfs(0, "", [])
print(ans)