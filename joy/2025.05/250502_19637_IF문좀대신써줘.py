import sys
input = sys.stdin.readline

N, M = map(int, input().split())
levels = []
points = []

for i in range(N):
    level, point = input().split()
    levels.append(level)
    points.append(int(point))

for i in range(M):
    score = int(input())
    left, right = 0, N - 1
    while left < right:
        mid = (left + right) // 2
        if score <= points[mid]:
            right = mid 
        else:
            left = mid + 1
    
    print(levels[left])

# N, M = map(int, input().split())
# titles = []
# for i in range(N):
#     level, point = input().split()
#     titles.append((level, int(point)))

# for i in range(M):
#     char_power = int(input())
#     for title, power in titles:
#         if char_power <= power:
#             print(title)
#             break