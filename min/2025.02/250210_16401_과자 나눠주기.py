M, N = map(int, input().split())
snack = list(map(int, input().split()))

left = 1
right = max(snack)
ret = 0
while left <= right:
    mid = (left + right) // 2

    sm = sum(s // mid for s in snack)

    if sm >= M:
        ret = mid
        left = mid + 1
    else:
        right = mid - 1

print(ret)