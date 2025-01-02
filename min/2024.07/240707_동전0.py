# 메모리 31120 / 시간 40
N, K = map(int, input().split())
arr = []
for n in range(N):
    a = int(input())
    arr.append(a)

arr.sort(reverse=True)

coin = 0
for i in arr:
    if K == 0:
        break
    if i <= K:
        coin += K // i
        K %= i

print(coin)