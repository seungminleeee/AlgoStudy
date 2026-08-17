from collections import deque

def solution(priorities, location):
    n = len(priorities)
    q = deque()
    for i in range(n):
        q.append(i)
    
    cnt = 0
    answer = -1
    mx = max(priorities)
    while q:
        curr = q.popleft()
        
        if priorities[curr] == mx:
            cnt += 1
            priorities[curr] = 0
            mx = max(priorities)
            
            if curr == location:
                answer = cnt
                break
        else:
            q.append(curr)
    
    return answer