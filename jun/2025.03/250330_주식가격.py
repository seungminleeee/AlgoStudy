"""
[PGS] 주식가격 / LV2
"""
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for idx, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            stack_idx = stack.pop()
            answer[stack_idx] = idx - stack_idx
        stack.append(idx)

    while stack:
        stack_idx = stack.pop()
        answer[stack_idx] = n - 1 - stack_idx

    return answer