def solution(brown, yellow):
    answer = []
    found = False
    
    # 브라운 최대 5000이므로 길이는 반값이 최대
    for x in range(2500):
        for y in range(2500):
            
            # 조건 맞으면 break
            if x * y == brown + yellow and 2 * (x + y - 2) == brown and (x-2) * (y-2) == yellow and x >= y:
                answer.append(x)
                answer.append(y)
                found = True

            if found:
                break
        if found:
            break
            
    return answer