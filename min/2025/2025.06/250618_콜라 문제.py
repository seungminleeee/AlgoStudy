def solution(a, b, n):
    ans = 0
    while n >= a:
        multi = n // a

        bottle = a * multi
        n -= bottle
        
        coke = multi * b
        n += coke
        ans += coke
    
    return ans