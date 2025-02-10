"""
[BOJ] 16401번: 과자 나눠주기 / 실버2
"""
m, n = map(int, input().split())
cookies = list(map(int, input().split()))

answer = 0

# 이분 탐색
left, right = 1, max(cookies)
while left <= right:
    mid = (left + right) // 2
    # 가능한 과자 가짓 수
    cnt = sum(i // mid for i in cookies)

    # 가능 -> 더 긴 길이 탐색
    if cnt >= m:
        answer = mid
        left = mid + 1
    # 불가능 -> 더 짧은 길이 탐색
    else:
        right = mid - 1

print(answer)