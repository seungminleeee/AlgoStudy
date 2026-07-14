H,W,X,Y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H+X)]

A = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i-X >= 0 and j-Y >= 0:
            A[i][j] = arr[i][j] - A[i-X][j-Y]
        else:
            A[i][j] = arr[i][j]

for a in A:
    print(*a)