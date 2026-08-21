def solution(n):
    answer = 0
    
    def dfs(start, sm):
        nonlocal answer
        
        if sm >= n:
            if sm == n:
                answer += 1
            return
        if start > n:
            return
        
        dfs(start + 1, sm + start)
    
    for i in range(1, n+1):
        dfs(i, 0)
    
    return answer