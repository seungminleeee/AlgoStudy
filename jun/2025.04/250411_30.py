"""
[BOJ] 30 / 실버4
"""
n = input().strip()  # 최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

if '0' not in n:
    print(-1)
else:
    num = list(map(int, n))

    if sum(num) % 3 != 0:
        print(-1)
    else:
        num.sort(reverse=True)
        print(''.join(map(str, num)))