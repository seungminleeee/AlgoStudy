"""
[BOJ] 10546번: 배부른 마라토너 / 실버4
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())  # (1 ≤ N ≤ 10^5)
# 명단
entry = defaultdict(int)

# 참여자
for _ in range(n):
    entry[input()] += 1

# 완주자
for _ in range(n - 1):
    entry[input()] -= 1

# 완주 못한 사람 출력
for k, v in entry.items():
    if v == 1:
        print(k)
        break