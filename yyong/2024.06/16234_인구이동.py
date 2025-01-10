from collections import deque

N, L, R = map(int, input().split())  # N칸, L 이상 R 이하 => 인구이동
country = [list(map(int, input().split())) for _ in range(N)]
day = 0
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

while True:
    visited = [[0] * N for _ in range(N)]
    move = False

    # 각 나라 돌면서 bfs
    for r in range(N):
        for c in range(N):
            
            if visited[r][c]:
                continue
            
            # 1. 국경선 체크

            Q = deque([(r, c)])
            visited[r][c] = 1   # 국경선 체크 표시
            open_country = [(r, c)]   # 현재 r, c와 인구이동할 국가 리스트
            sum_population = country[r][c]

            while Q:
                cur_r, cur_c = Q.popleft()

                for k in range(4):
                    nr, nc = cur_r + di[k], cur_c + dj[k]

                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and L <= abs(country[nr][nc] - country[cur_r][cur_c]) <= R:
                        Q.append((nr, nc))
                        open_country.append((nr, nc))
                        sum_population += country[nr][nc]
                        visited[nr][nc] = 1

            # 2. 인구이동
            if len(open_country) >= 2:
                move = True

                each_population = sum_population // len(open_country)

                for m_r, m_c in open_country:
                    country[m_r][m_c] = each_population

    if not move:
        break

    else:
        day += 1

print(day)