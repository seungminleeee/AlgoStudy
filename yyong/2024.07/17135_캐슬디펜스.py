from collections import deque
from itertools import combinations
from copy import deepcopy

N, M, D = map(int, input().split())  # 세로, 가로, 공격거리 D 이하
game_map = [list(map(int, input().split())) for _ in range(N)]

def game(archers, game_map, death):
    global max_death

    if game_map == [[0] * M for _ in range(N)]:
        max_death = max(max_death, death)
        return
    
    will_death = []

    # 궁수마다 가장 가까운 적 찾아서 제거
    for archer in archers:

        Q = deque([(0, N, archer)])
        visited = [[0] * M for _ in range(N)]
        enemies = []
        while Q:

            cd, cr, cc = Q.popleft()

            for k in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = cr + k[0], cc + k[1]

                if 0 <= nr < N and 0 <= nc < M and cd + 1 <= D and not visited[nr][nc]:
                    Q.append((cd + 1, nr, nc))
                    visited[nr][nc] = 1

                    if game_map[nr][nc] == 1:
                        enemies.append((cd + 1, nr, nc))

        enemies.sort(key=lambda x:(x[0], x[2], x[1]))

        if enemies:
            will_death.append(enemies[0])

    for enemy in will_death:
        if game_map[enemy[1]][enemy[2]] == 1:
            game_map[enemy[1]][enemy[2]] = 0
            death += 1


    # 적 한칸씩 전진
    game_map = [[0] * M] + game_map[:N-1]

    # 반복
    game(archers, game_map, death)

max_death = 0

for case in combinations(range(M), 3):

    cur_game_map = deepcopy(game_map)
    game(case, cur_game_map, 0)

print(max_death)