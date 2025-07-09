from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for i in range(n):
        
        if visited[i]:
            continue
            
        answer += 1
            
        q = deque([i])
        
        while q:
            j = q.popleft()
            
            for idx, next in enumerate(computers[j]):
                if next and not visited[idx]:
                    visited[idx] = True
                    q.append(idx)
    
    return answer