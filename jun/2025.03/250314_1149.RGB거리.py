"""
[BOJ] 1149번: RGB거리 / 실버1
"""
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0] = grid[0]

for i in range(1, n):
    dp[i][0] = grid[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = grid[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = grid[i][2] + min(dp[i - 1][1], dp[i - 1][0])

print(min(dp[-1]))