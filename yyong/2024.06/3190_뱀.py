# 파이썬 34132 KB, 64 ms

from collections import deque


N = int(input())
board = [[0] * N for _ in range(N)]

# 사과 놓기
for _ in range(int(input())):
    ar, ac = map(int, input().split())
    board[ar-1][ac-1] = 'A'


snake = deque([[0, 0]])  # 뱀의 모든 좌표
hr, hc, hd = [0, 0, 1]  # 머리 좌표, 머리 방향 (0, 1, 2, 3 = 위, 오, 아, 왼)
move_d = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 전진할때 머리 좌표 변경
cur_time = 0  # 총 시간


# 뱀 이동
for _ in range(int(input())):

    time, dir = map(str, input().split())  # 흘러간 시간, 방향

    for _ in range(int(time)-cur_time):  # time까지는 전진
        cur_time += 1

        hr, hc = hr + move_d[hd][0], hc + move_d[hd][1]  # 머리 이동

        if not(0 <= hr < N) or not(0 <= hc < N) or [hr, hc] in snake:
            print(cur_time)
            exit(0)
        else:
            snake.append([hr, hc])

        if board[hr][hc] == 'A':
            board[hr][hc] = 0
        else:
            snake.popleft()

    # 조건에 맞춰 방향 틀기
    if dir == 'L':
        hd = (hd-1) % 4

    if dir == 'D':
        hd = (hd+1) % 4


# 남은 시간동안 전진
while True:
    cur_time += 1

    hr, hc = hr + move_d[hd][0], hc + move_d[hd][1]  # 머리 이동

    if not(0 <= hr < N) or not(0 <= hc < N) or [hr, hc] in snake:
        print(cur_time)
        exit(0)
    else:
        snake.append([hr, hc])

    if board[hr][hc] == 'A':
        board[hr][hc] = 0
    else:
        snake.popleft()
