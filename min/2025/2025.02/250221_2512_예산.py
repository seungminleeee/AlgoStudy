N = int(input())
arr = list(map(int, input().split()))
M = int(input())

low = 0
high = max(arr)

while low <= high:
    mid = (low + high) // 2

    sm = sum(min(a, mid) for a in arr)

    if sm <= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)