N = int(input())

point = []
for _ in range(N):
    x, y = map(int, input().split())
    point.append((x, y))

total = 0
for i in range(N-1):
    x1, y1 = point[i]
    x2, y2 = point[i+1]

    total += abs(x1-x2) + abs(y1-y2)

trash = 0
for i in range(1, N-1):
    x1, y1 = point[i]
    x2, y2 = point[i+1]
    x3, y3 = point[i-1]

    distance = (abs(x1-x2) + abs(y1-y2)) + (abs(x1-x3) + abs(y1-y3)) - (abs(x3-x2) + abs(y3-y2))

    trash = max(trash, distance)

print(total - trash)