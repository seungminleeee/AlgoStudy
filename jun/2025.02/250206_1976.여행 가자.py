"""
[BOJ] 1976번: 여행 가자 / 골드4
"""
def dfs(city):
    visited[city] = True
    for next_city in range(n):
        if arr[city][next_city] == 1 and visited[next_city] == False:
            dfs(next_city)

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
travel = list(map(int, input().split()))

visited = [0] * n
dfs(travel[0] - 1)

for city in travel:
    if not visited[city - 1]:
        print("NO")
        break

else:
    print("YES")