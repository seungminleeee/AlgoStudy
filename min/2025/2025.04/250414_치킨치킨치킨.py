def dfs(start, idx, lst):
    global ans

    if idx == 3:
        ans = max(satisfy(lst), ans)
        return

    for i in range(start, M):
        dfs(i+1, idx+1, lst+[i])

def satisfy(lst):
    person = [0]*N

    for p in range(N):
        for l in lst:
            person[p] = max(person[p], chicken[p][l])

    return sum(person)


N, M = map(int, input().split())
chicken = [list(map(int, input().split())) for _ in range(N)]

visited = [0]*M
ans = 0
dfs(0, 0, [])

print(ans)