"""
[BOJ] 13144번: List of Unique Numbers / 골드4
"""
from collections import defaultdict

n = int(input())  # (1 ≤ N ≤ 100,000)
sequence = list(map(int, input().split()))

left, right = 0, 0
num_count = defaultdict(int)
answer = 0

# 투 포인터
while right < n:
    # 새로운 값 추가
    num_count[sequence[right]] += 1

    # 만약 중복이면 left 이동시키고 중복 제거
    while num_count[sequence[right]] > 1:
        num_count[sequence[left]] -= 1
        left += 1

    # 수열 개수 추가
    answer += (right - left + 1)
    # 계속 오른쪽으로
    right += 1

print(answer)