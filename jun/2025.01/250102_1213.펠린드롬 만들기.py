"""
[BOJ] 1213번: 펠린드롬 만들기 / 실버3

조건:
1. 알파벳 대문자
2. 최대 50글자
3. 시간제한 2초 (2억 / 50하면 4백만, 최대기준 4백만까진 OK)
4. 펠린드롬 X -> I'm Sorry Hansoo

생각:
1. 순열로 풀면 시간복잡도 n!로 50!이 되기 때문에 시간 초과
2. 문자열 개수 세서 짝수면 패스, 홀수면 홀수 개 문자 최대 1개
3. 홀수 개 문자가 2개 이상이 되면 I'm Sorry Hansoo(펠린드롬 불가) 출력
4. 개수 세고 문자 조합하면 시간복잡도 O(n)으로 예상

풀이:
1. 각 알파벳 개수 세기
2. 홀수 알파벳 개수가 2개 이상이라면, I'm Sorry Hansoo 출력
3. 문자 사전 순으로 정렬
4. 모두 다 짝수라면 절반은 왼쪽에, 절반 역순으로 오른쪽으로
5. 홀수라면 위랑 똑같은데 한 가운데 홀수 알파벳 하나 두기
"""
from collections import Counter

def solve(name):
    count = Counter(name)
    odd_count = 0
    odd_char = ''
    for char, cnt in count.items():
        if cnt % 2 != 0:
            odd_count += 1
            odd_char = char
            if odd_count > 1:
                return "I'm Sorry Hansoo"

    half_name = []
    for char in sorted(count.keys()):
        half_name.append(char * (count[char] // 2))

    left_half = ''.join(half_name)
    if odd_count == 1:
        return left_half + odd_char + left_half[::-1]
    else:
        return left_half + left_half[::-1]

name = input().rstrip()
print(solve(name))