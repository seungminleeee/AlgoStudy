# 파이썬 31120 KB, 40 ms
# 파이파이 108080 KB, 108 ms

N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]  # [가로, 세로, 대각선]

dp[0][1][0] = 1  # 초기에 가로방향으로 하나 놓여있음

for r in range(N):
    for c in range(N):
        if room[r][c] == 1:
            continue
        
        # 가로방향
        if 0 <= c-1 < N:
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]

        # 세로방향
        if 0 <= r-1 < N:
            dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]

        # 대각선 방향
        if 0 <= r-1 < N and 0 <= c-1 < N and not room[r-1][c-1] and not room[r-1][c] and not room[r][c-1]:
            dp[r][c][2] += dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

print(sum(dp[N-1][N-1]))