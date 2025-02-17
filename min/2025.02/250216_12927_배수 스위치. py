switch = list(map(str, input()))
N = len(switch)

S = [-1] * (N+1)
for n in range(1, N+1):
    if switch[n-1] == 'Y':
        S[n] = 1
    else:
        S[n] = 0

cnt = 0
for i in range(1, N+1):
    if S[i] == 1:
        cnt += 1

        for m in range(i, N+1, i):
            S[m] = (S[m] + 1) % 2

print(cnt)