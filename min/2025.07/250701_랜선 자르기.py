K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

left = 1
right = max(lan) + 1

while left < right:
    mid = (left + right) // 2

    cnt = 0
    for l in lan:
        cnt += l // mid

    if cnt >= N:
        left = mid + 1
    else:
        right = mid

print(left-1)