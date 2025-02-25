"""
[BOJ] 2422번: 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 / 실버4
"""
n, m = map(int, input().split())  # (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)
icecream = set()
for _ in range(m):
    a, b = map(int, input().split())
    icecream.add((a, b))
    icecream.add((b, a))

count = 0
# 조합 찾기
for a in range(1, n - 1):
    for b in range(a + 1, n):
        for c in range(b + 1, n + 1):
            # 안되는 조합에 있으면 다음
            if (a, b) in icecream or (b, c) in icecream or (a, c) in icecream:
                continue
            count += 1

print(count)