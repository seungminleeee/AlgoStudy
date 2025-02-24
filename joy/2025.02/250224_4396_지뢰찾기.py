n = int(input())
ji1 = [list(input()) for _ in range(n)]
ji2 = [list(input()) for _ in range(n)]
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

bang = False 

for i in range(n):
    for j in range(n):
        if ji2[i][j] == 'x':
            if ji1[i][j] == '*':
                bang = True
            else:
                r, c = i, j
                cnt = 0
                for k in range(8):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < n and 0 <= nc < n and ji1[nr][nc] == '*':
                        cnt += 1

                ji2[i][j] = cnt

if bang:
    for i in range(n):
        for j in range(n):
            if ji1[i][j] == '*':
                ji2[i][j] = '*'
                
for i in ji2:
    print(''.join(map(str, i)))