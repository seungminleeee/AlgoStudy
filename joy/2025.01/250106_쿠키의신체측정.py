N = int(input())
arr = [list(input()) for _ in range(N)]

# 머리 좌표 찾기 (i, j)
head = (0, 0)
for i in range(N):
    for j in range(N):
        if head == (0,0) and arr[i][j] == '*':
            head = (i, j)
            break 
    if head != (0,0): 
        break

# 심장좌표는 (i + 1, j) 
heart = (head[0]+1, head[1])
print(heart[0]+1, heart[1]+1)

# 왼쪽팔은 심장좌표 기준 열-왼쪽으로 카운트 
left_arm = 0
for j in range(heart[1] - 1 , -1, -1):
    if arr[heart[0]][j] == '*':
        left_arm += 1
    else:
        break

# 오른쪽팔은 심장좌표 기준 열-오른쪽으로 카운트 
right_arm = 0
for j in range(heart[1] + 1, N):
    if arr[heart[0]][j] == '*':
        right_arm += 1
    else:
        break

# 허리는 심장좌표 기준 행 - 아래쪽으로 카운트
waist = 0
for i in range(heart[0]+ 1, N):
    if arr[i][heart[1]] == '*':
        waist += 1
    else:
        break 

# 왼쪽 다리는 심장좌표 + 허리 기준으로 열-1 해주고 행 - 아래쪽으로 카운트
left_leg = 0
for i in range(heart[0] + waist + 1, N):
    if arr[i][heart[1]-1] == '*':
        left_leg += 1
    else:
        break

# 오른쪽 다리는 심장좌표 + 허리 기준으로 열+1 해주고 행 - 아래쪽으로 카운트
right_leg = 0
for i in range(heart[0] + waist + 1, N):
    if arr[i][heart[1] + 1] == '*':
        right_leg += 1
    else:
        break

print(left_arm, right_arm, waist, left_leg, right_leg)