"""
[BOJ] 20117번: 호반우 상인의 이상한 품질 계산법 / 실버1
"""
n = int(input())  # (1 ≤ N ≤ 100,000)
qualities = list(map(int, input().split()))
qualities.sort()

# 뒤에 큰 값들 합 구해서 곱하기 2
answer = sum(qualities[(n + 1) // 2:]) * 2

# 홀수 일때는 가운데 남는거 더해주기
if n % 2 == 1:
    answer += qualities[n // 2]

print(answer)