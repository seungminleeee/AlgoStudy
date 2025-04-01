"""
[BOJ] 10971번: 외판원 순회2 / 실버2
"""
def dfs(start, now, count, total):
    global answer

    if count == n:
        if grid[now][start] != 0:  # 도시 i에서 도시 j로 갈 수 없는 경우도 있으며
            answer = min(answer, total + grid[now][start])
        return

    for next in range(n):
        if not visited[next] and grid[now][next] != 0:
            visited[next] = True
            dfs(start, next, count + 1, total + grid[now][next])
            visited[next] = False

n = int(input())  # (2 ≤ N ≤ 10)
grid = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')

for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i, i, 1, 0)

print(answer)