"""
[BOJ] 13251번: 조약돌 꺼내기 / 실3

조건:
1. 시간 제한 2초
2. 돌 n개, 색상 1~m까지 중 하나
3. 랜덤하게 k개 뽑았을 때, 모두 같은 색일 확률 구하기
4. 1 <= m <= 50, 1 <= k <= n
"""
import math

def solve(m, n, k):
    all_v = sum(n)
    all_case = math.comb(all_v, k)

    specific_case = 0
    for i in n:
        specific_case += math.comb(i, k)

    return specific_case / all_case if all_case > 0 else 0.0

m = int(input())
n = list(map(int, input().split()))
k = int(input())
print(solve(m, n, k))