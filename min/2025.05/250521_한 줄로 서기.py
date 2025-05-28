N = int(input())
arr = list(map(int, input().split()))

line = [0]*N

for i in range(N):
    k = arr[i]
    cnt = 0

    for j in range(N):
        if line[j] == 0:
            if cnt == k:
                line[j] = i+1
                break
            cnt += 1

print(*line)