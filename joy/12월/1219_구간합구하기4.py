N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N + 1)]
for i in range(N):
    prefix[i+1] = arr[i] + prefix[i]

for i in range(M):
    num1, num2 = map(int, input().split())
    print(prefix[num2] - prefix[num1-1])