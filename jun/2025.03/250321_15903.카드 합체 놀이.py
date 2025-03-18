"""
[BOJ] 15903번: 카드 합체 놀이 / 실버1
"""
import heapq

n, m = map(int, input().split())  # (2 ≤ n ≤ 1,000) / (0 ≤ m ≤ 15×n)
cards = list(map(int, input().split()))
heapq.heapify(cards)

for i in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)

    temp = x + y
    heapq.heappush(cards, temp)
    heapq.heappush(cards, temp)

print(sum(cards))