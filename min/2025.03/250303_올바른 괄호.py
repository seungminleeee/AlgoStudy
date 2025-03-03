def solution(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                top = stack.pop()
                if top == ')':
                    continue
            else:
                return False
    
    if stack:
        return False
    else:
        return True