N = int(input())
color = [''] + list(map(str, input()))

blue = 0 # 파란색구간수
red = 0 # 빨간색구간수

for i in range(1, N+1):
    if color[i] == 'B' and color[i-1] != 'B':
        blue += 1
    elif color[i] == 'R' and color[i-1] != 'R':
        red += 1

print(min(blue, red) + 1)