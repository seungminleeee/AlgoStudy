import math

def prime_check(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def dfs(n, sm):
    if n == M:
        if prime_check(sm) == True:
            ans.add(sm)
        return

    for i in range(n, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, sm + H[i])
            visited[i] = 0


N, M = map(int,input().split())
H = list(map(int, input().split()))
ans = set()
visited = [0]*N

dfs(0,0)

if ans:
    ret = sorted(ans)
    print(*ret)
else:
    print(-1)