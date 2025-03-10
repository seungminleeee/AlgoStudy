N = int(input())
INF = float('inf')
dp = [INF] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    for coin in [7, 5, 2, 1]:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[N])
