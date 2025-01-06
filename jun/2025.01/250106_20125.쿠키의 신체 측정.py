"""
[BOJ] 20125번: 쿠키의 신체 측정 / 실4

조건:
1. 시간 제한 1초
2. N*N 정 사각형, 신체 부위는 판 밖으로 벗어 나지 않음.
3. 맨 왼쪽 위 칸이 (1,1)~(N,N)
4. 머리, 심장, 허리, 팔, 다리로 구성 (심장은 빨간 색, 머리는 심장 바로 위 칸의 1칸 크기)
5. 심장의 위치와 팔, 다리, 허리의 길이 구하기.
6. 5 <= N <= 1,000
7. _ 는 신체 없는 칸, * 는 신체 부위

생각:
1. 머리 먼저 찾고, 그 같은 행에 밑에 열에서 심장 찾고
2. 심장을 기준으로 허리, 팔, 다리 길이 재주기
"""
def heart(find):
    for i in range(N):
        for j in range(N):
            if find[i][j] == "*":
                return i + 2, j + 1

def left_hand(find, heart):
    y, x = heart
    cnt = 0
    for j in range(x-1):
        if find[y-1][j] == "*":
            cnt += 1
    return cnt

def right_hand(find, heart):
    y, x = heart
    cnt = 0
    for j in range(x, N):
        if find[y-1][j] == "*":
            cnt += 1
    return cnt

def waist(find, heart):
    y, x = heart
    cnt = 0
    for i in range(y, N):
        if find[i][x-1] == "*":
            cnt += 1
    return cnt

def left_leg(find, heart, waist_length):
    y, x = heart
    cnt = 0
    start_y = y + waist_length
    for i in range(start_y, N):
        if find[i][x-2] == "*":
            cnt += 1
    return cnt

def right_leg(find, heart, waist_length):
    y, x = heart
    cnt = 0
    start_y = y + waist_length
    for i in range(start_y, N):
        if find[i][x] == "*":
            cnt += 1
    return cnt

N = int(input())
cookie = [list(input()) for _ in range(N)]

heart_xy = heart(cookie)
left_length = left_hand(cookie, heart_xy)
right_length = right_hand(cookie, heart_xy)
waist_length = waist(cookie, heart_xy)
left_leg_length = left_leg(cookie, heart_xy, waist_length)
right_leg_length = right_leg(cookie, heart_xy, waist_length)

print(heart_xy[0], heart_xy[1])
print(left_length, right_length, waist_length, left_leg_length, right_leg_length)



