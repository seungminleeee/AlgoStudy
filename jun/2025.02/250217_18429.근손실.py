"""
[BOJ] 18429번: 근손실 / 실버3
"""
def dfs(day, weight):
    global answer

    if weight < 500:
        return

    if day == n:
        answer += 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(day + 1, weight + kits[i] - k)
            visited[i] = 0

n, k = map(int, input().split())
kits = list(map(int, input().split()))

answer = 0
visited = [0] * n
dfs(0, 500)
print(answer)