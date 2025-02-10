"""
[BOJ] 15486번: 퇴사2 / 골드5
"""
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

# 바텀업 DP
for i in range(n):
    t, p = arr[i]
    # 상담 했을 때
    if i + t <= n:
        dp[i + t] = max(dp[i + t], dp[i] + p)
    # 상담 안했을 때
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])