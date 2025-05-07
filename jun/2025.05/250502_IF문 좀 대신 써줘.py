"""
[BOJ] IF문 좀 대신 써줘 / 실버3
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

titles = []
limits = []

for _ in range(n):
    title, limit = input().split()
    titles.append(title)
    limits.append(int(limit))

powers = [int(input()) for _ in range(m)]

for power in powers:
    left = 0
    right = n - 1
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if power <= limits[mid]:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    print(titles[answer])