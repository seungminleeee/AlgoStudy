# 메모리31120	시간40

N = int(input())

ans = 0
if N == 0:
    print(ans)
else:
    for i in range(N, 0, -1):
        num = i
        while num % 5 == 0:
            ans += 1
            num //= 5
    print(ans)