N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

cnt = 1
tape = arr[0]

for i in range(1, N):
    if tape + L - 1 < arr[i]:
        tape = arr[i]
        cnt += 1

print(cnt)