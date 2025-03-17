from collections import Counter

def solution(k, tangerine):
    N = len(tangerine)
    tan_cnt = Counter(tangerine)
    
    tan_cnt = sorted(tan_cnt.items(), key=lambda x:-x[1])
    
    cnt = 0
    answer = 0
    for t in tan_cnt:
        cnt += t[1]
        answer += 1
        
        if cnt >= k:
            break
    
    return answer 
    