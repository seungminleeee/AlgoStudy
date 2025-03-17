def solution(k, tangerine):
    tan = {}
    for i in tangerine:
        if i in tan:
            tan[i] += 1
        else:
            tan[i] = 1
    
    tanvalue = sorted(tan.values(), reverse = True)
    answer = 0
    count = 0
    for tanger in tanvalue:
        count += tanger
        answer += 1
        if count >= k:
            return answer 