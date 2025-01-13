"""
[BOJ] 1189번: 컴백홈 / 실1

조건:
1. 시간 제한 2초
2. 한 번 지나친 곳은 다시 방문 X
3. T는 가지 못하는 부분
4. RXC 맵에서 거리가 K인 가짓 수 구하는 문제
5. 1 <= R, C <= 5 / 1 <= K <= RXC

생각:
1. 그냥 dfs로 풀면 될듯 싶다.
"""
R, C, K = map(int, input().split())
graph = [input().strip() for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False] * C for _ in range(R)]
ans = 0

def dfs(x, y, distance):
    global ans

    if (x, y) == (0, C - 1) and distance == K:
        ans += 1
        return

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] == '.':
            visited[nx][ny] = True
            dfs(nx, ny, distance + 1)
            visited[nx][ny] = False

visited[R - 1][0] = True
dfs(R - 1, 0, 1)

print(ans)