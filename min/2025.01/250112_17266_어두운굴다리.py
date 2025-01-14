import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
X = list(map(int, input().split()))
X.sort()

light_max = 0

if M == 1:
    light_max = max(X[0] - 0, N - X[0])
else:
    for i in range(M):
        if i == 0:
            diff = X[i] - 0
        elif i == M-1:
            diff = N - X[-1]
        else:
            diff = (X[i] - X[i-1] + 1) // 2
        light_max = max(light_max, diff)

print(light_max)