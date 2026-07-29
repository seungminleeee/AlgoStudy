def solution(elements):
    e = elements + elements
    
    sm = set()
    for i in range(1, len(elements)+1):
        for start in range(len(elements)):
            sm.add(sum(e[start: start+i]))

    return len(sm)