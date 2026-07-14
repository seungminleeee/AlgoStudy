def dfs(idx, lst):
    if idx == N:
        func(lst)
        return

    for i in range(0, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx + 1, lst + [nums[i]])
            visited[i] = 0

def func(lst):
    global ans

    n = len(lst)

    ret = 0
    for k in range(0, n-1):
        ret += abs(lst[k] - lst[k+1])

    if ret > ans:
        ans = ret

N=int(input())
nums = list(map(int, input().split()))
visited = [0]*(N)
ans  = 0
dfs(0, [])

print(ans)