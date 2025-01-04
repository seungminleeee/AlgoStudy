# 아이디어 문어 박사 보고 배움...
# 문어박사 dp 기본문제 몇개 듣고 푸니까 좋은거같아

N = int(input())
stairs = [0] * (N + 1)

for i in range(1, N + 1):
    stairs[i] = int(input())

dp = [[0] * (N + 1) for _ in range(3)]

for j in range(1, N + 1):

    # j번째 계단 안밟음 : j-1에서 한번밟은거, 연속 밟은거 중에 최댓값
    dp[0][j] = max(dp[1][j-1], dp[2][j-1])

    # j번째 계단 한번밟음 : j-1에서 안밟은 dp + 현재 계단
    dp[1][j] = dp[0][j-1] + stairs[j]

    # j번째 계단 연속밟음 : j-1에서 한번 밟은 dp + 현재 계단
    dp[2][j] = dp[1][j-1] + stairs[j]

# 결과 = N번째 계단 밟은 경우 중(dp[1][N], dp[2][N]) max
print(max(dp[1][N], dp[2][N]))