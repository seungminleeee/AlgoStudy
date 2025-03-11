"""
[BOJ] 12927번: 배수 스위치 / 실버4

1. 모든 전구를 끄기 위해 몇 번 눌러야 하는가
"""
switch = list(input())
switch.insert(0, 'Z')

cnt = 0
for i in range(1, len(switch)):
    if switch[i] == 'Y':
        for j in range(i, len(switch), i):
            if switch[j] == 'Y':
                switch[j] = 'N'
            else:
                switch[j] = 'Y'
        cnt += 1

print(cnt)