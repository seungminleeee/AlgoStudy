N = int(input())
arr = [list(map(str, input())) for _ in range(N)]

heart_x = 0
heart_y = 0

for i in range(1,N-1):
    for j in range(1,N-1):
        if arr[i][j] == "*" and arr[i-1][j] == "*" and arr[i+1][j] == "*" and arr[i][j-1] == "*"  and arr[i][j+1] == "*":
            heart_x = i
            heart_y = j
            break

print(heart_x + 1, heart_y + 1)

# 왼쪽 팔
left_arm = 0
for j in range(heart_y-1, -1, -1):
    if arr[heart_x][j] == "*":
        left_arm += 1
    else:
        break

# 오른쪽 팔
right_arm = 0
for j in range(heart_y+1, N):
    if arr[heart_x][j] == "*":
        right_arm += 1
    else:
        break

# 허리
waist = 0
waist_x = 0
for i in range(heart_x+1, N):
    if arr[i][heart_y] == "*":
        waist += 1
        if arr[i+1][heart_y] == "_":
            waist_x = i
    else:
        break

# 왼쪽 다리
left_leg = 0
for i in range(waist_x+1,N):
    if arr[i][heart_y-1] == "*":
        left_leg += 1
    else:
        break

# 오른쪽 다리
right_leg = 0
for i in range(waist_x+1,N):
    if arr[i][heart_y+1] == "*":
        right_leg += 1
    else:
        break

print(left_arm, right_arm, waist, left_leg, right_leg)