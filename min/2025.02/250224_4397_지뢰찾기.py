N = int(input())
# * -> 지뢰 / . -> 지뢰x
bomb = [list(map(str, input())) for _ in range(N)]

# x -> 열림 / . -> 안열림
open = [list(map(str, input())) for _ in range(N)]

ans = [['.'] * N for _ in range(N)]

d = [(1,0),(0,1),(-1,0),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1)]

openbomb = False

for i in range(N):
    for j in range(N):
        if open[i][j] == 'x':
            cnt = 0
            if bomb[i][j] == '*':
                openbomb = True
            else:
                for dx, dy in d:
                    nx, ny = i + dx, j + dy
                    if 0<=nx<N and 0<=ny<N and bomb[nx][ny] == '*':
                        cnt += 1
                ans[i][j] = str(cnt)

if openbomb == True:
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == '*':
                ans[i][j] = '*'

for a in ans:
    print("".join(map(str,a)))