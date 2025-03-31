def solution(prices):
    n = len(prices)
    stack = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            stack[i] += 1  
            if prices[i] > prices[j]:
                break
                     
    return stack

# 효율성 시간초과나넹 ..
# def solution(prices):
#     stack = []
#     n = len(prices)
#     for i in range(n):
#         cnt = 0
#         prices[i]
#         new = prices[i+1:]
#         for j in range(len(new)):
#             cnt += 1
#             if prices[i] > new[j]:
#                 break
#         stack.append(cnt)
    
#     return stack