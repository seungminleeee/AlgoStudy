import sys

N, K = map(int, input().split())
table = list(map(str, sys.stdin.readline().strip()))

cnt = 0
for i in range(N):
    if table[i] == 'P':
        for j in range(-K, K+1):
            pos = i+j
            if 0 <= pos < N and table[pos] == 'H':
                table[pos] = 'X'
                cnt += 1
                break
print(cnt)