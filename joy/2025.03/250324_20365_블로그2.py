N = int(input())
blog = list(input())

blue_cnt = 0
red_cnt = 0

if blog[0] == 'B':
    blue_cnt += 1
else:
    red_cnt += 1

for i in range(1, N):
    if blog[i] != blog[i - 1]:
        if blog[i] == 'B':
            blue_cnt += 1
        else:
            red_cnt += 1

print(min(blue_cnt, red_cnt) + 1)