N = int(input())
ans = -1

for i in range(N // 5, -1, -1):
    r = N - 5*i
    if r % 2 == 0:
        ans = i + r // 2
        break

print(ans)