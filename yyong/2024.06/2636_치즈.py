from collections import deque

def melt(cheeze, before_cheeze, i):  # 치즈 모양, 이전 치즈 양, i시간 후

    # 치즈 녹는 과정
    Q = deque([(0, 0)])
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    visited = [[0] * M for _ in range(N)]  # 방문 표시
    melting_count = 0                      # 녹은 치즈 양

    while Q:
        ci, cj = Q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < N and 0 <= nj < M and not cheeze[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                Q.append((ni, nj))
            elif 0 <= ni < N and 0 <= nj < M and cheeze[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                cheeze[ni][nj] = 0
                melting_count += 1

    if before_cheeze == melting_count:   # 다녹았으면 return
        return i + 1, before_cheeze
    
    return melt(cheeze, before_cheeze - melting_count, i + 1)   # 안녹았으면 재귀


N, M = map(int, input().split())  # 세로, 가로
init_cheeze = [list(map(int, input().split())) for _ in range(N)]  # 처음 치즈 모양
init_amount = 0 # 처음 치즈 양

for a in range(N):   # 처음 치즈 양 계산
    for b in range(M):
        if init_cheeze[a][b]:
            init_amount += 1

answer_1, answer_2 = melt(init_cheeze, init_amount, 0)
print(answer_1)
print(answer_2)