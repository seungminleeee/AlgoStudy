def check(arr):
    global max_candy

    # 행 검사
    for r in range(N):
        candy = 1
        for c in range(1, N):
            if arr[r][c] == arr[r][c-1]:
                candy += 1
                max_candy = max(candy, max_candy)
                if max_candy == N:
                    return
            else:
                candy = 1
    
    # 열 검사
    for c in range(N):
        candy = 1
        for r in range(1, N):
            if arr[r][c] == arr[r-1][c]:
                candy += 1
                max_candy = max(candy, max_candy)
                if max_candy == N:
                    return
            else:
                candy = 1


N = int(input())
bombony = [list(input()) for _ in range(N)]
max_candy = 0

# 행 순회
for r in range(N):
    for c in range(N-1):
        bombony[r][c], bombony[r][c+1] = bombony[r][c+1], bombony[r][c]  # 바꾸기
        check(bombony)
        if max_candy == N:
            print(max_candy)
            exit(0)
        bombony[r][c], bombony[r][c+1] = bombony[r][c+1], bombony[r][c]  # 돌려놓기

# 열 순회
for c in range(N):
    for r in range(N-1):
        bombony[r][c], bombony[r+1][c] = bombony[r+1][c], bombony[r][c]  # 바꾸기
        check(bombony)
        if max_candy == N:
            print(max_candy)
            exit(0)
        bombony[r][c], bombony[r+1][c] = bombony[r+1][c], bombony[r][c]  # 돌려놓기

print(max_candy)
