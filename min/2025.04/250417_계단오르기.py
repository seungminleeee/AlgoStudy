N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]

dp = [0]*(N+1)

for i in range(1, N+1):
    if i == 1:
        dp[i] = stairs[1]
    elif i == 2:
        dp[i] = stairs[1] + stairs[2]
    elif i == 3:
        dp[i] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])
    else:
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[N])