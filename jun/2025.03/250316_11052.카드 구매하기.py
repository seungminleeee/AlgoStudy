"""
[BOJ] 11052번: 카드 구매하기 / 실버1
"""
n = int(input())  # (1 ≤ N ≤ 1,000)
cards = list(map(int, input().split()))
cards.insert(0, 0)

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], cards[j] + dp[i - j])

print(dp[n])