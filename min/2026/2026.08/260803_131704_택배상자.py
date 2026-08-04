def solution(order):
    N = len(order)
    
    truck = []
    stack = []
    idx = 0
    
    for i in range(1, N+1):
        stack.append(i)
        while stack and stack[-1] == order[idx]:
            truck.append(stack.pop())
            idx += 1
    
    return len(truck)