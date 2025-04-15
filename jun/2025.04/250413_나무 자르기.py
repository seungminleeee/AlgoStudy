"""
[BOJ] 나무 자르기 / 실버2
"""
n, m = map(int, input().split())  # (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
trees = list(map(int, input().split()))

trees.sort()

left = 0
right = trees[-1]
res = 0

while left <= right:
    mid = (left + right) // 2
    cnt = sum(tree - mid for tree in trees if tree > mid)

    if cnt >= m:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)