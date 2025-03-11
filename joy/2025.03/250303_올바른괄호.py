def solution(s):
    stack = []
    result = True
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                result = False
                return result
    if stack:
        result = False
        return result
    
    return result
