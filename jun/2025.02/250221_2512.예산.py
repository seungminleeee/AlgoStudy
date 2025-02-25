"""
[BOJ] 2512번: 예산 / 실버2
"""
n = int(input()) # 3 <= n <= 10,000
budget = sorted(list(map(int, input().split()))) # 1 <= budget <= 100,000
total_budget = int(input()) # n <= total_budget <= 1,000,000,000

# 모든 요청이 배정될 수 있는 경우 요청한 금액 그대로 배정
if total_budget >= sum(budget):
    print(budget[-1])

# 모든 요청이 배정될 수 없는 경우
else:
    # 상한액 구하기
    total = 0
    rest = n
    temp = 0
    for i in range(n):
        # 예산 적정 시 다음 예산으로 넘기기
        if total_budget >= total + (budget[i] * rest):
            total += budget[i]
            rest -= 1

        # 예산 초과 시 상한액 구할 때까지 -1씩 줄이기
        else:
            temp = budget[i]
            while total_budget < total + (temp * rest):
                temp -= 1

            print(temp)
            break