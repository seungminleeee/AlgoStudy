"""
[BOJ] 4396번: 지뢰 찾기 / 실버4
"""
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def find(y, x):
    check = 0
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n:
            if before[ny][nx] == '*':
                check += 1
    if check == 0: after[y][x] = '0'
    else: after[y][x] = str(check)

def mine_open():
    for i in range(n):
        for j in range(n):
            if before[i][j] == '*' and play[i][j] == 'x':
                return True
    return False

n = int(input())

before = [list(map(str, input().strip())) for _ in range(n)]
play = [list(map(str, input().strip())) for _ in range(n)]
after = [['.'] * n for _ in range(n)]

mine_check = mine_open()

for i in range(n):
    for j in range(n):
        if play[i][j] == 'x' and before[i][j] != '*':
            find(i, j)
        if mine_check and before[i][j] == '*':
            after[i][j] = '*'

for row in after:
    print(''.join(row))