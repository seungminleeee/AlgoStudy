def solution(prices):
    N = len(prices)
    
    answer = [0]*N
    stack = []
    for i in range(N):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i-idx
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = (N-1)-idx
    
    return answer