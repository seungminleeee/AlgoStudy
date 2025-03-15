# 셋 중에 하나 선택하는데 같은 색에서 내려온거 말고 나머지 2개 중에 최솟값을 더해 기록. 쭉 채워나가서 제일 마지막에서 최솟값
# 처음에 백트래킹 생각했는데 ! 틀림 !! 

import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0] = house[0]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + house[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + house[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + house[i][2]

print(min(dp[N - 1]))