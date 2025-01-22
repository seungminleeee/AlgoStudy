"""
[BOJ] 11652번: 카드 / 실4

조건:
1. 시간 제한 1초
2. -2^62 <= card <= 2^62
3. 카드가 주어 졌을 때, 가장 많이 가지고 있는 정수를 구하라.
4. 최대가 여러 개라면 작은 것을 출력.
5. 1 <= n <= 100,000

풀이:
1. 숫자 개수를 센다.
2. 람다로 가장 많은 것과 같을 경우 작은거 순으로 정렬을 한다.
3. 첫번 째 값을 출력.

시간복잡도 n(for문) + n log n(정렬) 예상
"""
from collections import defaultdict

n = int(input())
cnt = defaultdict(int)

for _ in range(n):
    card = int(input())
    cnt[card] += 1

cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

print(cnt[0][0])