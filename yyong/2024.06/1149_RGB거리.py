# 파이썬 31120 KB, 80 ms

N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)] # [N번째집][색깔]

dp = [[0] * 3 for _ in range(N)]

dp[0] = houses[0]

for i in range(1, N):
    
    # 빨간집
    dp[i][0] = houses[i][0] + min(dp[i-1][1], dp[i-1][2])

    # 초록집
    dp[i][1] = houses[i][1] + min(dp[i-1][0], dp[i-1][2])

    # 파란집
    dp[i][2] = houses[i][2] + min(dp[i-1][1], dp[i-1][0])

print(min(dp[N-1]))