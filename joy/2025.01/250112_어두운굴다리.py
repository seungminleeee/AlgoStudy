N = int(input())
M = int(input())
light = list(map(int, input().split()))
 
gap = 0 
for i in range(1, M):
    gap = max(gap, light[i] - light[i - 1])

first_gap = light[0]
last_gap = N - light[-1]

height = max((gap + 1) // 2, first_gap, last_gap)
print(height)


