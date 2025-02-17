"""
[PGS] 괄호 변환 / LV2
"""
from collections import deque


# 균형잡힌 괄호 문자열 체크
def correct_string(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True


# u, v로 분리
def separate_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = '', ''

    while queue:
        char = queue.popleft()
        u += char

        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = ''.join(queue)
    return u, v


# 문자열 뒤집기
def reverse_string(string):
    reversed_string = ''
    for i in string:
        if i == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string


# 올바른 괄호 문자열로 변환
def change_string(string):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if string == '':
        return ''

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = separate_u_v(string)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if correct_string(u):
        return u + change_string(v)

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    #   4-3. ')'를 다시 붙입니다.
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    #   4-5. 생성된 문자열을 반환합니다.
    else:
        return "(" + change_string(v) + ")" + reverse_string(u[1:-1])


def solution(p):
    # 만약 p가 이미 "올바른 괄호 문자열"이라면 그대로 return 하면 됩니다.
    if correct_string(p):
        return p

    # "올바른 괄호 문자열"로 변환한 결과를 return
    else:
        return change_string(p)