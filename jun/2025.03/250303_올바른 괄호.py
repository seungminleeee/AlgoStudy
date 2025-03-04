"""
[PGS] 올바른 괄호 / LV2
"""
def solution(s):
    answer = False

    stack = []
    for parenthesis in s:
        if parenthesis == '(':
            stack.append(parenthesis)
        elif parenthesis == ')':
            if not stack:
                return False
            stack.pop()

    if not stack:
        answer = True

    return answer