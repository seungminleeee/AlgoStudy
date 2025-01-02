import sys; sys.stdin = open('input.txt')

N = 10

mx = 0
sm = 0
for i in range(N):
    decrease, increase = map(int, input().split())
    sm = sm + increase - decrease

    if mx < sm:
        mx = sm

print(mx)