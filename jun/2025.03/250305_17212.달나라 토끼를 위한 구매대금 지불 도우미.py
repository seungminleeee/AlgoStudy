"""
[BOJ] 17212번: 달나라 토끼를 위한 구매대금 지불 도우미 / 실버3
"""
n = int(input())  # (0 ≤ N ≤ 100,000)

coins = [1, 2, 5, 7]
dp = [float('inf')] * (n + 1)
dp[0] = 0

# 바텀업
for i in range(1, n + 1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[n])