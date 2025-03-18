"""
[BOJ] 13702번: 이상한 술집 / 실버2
"""
n, k = map(int, input().split())
makgeolli = [int(input()) for _ in range(n)]

left = 1
right = max(makgeolli)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = sum(m // mid for m in makgeolli)

    if cnt >= k:
        answer = mid
        left = mid + 1

    else:
        right = mid - 1

print(answer)