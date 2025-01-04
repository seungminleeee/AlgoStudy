from collections import deque
move = [(-1, -2), (-2, -1), (1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1)] # 나이트 이동 경우의수

for tc in range(int(input())):
    N = int(input())
    s1, s2 = map(int, input().split())  # 시작점
    f1, f2 = map(int, input().split())  # 끝점
    visited = [[0] * N for _ in range(N)]
    Q = deque([(s1, s2, 0)])  # 현재 위치 r, c, 이동 횟수

    while Q:
        ci, cj, t = Q.popleft()
        if (ci, cj) == (f1, f2):  # 도착점이면
            print(t)              # 프린트하고 break
            break

        for mi, mj in move:
            ni = mi + ci
            nj = mj + cj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = 1
                Q.append((ni, nj, t+1))