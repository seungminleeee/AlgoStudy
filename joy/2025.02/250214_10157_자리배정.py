C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
else:
    arr = [[0] * C for _ in range(R)]

    dr = [1, 0, -1, 0] # 상우하좌
    dc = [0, 1, 0, -1] 

    r, c = 0, 0
    d = 0

    for num in range(1, C * R + 1):
        arr[r][c] = num

        if num == K:
            print(c + 1, r + 1)
            break

        nr, nc = r + dr[d], c + dc[d] # 다음위치로 이동

        if not (0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 0): # 범위 벗어나거나 배열에 0이 아니면 
            d = (d + 1) % 4 # 방향 바꿔줌
            nr, nc = r + dr[d], c + dc[d] # 다음 위치로 이동

        r, c = nr, nc # 위치 갱신