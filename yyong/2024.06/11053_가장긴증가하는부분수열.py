# 모르겠어서 LIS 알고리즘 검색해서 풀었음..
# 근데 이것도 N이 커지면 시간초과나서 이분탐색으로 푸는듯?

N = int(input())
numbers = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    dp[i] = 1

    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))