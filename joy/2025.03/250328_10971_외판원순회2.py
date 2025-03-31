N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N 
min_cost = 21e8

def city(start, cur, cost, cnt):
    global min_cost

    if cnt == N:
        if arr[cur][start] != 0:
            min_cost = min(min_cost, cost + arr[cur][start])
        return 
    
    if cost >= min_cost:
        return
    
    for next in range(N):
        if visited[next] == 0 and arr[cur][next] != 0:
            visited[next] = 1
            city(start, next, cost + arr[cur][next], cnt + 1)
            visited[next] = 0

visited[0] = 1
city(0, 0, 0, 1)
print(min_cost)