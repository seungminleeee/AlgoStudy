C, R = map(int, input().split())
K = int(input())

if K > R*C:
    print(0)
else:

    arr = [[0]*C for _ in range(R)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    d = 0

    r, c = R-1, 0
    n = 1

    while n < K:
        arr[r][c] = n
        n += 1

        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nc < 0 or nr >= R or nc >= C or arr[nr][nc] != 0:
            d = (d+1) % 4
            nr = r + dr[d]
            nc = c + dc[d]
        r = nr
        c = nc

    print(c+1, R-r)