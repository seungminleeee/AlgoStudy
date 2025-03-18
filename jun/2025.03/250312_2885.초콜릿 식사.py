"""
[BOJ] 2888번: 초콜릿 식사 / 실버2
"""
k = int(input())  # (1 ≤ K ≤ 1,000,000)

chocolate = 1
while chocolate < k:
    chocolate *= 2

check = chocolate
answer = 0
while k % check != 0:
    check //= 2
    answer += 1

print(chocolate, answer)