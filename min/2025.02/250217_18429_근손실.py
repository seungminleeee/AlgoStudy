N, K = map(int,input().split())
A = list(map(int, input().split()))
visited = [0] * N

def dfs(n, lst, weight):
    global cnt
    if n == N:
        ans.append(lst)
        cnt += 1
        return

    for i in range(N):
        if visited[i] == 0:
            n_weight = weight + A[i] - K
            if n_weight >= 500:
                visited[i] = 1
                dfs(n+1, lst+[i], n_weight)
                visited[i] = 0


ans = []
cnt = 0
dfs(0, [], 500)

print(len(ans))