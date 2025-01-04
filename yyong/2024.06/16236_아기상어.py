# 파이썬 35680 KB, 164 ms
# 파이파이 120924 KB, 188 ms

from collections import deque

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
baby_shark = 2   # 아기상어 크기
feed = 0
time = 0

# 아기상어 위치
for a in range(N):
    for b in range(N):
        if sea[a][b] == 9:
            baby_shark_spot = (a, b)
            sea[a][b] = 0


# 아기상어 먹이찾기
def hunting(x, y):  # 아기상어 위치 xy
    global feed, baby_shark, time

    visited = [[0] * N for _ in range(N)]
    Q = deque([(0, x, y)])  # 거리, 위치xy
    visited[x][y] = 1
    small_fish = []

    while Q:
        d, cx, cy = Q.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and sea[nx][ny] <= baby_shark:

                visited[nx][ny] = 1
                Q.append((d+1, nx, ny))
                    
                # 잡아먹을 수 있으면 small_fish에 append
                if 0 < sea[nx][ny] < baby_shark:
                    small_fish.append((d+1, nx, ny))

    # 만약 small_fish가 비어있으면 return time
    if small_fish == []:
        return
    
    else:
        # 그렇지 않으면 small_fish 정렬 (거리 우선순위)하고 잡아먹기
        small_fish.sort(key=lambda x: (x[0], x[1], x[2]))

        feed_fish = small_fish[0]
        sea[feed_fish[1]][feed_fish[2]] = 0
        time += feed_fish[0]
        feed += 1

        if feed == baby_shark:
            baby_shark += 1
            feed = 0

        hunting(feed_fish[1], feed_fish[2])


hunting(baby_shark_spot[0], baby_shark_spot[1])

print(time)
