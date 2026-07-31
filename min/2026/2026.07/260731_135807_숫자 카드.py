import math

def G(lst):
    g = max(lst)
    
    for l in lst:
        g = math.gcd(g, l)
    
    return g

def solution(arrayA, arrayB):
    A = G(arrayA)
    checkB = True
    for b in arrayB:
        if b % A == 0:
            checkB = False
            break
    
    B = G(arrayB)
    checkA = True
    for a in arrayA:
        if a % B == 0:
            checkA = False
            break
    
    if not checkA and not checkB:
        return 0
    elif not checkA:
        return A
    elif not checkB:
        return B
    else:
        return max(A, B)
    