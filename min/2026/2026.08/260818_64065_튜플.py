def solution(s):
    S = list(map(str, s[2:-2].split("},{")))
    S.sort(key=lambda x: len(x))
    
    answer = []
    
    for st in S:
        st = list(map(int, st.split(",")))
        for k in st:
            if k not in answer:
                answer.append(k)
                
    return answer