# 시간초과때문에 질문게시판 뒤져봤더니 다익스트라 쓰라는 의견이 있었음..
# 하지만 난 다익스트라 못해서 더 뒤져봤더니 벽을 뚫는 경우와 안뚫는경우를 나눠서 3차원으로 저장하라는 의견 발견
# 그래서 3차원 visited (토마토 문제에서 썼던거) + 예진언니의 점프 코드 느낌으로 풀이해봄
# 엥 함수로 바꿨더니 1초 단축


from collections import deque

N, M = map(int, input().split())  # 세로, 가로
room = [list(map(int, list(input()))) for _ in range(N)]

def move():
    Q = deque([(0, 0, 0)])
    visited = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1  # 마지막인덱스 조건 - 0: 벽 부수지 않음, 1: 벽부숨

    while Q:
        r, c, broken = Q.popleft()   # 현재 위치 r, c, 벽 상태

        if (r, c) == (N-1, M-1):
            return min(visited[N-1][M-1][0], visited[N-1][M-1][1])

        for k in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + k[0], c + k[1]

            if 0 <= nr < N and 0 <= nc < M:

                # 다음 공간이 벽이 아닐경우
                if not room[nr][nc] and visited[nr][nc][broken] == float('inf'):
                    visited[nr][nc][broken] = visited[r][c][broken] + 1
                    Q.append((nr, nc, broken))

                # 다음 공간이 벽일 경우 -> broken이 0일 경우에만 이동 가능
                elif room[nr][nc] and broken == 0 and visited[nr][nc][1] == float('inf'):
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    Q.append((nr, nc, 1))
        
    return -1

print(move())
