def dfs(n, lst):
    if len(lst) == N // 2:
        team(lst)
        return

    for i in range(n, N):
        dfs(i+1, lst + [i])

def team(lst):
    global ans

    start = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            start += powers[lst[i]][lst[j]] + powers[lst[j]][lst[i]]

    llst = list(set(range(N)) - set(lst))
    link = 0
    for i in range(len(llst)):
        for j in range(i+1, len(llst)):
            link += powers[llst[i]][llst[j]] + powers[llst[j]][llst[i]]

    ans = min(abs(start-link), ans)
    return

N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
dfs(0, [])

print(ans)