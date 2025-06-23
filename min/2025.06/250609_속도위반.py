N, M = map(int, input().split())
road = [0]*101
start = 0
for _ in range(N):
    interval, speed = map(int, input().split())

    for i in range(start + 1, start + interval + 1):
        road[i] = speed

    start = start + interval

yj = 0
mx = 0
for _ in range(M):
    interval, speed = map(int, input().split())

    Y = yj + interval
    for k in range(yj+1, Y+1):
        if speed > road[k]:
            mx = max(speed-road[k], mx)

    yj = Y


print(mx)