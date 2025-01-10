R, C, T = map(int, input().split())  # 세로, 가로, 시간
room = [list(map(int, input().split())) for _ in range(R)]

di = [-1, 0, 1, 0]  # 위 오 아 왼
dj = [0, 1, 0, -1]

# 공기청정기 위치 찾기
air_cleaner = 0

for a in range(2, R):
    if room[a][0] == -1:
        air_cleaner = a
        break

# 공기청정기 매 초마다 작동
for _ in range(T):

    # 1. 미세먼지 확산
    pm = [[0] * C for _ in range(R)]

    # 1.1 확산되는 미세먼지와 확산되고 남는 미세먼지 저장
    for r in range(R):
        for c in range(C):
            if room[r][c] == -1:
                continue

            pm[r][c] = room[r][c] // 5  # 확산되는 미세먼지

            spread = 0  # 확산 가능한 방향 수

            for k in range(4):
                dr = r + di[k]
                dc = c + dj[k]
                if 0 <= dr < R and 0 <= dc < C and room[dr][dc] != -1:
                    spread += 1

            room[r][c] -= pm[r][c] * spread # 확산되고 남은 미세먼지

    # 1.2 미세먼지 동시에 확산 시작
    for r in range(R):
        for c in range(C):

            cur_pm = pm[r][c]

            for k in range(4):
                dr = r + di[k]
                dc = c + dj[k]
                if 0 <= dr < R and 0 <= dc < C and room[dr][dc] != -1:
                    room[dr][dc] += cur_pm

    # 2. 미세먼지 순환

    # 2.1 미세먼지 순환 : 위
    d = 0
    pre_r, pre_c = air_cleaner-1, 0

    while True:
        cur_r, cur_c = pre_r + di[d], pre_c + dj[d]

        if 0 <= cur_r <= air_cleaner and 0 <= cur_c < C and room[cur_r][cur_c] != -1:
            room[pre_r][pre_c] = room[cur_r][cur_c]
            pre_r, pre_c = cur_r, cur_c

        elif 0 <= cur_r <= air_cleaner and 0 <= cur_c < C and room[cur_r][cur_c] == -1:
            room[pre_r][pre_c] = 0
            break

        else:
            d = (d + 1) % 4


    # 2.1 미세먼지 순환 : 밑
    d = 2
    pre_r, pre_c = air_cleaner+2, 0

    while True:
        cur_r, cur_c = pre_r + di[d], pre_c + dj[d]

        if air_cleaner+1 <= cur_r < R and 0 <= cur_c < C and room[cur_r][cur_c] != -1:
            room[pre_r][pre_c] = room[cur_r][cur_c]
            pre_r, pre_c = cur_r, cur_c

        elif air_cleaner+1 <= cur_r < R and 0 <= cur_c < C and room[cur_r][cur_c] == -1:
            room[pre_r][pre_c] = 0
            break

        else:
            d = (d - 1) % 4


# 최종 미세먼지 계산

final_pm = 0

for a in range(R):
    final_pm += sum(room[a])

print(final_pm + 2)