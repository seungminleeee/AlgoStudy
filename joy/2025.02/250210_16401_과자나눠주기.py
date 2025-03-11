M, N = map(int, input().split())
arr = list(map(int, input().split()))
snack = 0
left, right = 1, max(arr)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid

    if cnt >= M:
        snack = mid
        left = mid + 1

    else:
        right = mid - 1
        
print(snack)
    