# 파이썬 34972 KB, 3116 ms
# 파이파이 110024 KB, 148 ms

N, K = map(int, input().split())  # N개의 물건, 가방 무게 한도 K
products = [list(map(int, input().split())) for _ in range(N)]  # 물건 무게 W, 물건 가치 V

dp = [0] * (K+1)

for w, v in products:
    for k in range(K, w-1, -1):
        dp[k] = max(dp[k-w] + v, dp[k])

print(dp[K])