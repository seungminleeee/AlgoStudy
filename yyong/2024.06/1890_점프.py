N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1
# time = 0

for i in range(N):
    for j in range(N):
        
        if (i == N-1 and j == N-1) or not dp[i][j]:
            continue

        # 행 이동
        if 0 <= i + board[i][j] < N:
            dp[i + board[i][j]][j] += dp[i][j]

        # 열 이동
        if 0 <= j + board[i][j] < N:
            dp[i][j + board[i][j]] += dp[i][j]

print(dp[N-1][N-1])

# print(time)
for line in dp:
    print(*line)
print('-----------')