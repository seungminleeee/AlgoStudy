# 파이썬 31120 KB, 208 ms

n, k = map(int, input().split())  # n가지 종류의 동전, 가치의 합이 k
coins = []

dp = [0] * (k+1)
dp[0] = 1  # 초기값 : 0원 만들수있는 경우의 수 1개

for _ in range(n):
    coin = int(input())
    for i in range(coin, k+1):  # 그 동전가치 이상부터
        dp[i] += dp[i-coin]     # 경우의 수 하나씩 추가

print(dp[k])
