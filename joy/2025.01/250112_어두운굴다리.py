N = int(input())
M = int(input())
light = list(map(int, input().split()))
 
gap = 0 # 일단 가로등 사이의 최대 거리를 구함 
for i in range(1, M):
    gap = max(gap, light[i] - light[i - 1])

first_gap = light[0] # 가로등 1번하고 처음시작 거리 구함
last_gap = N - light[-1] # 끝지점에서 가로등 M 번째 거리 구함

# 가로등 사이의 최대 거리를 가지고 있으니까 첫 시작 - 1번 가로등과의 거리와 M번째 가로등 - 끝 거리만 비교해 주면 됨
# 가로등 거리를 2로 나눈 부분을 비출 수 있음 .. ex 가로등 거리가 6이라면 3까지 비출 수 있음 
height = max((gap + 1) // 2, first_gap, last_gap) # 하지만 홀수일수도 있기 때문에 그냥 1을 더해주고 나눴다  
print(height)


